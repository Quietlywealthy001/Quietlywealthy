"""Brand kit: logo, avatar, 4 story-highlight covers, 3D product mockup."""
from common import BRAND, ROOT, Renderer, doc, handle, monogram_svg, write_html
from covers import COVER_CSS, checklist_cover, playbook_cover

OUT = ROOT / "assets" / "brand"

LOGO_CSS = """
.stage{width:1080px;height:1080px;position:relative;overflow:hidden;
  background:radial-gradient(70% 70% at 50% 42%,#14181F 0%,#0B0D10 72%)}
.mark{position:absolute;left:50%;top:__TOP__px;transform:translateX(-50%)}
.word{position:absolute;left:0;right:0;top:790px;text-align:center;font-family:var(--serif);font-weight:600;
  font-size:58px;letter-spacing:.24em;color:var(--white);padding-left:.24em}
.tag{position:absolute;left:0;right:0;top:885px;text-align:center;font-size:19px;letter-spacing:.55em;
  color:var(--gold);font-weight:600;text-transform:uppercase;padding-left:.55em}
.rule{position:absolute;left:50%;top:916px;width:120px;height:1px;background:rgba(229,184,75,.6);transform:translateX(-50%)}
"""

HL_CSS = """
.stage{width:1080px;height:1920px;position:relative;overflow:hidden;
  background:radial-gradient(60% 40% at 50% 50%,#14181F 0%,#0B0D10 75%)}
.ring{position:absolute;left:50%;top:50%;width:760px;height:760px;margin:-380px 0 0 -380px;border-radius:50%;
  background:radial-gradient(circle at 50% 35%,#14181F 0%,#0B0D10 100%);
  border:6px solid var(--gold);box-shadow:0 0 0 22px rgba(229,184,75,.10),0 0 0 23px rgba(229,184,75,.35)}
.icon{position:absolute;left:50%;top:50%;transform:translate(-50%,-78%)}
.label{position:absolute;left:0;right:0;top:1035px;text-align:center;font-weight:800;font-size:64px;
  letter-spacing:.14em;color:var(--white);padding-left:.14em}
.label small{display:block;font-size:24px;letter-spacing:.5em;color:var(--gold);font-weight:600;margin-top:22px;padding-left:.5em}
.brandline{position:absolute;left:0;right:0;bottom:170px;text-align:center;font-size:26px;letter-spacing:.45em;
  color:rgba(247,245,240,.45);font-weight:600;text-transform:uppercase}
.top{position:absolute;left:0;right:0;top:190px;display:flex;justify-content:center;opacity:.9}
"""

G, E, W = "#E5B84B", "#10B981", "#F7F5F0"
ICONS = {
    "START HERE": f"""<svg width="300" height="300" viewBox="0 0 100 100" fill="none" stroke="{G}" stroke-width="3.2"
        stroke-linecap="round" stroke-linejoin="round"><circle cx="50" cy="50" r="34"/>
        <path d="M50 16v8M50 76v8M16 50h8M76 50h8" stroke-opacity=".6"/>
        <path d="M62 38 L44 46 L38 62 L56 54 Z" fill="{G}" fill-opacity=".15"/><circle cx="50" cy="50" r="3" fill="{E}" stroke="{E}"/></svg>""",
    "FREE GUIDE": f"""<svg width="300" height="300" viewBox="0 0 100 100" fill="none" stroke="{G}" stroke-width="3.2"
        stroke-linecap="round" stroke-linejoin="round"><path d="M30 14h28l14 14v58H30z"/><path d="M58 14v14h14"/>
        <path d="M40 44h22M40 54h22M40 64h12" stroke-opacity=".6"/>
        <circle cx="70" cy="74" r="13" fill="#0B0D10" stroke="{E}"/><path d="M70 67v12M64.5 74.5 70 80l5.5-5.5" stroke="{E}"/></svg>""",
    "PLAYBOOKS": f"""<svg width="300" height="300" viewBox="0 0 100 100" fill="none" stroke="{G}" stroke-width="3.2"
        stroke-linecap="round" stroke-linejoin="round"><path d="M50 28c-8-6-20-8-34-7v52c14-1 26 1 34 7 8-6 20-8 34-7V21c-14-1-26 1-34 7z"/>
        <path d="M50 28v52"/><path d="M24 36c7 0 13 1 18 3M24 46c7 0 13 1 18 3M58 39c5-2 11-3 18-3M58 49c5-2 11-3 18-3" stroke-opacity=".55"/>
        <path d="M60 58l5 5 10-11" stroke="{E}"/></svg>""",
    "PROOF & FAQ": f"""<svg width="300" height="300" viewBox="0 0 100 100" fill="none" stroke="{G}" stroke-width="3.2"
        stroke-linecap="round" stroke-linejoin="round"><path d="M18 24h52a6 6 0 0 1 6 6v28a6 6 0 0 1-6 6H44L30 76V64H18a6 6 0 0 1-6-6V30a6 6 0 0 1 6-6z"/>
        <path d="M30 44l9 9 18-18" stroke="{E}"/><path d="M82 40h4a4 4 0 0 1 4 4v24a4 4 0 0 1-4 4h-6v8l-10-8H56" stroke-opacity=".55"/></svg>""",
}
SUBS = {"START HERE": "NEW? BEGIN HERE", "FREE GUIDE": "7-DAY CHECKLIST", "PLAYBOOKS": "THE LIBRARY",
        "PROOF & FAQ": "RESULTS · ANSWERS"}

