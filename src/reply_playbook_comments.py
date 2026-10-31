"""
Automated Comment-to-DM & Public Reply Responder for @quietlywealthy001.
- Scans recent media on @quietlywealthy001 via Official Instagram Graph API (Composio MCP).
- Finds comments containing keyword 'PLAYBOOK' or 'GUIDE' (case-insensitive).
- Skips comments already replied to (persisted in content_queue/replied_comments.json + checks existing thread replies).
- Posts warm public comment reply:
    "Just sent the free 7-Day Launch Checklist + Playbook link straight to your DMs! 📩"
- Sends Private Reply / DM with both live Selar storefront links:
    Free 7-Day Launch Checklist: https://selar.com/8ec448f48m
    $19 Faceless Business & Marketing Playbook: https://selar.com/8fj8h8327w
"""
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

SRC_DIR = Path(__file__).resolve().parent
ROOT = SRC_DIR.parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from publish_instagram import call_composio_tool, load_env

REPLIED_PATH = ROOT / "content_queue" / "replied_comments.json"
BRAND_PATH = ROOT / "brand.json"

KEYWORDS = ("playbook", "guide", "checklist", "link", "pdf")

PUBLIC_REPLY_TEXT = "Just sent the free 7-Day Launch Checklist + Playbook link straight to your DMs! 📩"


def build_dm_text(brand: dict) -> str:
    free_url = brand.get("product_1_url", "https://selar.com/8ec448f48m")
    core_url = brand.get("product_2_url", "https://selar.com/8fj8h8327w")
    store_url = brand.get("storefront_url", "https://selar.com/m/omowumi-ibrahim1")
    return (
        "Hey! 👋 Here are the Quietly Wealthy resources you requested:\n\n"
        f"1️⃣ Free 7-Day Digital Product Launch Checklist ($0):\n{free_url}\n\n"
        f"2️⃣ The Faceless Business & Marketing Playbook — 23 Pages ($19 Launch Offer):\n{core_url}\n\n"
        f"Full Storefront: {store_url}\n\n"
        "Start with Day 1 of the free checklist today — and reply here anytime if you have questions!"
    )


def load_replied_state() -> dict:
    if REPLIED_PATH.exists():
        try:
            return json.loads(REPLIED_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"replied_comment_ids": [], "history": []}


def save_replied_state(state: dict):
    REPLIED_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPLIED_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    env = load_env()
    api_key = env.get("COMPOSIO_API_KEY", "")
    mcp_url = env.get("COMPOSIO_MCP_URL", "https://connect.composio.dev/mcp")
    if not api_key:
        print("ERROR: COMPOSIO_API_KEY is missing.", file=sys.stderr)
        sys.exit(1)

    brand = json.loads(BRAND_PATH.read_text(encoding="utf-8")) if BRAND_PATH.exists() else {}
    dm_text = build_dm_text(brand)

    info_resp = call_composio_tool(api_key, mcp_url, "INSTAGRAM_GET_USER_INFO", {})
    if not info_resp.get("successful"):
        raise RuntimeError(f"INSTAGRAM_GET_USER_INFO failed: {info_resp}")
    user_data = info_resp.get("data", {})
    ig_user_id = str(user_data["id"])
    print(f"[Responder] Connected to @quietlywealthy001 (id={ig_user_id})")

    media_resp = call_composio_tool(
        api_key,
        mcp_url,
        "INSTAGRAM_GET_IG_USER_MEDIA",
        {"ig_user_id": ig_user_id, "fields": "id,caption,permalink,timestamp", "limit": 15},
    )
    media_items = media_resp.get("data", {}).get("data", [])
    print(f"[Responder] Scanning {len(media_items)} recent media posts for PLAYBOOK/GUIDE comments...")

    state = load_replied_state()
    replied_ids = set(state.get("replied_comment_ids", []))
    new_replies = 0

    for media in media_items:
        media_id = str(media.get("id", ""))
        if not media_id:
            continue
        comments_resp = call_composio_tool(
            api_key,
            mcp_url,
            "INSTAGRAM_GET_IG_MEDIA_COMMENTS",
            {"ig_media_id": media_id},
        )
        comments = comments_resp.get("data", {}).get("data", [])
        for c in comments:
            cid = str(c.get("id", ""))
            text = (c.get("text") or "").strip()
            username = c.get("username") or c.get("from", {}).get("username") or ""
            from_id = str(c.get("from", {}).get("id") or "")

            if not cid or cid in replied_ids:
                continue
            # Do not reply to our own comments
            if username.lower() == "quietlywealthy001" or from_id == ig_user_id:
                replied_ids.add(cid)
                continue

            text_lower = text.lower()
            if not any(kw in text_lower for kw in KEYWORDS):
                continue

            # Check existing replies on the comment if present
            existing_replies = c.get("replies", {}).get("data", [])
            if any("just sent the free 7-day" in (r.get("text") or "").lower() for r in existing_replies):
                replied_ids.add(cid)
                continue

            print(f"  [+] Trigger comment found: id={cid} user=@{username} text='{text}'")

            # 1. Public Comment Reply with Both Links as fallback + DM notice
            public_msg = (
                f"{PUBLIC_REPLY_TEXT}\n"
                f"(Free Checklist: {brand.get('product_1_url', 'https://selar.com/8ec448f48m')} | "
                f"Playbook: {brand.get('product_2_url', 'https://selar.com/8fj8h8327w')})"
            )
            pub_reply = call_composio_tool(
                api_key,
                mcp_url,
                "INSTAGRAM_POST_IG_COMMENT_REPLIES",
                {"ig_comment_id": cid, "message": PUBLIC_REPLY_TEXT},
            )
            print(f"    -> Public reply result: {pub_reply.get('successful')}")

            # 2. Send DM if recipient PSID / from_id is available
            dm_sent = False
            if from_id:
                try:
                    dm_resp = call_composio_tool(
                        api_key,
                        mcp_url,
                        "INSTAGRAM_SEND_TEXT_MESSAGE",
                        {
                            "ig_user_id": ig_user_id,
                            "recipient_id": from_id,
                            "text": dm_text,
                        },
                    )
                    dm_sent = bool(dm_resp.get("successful"))
                    print(f"    -> Direct message result: {dm_sent}")
                except Exception as e:
                    print(f"    -> DM note: {e}")

            replied_ids.add(cid)
            state.setdefault("history", []).append(
                {
                    "comment_id": cid,
                    "media_id": media_id,
                    "username": username,
                    "text": text,
                    "dm_sent": dm_sent,
                    "replied_at": datetime.now(timezone.utc).isoformat(),
                }
            )
            new_replies += 1

    state["replied_comment_ids"] = sorted(replied_ids)
    save_replied_state(state)
    print(f"[Responder] Completed cleanly. Processed {new_replies} new keyword comment(s).")


if __name__ == "__main__":
    main()

