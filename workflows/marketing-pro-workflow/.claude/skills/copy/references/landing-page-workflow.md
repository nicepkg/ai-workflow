# SaaS Landing Page Workflow

The difference between typing words onto rectangles and running a knowledge-generating machine.

## Phase 1: Define Strategy & Positioning

This is where we decide what the page is trying to do and for whom. Skipping this phase is how beautiful garbage gets made.

### Define

- **ICP** (ideal customer profile)
- **Job To Be Done**
- **Pain → Desired outcome**
- **Awareness level** (Schwartz: Unaware → Problem-aware → Solution-aware → Product-aware → Most aware)
- **Primary CTA**
- **Single conversion event** (signup, demo, waitlist, trial)

### Strategy Brief Template

```
Audience: [who specifically]
Primary pain: [exact problem they feel]
Desired outcome: [transformation they want]
Main value proposition: [unique benefit]
Alternative solutions today: [what they do now]
Primary CTA: [main action]
Secondary CTA: [fallback action]
Key objections: [what stops them]
Non-negotiable proof: [must-have credibility signals]
```

The page exists to serve that brief.

### Positioning Questions

1. **Who is this for?** Not "everyone"—a specific persona with specific pain
2. **What is the pain?** Not abstract. The moment they feel it.
3. **Why now?** What changed that makes this urgent?
4. **Why you?** What makes your solution unique/better?
5. **Why believe you?** What proof overcomes skepticism?

## Phase 2: Voice-of-Customer Research (VOC)

Pros don't invent copy. They harvest it from real humans.

### Sources

**Support tickets:**
- Pain language: "I'm struggling with..."
- Desired outcomes: "I wish I could..."
- Objections: "But what about..."
- Use cases: "I need this for..."

**Sales call transcripts:**
- Questions prospects ask repeatedly
- Phrases they use to describe their problem
- Hesitations and concerns
- Buying triggers: "Oh, you can do THAT?"

**Reviews (G2, Capterra, App stores):**
- What users love most
- What frustrated them before
- Unexpected use cases
- Comparison to alternatives

**Competitor reviews (goldmine!):**
- What users hate about competitors
- Missing features they desperately want
- Pricing objections
- Support complaints

**User interviews:**
- "What were you doing when you realized you needed this?"
- "What did you try before?"
- "What made you finally decide?"
- "What almost stopped you from buying?"

### Extract

- **Exact phrases about pain:** Copy their words verbatim
- **Desired outcomes:** What success looks like to them
- **Anxieties and objections:** What makes them hesitate
- **Buying triggers:** What pushed them over the edge

### Message Bank Format

| Theme | Quote | Source | Awareness Stage | Notes |
|-------|-------|--------|-----------------|-------|
| Pain: Time waste | "Spending 3 hours/day on reports" | Support #4512 | Problem-aware | Quantified pain |
| Outcome: Speed | "Just want it done in 5 minutes" | G2 review | Solution-aware | Clear metric |
| Objection: Complexity | "Too complicated to set up" | Competitor review | Product-aware | Setup friction |
| Trigger: Pricing | "Found out it was 1/3 the price" | Sales call | Most aware | Price anchor |

Patterns will emerge like constellations in a nerdy night sky.

## Phase 3: Build the Message Architecture

Translate VOC into structured narrative.

### SaaS-Optimized Structure

1. **Hero** = Value Proposition + Who it's for
2. **Context/Problem setup** = Pain they feel right now
3. **Outcome** = Life after using product (not features yet)
4. **How it works** = 3-step process (keep it simple)
5. **Social proof** = Testimonials, logos, metrics
6. **Objection handling** = Address top 3 concerns
7. **CTA** = Primary action (signup, demo)
8. **Risk removal** = Guarantee, free trial, no credit card
9. **Footer safety net CTA** = Last chance conversion

**If it does not help conversion or clarity, it is atmospheric noise.**

### Writing Standards

