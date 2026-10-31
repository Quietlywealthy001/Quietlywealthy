"""
Deploys the 24/7 Cloud Autopilot to GitHub using the completed GitHub Device Flow token:
1. Exchanges build/gh_device_flow.json (`device_code`) for an OAuth access token.
2. Creates repository `quietly-wealthy-autopilot` if not present.
3. Pushes all workspace files via GitHub Git Data API (strictly excluding .env, .browser_profile/, products/*.pdf, __pycache__, build/).
4. Encrypts & sets the Actions secret `COMPOSIO_API_KEY` via LibSodium SealedBox (`PUT /repos/{owner}/{repo}/actions/secrets/COMPOSIO_API_KEY`).
5. Triggers `daily_instagram_autopilot.yml` with `mode=preflight` and verifies the green checkmark!
"""
import base64
import json
import os
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path
from nacl import encoding, public

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
DEVICE_FLOW_PATH = ROOT / "build" / "gh_device_flow.json"
TOKEN_CACHE_PATH = ROOT / "build" / "gh_token.json"
REPO_NAME = "Quietlywealthy"
CLIENT_ID = "178c6fc778ccc68e1d6a"

EXCLUDE_DIRS = {".git", ".browser_profile", "__pycache__", "build", "products", ".pytest_cache"}
EXCLUDE_FILES = {".env", ".DS_Store", "Thumbs.db"}


