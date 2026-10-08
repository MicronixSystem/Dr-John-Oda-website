# Home page brief: drjohnoda.com redesign

Owner of the brief: Rupam Bhakta (design), Rajdeep (PM), Chandeadeep (project owner).
Source content: `site/_harvest/home-content.md` (verbatim live copy), assets in `site/_harvest/raw/`, catalogue in `site/_harvest/images.md`, brand notes in `site/_harvest/brand.md`.

The copy below is the approved rewrite. Use it as written. Testimonial quotes stay verbatim. Do not add facts, numbers, clients or claims that are not here.

---

## Direction

- **Feel:** a senior advisor's practice, not a coaching funnel. Editorial, confident, a lot of air, big type, few words. The current site is dense paragraphs on a navy gradient with pill buttons; the new one should feel like a business publication with diagrams.
- **Reading:** every block must be scannable in seconds. One idea per line. Long explanations become diagrams (inline SVG), never paragraphs.
- **Infographics are the main visual language**: radial diagram, equation, 2x2 matrix, flow with leak points, path. Draw them as real inline SVG with labels and icons, legible on a phone.
- **Two ways to act everywhere a CTA appears**: the quiz (primary) and a phone call (secondary). This was the key problem on the live site.

### Visual system

- Canvas: warm off-white `#F5F3EE`. Pure white only for cards on top of it.
- Ink: `#131D29`. Dark sections use the logo navy `#212F3F` (or a deeper `#16212D`) as a flat solid ground. No gradients.
- Accents from the logo (sampled): blue `#034CA0`, cyan `#029FDC`. Accent only: headings details, rules, figures, buttons, diagram strokes. Never a large fill.
- Type: a strong display face plus a clean text face from Google Fonts. Suggested: **Archivo** (use its wider widths, 700 to 800, for display) with **Inter** or **Archivo** for text, and a serif italic (e.g. **Source Serif 4** italic) only for testimonial quotes. Big scale contrast: H1 around 64 to 88px desktop, body 18px, nothing below 15px.
- Corners: 0 to 4px. Hairline rules (1px) for structure.
- Icons: one consistent line set (Lucide or Phosphor, inline SVG), 1.5px stroke.

### Banned (Rupam's rules, will be rejected)

- Repeating icon-card grids, generic three-column feature rows, coloured bars across the top of cards, over-rounded boxes, purple/blue gradients, glassmorphism, pill-shaped everything.
- "01 / 02 / 03" numerals as list markers (use icons). Letters O, D, A are fine because they are the method's name.
- Decorative section kickers ("Why you're here", "Start where it matters") and dotted composite lines ("A · B · C").
- Heavy scrims over photos or video. Give text its own solid ground.
- Empty-looking columns; stretched sections (no grid stretch or `space-between` to fill height). Size the type to the space or cut the height.
- Any em dash or en dash in visible text. Write ranges as "$5M to $100M+".
- Two consecutive sections with the same layout or ground.

---

## Assets to prepare (into `site/assets/`)

1. **Logo**: `raw/logo-header_*.webp` (332x98, the only version). Use as-is, displayed no larger than about 230px wide so it stays sharp. Prominent in the nav: trade nav padding for logo height.
2. **Portrait cut-out**: `raw/about-hero-portrait_*.jpg` (1200x1500, flat white background). Remove the white background (rembg if installed, otherwise a careful threshold plus edge feather) to get a transparent WebP. Used once, in the CGO section, standing on a solid ground.
3. **Hero video**: `raw/home-hero-video_*.mp4` (1920x1080, 122s, 72.9 MB, white background, Dr. Oda talking to camera, has audio). Re-encode with ffmpeg to H.264 720p, about 8 MB or less, `+faststart`. Poster frame: pick a frame where he is looking straight into the lens (around 49s to 57s), export as WebP. Plays with sound on click, never autoplays. Because the footage is on white, present it on a white card so it sits clean, no overlay.
4. **Tablet mock-up**: `raw/home-hero-tablet-diagnostic_*.png` (sample Growth Pressure Index report). Used in the BSSM-1 section next to the quadrant diagram.
5. **Book stack**: `raw/book-unlimited-business-growth_*.png`. Used in the book band.
6. **Press logos**: the seven `raw/home-press-*` files. Show them as a single-colour row (CSS filter or recoloured to match the ground). Correct alt text by what the image shows: Yahoo Finance, New York Weekly, America Daily Post, Disrupt, ABC, PBS, Oprah & Friends. The live alt text (NBC, CBS, Forbes...) is wrong: never use those names.
7. **McClendon photo**: `raw/home-testimonial-mcclendon_*.jpeg` is 96px. Avatar size only (48 to 64px).
8. Do not use the purple-ring headshot (off-brand ring baked in, and same shoot as the portrait) or the og-image.
9. Convert all to WebP, real alt text, explicit width/height, lazy-load below the fold.

