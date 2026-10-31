"""Render the 4 inner Story slides (1080x1920 JPEG, quality=92) into output/highlight_stories/."""
from common import BRAND, ROOT, Renderer, doc, handle, monogram_svg, write_html

OUT = ROOT / "output" / "highlight_stories"

STORY_CSS = """
.stage{width:1080px;height:1920px;position:relative;overflow:hidden;
  background:radial-gradient(85% 55% at 50% 18%,#14181F 0%,#0B0D10 72%);color:var(--white);font-family:var(--sans)}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(247,245,240,.03) 1px,transparent 1px),
  linear-gradient(90deg,rgba(247,245,240,.03) 1px,transparent 1px);background-size:90px 90px;
  -webkit-mask-image:radial-gradient(75% 55% at 50% 25%,#000 0%,transparent 75%)}
.top{position:absolute;top:150px;left:90px;right:90px;display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:18px;font-size:24px;font-weight:700;letter-spacing:.26em;text-transform:uppercase;color:rgba(247,245,240,.85)}
.pill{font-size:20px;font-weight:800;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);
  border:1.5px solid rgba(229,184,75,.5);padding:12px 24px;border-radius:999px;background:rgba(20,24,31,.8)}
.main{position:absolute;top:310px;left:90px;right:90px}
.kicker{font-size:25px;font-weight:700;letter-spacing:.34em;color:var(--gold);text-transform:uppercase;
  display:flex;align-items:center;gap:18px;margin-bottom:28px}
.kicker:before{content:"";width:52px;height:3px;background:var(--gold)}
h1{font-family:var(--serif);font-size:84px;line-height:1.04;font-weight:700;letter-spacing:-.01em}
h1 em{font-style:italic;color:var(--gold);font-weight:600}
p.lead{font-size:33px;line-height:1.45;color:rgba(247,245,240,.78);margin-top:26px}
.cards{display:flex;flex-direction:column;gap:22px;margin-top:44px}
.card{background:var(--card);border:1px solid rgba(229,184,75,.22);border-radius:24px;padding:34px 40px}
.card .tag{font-size:19px;font-weight:800;letter-spacing:.28em;color:var(--gold);text-transform:uppercase;margin-bottom:10px}
.card .tag.em{color:var(--emerald)}
.card h3{font-family:var(--serif);font-size:40px;font-weight:700;margin-bottom:8px;color:var(--white)}
.card p{font-size:28px;line-height:1.42;color:rgba(247,245,240,.78)}
.checks{list-style:none;margin-top:42px;display:flex;flex-direction:column;gap:18px}
.checks li{background:var(--card);border:1px solid rgba(247,245,240,.08);border-radius:20px;padding:26px 32px 26px 92px;
  position:relative;font-size:30px;line-height:1.38;color:var(--white)}
.checks li b{color:var(--gold)}
.checks li:before{content:"✓";position:absolute;left:30px;top:50%;transform:translateY(-50%);width:42px;height:42px;
  border-radius:50%;background:var(--emerald);color:var(--obsidian);font-weight:900;font-size:26px;
  display:flex;align-items:center;justify-content:center}
/* Link sticker target zone centered around y=1380px */
.sticker-zone{position:absolute;left:140px;right:140px;top:1290px;height:210px;border:2.5px dashed rgba(229,184,75,.65);
  border-radius:28px;background:rgba(20,24,31,.72);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.sticker-zone .hint{font-size:21px;font-weight:800;letter-spacing:.32em;color:var(--gold);text-transform:uppercase;margin-bottom:10px}
.sticker-zone .cta{font-family:var(--serif);font-size:40px;font-weight:700;color:var(--white)}
.price-row{display:flex;align-items:baseline;gap:24px;margin-top:34px}
.price-row .now{font-family:var(--serif);font-size:74px;font-weight:700;color:var(--emerald);line-height:1}
.price-row .was{font-size:34px;color:rgba(247,245,240,.4);text-decoration:line-through}
.price-row .note{font-size:24px;font-weight:700;letter-spacing:.2em;color:var(--gold);text-transform:uppercase}
.ftr{position:absolute;left:90px;right:90px;bottom:120px;display:flex;justify-content:space-between;align-items:center;
  border-top:1px solid rgba(247,245,240,.12);padding-top:28px;font-size:24px;letter-spacing:.28em;color:rgba(247,245,240,.55);font-weight:600;text-transform:uppercase}
"""