**Avoid slogans:**
- Bad: "Reinventing the future of work"
- Good: "Turn 3-hour reports into 5-minute dashboards"

**Prefer descriptive clarity:**
- Bad: "Next-generation analytics platform"
- Good: "Analytics that alert you when churn risk spikes"

**Clarity > Poetry. Always.**

### Hero Section Checklist (3-Second Test)

Can a visitor answer these in 3 seconds?
- [ ] What is this?
- [ ] Who is it for?
- [ ] Why should I care now?

If the hero doesn't answer these, back to the lab.

## Phase 4: Layout & Design Decisions

Typography, spacing, and hierarchy earn their keep here.

### Design Heuristics

**Visual hierarchy:**
- One primary CTA color—consistent throughout
- Remove navigation unless needed (reduces exit paths)
- 45–75 character line lengths (optimal readability)
- Body text ≥ 16px (no squinting)
- Contrast ratio ≥ WCAG AA (4.5:1 for text)

**Alignment:**
- Avoid center-aligned paragraphs (except short blocks)
- Left-align body text for scanability
- Center-align headlines and CTAs

**Whitespace:**
- Breathing room between sections
- Don't fear empty space
- Tighter spacing for related elements

### Button Design

**Primary CTA:**
- High contrast color (test against background)
- Large enough to tap (min 44x44px)
- Clear action verb: "Start Free Trial" not "Submit"
- Benefit-oriented: "Get My Free Analysis" not "Sign Up"

**Secondary CTA:**
- Lower contrast (visually de-prioritized)
- Alternative action: "Watch Demo" or "See Pricing"
- Don't compete with primary

## Phase 5: Wireframe First

Lo-fi wireframes before fancy visuals. Discipline over decoration.

### Tools

- FigJam / Figma
- Whimsical
- Miro
- Paper (yes, real trees)

### Process

**1. Work in grayscale first**
- No colors to distract
- Focus on layout and hierarchy
- Test information flow

**2. Typography next**
- Font selection
- Size hierarchy
- Line height and spacing

**3. Color last**
- Brand colors
- CTA contrast
- Emotional tone

This stops design from distracting you from structure.

### Wireframe Checklist

- [ ] Hero communicates value in 3 seconds
- [ ] Clear visual hierarchy (scan path obvious)
- [ ] CTA visible without scrolling
- [ ] Logical content flow (problem → solution → proof → CTA)
- [ ] Mobile-friendly layout

## Phase 6: Build the First Version

Ship fast because data beats theory.

### Build Tools

