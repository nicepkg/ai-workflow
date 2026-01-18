# Launch Strategy Patterns

**Purpose**: Guide for selecting and executing different product launch strategies based on product type, audience, and risk.

---

## Launch Strategy Matrix

| Strategy | Risk Tolerance | Audience Size | Feedback Loop | Speed to Market | Best For |
|----------|---------------|---------------|---------------|-----------------|----------|
| **Beta** | High | Small (10-100) | Tight | Slow | Unproven products, high complexity |
| **Soft Launch** | Medium-High | Medium (100-1000) | Moderate | Medium | Testing market fit, new segments |
| **Phased Rollout** | Medium | Growing | Continuous | Medium | Proven features, large user base |
| **Big Bang** | Low | All at once | Delayed | Fast | Low-risk features, competitive urgency |
| **Stealth** | High | Invite-only | Very tight | Slow | Novel concepts, competitive secrecy |
| **Relaunch** | Medium | Previous + New | Mixed | Medium | Failed launches, pivots, repositions |

---

## Strategy 1: Beta Launch

### Definition

Limited release to small, engaged group for feedback and iteration before public launch.

**Characteristics**:
- Invite-only access
- Direct communication channel with users
- Bugs expected and tolerated
- Rapid iteration based on feedback
- Graduation to broader launch

---

### When to Use

**Good Fit**:
- New product with uncertain market fit
- Complex workflow that needs validation
- High-risk technical implementation
- Need to build early champions

**Examples**:
- Gmail (2004): Invite-only for 3 years
- Superhuman: Invite + onboarding interview for 2 years
- Figma: Designer beta before general availability