---

## Sections and copy (in order)

### Nav (reused byte for byte on every page later)

- Logo (left, links home).
- Menu, same targets as live: About (About Me `/about-me`, PR & Media `/pr-media`), Coaching (dropdown, 7 links), Events (5), Business Divisions (5), Resources (3), Contact. Drop the empty Store menu. Full URLs are in `home-content.md`. Links point to `https://drjohnoda.com/...` for now.
- Right: phone link `(949) 868-9144` with a phone icon, and button "Take the Index" (quiz).
- Mobile: logo plus a menu button; the drawer holds the menu and both actions. A sticky bottom bar on mobile with "Call" and "Take the Index".

### 1. Hero (height: 100svh minus nav)

Layout idea: split. Copy on a solid navy panel, the video on a white card that overlaps the panel edge onto the off-white canvas.

- H1: **Growth exposes every weak point.**
- Sub: Dr. John Oda steps inside your leadership team as your Chief Growth Officer, aligning people, systems and profit so scale stops costing you.
- Primary button: **Take the Growth Pressure Index** -> quiz URL
- Secondary: **Call (949) 868-9144** -> `tel:9498689144`
- Under the buttons, three small items with icons: "20 questions" / "5 minutes" / "Instant executive summary"
- Video card caption: "A 2-minute message from Dr. John Oda" and under the name "The Ultimate Chief Growth Officer".

### 2. Proof band (short, horizontal)

- Three figures: **38 years** in mental health and neuroscience / **30 years** in business mastery / **#1** international best-selling author
- "Has worked alongside" Anthony Robbins, Chet Holmes, Jay Abraham, Joseph McClendon III, Scott Hallman (set as type, not pills)
- "As seen on" plus the seven logos.

### 3. Five signals (problem)

- H2: **Five signs growth pressure has reached the top.**
- Each row: icon, the signal in bold, one line beneath.
  - **Revenue is up. Profit is down.** Growth is hiding leaks in cost, vendors and overhead.
  - **Every decision still runs through you.** The business can't grow past the founder's calendar.
  - **Stress is making the calls.** Hiring turns reactive. Spending turns defensive.
  - **Sales are outrunning operations.** Teams work harder and deliver less.
  - **Culture is showing up in the numbers.** Turnover, absenteeism, conflict: symptoms, not HR problems.
- Closing line: **Sound familiar? This is where a Chief Growth Officer steps in.**
- Layout idea: big heading on the left that stays sticky while the five rows scroll on the right, separated by hairlines. Optional small pressure gauge graphic.

### 4. Who it's for

- H2: **Built for one moment: when growth starts creating problems.**
- Big figure: **$5M to $100M+** annual revenue
- Built for: Founder-led or board-managed companies under rising pressure / Teams preparing for scale, acquisition or a capital event / Leadership showing burnout, friction or strain
- Not for: Ideas still looking for product-market fit / Short-term tactical projects / Motivation without accountability / Anyone unwilling to tackle root causes
- Layout idea: a two-sided "yes / no" split with check and cross icons, the revenue figure as the anchor.

### 5. What a CGO is (with the portrait)

- H2: **Not coaching. Not consulting. A growth executive inside your business.**
- Line: A CGO looks across the whole company, not just sales or marketing, and makes growth intentional, coordinated and sustainable.
- Radial diagram: "CGO" at the centre, five nodes: Revenue growth / Profitability / Systems and execution / Leadership capacity / Organizational health.
- Pull line: **Growth is a human issue before it is a business issue.**
- Line: 38 years in mental health and neuroscience. 30 years in business. Dr. Oda works where most advisors never reach. He knows:
  - why leaders burn out under scale
  - why teams disengage under pressure
  - why revenue rises while profit disappears
  - why systems fail as demand accelerates
  - why culture erosion shows in the numbers
- Portrait cut-out on a solid ground, art-directed (cropped at chest, scaled large, not floating small).

### 6. The UCGO framework (equation)

- H2: **Three levers. One strategy.**
- Line: The UCGO framework aligns growth, savings and capital so each one strengthens the others.
- Equation infographic: **Growth + Savings + Capital = Sustainable scale**
  - Growth (BSSM-1 Model): Sales strategy and pipeline / Systems and operational scaling / Leadership capacity and decision quality / Market positioning
  - Savings (EBITDA Optimization): Cost reduction and vendor renegotiation / Merchant fee and payment processing / Operational efficiency and spend governance / Removing technology redundancy
  - Capital (Funding access): **$35K to $2M** for growing companies / **$100M to $5B** for large-scale projects / Capital partner network / Funding strategy and readiness