STORIES = [
    (
        "story_01_start_here.jpg",
        "01 · Start Here",
        f"""
        <div class="kicker">Welcome to {BRAND['brand_name']}</div>
        <h1>Systems for <em>faceless</em> digital product operators.</h1>
        <p class="lead">Zero fluff. Real unit economics. Tactical playbooks you can execute in 60–90 minutes a day.</p>
        <div class="cards">
          <div class="card"><div class="tag">Who We Help</div>
            <h3>Solopreneurs &amp; Quiet Operators</h3>
            <p>Build, package, and sell high-margin PDF guides &amp; playbooks without ever going on camera.</p></div>
          <div class="card"><div class="tag">How To Use This Page</div>
            <h3>1. Save Daily Carousels</h3>
            <p>Every post breaks down one actionable funnel, pricing model, or conversion system.</p></div>
          <div class="card"><div class="tag em">Your First Step</div>
            <h3>2. Grab the Free 7-Day Checklist</h3>
            <p>Tap the <b>FREE GUIDE</b> highlight next or DM us the word <b>PLAYBOOK</b> to start today.</p></div>
        </div>
        """,
    ),
    (
        "story_02_free_guide.jpg",
        "02 · Free Guide",
        """
        <div class="kicker">Free 8-Page PDF Download</div>
        <h1>The 7-Day Digital Product <em>Launch</em> Checklist</h1>
        <p class="lead">Go from blank page to a live, automated PDF product in one focused week:</p>
        <ul class="checks">
          <li><b>Day 1–2:</b> Pick &amp; validate a profitable painkiller niche</li>
          <li><b>Day 3–4:</b> Outline &amp; draft a 20-page actionable guide</li>
          <li><b>Day 5–6:</b> Package in clean editorial style &amp; connect checkout</li>
          <li><b>Day 7:</b> Launch with the Comment-to-DM conversion system</li>
        </ul>
        """,
        """
        <div class="sticker-zone">
          <div class="hint">↓ Tap Link Below To Download Free ($0) ↓</div>
          <div class="cta">Get The 7-Day Checklist</div>
        </div>
        """,
    ),
    (
        "story_03_playbooks.jpg",
        "03 · Core Playbook",
        """
        <div class="kicker">23-Page Executive Manual</div>
        <h1>Faceless Business <em>Marketing</em> Playbook</h1>
        <ul class="checks" style="margin-top:30px;gap:14px">
          <li><b>System 01:</b> 3P Niche Validation + 72-Hour Test Scorecard</li>
          <li><b>System 02:</b> Irresistible Offer Stacking &amp; Pricing Math</li>
          <li><b>System 03:</b> 9-Block Storefront &amp; Auto-Delivery Setup</li>
          <li><b>System 04:</b> The 80/20 Carousel System + 30 Proven Hooks</li>
          <li><b>System 05:</b> Comment-to-DM Scripts + 5-Email Sequence</li>
        </ul>
        <div class="price-row">
          <span class="now">$19</span><span class="was">$47</span>
          <span class="note">Launch Offer · Instant PDF</span>
        </div>
        """,
        """
        <div class="sticker-zone">
          <div class="hint">↓ Tap Link Sticker To Get Instant Access ↓</div>
          <div class="cta">Download The Full Playbook — $19</div>
        </div>
        """,
    ),
    (
        "story_04_proof_faq.jpg",
        "04 · Proof & FAQ",
        """
        <div class="kicker">Before You Download</div>
        <h1>Quick Buyer <em>FAQs</em></h1>
        <p class="lead">Everything you need to know about our playbooks and how they work.</p>
        <div class="cards">
          <div class="card"><div class="tag em">01 · Instant PDF Delivery</div>
            <h3>How do I receive my playbook?</h3>
            <p>Immediately after checkout, you get an instant download link plus an email copy you can read on phone, tablet, or desktop.</p></div>
          <div class="card"><div class="tag">02 · Beginner-Friendly</div>
            <h3>Do I need an existing audience or product?</h3>
            <p>No. System 01 starts at zero — validating a profitable problem in 72 hours before you write a single page.</p></div>
          <div class="card"><div class="tag">03 · Actionable Templates</div>
            <h3>Is this theory or plug-and-play?</h3>
            <p>Zero fluff. Includes weighted scorecards, pricing tables, 30 carousel hooks, DM scripts, and a 5-email sales sequence.</p></div>
        </div>
        """,
    ),
]


def build(r: Renderer) -> list:
    outs = []
    for item in STORIES:
        fname, badge, main_html = item[0], item[1], item[2]
        extra_html = item[3] if len(item) > 3 else ""
        body = f"""
        <div class="stage">
          <div class="grid"></div>
          <div class="top">
            <div class="brand">{monogram_svg(64, 24)}<span>{BRAND['brand_name']}</span></div>
            <div class="pill">{badge}</div>
          </div>
          <div class="main">{main_html}</div>
          {extra_html}
          <div class="ftr"><span>{handle()}</span><span>DM "PLAYBOOK" Anytime</span></div>
        </div>"""
        p = write_html(fname.replace(".jpg", ".html"), doc(body, STORY_CSS, badge))
        outs.append(r.jpg(p, OUT / fname, 1080, 1920, quality=92))
    return outs