**No-code:**
- [Webflow](https://webflow.com/) - Designer control, powerful
- [Framer](https://www.framer.com/) - Modern, fast, interactive
- [Unbounce](https://unbounce.com/) - A/B testing built-in

**Code-based:**
- Next.js + TailwindCSS
- Astro + TailwindCSS (fastest loading)
- WordPress (if team already uses it)

### Instrument Before Launch

**Analytics:**
- [GA4](https://analytics.google.com/) - Free, comprehensive
- [Microsoft Clarity](https://clarity.microsoft.com/) - Free heatmaps + session replay
- [PostHog](https://posthog.com/) - Product analytics

**Set up:**

**Events to track:**
- Page views
- CTA clicks (primary and secondary)
- Scroll depth (25%, 50%, 75%, 100%)
- Time on page
- Form starts and completions
- Video plays

**Funnels:**
```
Landing page → CTA click → Form view → Form submit → Success
```

**Goals:**
- Primary: Form submission
- Secondary: Demo request
- Micro: Email signup, video watch

Otherwise you're driving at night without headlights.

### Pre-Launch Checklist

- [ ] All links work
- [ ] Forms submit correctly
- [ ] Mobile responsive (test on real devices)
- [ ] Page speed < 3s (test with PageSpeed Insights)
- [ ] Analytics tracking verified (fire test events)
- [ ] SEO basics (title, meta description, OG tags)

## Phase 7: Form a Hypothesis Backlog

We do not "try stuff." We test hypotheses.

### Hypothesis Format

```
If we: [specific change]
Then: [expected outcome]
Because: [evidence/reasoning]
Measured by: [metric]
Success criteria: [threshold]
Risk: [low/medium/high]
Effort: [low/medium/high]
```

### Example

```
If we: Replace "Sign Up" with "Start Free Trial" on primary CTA
Then: Conversion rate will increase
Because: VOC shows users need reassurance it's free
Measured by: CTA click-through rate
Success criteria: +10% vs control
Risk: Low (easy to revert)
Effort: Low (text change only)
```

### Hypothesis Sources

**From VOC:**
- Users say X is confusing → Test clearer explanation
- Users mention Y benefit repeatedly → Test Y in headline

**From heatmaps:**
- Users not scrolling → Test stronger hook above fold
- Users clicking non-clickable element → Add CTA there

**From industry benchmarks:**
- Long forms converting poorly → Test shorter form
- Video engagement high → Test video in hero

### Prioritize by ICE Score

**I**mpact: How much will this move the needle? (1-10)
**C**onfidence: How sure are we this will work? (1-10)
**E**ffort: How easy is this to implement? (1-10, inverted: 10 = easy)

**ICE Score = (Impact × Confidence) / Effort**

Start with high ICE, low effort. Warm up conversions like stretching before a workout.

## Phase 8: A/B Testing & Experimentation

### Testing Tools

- [VWO](https://vwo.com/) - Visual editor, full-featured
- [Convert](https://www.convert.com/) - Privacy-focused
- [SplitSignal](https://splitsignal.io/) - SEO-safe testing (Ahrefs)
- [Google Optimize](https://optimize.google.com/) - Free (being deprecated)

### Clean Experiment Rules

**One variable at a time:**
- Test headline change alone
- Then test CTA button color alone
- Don't change both simultaneously

**Pre-define success metrics:**
- Primary: Form submissions
- Secondary: Engagement (scroll, time, clicks)
- Don't cherry-pick metrics after seeing results

**Ensure sample size:**
```
Calculator: https://www.optimizely.com/sample-size-calculator/

Example:
- Current conversion rate: 2%
- Minimum detectable effect: +20% (2.4%)
- Sample size needed: 15,000 visitors per variation
- At 1,000 visitors/day: 30 days to reach significance
```

**Avoid peeking biases:**
- Don't stop test early because variant is "winning"
- Run to statistical significance
- Account for day-of-week effects (run full weeks)

### Low Traffic Alternative

Can't reach sample size? Use **sequential learning**:

1. Ship change to 100% traffic
2. Monitor primary metric for 2 weeks
3. Compare to historical baseline
4. Document results
5. Keep or revert

Supplement with:
- User testing (5-user sessions per change)
- Surveys ("Was this page helpful?")
- Session recordings (watch 20 sessions)

## Phase 9: Analyze & Document Learnings

Pros ship reports, not vibes.

### Learning Report Structure

```markdown
## Test: Headline Clarity (2024-01-08)

**Hypothesis:**
If we change headline from "Revolutionary Platform" to 
"Turn 3-Hour Reports Into 5-Minute Dashboards",
then conversion rate will increase because VOC shows 
users value time savings over abstract benefits.

**Setup:**
- Duration: 14 days
- Traffic: 8,432 visitors per variation
- Split: 50/50

**Results:**
| Metric | Control | Variant | Change | Significance |
|--------|---------|---------|--------|--------------|
| Conversion rate | 2.1% | 2.8% | +33% | p < 0.01 ✓ |
| Time on page | 42s | 51s | +21% | p < 0.05 ✓ |
| Bounce rate | 68% | 61% | -10% | p < 0.05 ✓ |

**Winner: Variant** (+33% conversion, statistically significant)

**Behavioral Insights:**
- Heatmaps show more scrolling on variant (47% vs 38% to fold 2)
- Session recordings: 8/10 users verbally mentioned "5 minutes"
- Exit surveys: Variant viewers rated "clarity" 4.2/5 vs 3.1/5

**What We Learned:**
1. Concrete time savings resonate more than abstract value
2. Specific numbers (3 hours → 5 minutes) build credibility
3. Clarity beats cleverness (again!)

**Next Tests:**
- Apply "specific time savings" pattern to subheads
- Test "3 hours" pain point in problem section
```

**Store in shared repo** (Notion, Confluence, GitHub) so knowledge compounds. Your company becomes a memory organism rather than a goldfish.

### Key Metrics to Track

**Conversion funnel:**
```
Landing page → 100%
CTA click → 15%
Form view → 12%
Form submit → 8%
Success page → 7.5%

Drop-off points:
- Landing → CTA: 85% (improve hero)
- CTA → Form: 3% (reduce friction)
- Form → Submit: 4% (form too long?)
```

**Engagement:**
- Scroll depth (% reaching each section)
- Time on page (segmented by converters vs bouncers)
- Click patterns (heatmaps)
- Video watch rate

**Sources:**
- Organic search
- Paid ads
- Social media
- Referrals

Track performance per source—different audiences need different messaging.

## Phase 10: Continuous Optimization Loop

Great landing pages are garden ecosystems, not statues.

### Continually Refine

**Positioning:**
- Market changes (new competitors)
- Customer evolution (more sophisticated)
- Product maturity (new features)

**Messaging:**
- Test new pain points from customer feedback
- Refresh social proof (recent testimonials)
- Update statistics and metrics

**Interaction friction:**
- Reduce form fields (test progressive disclosure)
- Add live chat for questions
- Improve mobile experience

**Pricing clarity:**
- Address new objections
- Simplify plan comparison
- Add FAQs for common questions

**Trust signals:**
- Security badges
- Customer logos
- Press mentions
- Awards and certifications

### Optimization Cadence

**Weekly:**
- Review analytics
- Identify anomalies
- Check heatmaps for new patterns

**Monthly:**
- Run new A/B test
- Update social proof
- Review conversion funnel

**Quarterly:**
- Major redesign elements
- Repositioning if needed
- Competitive analysis

**Annually:**
- Complete page overhaul
- Fresh customer research
- Rebrand if appropriate

Like a scientific practice—endlessly curious, never fully satisfied.

## Common Failure Patterns

### The Beautiful Disaster
Gorgeous design, clever copy, zero conversions.
**Fix:** Put positioning before aesthetics.

### The Feature Dump
Lists 47 features, none resonate.
**Fix:** Benefits before features. Outcomes before benefits.

### The Vague Value Prop
"Best-in-class solution for modern teams."
**Fix:** Specific pain + specific outcome + specific proof.

### The Trust Desert
No social proof, no guarantees, no credibility signals.
**Fix:** Testimonials with attribution, logos, security badges.

### The CTA Graveyard
Seven different calls-to-action competing for attention.
**Fix:** One primary CTA per section.

### The Mystery Pricing
"Contact us for pricing" when competitors show theirs.
**Fix:** Transparent pricing builds trust (unless enterprise-only).

### The Wall of Text
3,000-word essay with no visual breaks.
**Fix:** Short paragraphs, bullets, whitespace, images.

## Success Indicators

**Conversion-focused:**
- Conversion rate > 2% (varies by industry)
- Improving funnel completion over time
- Decreasing cost per acquisition

**Engagement-focused:**
- Scroll depth > 50% to key sections
- Time on page > 60 seconds
- Low bounce rate (< 50%)

**Message-market fit:**
- User surveys: "This page speaks to me" > 70%
- Support: Fewer "What does this do?" questions
- Sales: "They understand the product before calling"

**Business outcomes:**
- Demo show-up rate
- Trial-to-paid conversion
- Customer quality (retention, LTV)

Landing page is the start of the customer journey. Optimize for long-term fit, not just short-term clicks.