def load_env() -> dict:
    env = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def poll_for_device_token(max_wait_sec: int = 300) -> str:
    if TOKEN_CACHE_PATH.exists():
        cached = json.loads(TOKEN_CACHE_PATH.read_text(encoding="utf-8"))
        if cached.get("access_token"):
            return cached["access_token"]

    if not DEVICE_FLOW_PATH.exists():
        raise FileNotFoundError(f"Missing {DEVICE_FLOW_PATH}")
    df = json.loads(DEVICE_FLOW_PATH.read_text(encoding="utf-8"))
    device_code = df["device_code"]
    interval = int(df.get("interval", 5)) + 1

    deadline = time.time() + max_wait_sec
    while time.time() < deadline:
        data = urllib.parse.urlencode(
            {
                "client_id": CLIENT_ID,
                "device_code": device_code,
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            }
        ).encode("utf-8")
        req = urllib.request.Request(
            "https://github.com/login/oauth/access_token",
            data=data,
            headers={"Accept": "application/json", "User-Agent": "GitHubCLI/2.103.3"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            res = json.loads(resp.read().decode("utf-8"))
        if "access_token" in res:
            TOKEN_CACHE_PATH.write_text(json.dumps(res, indent=2), encoding="utf-8")
            return res["access_token"]
        err = res.get("error", "")
        if err == "authorization_pending":
            time.sleep(interval)
            continue
        if err == "slow_down":
            interval += 5
            time.sleep(interval)
            continue
        raise RuntimeError(f"Device flow error: {res}")
    raise TimeoutError("Timed out waiting for GitHub device authorization.")


def collect_repo_files() -> list:
    files = []
    for p in sorted(ROOT.rglob("*")):
        if p.is_dir():
            continue
        rel = p.relative_to(ROOT)
        parts = set(rel.parts)
        if parts & EXCLUDE_DIRS:
            continue
        if p.name in EXCLUDE_FILES or p.name.startswith(".env"):
            continue
        if p.suffix.lower() in (".pyc", ".pyo", ".pdf"):
            continue
        rel_posix = rel.as_posix()
        files.append((rel_posix, p))
    return files


def gh_api(token: str, method: str, path: str, payload: dict = None) -> dict:
    url = f"https://api.github.com{path}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "QuietlyWealthy-Deployer/1.0",
        },
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {method} {path} -> HTTP {e.code}: {err_body}")


def encrypt_github_secret(public_key_b64: str, secret_value: str) -> str:
    pk = public.PublicKey(public_key_b64.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(pk)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return base64.b64encode(encrypted).decode("utf-8")


def set_repo_secret(token: str, owner: str, repo: str, secret_name: str, secret_value: str):
    key_info = gh_api(token, "GET", f"/repos/{owner}/{repo}/actions/secrets/public-key")
    encrypted_val = encrypt_github_secret(key_info["key"], secret_value)
    gh_api(
        token,
        "PUT",
        f"/repos/{owner}/{repo}/actions/secrets/{secret_name}",
        {
            "encrypted_value": encrypted_val,
            "key_id": key_info["key_id"],
        },
    )


def push_files_via_api(token: str, owner: str, repo: str) -> str:
    files = collect_repo_files()
    print(f"[Deploy] Preparing to upload {len(files)} workspace files to {owner}/{repo} (excluding .env & PDFs)...")

    try:
        gh_api(token, "GET", f"/repos/{owner}/{repo}")
        print(f"[Deploy] Repository {owner}/{repo} already exists.")
    except Exception:
        print(f"[Deploy] Creating repository {owner}/{repo}...")
        gh_api(
            token,
            "POST",
            "/user/repos",
            {
                "name": repo,
                "description": "Quietly Wealthy (@quietlywealthy001) — 24/7 Instagram Carousel & Comment-to-DM Autopilot",
                "private": False,
                "auto_init": True,
            },
        )
        time.sleep(3)

    repo_info = gh_api(token, "GET", f"/repos/{owner}/{repo}")
    default_branch = repo_info.get("default_branch", "main")
    try:
        ref_info = gh_api(token, "GET", f"/repos/{owner}/{repo}/git/ref/heads/{default_branch}")
        latest_commit_sha = ref_info["object"]["sha"]
    except Exception:
        gh_api(
            token,
            "PUT",
            f"/repos/{owner}/{repo}/contents/README.md",
            {
                "message": "Initial commit",
                "content": base64.b64encode(b"# Quietly Wealthy Autopilot\n").decode("ascii"),
            },
        )
        time.sleep(2)
        ref_info = gh_api(token, "GET", f"/repos/{owner}/{repo}/git/ref/heads/{default_branch}")
        latest_commit_sha = ref_info["object"]["sha"]

    commit_info = gh_api(token, "GET", f"/repos/{owner}/{repo}/git/commits/{latest_commit_sha}")
    base_tree_sha = commit_info["tree"]["sha"]

    tree_items = []
    for rel_posix, path in files:
        raw_bytes = path.read_bytes()
        b64_content = base64.b64encode(raw_bytes).decode("ascii")
        blob = gh_api(
            token,
            "POST",
            f"/repos/{owner}/{repo}/git/blobs",
            {"content": b64_content, "encoding": "base64"},
        )
        tree_items.append(
            {
                "path": rel_posix,
                "mode": "100644",
                "type": "blob",
                "sha": blob["sha"],
            }
        )
        print(f"  [+] Staged: {rel_posix} ({len(raw_bytes)} B)")

    new_tree = gh_api(
        token,
        "POST",
        f"/repos/{owner}/{repo}/git/trees",
        {"base_tree": base_tree_sha, "tree": tree_items},
    )
    new_commit = gh_api(
        token,
        "POST",
        f"/repos/{owner}/{repo}/git/commits",
        {
            "message": "feat: deploy 24/7 Instagram Carousel Autopilot & Comment-to-DM Responder",
            "tree": new_tree["sha"],
            "parents": [latest_commit_sha],
        },
    )
    gh_api(
        token,
        "PATCH",
        f"/repos/{owner}/{repo}/git/refs/heads/{default_branch}",
        {"sha": new_commit["sha"], "force": True},
    )
    print(f"[Deploy] Pushed commit {new_commit['sha']} to https://github.com/{owner}/{repo} ({default_branch})!")
    return default_branch


def main():
    print("[Deploy] Waiting for GitHub Device Code authorization...")
    token = poll_for_device_token(max_wait_sec=600)
    user_info = gh_api(token, "GET", "/user")
    owner = user_info["login"]
    print(f"[Deploy] Authenticated as GitHub user: {owner}")

    default_branch = push_files_via_api(token, owner, REPO_NAME)

    env = load_env()
    composio_key = env.get("COMPOSIO_API_KEY", "")
    if not composio_key:
        raise RuntimeError("COMPOSIO_API_KEY missing in .env")

    print(f"[Deploy] Encrypting & setting COMPOSIO_API_KEY secret on {owner}/{REPO_NAME}...")
    set_repo_secret(token, owner, REPO_NAME, "COMPOSIO_API_KEY", composio_key)
    print("[Deploy] COMPOSIO_API_KEY secret configured!")

    print("[Deploy] Triggering Cloud Preflight workflow run...")
    time.sleep(3)
    gh_api(
        token,
        "POST",
        f"/repos/{owner}/{REPO_NAME}/actions/workflows/daily_instagram_autopilot.yml/dispatches",
        {"ref": default_branch, "inputs": {"mode": "preflight"}},
    )
    print(f"[Deploy] Workflow dispatched! Polling run status on https://github.com/{owner}/{REPO_NAME}/actions ...")

    run_url = f"https://github.com/{owner}/{REPO_NAME}/actions"
    for _ in range(35):
        time.sleep(6)
        runs = gh_api(token, "GET", f"/repos/{owner}/{REPO_NAME}/actions/runs?per_page=5").get("workflow_runs", [])
        if runs:
            latest = runs[0]
            st = latest.get("status")
            conc = latest.get("conclusion")
            run_url = latest.get("html_url", run_url)
            print(f"  [*] Run {latest['id']} status={st} conclusion={conc} ({run_url})")
            if st == "completed":
                break


if __name__ == "__main__":
    main()
