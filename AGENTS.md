# AGENTS.md — Faceless Playbook Instagram Business

Workspace memory for every agent working in this repo. Read this first.

## Mission
Run a faceless Instagram brand that sells Ebooks, Business Playbooks and Marketing Guides,
with automated daily posting via the **official** Instagram Graph API.

## Permanent Rules (non-negotiable)
Full text: [`.agent/rules/instagram-brand-and-safety.md`](.agent/rules/instagram-brand-and-safety.md)

0. **LOCKED ACCOUNT IDENTITY (`@quietlywealthy001` / `Omowumi Ibrahim`).**
   NEVER modify the user's Instagram username (`quietlywealthy001`) or Display Name (`Omowumi Ibrahim`). Those two fields are permanently locked!
1. **No browser automation for publishing.** Never use Playwright/Selenium/Puppeteer/browser
   subagents or any unofficial/private API to log in to, or publish to, Instagram.
   Publishing happens **only** through the Official Instagram Graph API (v26.0) or the
   Composio MCP Instagram toolkit (which wraps the official API). Keeps the account trust score clean.
2. **Deterministic rendering only.** All slides, covers, logos and PDFs are rendered from
   HTML/CSS with Playwright (Chromium). Never use diffusion / image-generation models
   for anything that contains text.
3. **Brand palette (only these colors):**

   | Token | Hex | Use |
   |---|---|---|
   | Deep Obsidian | `#0B0D10` | Backgrounds |
   | Card Surface | `#14181F` | Cards, panels |
   | Warm Editorial White | `#F7F5F0` | Body text, light pages |
   | Executive Gold | `#E5B84B` | Accents, headlines, logo |
   | Growth Emerald | `#10B981` | Positive numbers, CTAs, checkmarks |

## Brand
- Default brand: **Quietly Wealthy** — handle `@quietlywealthy001` (Display Name locked: `Omowumi Ibrahim`; configured in `brand.json`).
- Alternates: `@gildedplaybook.co` (Gilded Playbook), `@marginmemo.co` (Margin Memo).
- Typography: Serif display (Playfair Display / Georgia fallback) + Inter / Segoe UI for body.
- Voice: executive, zero fluff, numbers-first, calm authority. No hype emojis, no fake income claims.

## Layout
```
brand.json                 # single source of truth for name/handle/palette
templates/                 # reusable HTML templates (carousel_slide.html ...)
src/                       # Python render pipeline (Playwright)
assets/brand/              # logo, highlights, mockups
products/                  # sellable PDFs
output/day_XX/             # rendered daily carousels + caption.txt
```

## Commands
```powershell
python src/render_all.py          # re-render every asset, PDF and Day 1 carousel
```

## Sprint status
- [x] Sprint 1 — workspace memory, handles, brand kit, 2 products, Day 1 carousel (local only)
- [ ] Sprint 2 — Graph API / Composio connection, scheduler, content calendar