MOCK_CSS = COVER_CSS + """
.stage{width:1600px;height:1200px;position:relative;overflow:hidden;
  background:radial-gradient(55% 60% at 70% 52%,#14181F 0%,#0B0D10 70%)}
.glow{position:absolute;left:820px;top:170px;width:760px;height:860px;border-radius:50%;
  background:radial-gradient(closest-side,rgba(229,184,75,.20),rgba(229,184,75,0));filter:blur(10px)}
.floor{position:absolute;left:700px;top:1010px;width:900px;height:90px;border-radius:50%;
  background:radial-gradient(closest-side,rgba(0,0,0,.85),rgba(0,0,0,0))}
.scene{position:absolute;perspective:2600px}
.book{position:relative;transform-style:preserve-3d}
.book .face{position:absolute;inset:0;overflow:hidden;backface-visibility:hidden}
.book .face:after{content:"";position:absolute;inset:0;
  background:linear-gradient(105deg,rgba(255,255,255,.0) 0%,rgba(255,255,255,.10) 22%,rgba(255,255,255,0) 38%,rgba(0,0,0,.18) 100%)}
.book .spine{position:absolute;top:0;height:100%;transform-origin:left center;transform:rotateY(-90deg);backface-visibility:hidden;
  background:linear-gradient(90deg,#0B0D10,#14181F 40%,#0B0D10);border-left:1px solid rgba(229,184,75,.4)}
.book .spine span{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(90deg);white-space:nowrap;
  color:var(--gold);font-weight:700;letter-spacing:.35em;font-size:15px}
.book .pages{position:absolute;top:1%;height:98%;transform-origin:left center;
  background:linear-gradient(90deg,rgba(11,13,16,0),rgba(11,13,16,.45)),repeating-linear-gradient(90deg,#F7F5F0 0 3px,rgba(247,245,240,.82) 3px 4px)}
.b1{left:960px;top:150px}
.b1 .book{width:560px;height:725px;transform:rotateY(-24deg) rotateX(3deg)}
.b1 .face{font-size:10.98px;box-shadow:0 40px 80px rgba(0,0,0,.55)}
.b1 .spine{left:0;width:56px}
.b1 .pages{left:560px;width:56px;transform:rotateY(90deg);transform-origin:left center}
.b2{left:700px;top:330px}
.b2 .book{width:400px;height:518px;transform:rotateY(-18deg) rotateZ(-6deg)}
.b2 .face{font-size:7.84px;box-shadow:0 30px 60px rgba(0,0,0,.6)}
.b2 .spine{left:0;width:16px}
.copy{position:absolute;left:110px;top:150px;width:560px}
.copy .eyebrow{color:var(--gold);font-weight:700;letter-spacing:.38em;font-size:17px;text-transform:uppercase}
.copy h2{font-family:var(--serif);font-size:66px;line-height:1.05;margin-top:26px;font-weight:700}
.copy h2 em{color:var(--gold);font-weight:600}
.copy ul{list-style:none;margin-top:40px}
.copy li{font-size:23px;line-height:1.4;padding:13px 0 13px 46px;position:relative;border-bottom:1px solid rgba(247,245,240,.08);color:rgba(247,245,240,.88)}
.copy li:before{content:"";position:absolute;left:0;top:19px;width:24px;height:24px;border-radius:50%;
  background:var(--emerald) url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M6 12.5l4 4 8-9' fill='none' stroke='%230B0D10' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/></svg>") center/16px no-repeat}
.price{display:flex;align-items:center;gap:22px;margin-top:44px}
.price .now{font-family:var(--serif);font-size:84px;color:var(--gold);font-weight:700;line-height:1}
.price .was{font-size:30px;color:rgba(247,245,240,.4);text-decoration:line-through}
.price .bonus{background:rgba(16,185,129,.12);color:var(--emerald);border:1px solid rgba(16,185,129,.45);
  font-weight:700;font-size:16px;letter-spacing:.2em;padding:12px 16px;border-radius:6px;text-transform:uppercase}
.seal{position:absolute;left:1395px;top:860px;width:170px;height:170px;border-radius:50%;background:var(--gold);
  color:var(--obsidian);display:flex;flex-direction:column;align-items:center;justify-content:center;
  box-shadow:0 0 0 8px rgba(229,184,75,.18),0 20px 40px rgba(0,0,0,.5);transform:rotate(10deg);text-align:center}
.seal b{font-family:var(--serif);font-size:46px;line-height:1}
.seal span{font-size:13px;font-weight:800;letter-spacing:.2em;margin-top:6px}
.handle{position:absolute;left:110px;bottom:70px;font-size:18px;letter-spacing:.35em;color:rgba(247,245,240,.5);font-weight:600;text-transform:uppercase}
"""


