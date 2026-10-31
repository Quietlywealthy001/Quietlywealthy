"""Generates content_queue/30_day_plan.json with 30 distinct, non-repeating 7-slide carousel blueprints for @quietlywealthy001."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
OUT_FILE = ROOT / "content_queue" / "30_day_plan.json"

# 30 distinct high-converting topics with custom math/comparison/steps data
RAW_DAYS = [
    (
        1,
        "How 1 Clean PDF Can Bring In $100/Day Without Showing Your Face",
        "Faceless Playbook · 01",
        "How 1 clean PDF can bring in <em>$100/day</em> without showing your face.",
        "$100/day is just <em>6 sales</em> of a $19 guide.",
        [("Storefront visits / day", "300"), ("Conversion rate (typical 1–3%)", "2%"), ("Sales × $19", "6 × $19"), ("Daily revenue", "$114")],
        "Sell a <em>painkiller</em>, not a topic.",
        '"Instagram growth tips"',
        '"Get your first 10 coaching clients from Instagram in 30 days"',
        "Package <em>one outcome</em> into ~20 clean pages.",
        ["The problem & why it's costly", "Your named framework (3–5 steps)", "Step-by-step execution", "Templates, scripts & examples", "A 7-day action plan"],
        "Post 1 value carousel a day. <em>80/20.</em>",
        "Turn comments into <em>customers</em>.",
        ['Post ends with: Comment "PLAYBOOK"', "Auto-DM sends the free checklist", "Reader gets immediate quick win", "Storefront link introduces core offer", "Offer: the $19 playbook"],
    ),
    (
        2,
        "The $19 Impulse-Price Psychology: Why Low-Ticket PDFs Outsell $297 Courses",
        "Pricing Architecture · 02",
        "Why a <em>$19 PDF</em> makes more money than a $297 video course.",
        "$3,420/mo is just <em>6 impulse buyers</em> a day.",
        [("Price point (Impulse zone)", "$19"), ("Sales calls required", "0"), ("Daily buyers needed", "6"), ("30-Day Revenue", "$3,420")],
        "Eliminate <em>buyer friction</em> completely.",
        '"Watch 18 hours of video modules"',
        '"Read this 23-page execution checklist in 20 minutes"',
        "The 5 triggers of an <em>impulse</em> digital offer.",
        ["Specific 7-day measurable outcome", "Price anchored against $47+ value", "Instant PDF download on checkout", "Plug-and-play copy/paste templates", "Zero tech setup required to start"],
        "Price at <em>$19</em>, anchor at $47.",
        "Stack a <em>free checklist</em> front door.",
        ['Give away the 7-Day Launch Checklist ($0)', "Prove your quality on page 1", "Show the complete system architecture", "Link directly to the $19 Playbook", "Convert warm readers automatically"],
    ),
    (
        3,
        "How To Validate A Faceless Digital Product Idea In 24 Hours (Before Writing Page 1)",
        "Market Validation · 03",
        "Never write a PDF until it passes this <em>24-hour</em> validation test.",
        "3 green flags = <em>guaranteed</em> buyer demand.",
        [("Time to validate", "24 hrs"), ("Cost to test", "$0"), ("Competitor proof needed", "3+ sellers"), ("Target price range", "$15–$29")],
        "Follow <em>existing</em> money, never guess.",
        '"I think people might want a mindset journal"',
        '"3,000+ people are buying B2B cold DM scripts right now"',
        "The 5-step <em>24-Hour</em> Validation Audit.",
        ["Search Selar, Gumroad & Etsy bestsellers", "Collect 10 recurring 3-star complaints", "Check Instagram Saves on similar carousels", "Define a narrower, faster solution", "Write the 5-part Table of Contents first"],
        "Solve the <em>missing 20%</em> competitors skipped.",
        "Test the <em>hook</em> with a single carousel.",
        ['Publish 1 carousel teaching the framework', 'End with: Comment "PLAYBOOK" for the checklist', "Measure comments & saves in 24 hours", "High saves = proven demand", "Scale daily traffic into the funnel"],
    ),
    (
        4,
        "The 7-Slide Carousel Formula That Turns Scrollers Into Storefront Buyers",
        "Content Engineering · 04",
        "The exact <em>7-slide</em> blueprint behind every high-saving carousel.",
        "Saves & shares drive <em>80%+</em> of non-follower reach.",
        [("Slide 1 goal", "Stop scroll"), ("Slide 2 goal", "Show math"), ("Slides 3–6 goal", "Earn save"), ("Slide 7 goal", "Trigger DM")],
        "Hook with <em>specificity</em>, not clickbait.",
        '"5 tips to grow your business online"',
        '"How 1 clean PDF can bring in $100/day (the exact math)"',
        "What goes on each of the <em>7 slides</em>.",
        ["Slide 1: Contrarian claim + numbers", "Slide 2: Unit economics table", "Slide 3: Bad vs. Good comparison card", "Slides 4–5: Numbered step-by-step system", "Slides 6–7: Funnel breakdown + Comment CTA"],
        "Design for <em>3-second</em> visual scanning.",
        "Automate the <em>Slide 7</em> conversion.",
        ['Ask readers to comment "PLAYBOOK"', "Official API spots the keyword instantly", "Public reply boosts post engagement", "Automated DM delivers the Selar link", "Reader claims the free guide in 1 tap"],
    ),
    (
        5,
        "Inside The Comment-To-DM Funnel: Why 'Link In Bio' Is Costing You 70% Of Sales",
        "Funnel Mechanics · 05",
        "Stop saying <em>'Link in Bio'</em>. Use this Comment-to-DM system instead.",
        "DM links convert <em>3x–5x higher</em> than bio clicks.",
        [("Bio link click rate", "~0.8%"), ("Comment-to-DM open rate", "80%+"), ("DM link click rate", "35%+"), ("Algorithm signal", "High comments")],
        "Make the algorithm work <em>for</em> your checkout.",
        '"Stop scrolling, leave this post, go to my profile, click link"',
        '"Comment PLAYBOOK below and get the link in your DMs"',
        "How the <em>2-link</em> DM message works.",
        ["Public reply confirms DM was sent", "DM greets reader warmly by context", "Link 1: Free 7-Day Launch Checklist ($0)", "Link 2: Full 23-Page Playbook ($19)", "Zero pushiness — pure utility"],
        "Every comment <em>compounds</em> organic reach.",
        "Run it <em>24/7</em> on Official Graph API.",
        ['Reader comments "PLAYBOOK" at 2 AM', "Cloud worker checks comments every 30m", "Posts warm public reply automatically", "Sends private DM with both Selar URLs", "You wake up to storefront notifications"],
    ),
    (
        6,
        "The Two-Offer Ladder: How A Free 8-Page Checklist Sells Your $19 Core Playbook",
        "Offer Architecture · 06",
        "Never sell cold. Use a <em>2-Step</em> Offer Ladder that builds instant trust.",
        "Free value first = <em>3x</em> higher checkout conversion.",
        [("Step 1 Offer", "$0 Checklist"), ("Step 2 Offer", "$19 Playbook"), ("Lead capture rate", "40–60%"), ("Upsell conversion", "8–15%")],
        "Give the <em>'What'</em> free, sell the <em>'How'</em>.",
        '"Buy my $19 guide even though you just found my page"',
        '"Download this free 8-page checklist first — upgrade if you want the templates"',
        "How the 2 PDFs lock together <em>seamlessly</em>.",
        ["Free PDF solves Day 1–7 setup clarity", "Shows editorial typography & rigor", "Highlights where people get stuck", "Introduces the 23-Page Playbook naturally", "Includes direct clickable checkout link"],
        "Your free guide must look worth <em>$19</em>.",
        "Both products live on <em>Selar</em> right now.",
        ['Comment "PLAYBOOK" on this post', "Grab the Free 7-Day Launch Checklist", "Audit your niche & offer in 15 minutes", "Unlock the 23-Page Playbook for $19", "Launch your storefront this week"],
    ),
    (
        7,
        "How To Structure A 23-Page Playbook That Readers Actually Finish And Recommend",
        "Product Design · 07",
        "Nobody wants a 300-page textbook. Build a <em>23-page</em> operational playbook.",
        "Short + actionable = <em>zero</em> refund requests.",
        [("Ideal page count", "20–25 pages"), ("Reading time", "25 mins"), ("Templates included", "10+"), ("Perceived value", "$47+")],
        "Write like an <em>operator</em>, not a professor.",
        '"Chapter 1: The History of Digital Commerce (12 pages of fluff)"',
        '"Section 1: The 15-Minute Painkiller Selection Matrix"',
        "The 5-section <em>Playbook</em> blueprint.",
        ["Pages 1–3: Executive Math & System Map", "Pages 4–8: Niche & Offer Architecture", "Pages 9–13: High-Converting Storefront Setup", "Pages 14–18: 30-Day Faceless Content Engine", "Pages 19–23: Comment-to-DM Scripts & KPIs"],
        "Use checklists, tables & <em>copy-paste</em> boxes.",
        "See our live <em>23-page</em> flagship inside.",
        ['Comment "PLAYBOOK" below', "Receive our free 8-page Launch Checklist", "See our exact Obsidian & Gold layout style", "Upgrade to the 23-page Playbook anytime", "Model this structure for your own niche"],
    ),
    (
        8,
        "Selar Storefront Optimization: 5 Checkout Tweaks That Double Conversion Rates",
        "Storefront CRO · 08",
        "Traffic is wasted if your <em>storefront</em> leaks buyers at checkout.",
        "Lifting conversion from 1.5% → <em>3%</em> doubles revenue.",
        [("1,000 visitors @ 1.5%", "15 sales ($285)"), ("1,000 visitors @ 3.0%", "30 sales ($570)"), ("Extra traffic needed", "0"), ("Setup time", "20 mins")],
        "Sell the <em>transformation</em> in the first 3 lines.",
        '"This is a PDF ebook about marketing strategies. 23 pages."',
        '"The complete 4-step operating system to build, price & automate a faceless PDF business."',
        "5 Selar product page <em>must-haves</em>.",
        ["3D hardcover-style mockup on dark canvas", "Strikethrough anchor price ($47 → $19)", "5 bullet points of tangible deliverables", "Clear 'Who this is for / NOT for' filter", "Instant 1-click PDF delivery enabled"],
        "Multi-currency checkout unlocks <em>global</em> buyers.",
        "Inspect our live <em>Selar</em> storefront.",
        ['Comment "PLAYBOOK" to get our links', "Open the Free Checklist page on Selar", "Notice the headline, bullets & 3D mockup", "Grab the free PDF to test the checkout flow", "Replicate the exact layout on your store"],
    ),
    (
        9,
        "The 5 Most Profitable Faceless Digital Product Niches For 2026 (With Examples)",
        "Niche Selection · 09",
        "5 evergreen <em>faceless niches</em> where buyers spend money every single day.",
        "Pick a niche tied to <em>money, time, or career</em>.",
        [("Niche #1", "B2B / Freelance Systems"), ("Niche #2", "Career & Resume Kits"), ("Niche #3", "AI Prompt Workflows"), ("Niche #4", "Personal Finance Trackers")],
        "Go <em>2 layers</em> deeper than the broad category.",
        '"Fitness & weight loss tips"',
        '"14-Day High-Protein Meal Prep Playbook for Busy Nurses"',
        "How to score any niche out of <em>25 points</em>.",
        ["Urgency: Does the problem hurt today?", "Purchasing power: Can they afford $19 easily?", "Search volume: Are people asking how?", "Templatability: Can a PDF solve 80% of it?", "Repeatability: Can you write 30 carousels on it?"],
        "If it scores 20+, <em>build it this week</em>.",
        "Use our <em>Niche Scorecard</em> inside the guide.",
        ['Comment "PLAYBOOK" right now', "Get the free 7-Day Launch Checklist in DMs", "Complete Day 1: Painkiller Selection", "Lock in your niche in under 30 minutes", "Never second-guess your topic again"],
    ),
    (
        10,
        "Why Dark-Mode Editorial Design Commands 3x Higher Trust Than Canva Templates",
        "Visual Authority · 10",
        "Your design tells buyers what your product is worth in <em>0.4 seconds</em>.",
        "High-contrast editorial slides win <em>2.4x</em> more saves.",
        [("Canvas ratio", "1080 × 1350 (4:5)"), ("Background", "Obsidian #0B0D10"), ("Accent color", "Warm Gold #E5B84B"), ("Signal color", "Emerald #10B981")],
        "Retire noisy rainbow templates <em>immediately</em>.",
        '"5 fonts, 6 pastel blobs, stock photos & unreadable 14px text"',
        '"1 serif headline font, 1 clean sans body font, generous dark margins"',
        "The 5 rules of <em>Quietly Wealthy</em> visual hierarchy.",
        ["4:5 portrait takes maximum mobile screen real estate", "Serif headlines with italic gold keyword emphasis", "Tabular lining numerals for all financial math", "Progress bar + slide counter at top/bottom", "Consistent monogram badge on every single slide"],
        "Consistency makes your feed look like a <em>publication</em>.",
        "Get our complete <em>Brand & Launch</em> system.",
        ['Comment "PLAYBOOK" below', "We'll DM you the free 7-Day Checklist", "Plus the link to the 23-Page Playbook", "See how every page & slide matches 100%", "Build a brand people trust at first glance"],
    ),
    (
        11,
        "How To Write Hooks That Stop The Scroll Without Resorting To Fake Hype",
        "Hook Psychology · 11",
        "You don't need loud hype when you lead with <em>clear math</em>.",
        "80% of carousel performance comes from <em>Slide 1</em>.",
        [("Words on Slide 1", "10–16 words"), ("Reading grade level", "Grade 6"), ("Numbers in hook", "At least 1"), ("Visual focal point", "Gold italic words")],
        "Trade vague promises for <em>concrete mechanisms</em>.",
        '"How to achieve financial freedom from home"',
        '"How 6 daily sales of a $19 PDF equals $3,420/month"',
        "5 proven <em>Slide 1</em> hook templates.",
        ["The Math Hook: How [X] sales of a [$Y] PDF...", "The Mistake Hook: Stop doing [X]. Do [Y] instead.", "The Teardown Hook: Inside the 4-step system that...", "The Timeframe Hook: How to validate a PDF in 24 hours.", "The Comparison Hook: Why a $19 guide beats a $297 course."],
        "Write 10 hooks for every <em>1 carousel</em> you publish.",
        "Want 50+ plug-and-play <em>hooks & scripts</em>?",
        ['Comment "PLAYBOOK" on this post', "Grab the free 7-Day Launch Checklist first", "Then check out the 23-Page Playbook ($19)", "Includes our full hook bank & caption formulas", "Never stare at a blank slide again"],
    ),
    (
        12,
        "The 80/20 Content Calendar: How To Sell Daily Without Burning Out Your Audience",
        "Content Strategy · 12",
        "If every post is a pitch, people unfollow. If <em>zero</em> posts pitch, you go broke.",
        "The golden ratio: <em>80% utility</em>, 20% offer.",
        [("Slides 1–6", "100% pure teaching"), ("Slide 7", "Clean Comment CTA"), ("Educational posts", "4 per 5 days"), ("Direct teardown posts", "1 per 5 days")],
        "Make the free post valuable enough to <em>bookmark</em>.",
        '"Buy my ebook! Link in bio! Limited time!"',
        '"Here is the exact 5-step framework on Slides 1–6. Comment PLAYBOOK for the PDF."',
        "A balanced <em>5-day</em> faceless rotation.",
        ["Day 1: Unit Economics & Revenue Math", "Day 2: Step-by-Step Tactical Tutorial", "Day 3: Bad vs. Good Case Study Comparison", "Day 4: Tool / Automation Stack Breakdown", "Day 5: Inside The Playbook (Direct Offer)"],
        "Every post teaches <em>and</em> feeds the DM funnel.",
        "Steal our <em>30-day</em> content calendar.",
        ['Comment "PLAYBOOK" below', "Get the free 7-Day Launch Checklist in DMs", "And inspect our $19 Faceless Marketing Playbook", "See how 30 days of carousels map out", "Put your content engine on autopilot"],
    ),
    (
        13,
        "How To Use AI As Your Research Analyst (Without Sounding Like A Robot)",
        "AI Leverage · 13",
        "AI should build your <em>skeleton</em>. Your operator brain adds the sharp edges.",
        "Cut product creation time from 30 days to <em>48 hours</em>.",
        [("Market research", "2 hours"), ("Outline & frameworks", "3 hours"), ("Drafting templates", "6 hours"), ("HTML/PDF typesetting", "3 hours")],
        "Never copy-paste raw <em>unfiltered</em> AI prose.",
        '" Write me an ebook about digital marketing"',
        '"Act as a direct-response strategist. Build a 5-step checklist for..."',
        "The 5-step <em>Human + AI</em> production workflow.",
        ["Use AI to cluster 50 real buyer questions", "Design a named 4-step framework yourself", "Prompt AI for concrete bad vs. good examples", "Strip every generic adjective and filler phrase", "Render into clean HTML/CSS → crisp PDF"],
        "Specificity + real numbers = <em>human authority</em>.",
        "Build your first asset in <em>7 days or less</em>.",
        ['Comment "PLAYBOOK" below', "We'll DM you the free 7-Day Launch Checklist", "Follow the exact daily milestones inside", "Or grab the full 23-Page Playbook for $19", "Turn your knowledge into a clean digital asset"],
    ),
    (
        14,
        "Why HTML-To-PDF Beats Drag-And-Drop Editors For High-Margin Digital Products",
        "Production Stack · 14",
        "Our PDFs aren't made in word processors. They're compiled from <em>code</em>.",
        "100% pixel-accurate margins, tables & <em>vector</em> typography.",
        [("Page size", "A4 / Letter exact"), ("Typography", "Playfair + Inter"), ("File size", "~1.3 MB crisp"), ("Re-brand time", "3 seconds")],
        "Treat your digital product like <em>software</em>.",
        '"Dragging text boxes by hand for 14 hours when you change 1 heading"',
        '"1 JSON brand file + HTML template renders 23 pages in 4 seconds"',
        "Why code-rendered PDFs win <em>long-term</em>.",
        ["Change brand colors or links in 1 central file", "Zero misaligned boxes or blurry screenshots", "Clickable table of contents & checkout buttons", "Identical design system across PDFs & carousels", "Version-controlled in Git alongside your scripts"],
        "Build once. Re-compile <em>instantly</em>.",
        "Inspect a code-compiled PDF <em>for free</em>.",
        ['Comment "PLAYBOOK" on this post', "Download the free 8-page Launch Checklist", "Zoom in on the typography, tables & layout", "Then check out the 23-page Playbook ($19)", "Experience the Quietly Wealthy standard"],
    ),
    (
        15,
        "The 4 Instagram Profile Elements That Convert Profile Visitors At 25%+",
        "Profile Conversion · 15",
        "When a carousel goes viral, your <em>profile</em> is your landing page.",
        "4 profile elements decide if visitors <em>follow & buy</em>.",
        [("Monogram avatar", "High contrast"), ("4-line bio", "Outcome + CTA"), ("4 Highlights", "Sales sequence"), ("Storefront link", "1-tap checkout")],
        "Clarity beats cleverness in your <em>150-character</em> bio.",
        '"Living life ✨ Entrepreneur | Coffee lover | DM for collabs"',
        '"Practical playbooks for building & scaling faceless digital products."',
        "The 4-Highlight <em>Sales Sequence</em>.",
        ["01 Start Here: Who we help & how to use the page", "02 Free Guide: Inside the 7-Day Launch Checklist", "03 Playbooks: Inside the $19 Flagship Playbook", "04 Proof / FAQ: Buyer questions answered clearly", "Pinned Carousel #1: The $100/day unit economics math"],
        "Every profile visit has a <em>clear next step</em>.",
        "Audit your profile against our <em>Checklist</em>.",
        ['Comment "PLAYBOOK" below', "Get the free 7-Day Launch Checklist in DMs", "Use the Profile Readiness Checklist inside", "Or unlock the full 23-Page Playbook ($19)", "Turn profile views into daily downloads"],
    ),
    (
        16,
        "How To Turn 1 Core Playbook Into 30 Days Of Non-Repeating Carousel Posts",
        "Content Multiplication · 16",
        "You don't need 30 ideas. You need <em>30 angles</em> on 1 great product.",
        "1 playbook × 6 chapters × 5 lenses = <em>30 carousels</em>.",
        [("Core chapters", "6 chapters"), ("Content lenses", "5 angles each"), ("Total carousels", "30 days"), ("CTA destination", "Same funnel")],
        "Stop inventing random topics every morning.",
        '"Talking about crypto Monday, productivity Tuesday, mindset Wednesday"',
        '"30 straight days of tactical faceless digital product execution"',
        "The 5 <em>Content Lenses</em> for any chapter.",
        ["Lens 1: The Math (Why this step prints ROI)", "Lens 2: The Mistake (Bad vs. Good comparison)", "Lens 3: The Checklist (5 steps to execute today)", "Lens 4: The Tool/Template (How to automate it)", "Lens 5: The FAQ (Overcoming the #1 objection)"],
        "Repetition of message builds <em>market authority</em>.",
        "Get the <em>Core Playbook</em> behind this feed.",
        ['Comment "PLAYBOOK" below', "We'll DM you the free 7-Day Launch Checklist", "Plus the link to the 23-Page Playbook ($19)", "Read the 6 chapters that power our entire page", "Apply this 6×5 matrix to your own product"],
    ),
    (
        17,
        "The Zero-Ad-Spend Traffic Loop: How Saves, Shares, And Comments Feed Each Other",
        "Algorithm Physics · 17",
        "You don't need paid ads when your carousels trigger <em>3 signals</em>.",
        "Saves + Shares + Comments = <em>Explore & Home</em> distribution.",
        [("Signal #1: Dwell time", "7-slide swipe"), ("Signal #2: Saves", "Reference math"), ("Signal #3: Comments", '"PLAYBOOK" CTA'), ("Ad spend required", "$0")],
        "Design every slide for a specific <em>algorithm signal</em>.",
        '"Single static quote image people scroll past in 0.5 seconds"',
        '"7-slide tactical breakdown that takes 45 seconds to read & save"',
        "How the <em>Organic Flywheel</em> compounds.",
        ["Slide 1 stops scroll → boosts swipe-through rate", "Slides 2–5 pack dense checklists → triggers Save", "Slide 7 asks for keyword → triggers Comment", "Auto-reply doubles total comment count instantly", "Instagram pushes post to more non-followers"],
        "Great unit economics start with <em>$0 CAC</em>.",
        "Test our automated loop right now.",
        ['Comment "PLAYBOOK" below', "Watch how fast our Official API replies", "Check your DMs for the free 7-Day Checklist", "And explore the $19 Playbook on Selar", "Build this exact flywheel for your brand"],
    ),
    (
        18,
        "Overcoming The 'Who Am I To Teach This?' Syndrome With Operator Frameworks",
        "Authority Positioning · 18",
        "You don't need to be a celebrity guru. You just need a <em>working checklist</em>.",
        "Buyers pay for <em>speed & organization</em>, not fame.",
        [("Guru course", "100 hrs of ego"), ("Operator playbook", "23 pages of steps"), ("Time saved for buyer", "40+ hours"), ("Price to buyer", "$19")],
        "Position the <em>system</em> as the hero, not your face.",
        '"Look at my rented Lamborghini and buy my vague lifestyle secrets"',
        '"Here is a 23-page documented SOP that saves you 40 hours of trial and error"',
        "How to build <em>undeniable</em> credibility from Day 1.",
        ["Show transparent math with realistic assumptions", "Give away a genuinely useful 8-page free guide", "Use side-by-side 'Bad vs. Good' examples", "Never fake screenshots or income claims", "Let your typography and structure prove your rigor"],
        "Rigor is the ultimate <em>unfair advantage</em>.",
        "Download our free <em>8-page proof of quality</em>.",
        ['Comment "PLAYBOOK" below', "Grab the free 7-Day Launch Checklist in DMs", "Judge our frameworks by their usefulness", "Upgrade to the $19 Playbook when ready", "Build quiet, compounding digital assets"],
    ),
    (
        19,
        "The $100/Day Unit Economics Breakdown: Traffic, Conversion, And AOV Levers",
        "Financial Modeling · 19",
        "When revenue is slow, you only ever have <em>3 numbers</em> to fix.",
        "Revenue = <em>Traffic × Conversion × Price</em>.",
        [("Lever 1: Storefront Visits", "300 / day"), ("Lever 2: Checkout Conv.", "2.0%"), ("Lever 3: Offer Price", "$19"), ("Daily Run Rate", "$114 / day")],
        "Stop guessing why sales are flat — <em>diagnose the bottleneck</em>.",
        '"The algorithm hates me, digital products don\'t work"',
        '"My carousel got 200 views (traffic issue) or 500 clicks with 0 sales (page issue)"',
        "How to fix each of the <em>3 levers</em> systematically.",
        ["Low impressions? Rewrite Slide 1 hooks & post daily", "Low comments? Clarify Slide 7 keyword CTA & freebie", "Low DM clicks? Shorten DM copy & highlight free PDF", "Low checkout %? Improve Selar bullets & $47 anchor", "Want higher AOV? Pair free guide with $19 core offer"],
        "What gets measured gets <em>compounded</em>.",
        "Get our KPI tracker inside the <em>Playbook</em>.",
        ['Comment "PLAYBOOK" below', "Receive the free 7-Day Launch Checklist", "Plus direct access to the 23-Page Playbook ($19)", "Track your weekly numbers like an operator", "Scale from first sale to consistent run rate"],
    ),
    (
        20,
        "How To Write Product Descriptions On Selar That Convert Skimmers Into Buyers",
        "Copywriting · 20",
        "85% of checkout visitors <em>skim</em>. Format your Selar page for skimmers.",
        "Structured copy lifts checkout completion by <em>40%+</em>.",
        [("Opening hook", "1 bold sentence"), ("What's inside", "5–6 clear bullets"), ("Audience filter", "For / Not For"), ("Risk reversal", "Free Checklist first")],
        "Sell <em>specific pages</em>, not abstract chapters.",
        '"Includes modules on mindset, branding, marketing and scaling"',
        '"Page 7: The 15-Minute Painkiller Matrix · Page 14: 30-Day Carousel Engine"',
        "The 5-block <em>Selar Description</em> template.",
        ["Block 1: The 1-sentence outcome statement", "Block 2: Bullet list of exact templates & checklists", "Block 3: Who this playbook is built for", "Block 4: Who should NOT buy this playbook", "Block 5: Instant PDF download specifications"],
        "Honesty about who it's <em>not</em> for builds massive trust.",
        "Read our live Selar copy <em>word-for-word</em>.",
        ['Comment "PLAYBOOK" on this post', "Click the Selar links in your DMs", "Study how both product descriptions are written", "Download the free 7-Day Checklist ($0)", "Or grab the full 23-Page Playbook for $19"],
    ),
    (
        21,
        "Why Official Graph API Automation Beats Sketchy Browser Bots Every Time",
        "Account Safety · 21",
        "Never risk your brand with grey-market bots. Use the <em>Official Graph API</em>.",
        "100% Meta-compliant publishing + <em>zero</em> shadowbans.",
        [("Publishing method", "Official Graph API"), ("Comment replies", "Official API"), ("Cloud uptime", "24/7 GitHub Actions"), ("Password sharing", "Never (OAuth 2.0)")],
        "Build on <em>sanctioned</em> infrastructure that lasts years.",
        '"Giving your IG password to a shady auto-liker bot that gets banned"',
        '"Connecting an Official Instagram Business OAuth token with scoped permissions"',
        "Our 5-layer <em>Safe Autopilot</em> stack.",
        ["Instagram Professional (Business) Account", "Official OAuth scopes for publishing & comments", "Pre-rendered 1080×1350 JPEG assets (quality 92)", "Scheduled GitHub Actions cron workflow", "Idempotent comment tracker (never double-replies)"],
        "Protect your equity while automating the <em>grunt work</em>.",
        "Experience our live API responder <em>right now</em>.",
        ['Comment "PLAYBOOK" below', "Our Official API workflow detects your comment", "Posts a public reply & sends your DM links", "Grab the free 7-Day Launch Checklist", "See how clean automation feels in production"],
    ),
    (
        22,
        "The 7-Day Launch Sprint: Day-By-Day Schedule From Blank Folder To Live Storefront",
        "Execution Roadmap · 22",
        "You don't need 6 months to launch. You need <em>7 focused days</em>.",
        "7 days × 90 mins/day = <em>1 live digital business</em>.",
        [("Days 1–2", "Niche & Free PDF"), ("Days 3–4", "Core $19 Playbook"), ("Day 5", "Selar Storefront"), ("Days 6–7", "IG + DM Autopilot")],
        "Kill perfectionism with a <em>daily ship</em> deadline.",
        '"Spending 4 months picking brand colors and never publishing a product"',
        '"Shipping the free checklist on Day 2 and the $19 playbook on Day 4"',
        "The <em>7-Day</em> Launch Checklist breakdown.",
        ["Day 1: Lock painkiller niche & $19 offer math", "Day 2: Compile the 8-page Free Lead Magnet PDF", "Day 3–4: Compile the 23-page Core Playbook PDF", "Day 5: Publish both offers live on Selar", "Day 6–7: Configure IG bio, Highlights & Day 1 Carousel"],
        "Momentum beats talent <em>10 times out of 10</em>.",
        "Get this entire <em>8-page checklist</em> for free.",
        ['Comment "PLAYBOOK" below', "We'll DM you the direct Selar download link", "Print or check off each day as you build", "And grab the $19 Playbook if you want the full SOPs", "Start Day 1 tonight"],
    ),
    (
        23,
        "How To Create 3D Product Mockups That Make Digital PDFs Feel Like Physical Assets",
        "Perceived Value · 23",
        "People struggle to value invisible files. Make your PDF <em>tangible</em>.",
        "3D mockups increase checkout click-through by <em>32%+</em>.",
        [("Cover lighting", "Subtle gold rim"), ("Perspective", "Isometric hardcover"), ("Badge callout", "23 Pages · Instant PDF"), ("Background", "Obsidian vignette")],
        "Show the <em>artifact</em>, not just a flat rectangle.",
        '"Uploading a generic stock photo as your Selar product thumbnail"',
        '"Rendering a high-resolution 3D book + tablet spread showing real inner pages"',
        "5 elements of a high-converting <em>product mockup</em>.",
        ["Bold serif title readable even at mobile thumbnail size", "Gold pill badge showing exact deliverable format", "Shadow & depth on dark obsidian background", "Consistent QW monogram mark on spine & cover", "Matching visual identity across IG and Selar"],
        "When it looks like a <em>$97 asset</em>, $19 is a no-brainer.",
        "See our live 3D mockup on <em>Selar</em>.",
        ['Comment "PLAYBOOK" below', "Open the Selar storefront link in your DMs", "Download the Free 7-Day Checklist ($0)", "Inspect the $19 Playbook cover & preview", "Elevate your digital product presentation"],
    ),
    (
        24,
        "The 3-Question Buyer FAQ: How To Answer Objections Before They Cost You Sales",
        "Objection Handling · 24",
        "Every silent visitor has <em>3 questions</em> before clicking Buy.",
        "Answering FAQs upfront recovers <em>15–25%</em> of hesitant buyers.",
        [("FAQ #1", "Do I need followers?"), ("FAQ #2", "Do I show my face?"), ("FAQ #3", "How fast is delivery?"), ("Where to place", "Highlight #4 + Selar")],
        "Address skepticism with <em>transparent facts</em>.",
        '"Trust me bro, anyone can make $10k tomorrow with zero work!"',
        '"No followers required to start; carousels reach non-followers via saves & shares."',
        "The 5 answers every buyer needs to see.",
        ["100% faceless: zero camera, zero voice recording", "Works from Day 1 with 0 existing audience", "Instant automated PDF delivery via Selar", "Free 8-page checklist lets you test quality first", "Realistic math & execution — never get-rich-quick"],
        "Transparency turns skeptics into <em>loyal customers</em>.",
        "Test our free guide with <em>zero risk</em>.",
        ['Comment "PLAYBOOK" below', "Get the free 7-Day Launch Checklist in DMs", "Read all 8 pages without spending a cent", "If it helps you, upgrade to the $19 Playbook", "Zero pressure, 100% practical utility"],
    ),
    (
        25,
        "Caption Engineering: How To Structure The First 125 Characters For Maximum '...more' Taps",
        "Caption Copy · 25",
        "Instagram hides your caption after <em>125 characters</em>. Make line 1 count.",
        "Caption dwell time boosts carousel <em>algorithmic score</em>.",
        [("Line 1 length", "< 110 chars"), ("Core bullets", "3–4 takeaways"), ("CTA placement", "Line 2 + bottom"), ("Hashtag count", "8–10 niche tags")],
        "Never waste Line 1 on <em>'Happy Monday guys!'</em>",
        '"Happy Tuesday! Today I want to talk a little bit about digital products..."',
        '"How 1 clean PDF can bring in $100/day — without showing your face 👇"',
        "The 5-part <em>Quietly Wealthy</em> caption template.",
        ["Line 1: Bold hook + 👇 pointer emoji", "Block 2: The 3-line unit economics math summary", "Block 3: Numbered 4-step takeaway list (1️⃣–4️⃣)", "Block 4: Clear keyword CTA (Comment 'PLAYBOOK')", "Block 5: Save reminder + 8–10 targeted hashtags"],
        "Your caption is the <em>sales letter</em> beneath the slides.",
        "Get our caption templates inside the <em>Playbook</em>.",
        ['Comment "PLAYBOOK" below', "We'll DM you the free 7-Day Launch Checklist", "Plus the link to the 23-Page Playbook ($19)", "Copy our exact caption structures for your niche", "Turn caption readers into commenters"],
    ),
    (
        26,
        "Why Selling Templates & Checklists Beats Selling 'Information' In 2026",
        "Product Utility · 26",
        "Information is free on Google. People pay for <em>finished tools</em>.",
        "Templates increase perceived value by <em>5x</em> instantly.",
        [("Pure theory ebook", "Low completion"), ("Checklist + scripts", "Immediate action"), ("Buyer time saved", "10+ hours"), ("Word-of-mouth", "High shares")],
        "Turn every chapter into a <em>fill-in-the-blank</em> asset.",
        '"3,000 words explaining why email marketing is important"',
        '"3 copy-paste welcome emails + 5 DM reply scripts you can use in 2 minutes"',
        "5 high-value assets to pack into your PDF.",
        ["1-page scored decision matrices", "Day-by-day execution checklists with checkboxes", "Copy-paste bio, hook & DM script templates", "Unit economics revenue tables", "Before vs. After teardown cards"],
        "Sell the <em>shortcut</em>, not the encyclopedia.",
        "Download our <em>Checklist + Playbook</em> bundle.",
        ['Comment "PLAYBOOK" on this post', "Grab the free 7-Day Launch Checklist first", "Then unlock the 23-Page Playbook ($19)", "Packed with scripts, tables & checklists", "Use them today or model them for your niche"],
    ),
    (
        27,
        "The Weekly Operator Review: 5 Metrics To Check Every Sunday In 15 Minutes",
        "Operations & KPIs · 27",
        "Run your faceless page like a <em>business</em>, not a hobby.",
        "15 minutes every Sunday keeps growth <em>compounding</em>.",
        [("Posts published", "7 / week"), ("Save-to-Reach %", "Target > 3%"), ("Comment-to-DM %", "100% automated"), ("Storefront Conv.", "Target 2%+")],
        "Double down on the top <em>20%</em> of carousels.",
        '"Posting randomly and never checking which topics actually drove clicks"',
        '"Identifying the #1 most-saved carousel each week and writing 3 follow-up angles"',
        "The 5-step <em>Sunday</em> Operator Audit.",
        ["Verify all 7 scheduled carousels published cleanly", "Rank posts by Saves + 'PLAYBOOK' comments", "Check Selar views vs. free checklist downloads", "Check free checklist downloads vs. $19 sales", "Queue next week's top-performing hook angles"],
        "Small weekly optimizations create <em>massive</em> 90-day gaps.",
        "Get the full <em>Operator System</em>.",
        ['Comment "PLAYBOOK" below', "We'll DM you the free 7-Day Launch Checklist", "And the link to the 23-Page Playbook ($19)", "Build a calm, measurable digital income stream", "Start your first 7-day sprint today"],
    ),
    (
        28,
        "How To Scale From $30/Day To $100+/Day By Adding A Second Tier Or Bundle",
        "Revenue Scaling · 28",
        "Once your first $19 PDF converts, scaling is <em>simple arithmetic</em>.",
        "Raising AOV from $19 → <em>$29</em> adds 52% more revenue.",
        [("6 sales @ $19", "$114 / day"), ("6 sales @ $29 bundle", "$174 / day"), ("Extra traffic needed", "0 visits"), ("Monthly lift", "+$1,800 / mo")],
        "Sell more to the buyers who <em>already trust you</em>.",
        '"Trying to get 10x more followers before optimizing average order value"',
        '"Adding a template pack or playbook bundle for existing storefront buyers"',
        "The 3-step <em>Quietly Wealthy</em> product expansion.",
        ["Tier 1 ($0): 7-Day Launch Checklist (Lead Magnet)", "Tier 2 ($19): 23-Page Core Playbook (Flagship)", "Tier 3 ($29–$47): Complete Template & Prompt Vault", "Cross-link every product inside the PDF footers", "Keep the exact same daily carousel + DM funnel"],
        "One traffic engine can power <em>multiple</em> products.",
        "Start with Tier 1 & Tier 2 <em>today</em>.",
        ['Comment "PLAYBOOK" below', "Get both Selar links in your DMs automatically", "Download the Free 7-Day Checklist ($0)", "Grab the 23-Page Flagship Playbook ($19)", "See how the product ecosystem fits together"],
    ),
    (
        29,
        "The 6 Deadly Mistakes That Kill Faceless Instagram Accounts In Month 1",
        "Risk Prevention · 29",
        "90% of faceless pages quit in 30 days because of <em>6 avoidable</em> mistakes.",
        "Avoid these 6 traps to reach <em>compounding</em> escape velocity.",
        [("Trap #1", "No product ready"), ("Trap #2", "Vague niche"), ("Trap #3", "Inconsistent design"), ("Trap #4", "Manual slow DMs")],
        "Set up the <em>monetization engine</em> before chasing views.",
        '"Going viral with a random reel when you have zero products in your bio"',
        '"Having your Free Checklist, $19 Playbook & Auto-DM live before Post #1"',
        "The 6-point <em>Pre-Flight</em> Survival Checklist.",
        ["Never launch content without your Selar links live", "Never change visual branding every 3 days", "Never write hooks without concrete numbers", "Never forget the Slide 7 keyword CTA", "Never miss a daily post — automate via cloud cron"],
        "Systems survive when <em>motivation</em> fades.",
        "Run our complete <em>Pre-Flight Checklist</em>.",
        ['Comment "PLAYBOOK" on this post', "Get the free 7-Day Launch Checklist in DMs", "Plus the 23-Page Faceless Playbook ($19)", "Launch with all 6 foundations locked in", "Build once, run daily"],
    ),
    (
        30,
        "The 30-Day Compounding Blueprint: What Happens When You Publish 30 Carousels In A Row",
        "The Masterplan · 30",
        "30 carousels × 7 slides = <em>210 digital billboards</em> working for you 24/7.",
        "Every carousel stays on your grid and <em>sells forever</em>.",
        [("30-Day Assets", "30 Carousels"), ("Total Slides", "210 Slides"), ("Live Products", "2 ($0 + $19)"), ("Autopilot Uptime", "24/7 Cloud")],
        "Think in <em>assets</em>, not fleeting 24-hour trends.",
        '"Chasing trendy audio dances that disappear in 48 hours"',
        '"Building an evergreen library of 30 tactical playbooks on your grid"',
        "Your <em>Next 7 Days</em> with Quietly Wealthy.",
        ["Download the Free 7-Day Digital Product Checklist", "Select your high-urgency painkiller niche", "Package your 20-page PDF playbook & freebie", "Publish on Selar with $0 + $19 offer ladder", "Turn on daily carousels + Comment-to-DM autopilot"],
        "The best time to plant the system is <em>today</em>.",
        "Claim your <em>Free Checklist + Playbook</em> now.",
        ['Comment "PLAYBOOK" below', "We'll DM you both Selar links immediately", "1️⃣ Free 7-Day Launch Checklist ($0)", "2️⃣ Faceless Business & Marketing Playbook ($19)", "Follow __HANDLE__ for daily operator playbooks"],
    ),
]


def make_day_entry(row):
    (
        day,
        topic,
        kicker,
        h1_html,
        math_h2,
        math_rows,
        s1_h2,
        bad_txt,
        good_txt,
        s2_h2,
        flow_1,
        s3_h2,
        s4_h2,
        flow_2,
    ) = row

    math_html = "\n".join(
        f'        <div{" class=\"total\"" if idx == len(math_rows) - 1 else ""}><span>{k}</span><span>{v}</span></div>'
        for idx, (k, v) in enumerate(math_rows)
    )
    flow1_html = "\n".join(
        f'        <div{" class=\"win\"" if idx == len(flow_1) - 1 else ""}><b>{idx + 1}</b>{item}</div>'
        for idx, item in enumerate(flow_1)
    )
    flow2_html = "\n".join(
        f'        <div{" class=\"win\"" if idx == len(flow_2) - 1 else ""}><b>{idx + 1}</b>{item}</div>'
        for idx, item in enumerate(flow_2)
    )

    slides = [
        {
            "variant": "cover",
            "content": f"""
      <div class="kicker">{kicker}</div>
      <h1>{h1_html}</h1>
      <p class="lead">The exact math + execution system behind it. <b style="color:#F7F5F0">Save this</b> before you scroll.</p>
      <div class="cover-mark">__MARK__</div>""",
        },
        {
            "variant": "body",
            "content": f"""
      <div class="kicker">The math first</div>
      <h2>{math_h2}</h2>
      <div class="math">
{math_html}
      </div>
      <p class="note">Example math, not a guarantee. Your numbers depend on niche, offer and traffic.</p>""",
        },
        {
            "variant": "body",
            "content": f"""
      <div class="step">Step 01</div>
      <h2>{s1_h2}</h2>
      <p class="lead">Clarity and specificity beat generic advice every single time.</p>
      <div class="vs">
        <div class="card bad"><div class="lbl">Amateur</div><div class="big">{bad_txt}</div></div>
        <div class="card good"><div class="lbl" style="color:#10B981">Operator</div><div class="big">{good_txt}</div></div>
      </div>""",
        },
        {
            "variant": "body",
            "content": f"""
      <div class="step">Step 02</div>
      <h2>{s2_h2}</h2>
      <div class="flow">
{flow1_html}
      </div>
      <p class="note">Built for fast execution — no camera, no face, instant PDF delivery.</p>""",
        },
        {
            "variant": "body",
            "content": f"""
      <div class="step">Step 03</div>
      <h2>{s3_h2}</h2>
      <div class="ratio"><div style="width:80%;background:#14181F;color:#F7F5F0;border:1px solid rgba(229,184,75,.25)">80% VALUE</div>
        <div style="width:20%;background:#E5B84B;color:#0B0D10">20% OFFER</div></div>
      <div class="card"><div class="lbl">Why it compounds</div><div class="big">High-utility slides earn <span class="g">saves &amp; shares</span> → non-follower reach.
        Clean CTAs convert that attention → <span class="g">customers</span>.</div></div>""",
        },
        {
            "variant": "body",
            "content": f"""
      <div class="step">Step 04</div>
      <h2>{s4_h2}</h2>
      <div class="flow">
{flow2_html}
      </div>
      <p class="note">Powered 100% by Official Instagram Graph API automation.</p>""",
        },
        {
            "variant": "cta",
            "content": """
      <div class="center">
        <div class="kicker" style="justify-content:center">Free Checklist + $19 Playbook</div>
        <h2>Want the 7-day launch <em>system</em>?</h2>
        <div class="ctaBox"><p>Comment the word</p><div class="kw">PLAYBOOK</div>
          <p>and I'll DM you the free <b style="color:#F7F5F0">7-Day Launch Checklist</b> + full Playbook link.</p></div>
        <p class="lead" style="font-size:30px">Follow <span style="color:#E5B84B">__HANDLE__</span> for a new playbook every day.</p>
      </div>""",
        },
    ]

    caption = f"""{topic} 👇