**Anti-Patterns** (Don't Use Beta If):
- Simple feature with proven demand (over-engineering)
- Time-sensitive competitive launch (too slow)
- Can't support small group intimately (defeats purpose)

---

### Execution Pattern

**Phase 1: Beta Recruitment (Weeks 1-2)**
- [ ] Define ideal beta profile (PER-XXX personas)
- [ ] Recruit 10-50 users (engaged, representative, articulate)
- [ ] Set expectations (bugs, changes, time commitment)
- [ ] Create private communication channel (Slack, Discord, email group)

**Phase 2: Beta Testing (Weeks 3-8)**
- [ ] Weekly feedback sessions (surveys, interviews, usage data)
- [ ] Bi-weekly product updates (iterate fast)
- [ ] Track engagement (who's using, who dropped off, why)
- [ ] Document feature requests and pain points

**Phase 3: Beta Expansion (Weeks 9-12)**
- [ ] Add 50-100 more users if initial feedback positive
- [ ] Test onboarding with less hand-holding
- [ ] Measure activation and retention
- [ ] Identify power users (potential case studies)

**Phase 4: Graduation to Public (Week 13+)**
- [ ] Fix critical bugs
- [ ] Polish onboarding based on learnings
- [ ] Prepare launch messaging (use beta learnings)
- [ ] Reward beta users (credits, swag, recognition)
- [ ] Public launch (next strategy: Soft Launch or Phased Rollout)

---

### Success Metrics

**Engagement**:
- 70%+ of beta users active weekly
- 10+ pieces of actionable feedback per week
- 3+ user interviews completed

**Quality**:
- 80%+ users would recommend to others (NPS)
- < 5 critical bugs reported per week (decreasing)
- 60%+ activation rate (complete first value action)

**Readiness**:
- Beta users becoming evangelists (sharing on social, referring others)
- No new critical feedback themes (diminishing returns on beta)
- Retention stable or increasing week-over-week

---

## Strategy 2: Soft Launch

### Definition

Limited public launch to specific segment or geography with minimal promotion to test GTM before full launch.

**Characteristics**:
- Public availability (but not promoted widely)
- Specific segment targeted (geography, user type)
- Monitor metrics before scaling
- Iterate GTM (messaging, onboarding, pricing)
- Scale up if metrics hit targets

---

### When to Use

**Good Fit**:
- Testing new market segment
- Uncertain pricing or positioning
- Want to avoid "big splash" with untested product
- Need proof points before larger investment

**Examples**:
- Netflix: Launched in DVD-by-mail in small cities before national
- Stripe: Invite-only soft launch to YC companies before public
- Superhuman: Soft launch to SF tech community before broader

**Anti-Patterns**:
- Established brand with high expectations (soft launch disappoints)
- Viral product that can't be contained (will leak anyway)
- Competitors watching closely (soft launch gives them time to copy)

---

### Execution Pattern

**Phase 1: Segment Selection (Week 1)**
- [ ] Choose test segment (geography, persona, use case)
- [ ] Size: 1,000-10,000 potential users
- [ ] Representative of broader market
- [ ] Low-risk if something goes wrong

**Phase 2: Quiet Launch (Weeks 2-4)**
- [ ] Make product available (no announcement, no PR)
- [ ] Targeted outreach to segment (email, direct sales, communities)
- [ ] Minimal ad spend (test messaging variations)
- [ ] Monitor metrics daily

**Phase 3: Learn & Iterate (Weeks 5-8)**
- [ ] A/B test messaging (which resonates?)
- [ ] Optimize onboarding (where do users drop off?)
- [ ] Test pricing (willingness to pay, plan selection)
- [ ] Customer development (why did they sign up? why did they churn?)

**Phase 4: Decision Point (Week 8)**

**If metrics hit targets**:
- [ ] Scale to broader launch (Phased Rollout or Big Bang)
- [ ] Increase marketing budget
- [ ] Announce publicly

**If metrics miss targets**:
- [ ] Iterate product, messaging, or pricing
- [ ] Extend soft launch period
- [ ] Or pivot/kill feature

---

### Success Metrics

**Acquisition**:
- Hit signup target (e.g., 500 signups in first month)
- CAC (Cost to Acquire) within budget (e.g., < $50/user)
- Organic growth starting (word of mouth, referrals)

**Activation**:
- 40%+ users complete onboarding
- 30%+ users reach "aha moment" (first value)

**Retention**:
- 50%+ users active in Week 2
- 30%+ users active in Week 4

**Revenue** (if applicable):
- 5-10% conversion to paid
- ARPU (Average Revenue Per User) meets expectations

---

## Strategy 3: Phased Rollout

### Definition

Gradual release to increasing percentages of users, monitoring metrics at each phase before expanding.

**Characteristics**:
- Feature flag controlled
- Incremental: 10% → 25% → 50% → 100%
- Monitor metrics at each phase
- Instant rollback if issues
- Reduces blast radius of bugs

---

### When to Use

**Good Fit**:
- Large existing user base (10,000+ users)
- Feature with moderate risk (not trivial, not mission-critical)
- Performance or infrastructure concerns
- Want to validate adoption before full launch

**Examples**:
- Facebook: New features to 1% → 5% → 10% → 50% → 100%
- Google: Search algorithm changes tested on small % of traffic
- Stripe: New payment methods to 10% of merchants first

**Anti-Patterns**:
- Small user base (< 1,000 - not enough signal at 10%)
- Urgent competitive launch (phasing takes time)
- Feature users will hear about and demand immediately (FOMO creates support burden)

---

### Execution Pattern

**Phase 1: 10% Rollout (Days 1-3)**
- [ ] Enable for 10% of users (random or targeted segment)
- [ ] Monitor error rates, latency, user feedback
- [ ] Success criteria: No increase in errors, < 5% support tickets about feature

**Phase 2: 25% Rollout (Days 4-7)**
- [ ] Expand to 25% of users
- [ ] Monitor adoption (what % of exposed users try feature?)
- [ ] Success criteria: 20%+ adoption, 50%+ positive sentiment

**Phase 3: 50% Rollout (Days 8-10)**
- [ ] Expand to 50% of users
- [ ] Monitor retention (do users keep using it?)
- [ ] Success criteria: 30%+ of users who tried it use it again

**Phase 4: 100% Rollout (Days 11-14)**
- [ ] Full availability
- [ ] Announce publicly (blog post, email)
- [ ] Monitor for 48 hours, then consider "launched"

---

### Success Metrics

**At Each Phase**:
- **Stability**: Error rate < 0.5% (same as baseline)
- **Performance**: Latency < 500ms (same as baseline)
- **Adoption**: 20-40% of exposed users try feature
- **Satisfaction**: < 2% negative support tickets

**Rollback Triggers**:
- Error rate > 1%
- Latency > 2x baseline
- Critical bug reported
- > 10% support tickets negative

---

## Strategy 4: Big Bang Launch

### Definition

Full public launch to all users at once with maximum promotion.

**Characteristics**:
- All-at-once availability
- Coordinated marketing push (PR, ads, email, social)
- High visibility, high stakes
- Can't easily rollback (reputational cost)

---

### When to Use

**Good Fit**:
- Low-risk, well-tested feature
- Competitive urgency (first-to-market advantage)
- Simple feature that doesn't need gradual rollout
- Want maximum visibility and PR impact

**Examples**:
- Apple product launches (iPhone, iPad)
- Superhuman launch to public (after 2 years of beta/soft launch)
- Notion 2.0 relaunch

**Anti-Patterns**:
- Untested product (high risk of public failure)
- Complex feature with infrastructure concerns
- Uncertain market fit (waste of marketing spend)

---

### Execution Pattern

**Pre-Launch (Weeks 1-4)**
- [ ] Feature 100% complete and tested
- [ ] Press embargo briefings (TechCrunch, Verge, etc.)
- [ ] Partner coordination (if applicable)
- [ ] Landing page, demo video, blog post ready
- [ ] Email list warmed up (teaser campaign)

**Launch Day (Hour-by-Hour)**
- [ ] 12:01 AM: Press embargo lifts, articles go live
- [ ] 6:00 AM: Email to full list (250k subscribers)
- [ ] 9:00 AM: Product Hunt launch
- [ ] 10:00 AM: Founder social media threads
- [ ] 12:00 PM: Paid ads go live (Google, LinkedIn, Twitter)
- [ ] Throughout day: Monitor metrics, respond to feedback, engage with press

**Post-Launch (Days 1-7)**
- [ ] Daily metrics review
- [ ] Rapid response to issues (bugs, negative feedback)
- [ ] Amplify positive coverage (retweet, share, thank journalists)
- [ ] Week 1 recap blog post ("First 1000 users")

---

### Success Metrics

**Launch Day**:
- 5,000+ signups (or target based on list size)
- Top 5 on Product Hunt
- 3+ press mentions (TechCrunch, Verge, etc.)
- 10,000+ social media impressions

**Week 1**:
- 10,000+ signups
- 40%+ activation rate
- 50+ customer testimonials/tweets
- NPS > 40

---

## Strategy 5: Stealth Launch

### Definition

Invite-only, secretive launch with no public announcement to build mystique and test with trusted users.

**Characteristics**:
- Invite-only access (no public signup)
- NDA or implicit expectation of confidentiality
- High exclusivity, builds FOMO
- Time to iterate before public scrutiny

---

### When to Use

**Good Fit**:
- Novel concept (educate market slowly)
- Competitive secrecy (don't tip off competitors)
- Building cult following (exclusivity drives demand)
- Need time to scale infrastructure

**Examples**:
- Gmail: Invite-only for 3 years (scarcity drove demand)
- Clubhouse: Invite-only for 1 year (FOMO marketing)
- Robinhood: Waitlist grew to 1M before launch

**Anti-Patterns**:
- Simple feature (stealth is overkill)
- Need revenue quickly (stealth delays monetization)
- Competitors already dominate (stealth gives them more lead time)

---

### Execution Pattern

**Phase 1: Invite-Only (Months 1-6)**
- [ ] Hand-pick first 100 users (influencers, early adopters)
- [ ] Give each user 3-5 invites to share
- [ ] Create waitlist for public interest
- [ ] Grow waitlist through word-of-mouth

**Phase 2: Waitlist Expansion (Months 7-12)**
- [ ] Batch invite waitlist users (1,000/week)
- [ ] Monitor capacity and quality
- [ ] Let waitlist grow (FOMO marketing)

**Phase 3: Public Launch (Month 13+)**
- [ ] Open to public (remove invite requirement)
- [ ] Announce waitlist size ("1 million people waited")
- [ ] Convert exclusivity into social proof

---

### Success Metrics

**Waitlist Growth**:
- 10,000+ waitlist in first 3 months (organic)
- 100,000+ waitlist before public launch
- Viral coefficient > 1.2 (each user invites > 1 person)

**Engagement**:
- 80%+ invite acceptance rate (people want in)
- 70%+ weekly active among invited users
- Retention > 60% Month 2

---

## Strategy 6: Relaunch

### Definition

Second attempt at launching a product/feature that previously failed or needs repositioning.

**Characteristics**:
- Acknowledge previous version (transparency)
- Significant improvements (not cosmetic)
- New messaging or positioning
- Win back skeptics

---

### When to Use

**Good Fit**:
- Previous launch failed but learned key lessons
- Product significantly improved (v2.0)
- Market timing now better (market caught up)
- New audience discovered

**Examples**:
- Notion: Relaunched after pivot from consumer to team product
- Slack: Relaunch from gaming to team communication
- Twitter: Multiple relaunches with new features and positioning

**Anti-Patterns**:
- Minor improvements (relaunch hype not justified)
- Same mistakes (team didn't learn from failure)
- Burned bridges (previous users too frustrated to give second chance)

---

### Execution Pattern

**Phase 1: Acknowledge & Apologize (Week 1)**
- [ ] Transparent blog post: "What went wrong, what we learned"
- [ ] Specific improvements made (show, don't tell)
- [ ] Invite previous users to try again (offer incentive)

**Phase 2: Beta with Previous Critics (Weeks 2-4)**
- [ ] Reach out to users who churned or left negative feedback
- [ ] Personal outreach (email, call)
- [ ] "We listened, here's what we built, will you try again?"
- [ ] Collect feedback, iterate

**Phase 3: Public Relaunch (Week 5-6)**
- [ ] New positioning, new messaging
- [ ] Press angle: "Comeback story"
- [ ] Customer testimonials from re-engaged users
- [ ] Fresh start, but own the past

---

### Success Metrics

**Re-engagement**:
- 20%+ of previous churned users return
- 40%+ of returning users activate (second chance conversion)

**New Users**:
- New users don't know about previous failure (clean slate)
- Acquisition metrics same as "new" launch

**Reputation**:
- Positive press ("redemption arc")
- Improved NPS (> 40)

---

## Decision Framework: Which Strategy?

### Step 1: Assess Risk

**High Risk** (Unproven product, complex, mission-critical):
- → **Beta** (if <6 months to validate)
- → **Stealth** (if need secrecy or building cult following)

**Medium Risk** (Proven concept, moderate complexity):
- → **Soft Launch** (if testing GTM in new segment)
- → **Phased Rollout** (if large user base, infrastructure concerns)

**Low Risk** (Simple feature, well-tested, low stakes):
- → **Big Bang** (if want maximum visibility)
- → **Phased Rollout** (if large user base, want data before announcement)

---

### Step 2: Assess Urgency

**High Urgency** (Competitive pressure, market window):
- → **Big Bang** (if low risk)
- → **Soft Launch** (if medium risk, can't afford long beta)

**Medium Urgency** (Normal product development):
- → **Phased Rollout** (default for most features)
- → **Soft Launch** (if testing new segment)

**Low Urgency** (Strategic, long-term):
- → **Beta** (time to iterate)
- → **Stealth** (build anticipation)

---

### Step 3: Assess User Base

**No Users Yet** (New product):
- → **Beta** → **Soft Launch** → **Big Bang** (staged approach)

**Small User Base** (<10,000):
- → **Soft Launch** or **Big Bang** (phased rollout not enough signal)

**Large User Base** (>10,000):
- → **Phased Rollout** (default for safety)

---

## Common Mistakes

### Mistake 1: Over-Engineering Launch

**Problem**: Treating simple feature like major product launch

**Example**: Dark mode with Beta → Soft Launch → Phased → Big Bang (overkill)

**Fix**: Match strategy to risk. Low-risk features: just launch.

---

### Mistake 2: Big Bang with High Risk

**Problem**: Full launch of unproven product

**Example**: Launch payment feature to all users without beta testing

**Fix**: Always de-risk with smaller audience first

---

### Mistake 3: Stealth with No Plan to Scale

**Problem**: Invite-only forever (Gmail trap)

**Example**: Invite-only for 2 years, but can't scale infrastructure when opening up

**Fix**: Plan public launch from day 1, use stealth as temporary phase

---

### Mistake 4: Phased Rollout Too Slow

**Problem**: Moving from 10% → 25% takes weeks (lose momentum)

**Example**: Ship 10%, wait 2 weeks, ship 25%, wait 2 weeks (competitors launch in that time)

**Fix**: Move fast through phases if metrics are green (days, not weeks)

---

*Reference: Use these patterns when planning GTM strategy in `prd-v09-gtm-strategy` skill.*
