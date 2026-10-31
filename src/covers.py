"""Book covers as em-scaled HTML components (reused by the PDFs and the 3D mockup)."""
from common import BRAND, handle, monogram_svg

COVER_CSS = """
.cv{position:relative;width:51em;height:66em;overflow:hidden;font-family:var(--sans)}
.cv *{line-height:1.15}
.cv-dark{background:radial-gradient(120% 75% at 85% 0%,#14181F 0%,#0B0D10 62%);color:var(--white)}
.cv-light{background:var(--white);color:var(--obsidian)}
.cv .frame{position:absolute;inset:2.2em;border:.09em solid rgba(229,184,75,.6)}
.cv .rings{position:absolute;right:-14em;top:-14em;width:40em;height:40em;border-radius:50%;
  border:.12em solid rgba(229,184,75,.14);box-shadow:0 0 0 3em rgba(11,13,16,0),inset 0 0 0 4em rgba(229,184,75,.035)}
.cv .rings:after{content:"";position:absolute;inset:7em;border-radius:50%;border:.12em solid rgba(229,184,75,.10)}
.cv .top{position:absolute;top:4.6em;left:4.8em;right:4.8em;display:flex;align-items:center;justify-content:space-between}
.cv .brand{display:flex;align-items:center;gap:1em;font-size:1em;font-weight:700;letter-spacing:.32em;text-transform:uppercase}
.cv .brand svg{width:3.6em;height:3.6em}
.cv .vol{font-size:.8em;letter-spacing:.3em;text-transform:uppercase;opacity:.65;font-weight:600}
.cv .mid{position:absolute;left:4.8em;right:4.8em;top:17em}
.cv .kick{font-size:1em;letter-spacing:.42em;text-transform:uppercase;color:var(--gold);font-weight:700;
  display:flex;align-items:center;gap:1em}
.cv .kick:before{content:"";width:3.2em;height:.12em;background:var(--gold)}
.cv h1{font-family:var(--serif);font-weight:700;font-size:6.1em;line-height:1.02;letter-spacing:-.01em;margin-top:.45em}
.cv h1 em{font-style:italic;color:var(--gold);font-weight:600}
.cv .sub{font-size:1.32em;line-height:1.5;margin-top:1.5em;max-width:30em;opacity:.78}
.cv .sys{position:absolute;left:4.8em;right:4.8em;bottom:6.2em;display:grid;grid-template-columns:repeat(5,1fr);gap:.8em}
.cv .sys div{border-top:.15em solid var(--gold);padding-top:.9em;font-size:.86em;font-weight:600;line-height:1.35}
.cv .sys b{display:block;font-family:var(--serif);color:var(--gold);font-size:1.6em;margin-bottom:.25em}
.cv .foot{position:absolute;left:4.8em;right:4.8em;bottom:3.6em;display:flex;justify-content:space-between;
  font-size:.78em;letter-spacing:.28em;text-transform:uppercase;opacity:.55;font-weight:600}
.cv .badge{display:inline-block;background:var(--emerald);color:var(--obsidian);font-weight:800;
  font-size:.9em;letter-spacing:.3em;padding:.7em 1.2em;text-transform:uppercase;border-radius:.3em}
.cv .days{position:absolute;left:4.8em;right:4.8em;bottom:7em;display:grid;grid-template-columns:repeat(7,1fr);gap:.6em}
.cv .days div{background:var(--obsidian);color:var(--white);border-radius:.5em;padding:1.1em .4em;text-align:center;
  font-size:.82em;font-weight:600;letter-spacing:.08em}
.cv .days div b{display:block;font-family:var(--serif);font-size:2.2em;color:var(--gold);margin-bottom:.15em}
.cv .days div.go{background:var(--emerald);color:var(--obsidian)}
.cv .days div.go b{color:var(--obsidian)}
"""


def playbook_cover() -> str:
    return f"""
<div class="cv cv-dark">
  <div class="rings"></div><div class="frame"></div>
  <div class="top"><div class="brand">{monogram_svg(60, 22)}{BRAND['brand_name']}</div>
    <div class="vol">Vol. 01 &nbsp;·&nbsp; Executive Edition</div></div>
  <div class="mid">
    <div class="kick">The Operator's Playbook</div>
    <h1>Faceless Business <em>Marketing</em> Playbook</h1>
    <div class="sub">Validate a niche, stack an irresistible offer, and turn carousels + DMs into
      daily digital product sales &mdash; without ever showing your face.</div>
  </div>
  <div class="sys">
    <div><b>01</b>Niche Validation</div><div><b>02</b>Offer Stacking</div><div><b>03</b>Storefront Setup</div>
    <div><b>04</b>80/20 Carousel System</div><div><b>05</b>Comment-to-DM Funnels</div>
  </div>
  <div class="foot"><span>{handle()}</span><span>Zero fluff · Real math · Scripts</span></div>
</div>"""


def checklist_cover() -> str:
    return f"""
<div class="cv cv-light">
  <div class="frame"></div>
  <div class="top"><div class="brand">{monogram_svg(60, 22, bg="#F7F5F0")}{BRAND['brand_name']}</div>
    <span class="badge">Free Guide</span></div>
  <div class="mid">
    <div class="kick">Beginner Launch System</div>
    <h1>The 7-Day Digital Product <em>Launch</em> Checklist</h1>
    <div class="sub">Pick a profitable problem, package it into a clean PDF guide, and launch it to
      paying buyers in one focused week.</div>
  </div>
  <div class="days">
    <div><b>1</b>Problem</div><div><b>2</b>Validate</div><div><b>3</b>Outline</div><div><b>4</b>Write</div>
    <div><b>5</b>Package</div><div><b>6</b>Store</div><div class="go"><b>7</b>Launch</div>
  </div>
  <div class="foot"><span>{handle()}</span><span>8 pages · Tick-box format</span></div>
</div>"""
