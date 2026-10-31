---
trigger: always_on
description: Permanent Instagram safety + brand rendering rules for this workspace.
---

# Instagram Brand & Safety Rules (ALWAYS ON)

## Rule A — Official API publishing only
- NEVER use browser automation (Playwright, Selenium, Puppeteer, browser subagents, headless
  Chrome, extensions, RPA) to log in to Instagram or to publish, schedule, like, comment, follow or DM.
- NEVER use unofficial/private Instagram APIs (instagrapi, instagram-private-api, etc.).
- Publishing is done **only** via:
  - Official **Instagram Graph API v26.0** (`/{ig-user-id}/media` → `/{ig-user-id}/media_publish`,
    carousels via `is_carousel_item=true` children + `media_type=CAROUSEL`), or
  - **Composio MCP** Instagram toolkit (which calls the official Graph API).
- Respect official rate limits (max 100 API-published posts / 24h; we target 1–2/day).
- Playwright is allowed ONLY for local rendering of our own HTML files (`file://`), never for instagram.com.
- Read-only public availability checks of handles (anonymous HTTP GET, no login) are permitted.

## Rule B — Deterministic rendering
- All visuals (logo, highlights, carousels, mockups) and all PDFs are rendered from HTML/CSS
  using Playwright Chromium (`page.screenshot` for PNG, `page.pdf` for PDF).
- NEVER use diffusion/image-generation models for slides or anything containing text.
- Output sizes: carousel `1080x1350` (4:5), story/highlight `1080x1920`, logo `1080x1080`, PDFs A4/Letter.

## Brand Palette (use only these)
| Token | Hex |
|---|---|
| Deep Obsidian | `#0B0D10` |
| Card Surface | `#14181F` |
| Warm Editorial White | `#F7F5F0` |
| Executive Gold | `#E5B84B` |
| Growth Emerald | `#10B981` |

Opacity variants (e.g. `rgba(247,245,240,.6)`) of these colors are allowed; new hues are not.

## Content compliance
- No guaranteed-income claims. Income examples must be framed as math/illustrations, not promises.
- Captions include a clear CTA and the disclaimer-friendly phrasing "example math, not a guarantee" where numbers are used.

