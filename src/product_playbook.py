"""Product 2 — $19 core offer: The Faceless Business Marketing Playbook (23 pages)."""
from covers import playbook_cover
from doc_base import cover_page, page

L = "Faceless Business Marketing Playbook"


def opener(num, title, sub, bullets, n):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return page(f"""
<div style="margin-top:60px" class="secnum">{num}</div>
<div class="eyebrow" style="margin-top:26px">System {num} of 05</div>
<h2 style="font-size:52px">{title}</h2>
<p class="lede" style="max-width:560px">{sub}</p>
<div class="box" style="margin-top:34px;border:1px solid rgba(229,184,75,.25)">
<h4 style="margin-top:0;color:var(--gold)">In this system</h4><ol class="num" style="margin:0">{lis}</ol></div>
""", n, L, dark=True)


def pages() -> list[str]:
    P = [cover_page(playbook_cover())]

    # 2 — Contents
    P.append(page("""
<div class="eyebrow">Contents</div>
<h2>Five systems. One <em>faceless</em> sales machine.</h2>
<p class="lede">Read it once front to back (about 60 minutes), then use it as a manual. Every section ends in actions, tables or scripts you can use the same day.</p>
<ul class="toc">
<li><b>00</b>The Operator's Math<span class="dots"></span><i>03</i></li>
<li><b>01</b>Niche Validation — pick a market that already pays<span class="dots"></span><i>04</i></li>
<li><b>02</b>Irresistible Offer Stacking — make the yes easy<span class="dots"></span><i>07</i></li>
<li><b>03</b>Storefront Setup — a checkout that sells while you sleep<span class="dots"></span><i>10</i></li>
<li><b>04</b>The 80/20 Carousel Conversion System<span class="dots"></span><i>13</i></li>
<li><b>05</b>Comment-to-DM Sales Funnels<span class="dots"></span><i>18</i></li>
<li><b>06</b>30-Day Execution Plan<span class="dots"></span><i>22</i></li>
<li><b>07</b>Operator Scorecard &amp; Next Steps<span class="dots"></span><i>23</i></li>
</ul>
<div class="grid2" style="margin-top:22px">
<div class="cell"><h3>This is for you if…</h3><ul class="dots">
<li>You want an online income without becoming an influencer.</li>
<li>You have a skill or experience someone would pay to shortcut.</li>
<li>You can commit ~60–90 minutes a day for 30 days.</li></ul></div>
<div class="cell"><h3>This is not for you if…</h3><ul class="dots">
<li>You want guaranteed income without testing anything.</li>
<li>You plan to buy followers, use bots or spam DMs.</li>
<li>You won't publish until everything is perfect.</li></ul></div>
</div>
<p class="small" style="margin-top:12px">Disclaimer: all revenue figures in this playbook are illustrative math, not promises or typical results. Platform features and fees change — verify current terms before you build.</p>
""", 2, L))

    # 3 — Operator's math
    P.append(page("""
<div class="eyebrow">00 · The Operator's Math</div>
<h2>Work backwards from the number, <em>not</em> the followers.</h2>
<p class="lede">Faceless brands win on systems, not personality. A system is just a funnel where every step has a number you can measure and improve.</p>
<div class="flowrow"><div><b>Reach</b>People who see a post</div><div><b>Profile</b>Tap your name</div><div><b>Click</b>Tap the link / DM</div><div><b>Lead</b>Get the free guide</div><div><b>Buyer</b>Buy the $19 playbook</div></div>
<h3>Worked example — the $100/day target</h3>
<table class="t">
<tr><th>Funnel step</th><th>Assumption</th><th class="num" style="text-align:right">Per day</th></tr>
<tr><td>Accounts reached (all posts)</td><td>Daily carousel + reshares</td><td class="num">15,000</td></tr>
<tr><td>Comment keyword / profile → DM</td><td>2% of reach</td><td class="num">300</td></tr>
<tr><td>Leads (open DM, take free guide)</td><td>70% of DMs</td><td class="num">210</td></tr>
<tr><td>Buy within 14 days (email + DM follow-up)</td><td>3% of leads</td><td class="num">6.3</td></tr>
<tr class="total"><td>Revenue</td><td>6.3 × $19</td><td class="num">$120</td></tr>
</table>
<div class="grid3" style="margin-top:6px">
<div class="stat"><b>×2</b><span>Double reach → double revenue. Fix with hooks &amp; shareability (System 04).</span></div>
<div class="stat"><b>×1.5</b><span>Lift lead→buyer from 3% to 4.5% with better offer + emails (Systems 02, 05).</span></div>
<div class="stat"><b>+$27</b><span>A $49 order bump at 15% take-rate adds ≈ $46/day on 6.3 orders.</span></div>
</div>
<div class="callout" style="margin-top:16px"><b>The operator's rule:</b> never try to fix everything. Each week, find the step with the biggest drop versus benchmark (page 21) and improve only that one.</div>
<h3>Your three levers</h3>
<ol class="num">
<li><b>Traffic</b> — more qualified reach (content volume × hook quality × shareability).</li>
<li><b>Conversion</b> — a sharper offer, better page, faster delivery of the first win.</li>
<li><b>Order value</b> — bumps, bundles and a next product. More money per buyer, same traffic.</li>
</ol>
""", 3, L))

    # 4 — Section 01 opener
    P.append(opener("01", "Niche <em>Validation</em>",
        "Most faceless pages die because they pick a topic instead of a market. A market is a group of people with a specific, expensive problem who already buy solutions.",
        ["The 3P Filter: Pain, Payer, Pipeline", "The 72-hour validation sprint (no product needed)",
         "Niche scorecard — 3 niches scored with real criteria", "Kill criteria: when to walk away"], 4))

    # 5 — 3P filter + sprint
    P.append(page("""
<div class="eyebrow">01 · Niche Validation</div>
<h2>The <em>3P Filter</em></h2>
<p>A profitable faceless niche must pass all three. Two out of three is how people end up with 10,000 followers and $0.</p>
<div class="grid3">
<div class="cell"><h3>1 · Pain</h3><p>The problem costs money, time, clients or status. Test: can you put a dollar figure on it?</p><p class="small"><b>Pass:</b> "Losing $2K/mo in no-show bookings." <b>Fail:</b> "Wants to be more productive."</p></div>
<div class="cell"><h3>2 · Payer</h3><p>The audience already buys solutions — courses, templates, tools, coaching.</p><p class="small"><b>Pass:</b> real estate agents, coaches, Etsy sellers, freelancers. <b>Fail:</b> teens, "everyone".</p></div>
<div class="cell"><h3>3 · Pipeline</h3><p>You can reach them daily on Instagram and they engage with educational carousels.</p><p class="small"><b>Pass:</b> 10+ active accounts in the niche with carousel posts above 300 likes.</p></div>
</div>
<h3>The 72-hour validation sprint</h3>
<table class="t">
<tr><th style="width:90px">When</th><th>Action</th><th>Pass threshold</th></tr>
<tr><td><b>Hour 0–4</b></td><td>Marketplace scan: Gumroad, Etsy, Payhip, Amazon Kindle, Stan Store pages linked from niche accounts.</td><td>3+ paid products with visible reviews/sales</td></tr>
<tr><td><b>Hour 4–8</b></td><td>Instagram scan: save the top 20 carousels in the niche. Log hook, saves/comments, CTA.</td><td>5+ posts with 100+ comments or clearly high saves</td></tr>
<tr><td><b>Hour 8–12</b></td><td>Language mining: read 100 comments/reviews/Reddit posts. Copy exact phrases.</td><td>10 repeated pain phrases</td></tr>
<tr><td><b>Hour 12–48</b></td><td>Publish 3 test carousels on your new account teaching sub-problems.</td><td>Saves ≥ likes ÷ 10 on at least one post</td></tr>
<tr><td><b>Hour 48–72</b></td><td>"Comment WAITLIST" post for a free mini-guide you'll send in 7 days.</td><td>10+ comments from real accounts</td></tr>
</table>
<div class="callout green"><b>Why it works:</b> you validate with behavior (money spent, posts saved, comments made) instead of opinions. New accounts have small reach, so judge ratios, not raw totals.</div>
<h3>Where faceless playbooks sell well</h3>
<ul class="dots">
<li><b>B2B-ish micro-niches:</b> freelancers, agency owners, coaches, real estate, local service businesses.</li>
<li><b>Money skills:</b> Etsy/print-on-demand, UGC creators, newsletter growth, freelancing on Upwork.</li>
<li><b>Career leverage:</b> resumes for a specific industry, interview playbooks, salary negotiation.</li>
</ul>
""", 5, L))

    # 6 — Scorecard
    P.append(page("""
<div class="eyebrow">01 · Niche Validation</div>
<h2>Niche scorecard: <em>worked example</em></h2>
<p>Score each criterion 1–5. Weighted total out of 100. Build only in niches scoring <b>70+</b>.</p>
<table class="t">
<tr><th>Criterion (weight)</th><th class="num" style="text-align:right">"Productivity tips"</th><th class="num" style="text-align:right">"Freelance copywriters: first clients"</th><th class="num" style="text-align:right">"Wedding photographers: bookings"</th></tr>
<tr><td>Pain — $ cost of problem (×5)</td><td class="num">2</td><td class="num">5</td><td class="num">4</td></tr>
<tr><td>Payer — already buy solutions (×5)</td><td class="num">2</td><td class="num">4</td><td class="num">4</td></tr>
<tr><td>Pipeline — reachable on IG (×4)</td><td class="num">5</td><td class="num">4</td><td class="num">5</td></tr>
<tr><td>Specificity — narrow outcome (×3)</td><td class="num">1</td><td class="num">5</td><td class="num">4</td></tr>
<tr><td>Your edge — knowledge/research (×3)</td><td class="num">3</td><td class="num">3</td><td class="num">3</td></tr>
<tr class="total"><td>Weighted score / 100</td><td class="num">48</td><td class="num">85</td><td class="num">81</td></tr>
</table>
<p class="small">Formula: Σ(score × weight) ÷ (5 × 20) × 100. Weights sum to 20.</p>
<div class="grid2" style="margin-top:12px">
<div class="cell"><h3>Read the result</h3><ul class="dots">
<li><b>85 · Copywriters</b> → build. High pain, buyers used to paying for skills, ultra-specific outcome.</li>
<li><b>81 · Photographers</b> → keep as niche #2 or a later product line.</li>
<li><b>48 · Productivity</b> → kill. Huge reach, no urgency, no payer.</li></ul></div>
<div class="cell"><h3>Kill criteria (walk away if…)</h3><ul class="dots">
<li>No paid products exist anywhere (no market, not "no competition").</li>
<li>Best niche carousels get likes but almost no saves or comments.</li>
<li>You can't name 3 specific outcomes people would pay for.</li>
<li>Regulated advice (medical, legal, investment) you can't support.</li></ul></div>
</div>
<h3>Turn the winner into a positioning statement</h3>
<div class="box"><p style="margin:0;font-size:14px">"<b class="gold">Operator Ledger</b> helps <b class="gold">new freelance copywriters</b> land <b class="gold">their first 3 retainer clients</b> in <b class="gold">30 days</b> — without cold-calling or a portfolio site."</p></div>
<p>Your bio, product title, carousel hooks and lead magnet all come from this one sentence. If a post doesn't serve it, don't publish it.</p>
""", 6, L))

    # 7 — Section 02 opener
    P.append(opener("02", "Irresistible <em>Offer Stacking</em>",
        "People don't buy PDFs. They buy a faster, more certain path to a result. Your offer is the PDF plus everything that removes risk and effort.",
        ["The value equation, applied to a $19 product", "The 4-step product ladder",
         "Stack anatomy: core + bonuses with perceived-value math", "Pricing, naming and guarantees"], 7))

    # 8 — value equation + ladder
    P.append(page("""
<div class="eyebrow">02 · Offer Stacking</div>
<h2>The value equation for <em>digital products</em></h2>
<div class="box" style="text-align:center;padding:20px">
<p style="font-size:17px;margin:0">Perceived value = <b class="gold">Dream outcome</b> × <b class="gold">Likelihood of success</b> &nbsp;÷&nbsp; <b class="gold">Time to result</b> × <b class="gold">Effort required</b></p></div>
<table class="t">
<tr><th>Lever</th><th>Weak offer</th><th>Stacked offer</th></tr>
<tr><td><b>Dream outcome ↑</b></td><td>"Learn copywriting"</td><td>"Land 3 retainer clients ($1.5K+/mo)"</td></tr>
<tr><td><b>Likelihood ↑</b></td><td>Theory only</td><td>Step-by-step + real examples + scripts</td></tr>
<tr><td><b>Time ↓</b></td><td>"Over the coming months"</td><td>"First pitch sent in 48 hours"</td></tr>
<tr><td><b>Effort ↓</b></td><td>Blank page</td><td>Fill-in-the-blank templates + checklists</td></tr>
</table>
<h3>The 4-step product ladder</h3>
<table class="t">
<tr><th>Rung</th><th>Example</th><th class="num" style="text-align:right">Price</th><th>Job</th></tr>
<tr><td><b>1 · Lead magnet</b></td><td>7-Day Launch Checklist (8 pages)</td><td class="num">Free</td><td>Collect email + DM permission</td></tr>
<tr><td><b>2 · Core offer</b></td><td>This playbook (20–30 pages)</td><td class="num">$19</td><td>Turn followers into customers</td></tr>
<tr><td><b>3 · Order bump</b></td><td>Template pack: 30 Canva/HTML carousel layouts</td><td class="num">$27</td><td>Raise average order value</td></tr>
<tr><td><b>4 · Premium</b></td><td>Complete vault: all playbooks + monthly updates</td><td class="num">$97</td><td>Serve your best 5–10% of buyers</td></tr>
</table>
<h3>Average order value math</h3>
<table class="t" style="width:78%">
<tr><td>100 orders × $19 core</td><td class="num">$1,900</td></tr>
<tr><td>+ 20% take the $27 bump (20 × $27)</td><td class="num">$540</td></tr>
<tr><td>+ 4% upgrade to $97 vault (4 × $97)</td><td class="num">$388</td></tr>
<tr class="total"><td>Total · average order value $28.28 (+49%)</td><td class="num">$2,828</td></tr>
</table>
<div class="callout">Launch with rungs 1 and 2 only. Add the bump after 25 sales and the premium tier after 100 — when you know what buyers ask for.</div>
""", 8, L))

    # 9 — stack anatomy
    P.append(page("""
<div class="eyebrow">02 · Offer Stacking</div>
<h2>Stack anatomy: <em>worked example</em></h2>
<p>Every bonus must kill a specific objection or speed up a specific step. Bonuses that are "more content" lower perceived value.</p>
<table class="t">
<tr><th>Component</th><th>Objection it kills</th><th class="num" style="text-align:right">Stand-alone value</th></tr>
<tr><td><b>Core:</b> First Retainer Playbook (24 pages)</td><td>"I don't know where to start."</td><td class="num">$49</td></tr>
<tr><td><b>Bonus 1:</b> 12 cold-pitch email templates</td><td>"I don't know what to say."</td><td class="num">$29</td></tr>
<tr><td><b>Bonus 2:</b> Pricing calculator sheet</td><td>"I don't know what to charge."</td><td class="num">$19</td></tr>
<tr><td><b>Bonus 3:</b> 3 sample portfolio pieces to adapt</td><td>"I have no portfolio."</td><td class="num">$29</td></tr>
<tr><td><b>Bonus 4:</b> 30-day action tracker</td><td>"I won't follow through."</td><td class="num">$9</td></tr>
<tr class="total"><td>Total stated value → Price today</td><td>Value-to-price ratio ≈ 7 : 1</td><td class="num">$135 → $19</td></tr>
</table>
<div class="callout"><b>Honesty rule:</b> "stand-alone value" must be a price you would genuinely charge or a comparable product's real price. Inflated anchors kill trust and refund rates show it.</div>
<h3>The offer one-liner</h3>
<div class="box"><p style="margin:0;font-size:14px">"Get <b class="gold">[result]</b> in <b class="gold">[time]</b> with the <b class="gold">[named system]</b> — including <b class="gold">[best bonus]</b> — for <b class="gold">$19</b>, risk-free."</p></div>
<h3>Risk reversal options</h3>
<div class="grid3">
<div class="cell"><h4 style="margin-top:0">Simple</h4><p>"14-day money-back guarantee. Not useful? Email us for a full refund."</p></div>
<div class="cell"><h4 style="margin-top:0">Conditional</h4><p>"Do the 7-day plan. No first pitch sent? Full refund."</p></div>
<div class="cell"><h4 style="margin-top:0">Better-than</h4><p>"If it's not the most practical $19 you spend this year, we refund you."</p></div>
</div>
<p class="small" style="margin-top:10px">Expect 2–5% refunds on low-ticket PDFs. A clear guarantee usually lifts conversion by more than it costs — test it.</p>
""", 9, L))

    # 10 — pricing & naming
    P.append(page("""
<div class="eyebrow">02 · Offer Stacking</div>
<h2>Pricing &amp; naming that <em>convert</em></h2>
<h3>Price-point decision table</h3>
<table class="t">
<tr><th>Price</th><th>Buyer psychology</th><th>Use when</th></tr>
<tr><td class="num" style="text-align:left">$7–$12</td><td>Impulse, no thought</td><td>Tiny tools: swipe files, one template</td></tr>
<tr><td class="num" style="text-align:left"><b>$17–$29</b></td><td>"Less than lunch for two" — easy yes</td><td><b>First core playbook (recommended)</b></td></tr>
<tr><td class="num" style="text-align:left">$37–$67</td><td>Needs proof + preview pages</td><td>Bundles, once you have testimonials</td></tr>
<tr><td class="num" style="text-align:left">$97+</td><td>Needs trust, emails, social proof</td><td>Vaults, mini-courses, cohorts</td></tr>
</table>
<h3>Break-even pricing math</h3>
<p>At $19 with ~10% platform + payment fees you keep ≈ $17.10. If your only paid cost is a $29/month store, you break even at <b>2 sales a month</b>. Everything after that is margin — which is why low-ticket PDFs are the right first product.</p>
<h3>Title formulas</h3>
<div class="grid2">
<div class="cell"><p><b>The [Outcome] Playbook</b> — "The First Retainer Playbook"</p></div>
<div class="cell"><p><b>[Number] [Things] to [Result]</b> — "27 Hooks That Sell Digital Products"</p></div>
<div class="cell"><p><b>[Result] Without [Pain]</b> — "Clients Without Cold Calls"</p></div>
<div class="cell"><p><b>The [Time] [Result] System</b> — "The 30-Day Faceless Launch System"</p></div>
</div>
<h3>Checklist before you publish the offer</h3>
<ul class="check">
<li>The title promises one specific outcome a buyer can picture.</li>
<li>The cover reads clearly at 150px wide (thumbnail test on your phone).</li>
<li>You can list 5 concrete "you'll get" bullets — each a tool or result, not a chapter name.</li>
<li>Price ends in 7 or 9 and sits inside the $17–$29 band for a first offer.</li>
<li>Guarantee is stated in one sentence near the buy button.</li>
<li>A free lead magnet leads naturally into the paid product (same problem, next step).</li>
</ul>
""", 10, L))

    # 11 — Section 03 opener
    P.append(opener("03", "Storefront <em>Setup</em>",
        "Your storefront is your only salesperson. It must load fast on a phone, explain the result in 3 seconds, and deliver the file automatically.",
        ["Platform comparison & how to choose", "The 9-block sales page (with copy)",
         "Bio, link-in-bio and delivery automation", "Pre-launch QA checklist"], 11))

    # 12 — platforms + sales page
    P.append(page("""
<div class="eyebrow">03 · Storefront Setup</div>
<h2>Choose a platform in <em>10 minutes</em></h2>
<table class="t">
<tr><th>Platform</th><th>Cost model (verify current pricing)</th><th>Best for</th></tr>
<tr><td><b>Stan Store</b></td><td>Monthly subscription, no per-sale platform fee</td><td>Instagram-first, mobile link-in-bio store</td></tr>
<tr><td><b>Gumroad</b></td><td>No monthly fee; percentage per sale + processing</td><td>Zero upfront cost, fastest start</td></tr>
<tr><td><b>Payhip</b></td><td>Free plan with % fee, or paid plans with lower/no fee</td><td>Cheap scaling, coupons, upsells</td></tr>
<tr><td><b>Lemon Squeezy</b></td><td>% + fixed fee per sale; handles global sales tax</td><td>International buyers, tax handled</td></tr>
<tr><td><b>Shopify</b></td><td>Monthly plan + digital download app</td><td>Larger catalogs, brand sites later</td></tr>
</table>
<div class="callout"><b>Decision rule:</b> under 30 sales/month → a no-monthly-fee option keeps risk at zero. Above ~30 sales/month, a flat monthly plan usually becomes cheaper than per-sale fees. Re-check the math quarterly.</div>
<h3>The 9-block sales page</h3>
<table class="t">
<tr><th style="width:26px">#</th><th style="width:150px">Block</th><th>Example copy</th></tr>
<tr><td>1</td><td><b>Headline (result)</b></td><td>"Land your first 3 retainer clients in 30 days — no cold calls."</td></tr>
<tr><td>2</td><td><b>Sub-headline</b></td><td>"The exact pitch system, templates and pricing used by working copywriters."</td></tr>
<tr><td>3</td><td><b>Cover + previews</b></td><td>3D cover + 3 inside pages (a table, a script, a checklist).</td></tr>
<tr><td>4</td><td><b>Pain mirror</b></td><td>"Sent 40 applications, heard nothing back? It's not your writing."</td></tr>
<tr><td>5</td><td><b>What's inside</b></td><td>5 bullets: tool or outcome + benefit. "12 pitch templates → send your first pitch tonight."</td></tr>
<tr><td>6</td><td><b>Who it's for / not for</b></td><td>Two short lists. Repels refund-prone buyers.</td></tr>
<tr><td>7</td><td><b>Offer stack</b></td><td>Core + bonuses with value, then "Today: $19".</td></tr>
<tr><td>8</td><td><b>Guarantee + FAQ</b></td><td>Refund line + 4 FAQs: format, delivery, beginner-friendly, refunds.</td></tr>
<tr><td>9</td><td><b>Button (repeat)</b></td><td>"Get instant access — $19". Repeat after blocks 3, 5 and 8.</td></tr>
</table>
""", 12, L))

    # 13 — bio / delivery / QA
    P.append(page("""
<div class="eyebrow">03 · Storefront Setup</div>
<h2>Profile, link &amp; <em>delivery</em> automation</h2>
<div class="grid2">
<div>
<h3>The converting bio (4 lines)</h3>
<div class="script"><div class="who">Name field (searchable)</div>Operator Ledger | Digital Product Playbooks</div>
<div class="script"><div class="who">Bio</div>Faceless business playbooks, zero fluff.<br>Daily carousels on offers, content &amp; DMs.<br>📘 Free 7-Day Launch Checklist ↓</div>
<div class="script"><div class="who">Link</div>yourstore.com/start → free guide first, paid playbook second</div>
<p class="small">The name field is searchable — put your keyword there, not just the brand.</p>
</div>
<div>
<h3>Highlights = your FAQ</h3>
<ul class="dots"><li><b>START HERE</b> — who you help + your best 3 posts.</li>
<li><b>FREE GUIDE</b> — the lead magnet, with a link sticker.</li>
<li><b>PLAYBOOKS</b> — product previews + the $19 offer.</li>
<li><b>PROOF &amp; FAQ</b> — buyer messages, delivery, refunds.</li></ul>
<h3>Pin 3 posts</h3>
<ol class="num"><li>Your best-performing value carousel.</li><li>The lead magnet post ("Comment GUIDE").</li><li>The product walkthrough post.</li></ol>
</div>
</div>
<h3>Delivery automation flow</h3>
<div class="flowrow"><div><b>Checkout</b>Card / Apple Pay / PayPal</div><div><b>Instant</b>File download + receipt</div><div><b>Email 1</b>"Start on page 3"</div><div><b>Day 3</b>Quick-win check-in</div><div><b>Day 7</b>Review + bump offer</div></div>
<h3>Pre-launch QA checklist</h3>
<ul class="check">
<li>Buy your own product with a 100%-off code on your phone — download works on iOS and Android.</li>
<li>File name is clean (<i>Faceless_Business_Marketing_Playbook.pdf</i>) and under 20 MB.</li>
<li>Receipt email shows your brand name and a support address.</li>
<li>Sales page loads in under 3 seconds on mobile data.</li>
<li>Refund policy, terms and contact email are visible.</li>
<li>Store link in bio, in the auto-DM, and in the lead magnet's last page.</li>
<li>Analytics on: store visits, conversion rate, revenue per visitor.</li>
</ul>
""", 13, L))

    # 14 — Section 04 opener
    P.append(opener("04", "The 80/20 <em>Carousel</em> Conversion System",
        "Carousels are the highest-leverage faceless format: no camera, high saves, and every slide is a chance to build authority. 80% teach. 20% sell. Every single post converts.",
        ["Content pillars and the 80/20 ratio", "The 7-slide conversion anatomy",
         "Hook bank — 30 templates", "Captions, cadence, metrics and a weekly calendar"], 14))

    # 15 — pillars
    P.append(page("""
<div class="eyebrow">04 · Carousel System</div>
<h2>Four pillars, one <em>ratio</em></h2>
<p>Plan content by job, not by mood. Each pillar does one job in the funnel. Over any 10 posts, aim for 8 value posts and 2 offer posts.</p>
<table class="t">
<tr><th>Pillar</th><th>Job</th><th>Share</th><th>Example (copywriter niche)</th></tr>
<tr><td><b>Teach</b></td><td>Saves → authority</td><td class="num">40%</td><td>"The 4-line cold pitch that gets replies"</td></tr>
<tr><td><b>Myth-bust</b></td><td>Shares → reach</td><td class="num">20%</td><td>"You don't need a portfolio site. Do this instead."</td></tr>
<tr><td><b>Proof &amp; math</b></td><td>Belief → desire</td><td class="num">20%</td><td>"$0 → $3K/mo: the exact client math"</td></tr>
<tr><td><b>Offer</b></td><td>DMs → sales</td><td class="num">20%</td><td>"Everything I'd do in 30 days, in one playbook"</td></tr>
</table>
<p class="small">Teach + Myth-bust + Proof = the "80". Offer = the "20". Every post, including value posts, ends with a soft CTA (save, follow, or comment keyword).</p>
<h3>Three carousel formats that convert</h3>
<div class="grid3">
<div class="cell"><h3>The Framework</h3><p>Name a 3–5 step system and give one step per slide.</p><p class="small">Best for: saves, authority, leading into the paid playbook.</p></div>
<div class="cell"><h3>The Before/After</h3><p>Show a weak example vs. a strong one, then explain the difference.</p><p class="small">Best for: shares, proving expertise without a face.</p></div>
<div class="cell"><h3>The Math Breakdown</h3><p>Turn a goal into numbers (like $100/day = 6 sales).</p><p class="small">Best for: belief and comment-keyword CTAs.</p></div>
</div>
<h3>The faceless authority rules</h3>
<ul class="check">
<li>One idea per carousel. If you need a second idea, it's tomorrow's post.</li>
<li>Specific beats clever: numbers, names of tools, exact words to say.</li>
<li>Consistent template: same fonts, colors and layout → people recognise you in the feed.</li>
<li>Write like a memo from an operator: short sentences, no hype, no emojis on slides.</li>
<li>Never claim personal results you can't prove. Teach the method; show the math.</li>
</ul>
""", 15, L))

    # 16 — 7-slide anatomy
    P.append(page("""
<div class="eyebrow">04 · Carousel System</div>
<h2>The 7-slide <em>conversion anatomy</em></h2>
<p>Instagram can re-show your carousel starting from slide 2 to people who skipped slide 1 — so slide 2 must work as a second hook.</p>
<table class="t">
<tr><th style="width:60px">Slide</th><th style="width:140px">Job</th><th>What to write</th><th style="width:190px">Example</th></tr>
<tr><td><b>1</b></td><td>Hook — stop the scroll</td><td>Specific result + curiosity. ≤ 12 words. Big serif.</td><td>"How 1 clean PDF can bring in $100/day without showing your face."</td></tr>
<tr><td><b>2</b></td><td>Re-hook — the stakes</td><td>A number, a myth, or a contrast that proves the post is worth it.</td><td>"$100/day is just 6 sales of a $19 guide."</td></tr>
<tr><td><b>3</b></td><td>Step 1</td><td>Headline = action. 1–2 lines of why. One example.</td><td>"Sell a painkiller, not a topic."</td></tr>
<tr><td><b>4</b></td><td>Step 2</td><td>Same structure. Add a visual: list, table, flow.</td><td>"Package one outcome into ~20 pages."</td></tr>
<tr><td><b>5</b></td><td>Step 3</td><td>The step people get wrong — highest save value.</td><td>"Post 1 value carousel a day. 80/20."</td></tr>
<tr><td><b>6</b></td><td>Step 4 / bridge</td><td>Connect the method to your free resource.</td><td>"Turn comments into customers."</td></tr>
<tr><td><b>7</b></td><td>CTA — one action</td><td>Keyword comment for the freebie + follow line.</td><td>"Comment GUIDE and I'll DM you the checklist."</td></tr>
</table>
<div class="grid2">
<div class="cell"><h3>Design specs</h3><ul class="dots">
<li>1080 × 1350 px (4:5) — takes the most screen space in the feed.</li>
<li>Headlines 70–100 px, body 30–36 px. Readable without zooming.</li>
<li>Keep text 80 px from edges; avoid the bottom 170 px on slide 1.</li>
<li>Progress bar + "Swipe →" on every slide but the last.</li></ul></div>
<div class="cell"><h3>Write it in this order</h3><ol class="num" style="margin:0">
<li>The CTA (what should they do?).</li><li>The 3–4 steps.</li><li>Slide 2 re-hook.</li><li>Slide 1 hook — last, using the hook bank.</li></ol></div>
</div>
""", 16, L))

    # 17 — hook bank
    hooks = [
        "How I'd [result] in [time] if I started from zero today", "[Number] [things] that [result] (#[n] is underrated)",
        "Stop [common action]. Do this instead.", "The [adjective] way to [result] without [pain]",
        "$[X]/day is just [N] sales of a $[Y] product", "Why your [thing] isn't [result] (and the 1 fix)",
        "I studied [N] [winners]. Here's the pattern.", "The [name] framework for [result]",
        "[Result] in [time]: the exact steps", "You don't need [thing]. You need [thing].",
        "[N] mistakes that kill your [result]", "Steal this [template/script] for [result]",
        "The math behind [impressive result]", "If you [situation], read this before [action]",
        "Beginner vs. pro: [task] edition", "What nobody tells you about [topic]",
        "The 80/20 of [skill]: the only [N] things that matter", "Do this before you [launch/post/sell]",
        "[Big result] starts with this boring habit", "The [N]-minute [task] that replaced my [old task]",
        "Save this if you want [result] this month", "[Old way] is dead. Here's what works now.",
        "Copy this [N]-step [process]", "Why [popular advice] is costing you [money/time]",
        "The cheapest way to [result]", "Exactly what to post for [N] days to [result]",
        "My checklist for [task] (save for later)", "How [type of person] gets [result] faceless",
        "Read this if you've been [frustration] for months", "[N] [assets] I'd build before quitting my job",
    ]
    rows = "".join(f"<tr><td class='num' style='width:30px;text-align:left'>{i+1:02d}</td><td>{h}</td></tr>"
                   for i, h in enumerate(hooks[:15]))
    rows2 = "".join(f"<tr><td class='num' style='width:30px;text-align:left'>{i+16:02d}</td><td>{h}</td></tr>"
                    for i, h in enumerate(hooks[15:]))
    P.append(page(f"""
<div class="eyebrow">04 · Carousel System</div>
<h2>Hook bank: <em>30 templates</em></h2>
<p>Fill the brackets with your niche's words (from your Day 2 language mining). Test 2 hooks per idea by turning the loser into tomorrow's slide-2 re-hook.</p>
<div class="grid2" style="gap:14px">
<table class="t" style="margin-top:4px"><tr><th colspan="2">Hooks 01–15</th></tr>{rows}</table>
<table class="t" style="margin-top:4px"><tr><th colspan="2">Hooks 16–30</th></tr>{rows2}</table>
</div>
<div class="callout"><b>Hook quality test:</b> (1) Is there a number or a named outcome? (2) Would your ideal buyer feel "that's me"? (3) Is it under 12 words? Three yeses → publish.</div>
""", 17, L))

    # 18 — captions, cadence, metrics
    P.append(page("""
<div class="eyebrow">04 · Carousel System</div>
<h2>Captions, cadence &amp; <em>metrics</em></h2>
<div class="grid2">
<div>
<h3>The 5-part caption</h3>
<ol class="num">
<li><b>Hook line</b> — restate slide 1 with a twist (first 125 characters show before "more").</li>
<li><b>Context</b> — 1–2 lines on why this matters now.</li>
<li><b>Summary</b> — the steps as a scannable list.</li>
<li><b>CTA</b> — one keyword: "Comment GUIDE and I'll DM it to you."</li>
<li><b>Keywords</b> — 3–5 niche hashtags + searchable words in plain text.</li>
</ol>
</div>
<div>
<h3>Cadence that compounds</h3>
<table class="t">
<tr><th>Format</th><th class="num" style="text-align:right">Per week</th></tr>
<tr><td>Carousels (1080×1350)</td><td class="num">7</td></tr>
<tr><td>Stories (poll, preview, link)</td><td class="num">10–15</td></tr>
<tr><td>Reels (optional, faceless b-roll + text)</td><td class="num">2–3</td></tr>
<tr><td>Offer-led posts</td><td class="num">1–2</td></tr>
</table>
<p class="small">Publish via the official Instagram Graph API or a Meta-approved scheduler only — never browser bots.</p>
</div>
</div>
<h3>The metrics that matter (per post, after 72 hours)</h3>
<table class="t">
<tr><th>Metric</th><th>Formula</th><th>Healthy</th><th>If low</th></tr>
<tr><td><b>Save rate</b></td><td>Saves ÷ reach</td><td class="num">≥ 1.5%</td><td>More specific, more "steal this"</td></tr>
<tr><td><b>Share rate</b></td><td>Shares ÷ reach</td><td class="num">≥ 0.5%</td><td>Myth-busts, relatable contrasts</td></tr>
<tr><td><b>Non-follower reach</b></td><td>Non-follower ÷ total reach</td><td class="num">≥ 40%</td><td>Stronger hooks; broader sub-topic</td></tr>
<tr><td><b>Keyword comment rate</b></td><td>Keyword comments ÷ reach</td><td class="num">≥ 1%</td><td>More desirable freebie; clearer CTA</td></tr>
<tr><td><b>Follows per 1K reach</b></td><td>Follows ÷ reach × 1000</td><td class="num">≥ 3</td><td>Bio clarity + consistent template</td></tr>
</table>
<p class="small">Benchmarks are working targets for small educational accounts, not platform guarantees.</p>
<h3>Weekly production workflow (≈ 5 hours/week)</h3>
<table class="t">
<tr><td style="width:120px"><b>Mon · 90 min</b></td><td>Pick 7 ideas from comments/DMs + hook bank. Write slide text for all 7.</td></tr>
<tr><td><b>Tue · 90 min</b></td><td>Render all 7 carousels from your template (HTML/CSS or Canva). Write captions.</td></tr>
<tr><td><b>Wed · 30 min</b></td><td>Schedule the week through the official API / approved scheduler.</td></tr>
<tr><td><b>Daily · 15 min</b></td><td>Reply to comments in the first hour; answer DMs; log metrics on Sunday.</td></tr>
</table>
""", 18, L))

    # 19 — Section 05 opener
    P.append(opener("05", "Comment-to-DM <em>Sales Funnels</em>",
        "A comment keyword turns a passive viewer into a conversation. A conversation turns into an email subscriber. Email turns into a sale. All of it can run automatically — inside Meta's rules.",
        ["The funnel map and compliance rules", "DM scripts: delivery, qualify, offer",
         "The 5-email follow-up sequence", "Funnel math & KPI dashboard"], 19))

    # 20 — funnel map + DM scripts
    P.append(page("""
<div class="eyebrow">05 · Comment-to-DM</div>
<h2>The funnel map &amp; <em>DM scripts</em></h2>
<div class="flowrow"><div><b>Post</b>"Comment GUIDE"</div><div><b>Auto-reply</b>Public reply + DM</div><div><b>DM</b>Free guide link</div><div><b>Opt-in</b>Email captured</div><div><b>Sale</b>$19 playbook</div></div>
<div class="callout"><b>Compliance:</b> use an official Meta Business Partner tool (e.g. ManyChat) or the Instagram Messaging API. Automated DMs may only go to people who messaged or commented first, within Meta's messaging window (currently 24 hours). No cold DMs, no bulk follow/unfollow.</div>
<div class="grid2" style="gap:14px">
<div>
<h4>Message 1 — instant delivery</h4>
<div class="script"><div class="who">Auto-DM</div>Hey! Here's your free 7-Day Launch Checklist 👇<br>[button: Send me the guide]<br>Quick question so I can point you to the right page: are you <b>(A)</b> still picking a niche or <b>(B)</b> ready to build your first product?</div>
<h4>Public comment reply (rotate 3 variants)</h4>
<div class="script"><div class="who">Auto-reply</div>"Sent! Check your DMs 📩" · "Just sent it over — enjoy!" · "In your inbox now 🙌"</div>
</div>
<div>
<h4>Message 2 — qualify (if they reply A or B)</h4>
<div class="script"><div class="who">If A</div>Perfect — start with Day 1 on page 3. The scoring table takes 30 minutes and saves weeks.</div>
<div class="script"><div class="who">If B</div>Nice. Skip to page 5 — the 20-page structure. Most people overbuild here.</div>
<h4>Message 3 — offer (24h later, only if they engaged)</h4>
<div class="script"><div class="who">Manual or automated</div>How's the checklist going? If you want the full system — validation scorecard, offer math, DM scripts and 30 hooks — it's in the playbook ($19): [link]. Totally fine if not, the checklist alone will get you moving.</div>
</div>
</div>
<p class="small">Keep the tone helpful, not pushy. One offer message per lead in DMs; let email do the rest.</p>
""", 20, L))

    # 21 — email sequence
    P.append(page("""
<div class="eyebrow">05 · Comment-to-DM</div>
<h2>The 5-email <em>follow-up sequence</em></h2>
<p>Everyone who downloads the free guide gets this sequence. It does 70% of the selling — while you make tomorrow's carousel.</p>
<table class="t">
<tr><th style="width:52px">Day</th><th style="width:200px">Subject line</th><th>Body (what to say)</th><th style="width:80px">Goal</th></tr>
<tr><td><b>0</b></td><td>"Your checklist is inside (+ start here)"</td><td>Deliver the link. Tell them the one page to start on and the quick win they'll get in 30 minutes.</td><td>Consume</td></tr>
<tr><td><b>1</b></td><td>"The $100/day math nobody shows you"</td><td>Walk through the funnel math (page 3 of this playbook). End: "Reply with your niche — I read every one."</td><td>Belief + reply</td></tr>
<tr><td><b>3</b></td><td>"Why most first products don't sell"</td><td>Story: topic vs. painkiller. Show the scorecard example. Soft mention: the full scorecard is in the playbook.</td><td>Desire</td></tr>
<tr><td><b>5</b></td><td>"Everything I'd do in 30 days"</td><td>Direct pitch: what's inside, who it's for, the stack, the guarantee, the button. Price: $19.</td><td>Sale</td></tr>
<tr><td><b>7</b></td><td>"Last note on this (+ a quick FAQ)"</td><td>Answer 4 objections (time, beginner, format, refunds). Optional: 48-hour bonus for buyers (e.g. carousel template pack).</td><td>Sale</td></tr>
</table>
<h3>Copy-paste: Day 5 email</h3>
<div class="box">
<p><b class="gold">Subject:</b> Everything I'd do in 30 days</p>
<p>If I had to launch a faceless digital product from zero this month, I wouldn't guess. I'd validate a niche in 72 hours, stack an offer that makes the yes easy, set up a store that delivers automatically, post one 80/20 carousel a day, and let a comment-to-DM funnel do the selling.</p>
<p>That's exactly what's inside <b class="gold">The Faceless Business Marketing Playbook</b>: 23 pages, five systems, the niche scorecard, offer math, the 7-slide anatomy, 30 hooks, DM scripts and this email sequence.</p>
<p style="margin:0">It's $19, with a 14-day refund if it's not useful. → <b class="gold">[Get the playbook]</b></p>
</div>
<p class="small">Send from a dedicated domain email, include an unsubscribe link and your business address — required by anti-spam laws (CAN-SPAM, GDPR, CASL).</p>
""", 21, L))

    # 22 — funnel dashboard + 30-day plan
    P.append(page("""
<div class="eyebrow">05 → 06 · Dashboard &amp; 30-Day Plan</div>
<h2>Funnel KPIs &amp; your <em>30-day plan</em></h2>
<table class="t">
<tr><th>Stage</th><th>KPI</th><th>Target</th><th>Fix if below</th></tr>
<tr><td>Post → comment</td><td>Keyword comments ÷ reach</td><td class="num">1–3%</td><td>Freebie specificity, CTA on slide 7 + caption</td></tr>
<tr><td>Comment → DM opened</td><td>Opened ÷ sent</td><td class="num">70%+</td><td>Shorter first DM, button instead of link</td></tr>
<tr><td>DM → email opt-in</td><td>Emails ÷ DMs</td><td class="num">40–60%</td><td>Fewer fields, deliver instantly after email</td></tr>
<tr><td>Email → sale (14 days)</td><td>Buyers ÷ new subscribers</td><td class="num">2–5%</td><td>Day 5 offer clarity, guarantee, previews</td></tr>
<tr><td>Store visit → sale</td><td>Orders ÷ visits</td><td class="num">1–3%</td><td>Headline, previews, price anchor</td></tr>
</table>
<h3>30-day execution plan</h3>
<table class="t">
<tr><th style="width:110px">Week</th><th>Build</th><th>Publish</th><th style="width:150px">Milestone</th></tr>
<tr><td><b>1 · Foundation</b></td><td>72-hour validation · positioning sentence · brand template · bio + highlights</td><td>3 test carousels, then 1/day</td><td>Niche scores 70+</td></tr>
<tr><td><b>2 · Product</b></td><td>Write lead magnet (8 pages) + core playbook draft · storefront live</td><td>7 carousels (1 "WAITLIST")</td><td>Store + delivery tested</td></tr>
<tr><td><b>3 · Funnel</b></td><td>Comment-to-DM automation · 5-email sequence · launch</td><td>7 carousels (2 offer posts)</td><td>First sale</td></tr>
<tr><td><b>4 · Optimize</b></td><td>Read KPIs · fix weakest stage · add order bump after 25 sales</td><td>7 carousels + best-post remix</td><td>10+ sales, data on all KPIs</td></tr>
</table>
<div class="grid3">
<div class="stat"><b>28</b><span>Carousels published by day 30 (one template, rendered in batches)</span></div>
<div class="stat"><b>2</b><span>Products live: free lead magnet + $19 core playbook</span></div>
<div class="stat"><b>1</b><span>Funnel stage improved per week — never more</span></div>
</div>
""", 22, L))

    # 23 — scorecard + close
    P.append(page("""
<div class="eyebrow">07 · Operator Scorecard</div>
<h2>Track weekly. Improve <em>one thing</em>.</h2>
<table class="t">
<tr><th>Weekly number</th><th class="num" style="text-align:right">Wk 1</th><th class="num" style="text-align:right">Wk 2</th><th class="num" style="text-align:right">Wk 3</th><th class="num" style="text-align:right">Wk 4</th></tr>
<tr><td>Posts published</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Total reach</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Saves + shares</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Keyword comments / DMs</td><td></td><td></td><td></td><td></td></tr>
<tr><td>New email subscribers</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Store visits</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Sales · revenue</td><td></td><td></td><td></td><td></td></tr>
<tr><td><b>Weakest stage → this week's fix</b></td><td></td><td></td><td></td><td></td></tr>
</table>
<h3>The operator's principles</h3>
<div class="grid2">
<ol class="num" style="margin:0">
<li>Market before product. Product before audience size.</li>
<li>One problem, one product, one CTA.</li>
<li>Ratios over totals while you're small.</li></ol>
<ol class="num" style="margin:0;counter-reset:n 3">
<li>Systems over motivation: batch, template, schedule.</li>
<li>Official tools only. Your account is your asset.</li>
<li>Done and published beats perfect and private.</li></ol>
</div>
<div class="box" style="margin-top:18px">
<h3>Keep going</h3>
<p>Follow <b class="gold">@operatorledger.co</b> for a new playbook carousel every day. Questions or a win to share? DM us the word <b class="gold">LEDGER</b> — we read every message and feature buyer results (with permission) in our PROOF highlight.</p>
<p style="margin:0" class="small">© Operator Ledger. For personal use by the purchaser. Please don't redistribute — share the link instead. Figures are illustrative examples, not guarantees of income.</p>
</div>
""", 23, L))
    return P

