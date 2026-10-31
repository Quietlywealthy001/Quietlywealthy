"""Product 1 — FREE lead magnet: 7-Day Digital Product Launch Checklist (8 pages)."""
from covers import checklist_cover
from doc_base import cover_page, page

L = "7-Day Launch Checklist"


def pages() -> list[str]:
    P = [cover_page(checklist_cover())]

    P.append(page("""
<div class="eyebrow">How to use this checklist</div>
<h2>One week. One problem. <em>One product.</em></h2>
<p class="lede">Most first digital products fail for one reason: they take three months, solve a vague problem, and launch to nobody.
This checklist forces the opposite — a narrow problem, a short guide, and real buyers in seven days.</p>
<div class="grid3" style="margin:16px 0 18px">
  <div class="stat"><b>~12 hrs</b><span>Total focused work across the week (≈ 90 min/day)</span></div>
  <div class="stat"><b>15–25</b><span>Pages in your finished guide — short beats long</span></div>
  <div class="stat"><b>$0–$29</b><span>Startup cost. Free tools work for everything here</span></div>
</div>
<h4>The 7-day map</h4>
<table class="t">
<tr><th style="width:70px">Day</th><th>Mission</th><th>Deliverable by end of day</th></tr>
<tr><td><b>1</b></td><td>Pick a profitable problem</td><td>One sentence: "I help [who] get [result] without [pain]"</td></tr>
<tr><td><b>2</b></td><td>Validate demand in public</td><td>3 proof signals + 10 written buyer phrases</td></tr>
<tr><td><b>3</b></td><td>Outline the guide</td><td>Named framework + chapter list</td></tr>
<tr><td><b>4</b></td><td>Write the first draft</td><td>Full draft, ugly but complete</td></tr>
<tr><td><b>5</b></td><td>Design &amp; package</td><td>Finished PDF, cover, title, price</td></tr>
<tr><td><b>6</b></td><td>Storefront &amp; delivery</td><td>Live checkout that auto-delivers the file</td></tr>
<tr><td><b>7</b></td><td>Launch</td><td>Launch post + DM funnel live + first sales</td></tr>
</table>
<div class="callout"><b>Rules of the week:</b> tick every box before moving on · done beats perfect ·
do not add a second product, course or membership until this one has sold 10 copies.</div>
<p class="small">Tip: print this PDF or duplicate it into your notes app and tick the boxes as you go.</p>
""", 2, L))

    P.append(page("""
<div class="dayhead"><div class="d"><small>DAY</small>1</div><div><h2>Pick a <em>profitable problem</em></h2>
<div class="meta">90 minutes · Output: one positioning sentence</div></div></div>
<p>Profitable problems sit at the intersection of <b>pain</b> (it costs them money, time or status),
<b>urgency</b> (they want it solved this month) and <b>payers</b> (they already buy solutions). Start from what you already know.</p>
<h3>Step 1 — Brain-dump 20 problems (30 min)</h3>
<ul class="check">
<li>List 10 things people ask you for help with (work, hobbies, past jobs, things you learned the hard way).</li>
<li>List 10 problems you solved for yourself in the last 3 years that cost you money or time.</li>
<li>Rewrite each as an outcome: "Get [specific result] in [timeframe]".</li>
</ul>
<h3>Step 2 — Score each problem 1–5 (30 min)</h3>
<table class="t">
<tr><th>Criterion</th><th>Ask yourself</th><th style="width:70px">Score</th></tr>
<tr><td><b>Pain</b></td><td>Does not solving it cost money, clients, time or reputation?</td><td>1–5</td></tr>
<tr><td><b>Urgency</b></td><td>Do they want it fixed in the next 30 days?</td><td>1–5</td></tr>
<tr><td><b>Payers</b></td><td>Are people already buying courses, tools or services for it?</td><td>1–5</td></tr>
<tr><td><b>Reach</b></td><td>Can you find 10+ Instagram accounts serving this audience?</td><td>1–5</td></tr>
<tr><td><b>Edge</b></td><td>Can you explain it more simply or specifically than others?</td><td>1–5</td></tr>
</table>
<ul class="check">
<li>Keep only problems scoring <b>18+ out of 25</b>. Pick the top one. Don't overthink — you can pivot on Day 2.</li>
</ul>
<h3>Step 3 — Write your positioning sentence (30 min)</h3>
<div class="box"><p style="margin:0;font-size:14px">I help <b class="gold">[specific who]</b> get <b class="gold">[measurable result]</b>
in <b class="gold">[timeframe]</b> without <b class="gold">[the pain they hate]</b>.</p></div>
<div class="grid2">
<div class="cell"><h4 style="margin-top:0">Too vague ✗</h4><p>"I help people with social media."</p></div>
<div class="cell"><h4 style="margin-top:0">Profitable ✓</h4><p>"I help new wedding photographers book 5 paid shoots in 30 days without paying for ads."</p></div>
</div>
""", 3, L))

    P.append(page("""
<div class="dayhead"><div class="d"><small>DAY</small>2</div><div><h2>Validate demand <em>in public</em></h2>
<div class="meta">90 minutes · Output: 3 proof signals + buyer language</div></div></div>
<p>You are not asking "would you buy this?" (people lie). You are looking for evidence that people <b>already spend money and attention</b> on this problem.</p>
<h3>Proof signal 1 — Money is already moving</h3>
<ul class="check">
<li>Search Gumroad, Etsy, Payhip and Amazon Kindle for your problem. Find <b>3+ paid products</b> with reviews or sales counts.</li>
<li>Note their price, page count, title and the #1 complaint in their reviews (that's your angle).</li>
</ul>
<h3>Proof signal 2 — Attention is already there</h3>
<ul class="check">
<li>Find 5 Instagram accounts in the niche with posts that got <b>100+ comments or 1,000+ saves-looking engagement</b>.</li>
<li>Screenshot their 3 best-performing carousels. Write down the hook (slide 1 headline) of each.</li>
</ul>
<h3>Proof signal 3 — People describe the pain in their own words</h3>
<ul class="check">
<li>Read 50 comments, Reddit threads or reviews. Copy <b>10 exact phrases</b> people use ("I've tried everything and…").</li>
<li>Highlight the 3 phrases that show up most — they become your title, hooks and sales page headline.</li>
</ul>
<table class="t">
<tr><th>Signal found?</th><th>Decision</th></tr>
<tr><td>3 of 3</td><td><span class="g">GO</span> — move to Day 3.</td></tr>
<tr><td>2 of 3</td><td>Narrow the audience (e.g. "freelancers" → "freelance copywriters") and re-check once.</td></tr>
<tr><td>0–1 of 3</td><td>Switch to your #2 problem from Day 1. You've lost one day, not three months.</td></tr>
</table>
<div class="callout green"><b>Bonus test (optional, 10 min):</b> post a poll story or a simple carousel asking
"What's your biggest struggle with [problem]?" Every reply is a validated sub-problem and a future post.</div>
""", 4, L))

    P.append(page("""
<div class="dayhead"><div class="d"><small>DAYS</small>3–4</div><div><h2>Outline &amp; write the <em>guide</em></h2>
<div class="meta">3–4 hours total · Output: complete first draft</div></div></div>
<p>Buyers don't pay for pages. They pay for a <b>shortcut</b>. Your guide is one named framework that takes them from problem to result.</p>
<h3>Day 3 — Build the skeleton</h3>
<ul class="check">
<li>Name your framework with 3–5 steps (e.g. <i>"The 5-Shoot System"</i> or <i>"The P.A.C.K. Method"</i>).</li>
<li>Each step = one chapter = one clear action the reader takes.</li>
<li>Add a "quick win" in the first 3 pages so readers feel progress immediately.</li>
<li>List the templates, scripts or examples each chapter needs (these create perceived value).</li>
</ul>
<h4>The 20-page structure that sells</h4>
<table class="t">
<tr><th>Section</th><th>Purpose</th><th class="num" style="text-align:right">Pages</th></tr>
<tr><td>Intro + quick win</td><td>Why this works, the result, one fast action</td><td class="num">2–3</td></tr>
<tr><td>The framework overview</td><td>One-page visual map of your steps</td><td class="num">1</td></tr>
<tr><td>Steps 1–5 (chapters)</td><td>What, why, how + example per step</td><td class="num">10–12</td></tr>
<tr><td>Templates &amp; scripts</td><td>Copy-paste assets</td><td class="num">3–4</td></tr>
<tr><td>7-day action plan</td><td>Exactly what to do next</td><td class="num">1–2</td></tr>
</table>
<h3>Day 4 — Write fast, edit later</h3>
<ul class="check">
<li>Write each chapter as: <b>Problem → Principle → Steps → Example → Mistake to avoid</b>.</li>
<li>Use your Day 2 buyer phrases in headings. Their words &gt; your words.</li>
<li>Replace every vague claim with a number, a screenshot description or an example.</li>
<li>Use AI as an editor (tighten, simplify, find gaps) — not as the author of your expertise.</li>
<li>Read it once aloud. Cut every sentence that doesn't help the reader take an action.</li>
</ul>
""", 5, L))

    P.append(page("""
<div class="dayhead"><div class="d"><small>DAY</small>5</div><div><h2>Design, title &amp; <em>price</em></h2>
<div class="meta">2 hours · Output: finished PDF + cover + price</div></div></div>
<h3>Design checklist (clean beats fancy)</h3>
<ul class="check">
<li>One template: 2 fonts max (a serif for headings, a sans for body), 2–3 brand colors.</li>
<li>Body text 11–13pt, generous margins, one idea per page section.</li>
<li>Add a checklist or table every 2–3 pages — skimmable pages feel more valuable.</li>
<li>Design a cover that reads clearly at thumbnail size (title ≤ 7 words, high contrast).</li>
<li>Export as PDF, open it on your phone, fix anything hard to read.</li>
</ul>
<h3>Title formulas that convert</h3>
<div class="grid2">
<div class="cell"><h4 style="margin-top:0">The outcome</h4><p><b>The [Result] Playbook</b><br>"The First 10 Clients Playbook"</p></div>
<div class="cell"><h4 style="margin-top:0">The number</h4><p><b>[X] Steps to [Result] in [Time]</b><br>"5 Steps to Your First $1K Month"</p></div>
<div class="cell"><h4 style="margin-top:0">The anti-pain</h4><p><b>[Result] Without [Pain]</b><br>"Booked Out Without Paid Ads"</p></div>
<div class="cell"><h4 style="margin-top:0">The system</h4><p><b>The [Name] System</b><br>"The 30-Day Content Engine"</p></div>
</div>
<h3>Price it with simple math</h3>
<table class="t">
<tr><th>Product type</th><th>Typical price</th><th>Best for</th></tr>
<tr><td>Checklist / cheat sheet</td><td>Free – $9</td><td>Lead magnet, list building</td></tr>
<tr><td>15–30 page guide / playbook</td><td>$17 – $29</td><td>Your first paid product (sweet spot)</td></tr>
<tr><td>Guide + templates bundle</td><td>$37 – $67</td><td>Upsell once the guide sells</td></tr>
</table>
<div class="callout"><b>Rule of thumb:</b> price at roughly 1–5% of the value of the result. If the result is worth
$1,000 to the buyer, $19–$49 is an easy yes.</div>
""", 6, L))

    P.append(page("""
<div class="grid2" style="gap:22px">
<div>
<div class="dayhead"><div class="d"><small>DAY</small>6</div><div><h2 style="font-size:28px">Storefront</h2>
<div class="meta">90 min</div></div></div>
<ul class="check">
<li>Pick one platform: Stan Store, Gumroad, Payhip or Lemon Squeezy.</li>
<li>Upload the PDF and switch on <b>automatic delivery</b> after payment.</li>
<li>Write the product page: headline (result), 5 bullets (what's inside), who it's for, price.</li>
<li>Add the cover image + 2–3 inside-page previews.</li>
<li>Connect payouts and buy your own product once with a discount code to test delivery.</li>
<li>Put the store link in your Instagram bio.</li>
<li>Create a free "lead magnet" version (a checklist like this one) to collect emails.</li>
</ul>
</div>
<div>
<div class="dayhead"><div class="d" style="background:var(--emerald);color:var(--obsidian)"><small style="color:rgba(11,13,16,.6)">DAY</small>7</div><div><h2 style="font-size:28px">Launch</h2>
<div class="meta">2 hrs + replies</div></div></div>
<ul class="check">
<li>Post a value carousel teaching one step from your guide.</li>
<li>End it with: <b>"Comment GUIDE and I'll send you the free checklist."</b></li>
<li>Set up keyword auto-DM with a Meta-approved tool (e.g. ManyChat).</li>
<li>Post 3 stories: the problem → a sneak peek → the link.</li>
<li>Personally reply to every comment within the first hour.</li>
<li>Send your email list (even if it's 5 people) a launch-day note.</li>
<li>Log: reach, comments, DMs, link clicks, sales.</li>
</ul>
</div>
</div>
<h4>Copy-paste launch post (slide 1 + caption opener)</h4>
<div class="script"><div class="who">Slide 1 hook</div>"How I'd get <b>[result]</b> in <b>[timeframe]</b> if I started from zero today."</div>
<div class="script"><div class="who">Caption opener</div>"I put my entire process for [result] into one short guide. Here are the first 3 steps for free 👇 …
Want the full checklist? Comment GUIDE and I'll DM it to you."</div>
<div class="script"><div class="who">Auto-DM message</div>"Here it is 👉 [link]. Quick question so I can help: what's your biggest roadblock with [problem] right now?"</div>
""", 7, L))

    P.append(page("""
<div class="eyebrow">After launch</div>
<h2>Read the numbers, then <em>double down</em>.</h2>
<p class="lede">Your first launch is data, not a verdict. Track five numbers for 14 days and fix the weakest link first.</p>
<table class="t">
<tr><th>Metric</th><th>Healthy benchmark</th><th>If below, fix this</th></tr>
<tr><td>Saves + shares per 1,000 reach</td><td class="num">20+</td><td>Hooks &amp; slide-2 promise. Teach more specifically.</td></tr>
<tr><td>Comments on CTA posts</td><td class="num">1–3% of reach</td><td>Make the free resource more specific + desirable.</td></tr>
<tr><td>Profile → link click rate</td><td class="num">5–10%</td><td>Bio: who you help + result + single clear link.</td></tr>
<tr><td>Store page conversion</td><td class="num">1–3%</td><td>Headline, preview pages, price anchor, bullets.</td></tr>
<tr><td>Email → purchase (14 days)</td><td class="num">2–5%</td><td>Add story + proof + a clear deadline offer.</td></tr>
</table>
<p class="small">Benchmarks are typical ranges for small accounts, not guarantees. Compare yourself week over week.</p>
<h3>Your example $100/day math</h3>
<table class="t" style="width:70%">
<tr><td>$19 guide × 6 sales/day</td><td class="num">$114/day</td></tr>
<tr><td>Needed at a 2% store conversion</td><td class="num">300 visits/day</td></tr>
<tr class="total"><td>Monthly (30 days)</td><td class="num">≈ $3,420</td></tr>
</table>
<div class="box" style="margin-top:18px">
<h3>Ready for the full system?</h3>
<p>This checklist is the <b>what</b>. <b class="gold">The Faceless Business Marketing Playbook</b> is the <b>how</b>:
niche-validation scorecards, offer-stacking math, storefront templates, the 80/20 carousel system with 30 hooks,
and complete comment-to-DM scripts + a 5-email sales sequence.</p>
<p style="margin:0"><span style="background:var(--emerald);color:var(--obsidian);font-weight:800;padding:4px 10px;border-radius:4px">$19 · Link in bio</span>
&nbsp; DM us the word <b class="gold">PLAYBOOK</b> on Instagram.</p>
</div>
""", 8, L))
    return P

