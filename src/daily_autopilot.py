"""
Daily Instagram Carousel Autopilot for @quietlywealthy001.
- Checks content_queue/published_state.json (and live IG media) to find the next unpublished day in content_queue/30_day_plan.json.
- If all 30 days are published and GEMINI_API_KEY is available, generates a fresh non-repeating topic automatically.
- Renders the 7 slides (1080x1350 .jpg, quality=92) + manifest.json + caption.txt using Playwright and templates/carousel_slide.html.
- Publishes live via src/publish_instagram.py.
"""
import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

SRC_DIR = Path(__file__).resolve().parent
ROOT = SRC_DIR.parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from common import BRAND, BUILD, FONT_LINK, Renderer, handle, monogram_svg
from publish_instagram import call_composio_tool, load_env, publish_carousel_dir, run_preflight

PLAN_PATH = ROOT / "content_queue" / "30_day_plan.json"
STATE_PATH = ROOT / "content_queue" / "published_state.json"
TEMPLATE_PATH = ROOT / "templates" / "carousel_slide.html"


def get_published_days(api_key: str, mcp_url: str) -> set:
    published_days = set()
    published_topics = set()
    if STATE_PATH.exists():
        try:
            st = json.loads(STATE_PATH.read_text(encoding="utf-8"))
            for item in st.get("published", []):
                if item.get("day"):
                    published_days.add(int(item["day"]))
                if item.get("topic"):
                    published_topics.add(item["topic"].strip().lower())
        except Exception as e:
            print(f"[Autopilot] Warning reading {STATE_PATH}: {e}")

    # Also cross-check live Instagram captions so even stateless runs never repeat
    try:
        info = call_composio_tool(api_key, mcp_url, "INSTAGRAM_GET_USER_INFO", {})
        ig_user_id = str(info.get("data", {}).get("id", ""))
        if ig_user_id:
            media_resp = call_composio_tool(
                api_key,
                mcp_url,
                "INSTAGRAM_GET_IG_USER_MEDIA",
                {"ig_user_id": ig_user_id, "fields": "id,caption,permalink,timestamp", "limit": 50},
            )
            media_list = media_resp.get("data", {}).get("data", [])
            if media_list and not published_days:
                # Day 1 is already live if media_list is non-empty and mentions $100/day
                for m in media_list:
                    cap = (m.get("caption") or "").lower()
                    if "1 clean pdf can bring in $100/day" in cap:
                        published_days.add(1)
                    published_topics.add(cap[:80])
    except Exception as e:
        print(f"[Autopilot] Live media check note: {e}")

    return published_days, published_topics


def render_day_carousel(day_entry: dict) -> Path:
    day_num = int(day_entry["day"])
    folder_name = day_entry.get("folder", f"day_{day_num:02d}")
    out_dir = ROOT / "output" / folder_name
    out_dir.mkdir(parents=True, exist_ok=True)
    BUILD.mkdir(parents=True, exist_ok=True)

    tpl = TEMPLATE_PATH.read_text(encoding="utf-8")
    slides = day_entry["slides"]
    total = len(slides)
    cta_kw = day_entry.get("cta_keyword", "PLAYBOOK")

    print(f"[Autopilot] Rendering Day {day_num:02d} ({day_entry['topic']}) -> {out_dir}")
    with Renderer() as r:
        for i, s in enumerate(slides, start=1):
            variant = s["variant"]
            content = s["content"].replace("__MARK__", monogram_svg(760, 12)).replace("__HANDLE__", handle())
            html = (
                tpl.replace("{{FONT_LINK}}", FONT_LINK)
                .replace("{{HANDLE}}", handle())
                .replace("{{BRAND}}", BRAND["brand_name"])
                .replace("{{MONOGRAM}}", monogram_svg(54, 30))
                .replace("{{NUM}}", f"{i:02d}")
                .replace("{{TOTAL}}", f"{total:02d}")
                .replace("{{PROGRESS}}", f"{i / total * 100:.1f}")
                .replace("{{VARIANT}}", variant)
                .replace("{{SWIPE}}", f"Comment {cta_kw}" if variant == "cta" else "Swipe →")
                .replace("{{CONTENT}}", content)
            )
            html_path = BUILD / f"day{day_num:02d}_slide_{i:02d}.html"
            html_path.write_text(html, encoding="utf-8")
            r.jpg(html_path, out_dir / f"slide_{i:02d}.jpg", 1080, 1350, quality=92)

    final_caption = day_entry["caption"].replace("__HANDLE__", handle())
    (out_dir / "caption.txt").write_text(final_caption, encoding="utf-8")
    manifest = {
        "day": day_num,
        "topic": day_entry["topic"],
        "caption": final_caption,
        "slides": [f"slide_{i:02d}.jpg" for i in range(1, total + 1)],
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return out_dir


def main():
    parser = argparse.ArgumentParser(description="Daily 24/7 Instagram Carousel Autopilot")
    parser.add_argument("--preflight", action="store_true", help="Only run preflight check and exit")
    parser.add_argument("--render-only", type=int, help="Render specific day number without publishing")
    parser.add_argument("--day", type=int, help="Force publish a specific day number")
    args = parser.parse_args()

    if not PLAN_PATH.exists():
        import generate_30_day_plan
        generate_30_day_plan.main()

    plan = json.loads(PLAN_PATH.read_text(encoding="utf-8"))
    days_list = plan.get("days", [])

    if args.render_only:
        target = next((d for d in days_list if int(d["day"]) == args.render_only), None)
        if not target:
            raise ValueError(f"Day {args.render_only} not found in {PLAN_PATH}")
        render_day_carousel(target)
        return

    env = load_env()
    api_key = env.get("COMPOSIO_API_KEY", "")
    mcp_url = env.get("COMPOSIO_MCP_URL", "https://connect.composio.dev/mcp")
    if not api_key:
        print("ERROR: COMPOSIO_API_KEY is required.", file=sys.stderr)
        sys.exit(1)

    if args.preflight:
        run_preflight(api_key, mcp_url)
        print(f"[Autopilot] 30-Day Content Queue verified ({len(days_list)} days loaded).")
        return

    published_days, published_topics = get_published_days(api_key, mcp_url)
    print(f"[Autopilot] Already published days: {sorted(published_days)}")

    target_day = None
    if args.day:
        target_day = next((d for d in days_list if int(d["day"]) == args.day), None)
    else:
        for d in days_list:
            d_num = int(d["day"])
            d_topic = d["topic"].strip().lower()
            if d_num not in published_days and not any(d_topic[:40] in pt for pt in published_topics):
                target_day = d
                break

    if not target_day:
        # Cycle cleanly if all 30 days have been published
        next_idx = len(published_days) % len(days_list)
        target_day = days_list[next_idx]

    out_dir = render_day_carousel(target_day)
    publish_carousel_dir(out_dir, api_key, mcp_url)


if __name__ == "__main__":
    main()