### 7. BSSM-1 operating system (2x2 matrix plus the tablet)

- H2: **BSSM-1: four quadrants, one clear diagnosis.**
- Line: Most growth plans treat symptoms. BSSM-1 finds the structure underneath.
- 2x2 matrix diagram with an icon per quadrant:
  - **Foundation**: structure, lifecycle, financial stability
  - **Symptoms**: burnout, morale, leadership stress
  - **Systemize**: sales systems, execution rhythm, time leverage
  - **Monetize**: profit stations, cost optimization, hidden revenue
- Statement: **Revenue is optional. Profit is survival.**
- Tablet mock-up beside it with: "See your own quadrant summary" and the quiz button.

### 8. EBITDA (flow with leak points)

- H2: **Revenue is visibility. EBITDA is valuation.**
- Line: Mid-market companies are often revenue-strong and structurally inefficient. Growth hides the leaks.
- Flow infographic: Revenue flows in, six leak points along the way, protected margin comes out. Leak points: Vendor contracts / Procurement / Payment processing / Operating expenses / Technology redundancy / Contract oversight
- Statement: **This isn't cost cutting. It's structural profit engineering.**
- Proof line: Enterprise implementations, from $100M companies to billion-dollar organizations, often improve cost structure by 15 to 30%.
- Outcomes (icons): Higher operating margin / Stronger enterprise valuation / Better cash flow without more revenue
- Small card, **Cost Optimization Diagnostic**: Find recoverable profit before you chase more revenue. Clarity, not a pitch.

### 9. ODA Command Method

- H2: **The ODA Command Method**
- Line: BSSM-1 steadies the business. ODA steadies the leader.
- Three giant letters as the visual device:
  - **O, Outcome**: Define success across revenue, leadership, culture and operations before anyone acts.
  - **D, Desire to serve others**: Lead from service, not ego. Teams that feel served stay, and execute faster.
  - **A, Act as is**: Decide with certainty, not fear, as if the outcome is already in motion.

### 10. What leaders say

- H2: **What leaders say**
- Featured, large: "In just eight months, my business doubled and my net profit increased by 120%." Rob Heidemanns, United Kingdom
- "Dr. Oda is the real deal. He brings a level of insight and depth that I've rarely seen in over 30 years of working with peak performance professionals." Joseph McClendon III, Best-Selling Author, Speaker & Peak Performance Expert (avatar)
- "John's coaching enabled us to gain clarity in both our business and personal life which translated into massive progress and success. The results in our business already paid for the coaching." Leslie Chase & Christy Norton, Business Growth Partners

### 11. How an engagement runs (path)

- H2: **How an engagement runs**
- A horizontal path with three stops (icons, not numbers), vertical on mobile:
  - **Diagnose**: BSSM-1 and cost assessment reveal your constraints and recoverable profit.
  - **Stabilize**: Fix the root causes of burnout, decision fatigue and bottlenecks.
  - **Scale**: Build systems that grow revenue and protect margin together.

### 12. Book band

- Book stack image, art-directed large.
- **Unlimited Business Growth** / #1 international best-seller by Dr. John Oda
- Button: **Get the Book** -> https://ubgp.pnbcgroup.com/book (new tab)

### 13. Final CTA

- H2: **Growth pressure is a signal. Not a sentence.**
- Line: Find out where your business is most exposed. 20 questions, 5 minutes, an instant BSSM-1 quadrant summary.
- Buttons: **Take the Growth Pressure Index** / **Call (949) 868-9144**

### Footer (reused byte for byte on every page later)

- Podcast block: **The Dr. John Oda Method Podcast**, "Where neuroscience meets business mastery", links: Spotify `https://open.spotify.com/show/7MrsGGRrahW0yEIFN0VAcD`, Apple Podcasts, iHeartRadio (URLs in `home-content.md`). Links, not a heavy embed.
- Menu columns (same groups as the nav).
- Contact: phone, address 17595 Harvard Ave Ste C, PMB 4004, Irvine, CA 92614. Social: Facebook, Instagram, LinkedIn, plus TikTok and YouTube if their URLs are in `about-content.md`.
- © 2026 Dr. John Oda, PNBC Group. All rights reserved.
- No Privacy or Terms links (they go nowhere on the live site).

---

## Left out on purpose

- The unsourced statistics (77% burnout, 50%+ decision fatigue, 21% lower profitability, "15 to 33% of profit leaking"). They return only when the client supplies sources.
