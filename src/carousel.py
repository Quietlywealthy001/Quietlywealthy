"""Day 1 carousel: renders templates/carousel_slide.html x7 -> output/day_01/ (.png + .jpg + manifest.json + caption.txt)"""
import json
from common import BRAND, BUILD, FONT_LINK, ROOT, Renderer, handle, monogram_svg

TEMPLATE = ROOT / "templates" / "carousel_slide.html"
OUT = ROOT / "output" / "day_01"
TOPIC = "How 1 Clean PDF Can Bring In $100/Day Without Showing Your Face"

SLIDES = [
    ("cover", """
      <div class="kicker">Faceless Playbook · 01</div>
      <h1>How 1 clean PDF can bring in <em>$100/day</em> without showing your face.</h1>
      <p class="lead">The exact math + the 4-step system behind it. <b style="color:#F7F5F0">Save this</b> before you scroll.</p>
      <div class="cover-mark">__MARK__</div>"""),
    ("body", """
      <div class="kicker">The math first</div>
      <h2>$100/day is just <em>6 sales</em> of a $19 guide.</h2>
      <div class="math">
        <div><span>Storefront visits / day</span><span>300</span></div>
        <div><span>Conversion rate (typical 1–3%)</span><span>2%</span></div>
        <div><span>Sales × $19</span><span>6 × $19</span></div>
        <div class="total"><span>Daily revenue</span><span>$114</span></div>
      </div>
      <p class="note">Example math, not a guarantee. Your numbers depend on niche, offer and traffic.</p>"""),
    ("body", """
      <div class="step">Step 01</div>
      <h2>Sell a <em>painkiller</em>, not a topic.</h2>
      <p class="lead">People don't pay for "marketing." They pay to fix one specific, expensive problem — fast.</p>
      <div class="vs">
        <div class="card bad"><div class="lbl">Topic</div><div class="big">"Instagram growth tips"</div></div>
        <div class="card good"><div class="lbl" style="color:#10B981">Painkiller</div><div class="big">"Get your first 10 coaching clients from Instagram in 30 days"</div></div>
      </div>"""),
    ("body", """
      <div class="step">Step 02</div>
      <h2>Package <em>one outcome</em> into ~20 clean pages.</h2>
      <div class="flow">
        <div><b>1</b>The problem &amp; why it's costly</div>
        <div><b>2</b>Your named framework (3–5 steps)</div>
        <div><b>3</b>Step-by-step execution</div>
        <div><b>4</b>Templates, scripts &amp; examples</div>
        <div class="win"><b>5</b>A 7-day action plan</div>
      </div>
      <p class="note">No course, no filming, no face. One PDF, delivered instantly.</p>"""),
    ("body", """
      <div class="step">Step 03</div>
      <h2>Post 1 value carousel a day. <em>80/20.</em></h2>
      <div class="ratio"><div style="width:80%;background:#14181F;color:#F7F5F0;border:1px solid rgba(229,184,75,.25)">80% TEACH</div>
        <div style="width:20%;background:#E5B84B;color:#0B0D10">20% SELL</div></div>
      <div class="card"><div class="lbl">Why it works</div><div class="big">Teaching earns <span class="g">saves &amp; shares</span> → reach.
        Selling once every 5 posts converts that trust → <span class="g">sales</span>.</div></div>"""),
    ("body", """
      <div class="step">Step 04</div>
      <h2>Turn comments into <em>customers</em>.</h2>
      <div class="flow">
        <div><b>1</b>Post ends with: Comment "GUIDE"</div>
        <div><b>2</b>Auto-DM sends the free checklist</div>
        <div><b>3</b>They join your email list</div>
        <div><b>4</b>3 emails deliver value + the story</div>
        <div class="win"><b>5</b>Offer: the $19 playbook</div>
      </div>
      <p class="note">Use Meta-approved DM automation only. Never bots or fake engagement.</p>"""),
    ("cta", """
      <div class="center">
        <div class="kicker" style="justify-content:center">Free · 8 pages</div>
        <h2>Want the 7-day launch <em>checklist</em>?</h2>
        <div class="ctaBox"><p>Comment the word</p><div class="kw">GUIDE</div>
          <p>and I'll DM you the free <b style="color:#F7F5F0">7-Day Digital Product Launch Checklist</b>.</p></div>
        <p class="lead" style="font-size:30px">Follow <span style="color:#E5B84B">__HANDLE__</span> for a new playbook every day.</p>
      </div>"""),
]

CAPTION = """How 1 clean PDF can bring in $100/day — without showing your face 👇

The math is simpler than you think:
→ $19 guide × 6 sales = $114/day
→ 6 sales ≈ 300 storefront visits at a 2% conversion rate
(Example math, not a guarantee — results depend on niche, offer and traffic.)

The 4-step system:
1️⃣ Sell a painkiller, not a topic — one specific, expensive problem.
2️⃣ Package one outcome into ~20 clean pages (framework + steps + templates).
3️⃣ Post one value carousel a day: 80% teach, 20% sell.
4️⃣ Turn comments into customers with a comment-to-DM funnel.

Want my free 7-Day Digital Product Launch Checklist?
💬 Comment "GUIDE" and I'll send it to your DMs.

Save this for later & follow __HANDLE__ for a new business playbook every day.

#digitalproducts #facelessbusiness #passiveincomeideas #ebookbusiness #digitalmarketing #sidehustleideas #onlinebusinesstips #instagrammarketing #contentstrategy #solopreneur
"""


def build(r: Renderer) -> list:
    tpl = TEMPLATE.read_text(encoding="utf-8")
    total = len(SLIDES)
    outs = []
    BUILD.mkdir(parents=True, exist_ok=True)
    for i, (variant, content) in enumerate(SLIDES, start=1):
        content = content.replace("__MARK__", monogram_svg(760, 12)).replace("__HANDLE__", handle())
        html = (tpl.replace("{{FONT_LINK}}", FONT_LINK).replace("{{HANDLE}}", handle())
                .replace("{{BRAND}}", BRAND["brand_name"]).replace("{{MONOGRAM}}", monogram_svg(54, 30))
                .replace("{{NUM}}", f"{i:02d}").replace("{{TOTAL}}", f"{total:02d}")
                .replace("{{PROGRESS}}", f"{i / total * 100:.1f}").replace("{{VARIANT}}", variant)
                .replace("{{SWIPE}}", "Comment GUIDE" if variant == "cta" else "Swipe →")
                .replace("{{CONTENT}}", content))
        p = BUILD / f"day01_slide_{i:02d}.html"
        p.write_text(html, encoding="utf-8")
        outs.append(r.png(p, OUT / f"slide_{i:02d}.png", 1080, 1350))
        outs.append(r.jpg(p, OUT / f"slide_{i:02d}.jpg", 1080, 1350, quality=92))
    OUT.mkdir(parents=True, exist_ok=True)
    final_caption = CAPTION.replace("__HANDLE__", handle())
    (OUT / "caption.txt").write_text(final_caption, encoding="utf-8")
    manifest = {
        "topic": TOPIC,
        "caption": final_caption,
        "slides": [f"slide_{i:02d}.jpg" for i in range(1, total + 1)],
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return outs

