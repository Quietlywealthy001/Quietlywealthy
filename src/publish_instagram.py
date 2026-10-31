import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
STATE_PATH = BASE_DIR / "content_queue" / "published_state.json"


def load_env():
    env = dict(os.environ)
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    return env


def call_composio_tool(api_key: str, mcp_url: str, tool_slug: str, arguments: dict) -> dict:
    payload = {
        "jsonrpc": "2.0",
        "id": int(time.time() * 1000) % 1000000,
        "method": "tools/call",
        "params": {
            "name": "COMPOSIO_MULTI_EXECUTE_TOOL",
            "arguments": {
                "tools": [
                    {
                        "tool_slug": tool_slug,
                        "arguments": arguments,
                    }
                ]
            },
        },
    }
    req = urllib.request.Request(
        mcp_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "x-consumer-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "User-Agent": "Antigravity-Autopilot/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        raw = resp.read().decode("utf-8", errors="replace")

    for line in raw.splitlines():
        if line.startswith("data: "):
            msg = json.loads(line[6:])
            content = msg.get("result", {}).get("content", [])
            if content and "text" in content[0]:
                inner = json.loads(content[0]["text"])
                results = inner.get("data", {}).get("results", [])
                if results:
                    return results[0].get("response", results[0])
                return inner
    raise RuntimeError(f"Unexpected MCP response for {tool_slug}: {raw[:400]}")


def verify_public_jpeg_url(url: str) -> bool:
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"},
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            ctype = resp.headers.get("Content-Type", "").lower()
            head_bytes = resp.read(16)
            is_jpeg_magic = head_bytes.startswith(b"\xff\xd8\xff")
            return resp.status == 200 and ("image/jpeg" in ctype or "image/jpg" in ctype or is_jpeg_magic)
    except Exception as e:
        print(f"  [!] URL verification failed for {url}: {e}")
        return False


def _multipart_upload(url: str, fields: dict, file_field: str, file_path: Path) -> str:
    boundary = f"----WebKitFormBoundary{int(time.time() * 1000)}"
    body = bytearray()
    for k, v in fields.items():
        body.extend(f"--{boundary}\r\n".encode("utf-8"))
        body.extend(f'Content-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode("utf-8"))
    body.extend(f"--{boundary}\r\n".encode("utf-8"))
    body.extend(
        f'Content-Disposition: form-data; name="{file_field}"; filename="{file_path.name}"\r\n'.encode("utf-8")
    )
    body.extend(b"Content-Type: image/jpeg\r\n\r\n")
    body.extend(file_path.read_bytes())
    body.extend(f"\r\n--{boundary}--\r\n".encode("utf-8"))

    req = urllib.request.Request(
        url,
        data=bytes(body),
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "User-Agent": "curl/8.4.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", errors="replace").strip()


def stage_jpeg_public_url(file_path: Path) -> str:
    # Host 1: catbox.moe
    try:
        out = _multipart_upload(
            "https://catbox.moe/user/api.php",
            {"reqtype": "fileupload"},
            "fileToUpload",
            file_path,
        )
        if out.startswith("https://") and verify_public_jpeg_url(out):
            return out
    except Exception as e:
        print(f"  [!] catbox upload error: {e}")

    # Host 2: litterbox.catbox.moe (72h)
    try:
        out = _multipart_upload(
            "https://litterbox.catbox.moe/resources/internals/api.php",
            {"reqtype": "fileupload", "time": "72h"},
            "fileToUpload",
            file_path,
        )
        if out.startswith("https://") and verify_public_jpeg_url(out):
            return out
    except Exception as e:
        print(f"  [!] litterbox upload error: {e}")

    # Host 3: uguu.se
    try:
        out = _multipart_upload(
            "https://uguu.se/upload",
            {},
            "files[]",
            file_path,
        )
        data = json.loads(out)
        if data.get("success") and data.get("files"):
            u = data["files"][0]["url"]
            if verify_public_jpeg_url(u):
                return u
    except Exception as e:
        print(f"  [!] uguu upload error: {e}")

    # Host 4: tmpfiles.org
    try:
        out = _multipart_upload(
            "https://tmpfiles.org/api/v1/upload",
            {},
            "file",
            file_path,
        )
        data = json.loads(out)
        raw_url = data.get("data", {}).get("url", "")
        if raw_url:
            dl_url = raw_url.replace("http://tmpfiles.org/", "https://tmpfiles.org/dl/").replace(
                "https://tmpfiles.org/", "https://tmpfiles.org/dl/"
            )
            if verify_public_jpeg_url(dl_url):
                return dl_url
    except Exception as e:
        print(f"  [!] tmpfiles upload error: {e}")

    raise RuntimeError(f"Failed to stage {file_path.name} to a verified public JPEG URL.")


def run_preflight(api_key: str, mcp_url: str) -> dict:
    print("[Preflight] Checking Instagram Business connection via Composio MCP...")
    info_resp = call_composio_tool(api_key, mcp_url, "INSTAGRAM_GET_USER_INFO", {})
    if not info_resp.get("successful"):
        raise RuntimeError(f"INSTAGRAM_GET_USER_INFO failed: {info_resp}")
    user_data = info_resp.get("data", {})
    ig_user_id = str(user_data.get("id", ""))
    account_type = user_data.get("account_type", "")
    name = user_data.get("name", "")
    media_count = user_data.get("media_count", 0)
    print(f"[Preflight] Connected Account: name='{name}' | id={ig_user_id} | type={account_type} | media_count={media_count}")

    limit_resp = call_composio_tool(
        api_key,
        mcp_url,
        "INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT",
        {"ig_user_id": ig_user_id},
    )
    quota_data = limit_resp.get("data", {})
    print(f"[Preflight] Publishing Quota Check: {json.dumps(quota_data)}")
    return user_data


def publish_carousel_dir(folder: Path, api_key: str, mcp_url: str) -> dict:
    user_data = run_preflight(api_key, mcp_url)
    ig_user_id = str(user_data["id"])

    manifest_path = folder / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Missing manifest.json in {folder}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    caption = manifest.get("caption", "")
    slide_names = manifest.get("slides_jpg") or manifest.get("slides", [])
    if not slide_names:
        slide_names = [f"slide_0{i}.jpg" for i in range(1, 8)]

    slide_paths = [folder / s for s in slide_names]
    for sp in slide_paths:
        if not sp.exists():
            raise FileNotFoundError(f"Slide JPEG not found: {sp}")

    print(f"[Publish] Staging {len(slide_paths)} slides to direct HTTPS JPEG URLs...")
    public_urls = []
    for sp in slide_paths:
        u = stage_jpeg_public_url(sp)
        print(f"  [+] {sp.name} -> {u} (Verified image/jpeg 200 OK)")
        public_urls.append(u)

    print("[Publish] Creating Instagram Carousel Container...")
    carousel_resp = call_composio_tool(
        api_key,
        mcp_url,
        "INSTAGRAM_CREATE_CAROUSEL_CONTAINER",
        {
            "ig_user_id": ig_user_id,
            "caption": caption,
            "child_image_urls": public_urls,
        },
    )

    creation_id = None
    if carousel_resp.get("successful") and carousel_resp.get("data", {}).get("id"):
        creation_id = str(carousel_resp["data"]["id"])
        print(f"  [+] Carousel container created directly: creation_id={creation_id}")
    else:
        print(f"  [!] Direct child_image_urls returned {carousel_resp}; falling back to explicit child containers...")
        child_ids = []
        for idx, u in enumerate(public_urls, 1):
            c_resp = call_composio_tool(
                api_key,
                mcp_url,
                "INSTAGRAM_POST_IG_USER_MEDIA",
                {
                    "ig_user_id": ig_user_id,
                    "image_url": u,
                    "is_carousel_item": True,
                    "media_type": "IMAGE",
                },
            )
            if not c_resp.get("successful") or not c_resp.get("data", {}).get("id"):
                raise RuntimeError(f"Failed creating child container {idx}: {c_resp}")
            cid = str(c_resp["data"]["id"])
            print(f"  [+] Child {idx} container id={cid}")
            child_ids.append(cid)

        carousel_resp = call_composio_tool(
            api_key,
            mcp_url,
            "INSTAGRAM_CREATE_CAROUSEL_CONTAINER",
            {
                "ig_user_id": ig_user_id,
                "caption": caption,
                "children": child_ids,
            },
        )
        if not carousel_resp.get("successful") or not carousel_resp.get("data", {}).get("id"):
            raise RuntimeError(f"Failed creating parent carousel container: {carousel_resp}")
        creation_id = str(carousel_resp["data"]["id"])
        print(f"  [+] Parent carousel container created: creation_id={creation_id}")

    # Poll container status briefly before publishing
    for attempt in range(1, 7):
        status_resp = call_composio_tool(
            api_key,
            mcp_url,
            "INSTAGRAM_GET_POST_STATUS",
            {"creation_id": creation_id},
        )
        st = status_resp.get("data", {}).get("status_code", "UNKNOWN")
        print(f"  [*] Container {creation_id} status (check {attempt}): {st}")
        if st in ("FINISHED", "PUBLISHED"):
            break
        if st in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"Container failed processing: {status_resp}")
        time.sleep(4)

    print(f"[Publish] Publishing container {creation_id} to @quietlywealthy001...")
    pub_resp = call_composio_tool(
        api_key,
        mcp_url,
        "INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH",
        {
            "ig_user_id": ig_user_id,
            "creation_id": creation_id,
            "max_wait_seconds": 60,
            "poll_interval_seconds": 5,
        },
    )
    if not pub_resp.get("successful") or not pub_resp.get("data", {}).get("id"):
        raise RuntimeError(f"Publish failed: {pub_resp}")

    media_id = str(pub_resp["data"]["id"])
    print(f"  [+] Published Media ID: {media_id}")

    media_resp = call_composio_tool(
        api_key,
        mcp_url,
        "INSTAGRAM_GET_IG_MEDIA",
        {
            "ig_media_id": media_id,
            "fields": "id,permalink,caption,media_type,timestamp,username",
        },
    )
    media_info = media_resp.get("data", {})
    permalink = media_info.get("permalink", "")
    print(f"  [SUCCESS] LIVE PERMALINK: {permalink}")

    # Record in published_state.json
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    state = {"published": []}
    if STATE_PATH.exists():
        try:
            state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass

    entry = {
        "day": manifest.get("day", 1),
        "folder": folder.name,
        "topic": manifest.get("topic", ""),
        "media_id": media_id,
        "creation_id": creation_id,
        "permalink": permalink,
        "published_at": datetime.now(timezone.utc).isoformat(),
    }
    state.setdefault("published", []).append(entry)
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")

    manifest["published_media_id"] = media_id
    manifest["permalink"] = permalink
    manifest["published_at"] = entry["published_at"]
    manifest["public_urls"] = public_urls
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return entry


def main():
    parser = argparse.ArgumentParser(description="Publish Instagram Carousel via Composio Official Graph API")
    parser.add_argument("--preflight", action="store_true", help="Run preflight check only")
    parser.add_argument("--dir", type=str, help="Path to carousel output directory (e.g., output/day_01)")
    args = parser.parse_args()

    env = load_env()
    api_key = env.get("COMPOSIO_API_KEY", "")
    mcp_url = env.get("COMPOSIO_MCP_URL", "https://connect.composio.dev/mcp")
    if not api_key:
        print("ERROR: COMPOSIO_API_KEY is missing in environment or .env", file=sys.stderr)
        sys.exit(1)

    if args.preflight and not args.dir:
        run_preflight(api_key, mcp_url)
        sys.exit(0)

    if args.dir:
        folder = Path(args.dir)
        if not folder.is_absolute():
            folder = (BASE_DIR / folder).resolve()
        publish_carousel_dir(folder, api_key, mcp_url)
        sys.exit(0)

    parser.print_help()


if __name__ == "__main__":
    main()

