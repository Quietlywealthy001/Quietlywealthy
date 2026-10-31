"""Shared helpers: brand config, CSS, and a deterministic Playwright renderer.

Rule B (see .agent/rules): every visual + PDF is rendered from HTML/CSS via Playwright.
Playwright here only ever opens local file:// URLs — never instagram.com.
"""
from __future__ import annotations

import json
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
BRAND = json.loads((ROOT / "brand.json").read_text(encoding="utf-8"))
P = BRAND["palette"]

FONT_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800'
    '&family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,500;1,600&display=block" rel="stylesheet">'
)

BASE_CSS = """
:root{--obsidian:%(obsidian)s;--card:%(card)s;--white:%(white)s;--gold:%(gold)s;--emerald:%(emerald)s;
--serif:'Playfair Display',Georgia,'Times New Roman',serif;--sans:'Inter','Segoe UI',Arial,sans-serif;}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--obsidian);color:var(--white);font-family:var(--sans);
-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;font-variant-numeric:lining-nums}
""" % P


def handle() -> str:
    h = BRAND["handle"].strip()
    return h if h.startswith("@") else "@" + h


def doc(body: str, css: str = "", title: str = "render") -> str:
    return (
        f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title>{FONT_LINK}"
        f"<style>{BASE_CSS}{css}</style></head><body>{body}</body></html>"
    )


def write_html(name: str, html: str) -> Path:
    BUILD.mkdir(parents=True, exist_ok=True)
    path = BUILD / name
    path.write_text(html, encoding="utf-8")
    return path


_MASK_N = 0


def monogram_svg(size: int = 560, stroke: float = 16, bg: str | None = None) -> str:
    """Geometric gold monogram inside a double square frame (viewBox 0..1000).
    `bg` = background color used for the interlace knockouts."""
    g = P["gold"]
    o = bg or P["obsidian"]
    mono = BRAND.get("monogram", "OL")
    if mono == "OL":
        global _MASK_N
        _MASK_N += 1
        m = f"olm{_MASK_N}"
        sw = stroke * 1.15
        letters = f"""
        <defs>
          <mask id="{m}c" maskUnits="userSpaceOnUse" x="0" y="0" width="1000" height="1000">
            <rect width="1000" height="1000" fill="#fff"/>
            <path d="M570 520 V660" stroke="#000" stroke-width="{sw*3}"/></mask>
          <mask id="{m}l" maskUnits="userSpaceOnUse" x="0" y="0" width="1000" height="1000">
            <rect width="1000" height="1000" fill="#fff"/>
            <path d="M520 373 A135 135 0 0 1 600 450" fill="none" stroke="#000" stroke-width="{sw*3}"/></mask>
        </defs>
        <circle cx="475" cy="500" r="135" fill="none" stroke="{g}" stroke-width="{sw}" mask="url(#{m}c)"/>
        <path d="M570 322 V678 H735" fill="none" stroke="{g}" stroke-width="{sw}" stroke-linecap="square" mask="url(#{m}l)"/>
        """
    else:
        letters = (
            f'<text x="500" y="590" text-anchor="middle" font-family="Playfair Display, Georgia, serif" '
            f'font-weight="600" font-size="300" letter-spacing="-10" fill="{g}">{mono}</text>'
        )
    return f"""
    <svg width="{size}" height="{size}" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg">
      <rect x="150" y="150" width="700" height="700" fill="none" stroke="{g}" stroke-opacity=".45" stroke-width="3"/>
      <rect x="185" y="185" width="630" height="630" fill="none" stroke="{g}" stroke-width="{stroke*0.55}"/>
      <g fill="{g}">
        <rect x="490" y="140" width="20" height="20" transform="rotate(45 500 150)"/>
        <rect x="490" y="840" width="20" height="20" transform="rotate(45 500 850)"/>
        <rect x="140" y="490" width="20" height="20" transform="rotate(45 150 500)"/>
        <rect x="840" y="490" width="20" height="20" transform="rotate(45 850 500)"/>
      </g>
      {letters}
    </svg>"""


class Renderer:
    """Context manager wrapping one headless Chromium instance."""

    def __enter__(self):
        self._pw = sync_playwright().start()
        self.browser = self._pw.chromium.launch()
        return self

    def __exit__(self, *exc):
        self.browser.close()
        self._pw.stop()

    def _open(self, html_path: Path, w: int, h: int, scale: float = 1):
        page = self.browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=scale)
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
        page.evaluate("document.fonts.ready.then(() => true)")
        page.wait_for_timeout(150)
        return page

    def png(self, html_path: Path, out: Path, w: int, h: int, scale: float = 1, selector: str | None = None):
        out.parent.mkdir(parents=True, exist_ok=True)
        page = self._open(html_path, w, h, scale)
        if selector:
            page.locator(selector).first.screenshot(path=str(out))
        else:
            page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": w, "height": h})
        page.close()
        return out

    def jpg(self, html_path: Path, out: Path, w: int, h: int, quality: int = 92, scale: float = 1, selector: str | None = None):
        out.parent.mkdir(parents=True, exist_ok=True)
        page = self._open(html_path, w, h, scale)
        if selector:
            page.locator(selector).first.screenshot(path=str(out), type="jpeg", quality=quality)
        else:
            page.screenshot(path=str(out), type="jpeg", quality=quality, clip={"x": 0, "y": 0, "width": w, "height": h})
        page.close()
        return out

    def pdf(self, html_path: Path, out: Path, preview_dir: Path | None = None) -> dict:
        """Render a paged document (.page elements) to PDF; returns overflow report.
        Optionally screenshots every page to preview_dir for QA / artifacts."""
        out.parent.mkdir(parents=True, exist_ok=True)
        page = self._open(html_path, 816, 1056)
        report = page.evaluate(
            """() => [...document.querySelectorAll('.page')].map((p, i) => {
                const c = p.querySelector('.content') || p;
                return {page: i + 1, overflow: c.scrollHeight - c.clientHeight};
            })"""
        )
        if preview_dir:
            preview_dir.mkdir(parents=True, exist_ok=True)
            for i, el in enumerate(page.locator(".page").all(), start=1):
                el.screenshot(path=str(preview_dir / f"page_{i:02d}.png"))
        page.pdf(path=str(out), width="8.5in", height="11in", print_background=True,
                 margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}, prefer_css_page_size=True)
        page.close()
        return {"pages": len(report), "overflows": [r for r in report if r["overflow"] > 1]}