Key numbers to know:
→ {math_rows[0][0]}: {math_rows[0][1]}
→ {math_rows[1][0]}: {math_rows[1][1]}
→ {math_rows[-1][0]}: {math_rows[-1][1]}
(Example framework math, not an income guarantee — results depend on niche, offer & execution.)

The execution checklist:
1️⃣ {flow_1[0]}
2️⃣ {flow_1[1]}
3️⃣ {flow_1[2]}
4️⃣ {flow_1[3]}
5️⃣ {flow_1[4]}

Want our Free 7-Day Digital Product Launch Checklist + the 23-Page Faceless Marketing Playbook?
💬 Comment "PLAYBOOK" below and I'll send both links straight to your DMs!

Save this post for reference & follow __HANDLE__ for a new business playbook every day.

#digitalproducts #facelessbusiness #quietlywealthy #selar #passiveincomeideas #ebookbusiness #digitalmarketing #onlinebusinesstips #instagramgrowth #solopreneur"""

    return {
        "day": day,
        "folder": f"day_{day:02d}",
        "topic": topic,
        "kicker": kicker,
        "cta_keyword": "PLAYBOOK",
        "caption": caption,
        "slides": slides,
    }


def main():
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    plan = {"brand": "Quietly Wealthy", "handle": "@quietlywealthy001", "days": [make_day_entry(r) for r in RAW_DAYS]}
    OUT_FILE.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated {len(plan['days'])} days in {OUT_FILE}")


if __name__ == "__main__":
    main()