def build(r: Renderer) -> list:
    outs = []
    # 1) Logo 1080x1080 (with wordmark)
    body = f"""<div class="stage"><div class="mark">{monogram_svg(700, 16)}</div>
      <div class="word">{BRAND['brand_name'].upper()}</div>
      <div class="tag">Playbooks · Ebooks · Guides</div></div>"""
    p = write_html("logo.html", doc(body, LOGO_CSS.replace("__TOP__", "110")))
    outs.append(r.png(p, OUT / "logo.png", 1080, 1080))
    # 1b) Avatar (monogram only — survives Instagram's circular crop)
    body = f"""<div class="stage"><div class="mark">{monogram_svg(900, 14)}</div></div>"""
    p = write_html("avatar.html", doc(body, LOGO_CSS.replace("__TOP__", "40")))
    outs.append(r.png(p, OUT / "avatar_profile.png", 1080, 1080))

    # 2) Highlight covers 1080x1920
    for i, (title, icon) in enumerate(ICONS.items(), start=1):
        slug = title.lower().replace(" & ", "_").replace(" ", "_")
        body = f"""<div class="stage"><div class="top">{monogram_svg(120, 26)}</div>
          <div class="ring"></div><div class="icon">{icon}</div>
          <div class="label">{title}<small>{SUBS[title]}</small></div>
          <div class="brandline">{handle()}</div></div>"""
        p = write_html(f"highlight_{slug}.html", doc(body, HL_CSS))
        outs.append(r.png(p, OUT / "highlights" / f"{i:02d}_{slug}.png", 1080, 1920))

    # 3) 3D mockup 1600x1200
    body = f"""<div class="stage"><div class="glow"></div><div class="floor"></div>
      <div class="copy"><div class="eyebrow">{BRAND['brand_name']} · Vol. 01</div>
        <h2>The Faceless Business <em>Marketing</em> Playbook</h2>
        <ul><li>23-page executive ebook &mdash; zero fluff</li>
          <li>Niche validation scorecard + 72-hour test</li>
          <li>Offer-stack &amp; pricing math worksheets</li>
          <li>80/20 carousel system + 30 hook templates</li>
          <li>Comment-to-DM scripts &amp; 5-email sequence</li></ul>
        <div class="price"><span class="now">$19</span><span class="was">$49</span>
          <span class="bonus">+ Free 7-Day Checklist</span></div></div>
      <div class="scene b2"><div class="book"><div class="spine"></div><div class="face">{checklist_cover()}</div></div></div>
      <div class="scene b1"><div class="book"><div class="spine"><span>{BRAND['brand_name'].upper()} · VOL. 01</span></div>
        <div class="pages"></div><div class="face">{playbook_cover()}</div></div></div>
      <div class="seal"><b>$19</b><span>INSTANT PDF</span></div>
      <div class="handle">{handle()}</div></div>"""
    p = write_html("mockup.html", doc(body, MOCK_CSS))
    outs.append(r.png(p, OUT / "playbook_3d_mockup.png", 1600, 1200))
    return outs


