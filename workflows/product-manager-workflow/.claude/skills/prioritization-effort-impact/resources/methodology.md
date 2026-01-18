# Prioritization: Advanced Methodologies

## Table of Contents
1. [Advanced Scoring Frameworks](#1-advanced-scoring-frameworks)
2. [Alternative Prioritization Models](#2-alternative-prioritization-models)
3. [Stakeholder Alignment Techniques](#3-stakeholder-alignment-techniques)
4. [Data-Driven Prioritization](#4-data-driven-prioritization)
5. [Roadmap Optimization](#5-roadmap-optimization)
6. [Common Pitfalls and Solutions](#6-common-pitfalls-and-solutions)

---

## 1. Advanced Scoring Frameworks

### RICE Score (Reach × Impact × Confidence / Effort)

**Formula**: `Score = (Reach × Impact × Confidence) / Effort`

**When to use**: Product backlogs where user reach and confidence matter more than simple impact

**Components**:
- **Reach**: Users/customers affected per time period (e.g., 1000 users/quarter)
- **Impact**: Value per user (1=minimal, 2=low, 3=medium, 4=high, 5=massive)
- **Confidence**: How certain are we? (100%=high, 80%=medium, 50%=low)
- **Effort**: Person-months (e.g., 2 = 2 engineers for 1 month, or 1 engineer for 2 months)

**Example**:
- Feature A: (5000 users/qtr × 3 impact × 100% confidence) / 2 effort = **7500 score**
- Feature B: (500 users/qtr × 5 impact × 50% confidence) / 1 effort = **1250 score**
- **Decision**: Feature A scores 6× higher despite lower per-user impact

**Advantages**: More nuanced than 2x2 matrix, accounts for uncertainty
**Disadvantages**: Requires estimation of reach (hard for new features)

### ICE Score (Impact × Confidence × Ease)

**Formula**: `Score = Impact × Confidence × Ease`

**When to use**: Growth experiments, marketing campaigns, quick prioritization

**Components**:
- **Impact**: Potential value (1-10 scale)
- **Confidence**: How sure are we this will work? (1-10 scale)
- **Ease**: How easy to implement? (1-10 scale, inverse of effort)

**Example**:
- Experiment A: 8 impact × 9 confidence × 7 ease = **504 score**
- Experiment B: 10 impact × 3 confidence × 5 ease = **150 score**
- **Decision**: A scores higher due to confidence, even with lower max impact

**Advantages**: Simpler than RICE, no time period needed
**Disadvantages**: Multiplicative scoring can exaggerate differences

### Weighted Scoring (Custom Criteria)

**When to use**: Complex decisions with multiple evaluation dimensions beyond effort/impact

**Process**:
1. Define criteria (e.g., Revenue, Strategic Fit, User Pain, Complexity, Risk)
2. Weight each criterion (sum to 100%)
3. Score each item on each criterion (1-5)
4. Calculate weighted score: `Score = Σ(criterion_score × criterion_weight)`

**Example**:

| Criteria | Weight | Feature A Score | Feature A Weighted | Feature B Score | Feature B Weighted |
|----------|--------|----------------|-------------------|----------------|-------------------|
| Revenue | 40% | 4 | 1.6 | 2 | 0.8 |
| Strategic | 30% | 5 | 1.5 | 4 | 1.2 |
| User Pain | 20% | 3 | 0.6 | 5 | 1.0 |
| Complexity | 10% | 2 (low) | 0.2 (penalty) | 4 (high) | 0.4 (penalty) |
| **Total** | **100%** | - | **3.9** | - | **3.0** |

**Decision**: Feature A scores higher (3.9 vs 3.0) due to revenue and strategic fit

**Advantages**: Transparent, customizable to organization's values
**Disadvantages**: Can become analysis paralysis with too many criteria

### Kano Model (Customer Satisfaction)

**When to use**: Understanding which features delight vs must-have vs don't-matter

**Categories**:
- **Must-Be (Basic)**: Absence causes dissatisfaction, presence is expected (e.g., product works, no security bugs)
- **Performance (Linear)**: More is better, satisfaction increases linearly (e.g., speed, reliability)
- **Delighters (Excitement)**: Unexpected features that wow users (e.g., dark mode before it was common)
- **Indifferent**: Users don't care either way (e.g., internal metrics dashboard for end users)
- **Reverse**: Some users actively dislike (e.g., forced tutorials, animations)

**Survey technique**:
- Ask functional question: "How would you feel if we had feature X?" (Satisfied / Expected / Neutral / Tolerate / Dissatisfied)
- Ask dysfunctional question: "How would you feel if we did NOT have feature X?"
- Map responses to category

**Prioritization strategy**:
1. **Must-Be first**: Fix broken basics (dissatisfiers)
2. **Delighters for differentiation**: Quick wins that wow
3. **Performance for competitiveness**: Match or exceed competitors
4. **Avoid indifferent/reverse**: Don't waste time

**Example**:
- Must-Be: Fix crash on login (everyone expects app to work)
- Performance: Improve search speed from 2s to 0.5s
- Delighter: Add "undo send" for emails (unexpected delight)
- Indifferent: Add 50 new color themes (most users don't care)

### Value vs Complexity (Alternative Labels)

**When to use**: Same as effort-impact, but emphasizes business value and technical complexity

**Axes**:
- **X-axis: Complexity** (technical difficulty, dependencies, unknowns)
- **Y-axis: Value** (business value, strategic value, user value)

**Quadrants** (same concept, different framing):
- **High Value, Low Complexity** = Quick Wins (same)
- **High Value, High Complexity** = Strategic Investments (same as Big Bets)
- **Low Value, Low Complexity** = Nice-to-Haves (same as Fill-Ins)
- **Low Value, High Complexity** = Money Pits (same as Time Sinks)

**When to use this framing**: Technical audiences respond to "complexity", business audiences to "value"

---

## 2. Alternative Prioritization Models

### MoSCoW (Must/Should/Could/Won't)

**When to use**: Fixed-scope projects (e.g., product launch, migration) with deadline constraints

**Categories**:
- **Must Have**: Non-negotiable, project fails without (e.g., core functionality, security, legal requirements)
- **Should Have**: Important but not critical, defer if needed (e.g., nice UX, analytics)
- **Could Have**: Desirable if time/budget allows (e.g., polish, edge cases)
- **Won't Have (this time)**: Out of scope, revisit later (e.g., advanced features, integrations)

**Process**:
1. List all requirements
2. Stakeholders categorize each (force hard choices: only 60% can be Must/Should)
3. Build Must-Haves first, then Should-Haves, then Could-Haves if time remains
4. Communicate Won't-Haves to set expectations

**Example (product launch)**:
- **Must**: User registration, core workflow, payment processing, security
- **Should**: Email notifications, basic analytics, help docs
- **Could**: Dark mode, advanced filters, mobile app
- **Won't**: Integrations, API, white-labeling (v2 scope)

**Advantages**: Forces scope discipline, clear for deadline-driven work
**Disadvantages**: Doesn't account for effort (may put high-effort items in Must)

### Cost of Delay (CD3: Cost, Duration, Delay)

**When to use**: Time-sensitive decisions where delaying has quantifiable revenue/strategic cost

**Formula**: `CD3 Score = Cost of Delay / Duration`
- **Cost of Delay**: $/month of delaying this (revenue loss, market share, customer churn)
- **Duration**: Months to complete

**Example**:
- Feature A: $100K/mo delay cost, 2 months duration → **$50K/mo score**
- Feature B: $200K/mo delay cost, 5 months duration → **$40K/mo score**
- **Decision**: Feature A higher score (faster time-to-value despite lower total CoD)

**When to use**: Competitive markets, revenue-critical features, time-limited opportunities (e.g., seasonal)

**Advantages**: Explicitly values speed to market
**Disadvantages**: Requires estimating revenue impact (often speculative)

### Opportunity Scoring (Jobs-to-be-Done)

**When to use**: Understanding which user jobs are underserved (high importance, low satisfaction)

**Survey**:
- Ask users to rate each "job" on:
  - **Importance**: How important is this outcome? (1-5)
  - **Satisfaction**: How well does current solution satisfy? (1-5)

**Opportunity Score**: `Importance + max(Importance - Satisfaction, 0)`
- Score ranges 0-10
- **>8 = High opportunity** (important but poorly served)
- **<5 = Low opportunity** (either unimportant or well-served)

**Example**:
- Job: "Quickly find relevant past conversations"
  - Importance: 5 (very important)
  - Satisfaction: 2 (very dissatisfied)
  - Opportunity: 5 + (5-2) = **8 (high opportunity)** → prioritize search improvements

- Job: "Customize notification sounds"
  - Importance: 2 (not important)
  - Satisfaction: 3 (neutral)
  - Opportunity: 2 + 0 = **2 (low opportunity)** → deprioritize

**Advantages**: User-centric, identifies gaps between need and solution
**Disadvantages**: Requires user research, doesn't account for effort

---

## 3. Stakeholder Alignment Techniques

### Silent Voting (Avoid Anchoring Bias)

**Problem**: First person to score influences others (anchoring bias), HIPPO dominates
**Solution**: Everyone scores independently, then discuss

**Process**:
1. Each stakeholder writes scores on sticky notes (don't share yet)
2. Reveal all scores simultaneously
3. Discuss discrepancies (why did eng score Effort=5 but product scored Effort=2?)
4. Converge on consensus score

**Tools**: Planning poker (common in agile), online voting (Miro, Mural)

### Forced Ranking (Avoid "Everything is High Priority")

**Problem**: Stakeholders rate everything 4-5, no differentiation
**Solution**: Force stack ranking (only one item can be #1)

**Process**:
1. List all items
2. Stakeholders must rank 1, 2, 3, ..., N (no ties allowed)
3. Convert ranks to scores (e.g., top 20% = 5, next 20% = 4, middle 20% = 3, etc.)

**Variant: $100 Budget**:
- Give stakeholders $100 to "invest" across all items
- They allocate dollars based on priority ($30 to A, $25 to B, $20 to C, ...)
- Items with most investment are highest priority

### Weighted Stakeholder Input (Account for Expertise)

**Problem**: Not all opinions are equal (eng knows effort, sales knows customer pain)
**Solution**: Weight scores by expertise domain

**Example**:
- Effort score = 100% from Engineering (they know effort best)
- Impact score = 40% Product + 30% Sales + 30% Customer Success (all know value)

**Process**:
1. Define who estimates what (effort, user impact, revenue, etc.)
2. Assign weights (e.g., 60% engineering + 40% product for effort)
3. Calculate weighted average: `Score = Σ(stakeholder_score × weight)`

### Pre-Mortem for Controversial Items

**Problem**: Stakeholders disagree on whether item is Quick Win or Time Sink
**Solution**: Run pre-mortem to surface hidden risks/assumptions

**Process**:
1. Assume item failed spectacularly ("We spent 6 months and it failed")
2. Each stakeholder writes down "what went wrong" (effort blowups, impact didn't materialize)
3. Discuss: Are these risks real? Should we adjust scores or descope?

**Example**:
- Item: "Build mobile app" (scored Impact=5, Effort=3)
- Pre-mortem reveals: "App store approval took 3 months", "iOS/Android doubled effort", "Users didn't download"
- **Revised score**: Impact=3 (uncertain), Effort=5 (doubled for two platforms) → Time Sink, defer

---

## 4. Data-Driven Prioritization

### Usage Analytics (Prioritize High-Traffic Areas)

**When to use**: Product improvements where usage data is available

**Metrics**:
- **Page views / Feature usage**: Improve high-traffic areas first (more users benefit)
- **Conversion funnel**: Fix drop-off points with biggest impact (e.g., 50% drop at checkout)
- **Support tickets**: High ticket volume = high user pain

**Example**:
- Dashboard page: 1M views/mo, 10% bounce rate → **100K frustrated users** → high impact
- Settings page: 10K views/mo, 50% bounce rate → **5K frustrated users** → lower impact
- **Decision**: Fix dashboard first (20× more impact)

**Advantages**: Objective, quantifies impact
**Disadvantages**: Ignores new features (no usage data yet), low-traffic areas may be high-value for specific users

### A/B Test Results (Validate Impact Assumptions)

**When to use**: Uncertain impact; run experiment to measure before committing

**Process**:
1. Build minimal version of feature (1-2 weeks)
2. A/B test with 10% of users
3. Measure impact (conversion, retention, revenue, NPS)
4. If impact validated, commit to full version; if not, deprioritize

**Example**:
- Hypothesis: "Adding social login will increase signups 20%"
- A/B test: 5% increase (not 20%)
- **Decision**: Impact=3 (not 5 as assumed), deprioritize vs other items

**Advantages**: Reduces uncertainty, validates assumptions before big bets
**Disadvantages**: Requires experimentation culture, time to run tests

### Customer Request Frequency (Vote Counting)

**When to use**: Feature requests from sales, support, customers

**Metrics**:
- **Request count**: Number of unique customers asking
- **Revenue at risk**: Total ARR of customers requesting (enterprise vs SMB)
- **Churn risk**: Customers threatening to leave without feature

**Example**:
- Feature A: 50 SMB customers requesting ($5K ARR each) = **$250K ARR**
- Feature B: 2 Enterprise customers requesting ($200K ARR each) = **$400K ARR**
- **Decision**: Feature B higher impact (more revenue at risk) despite fewer requests

**Guardrail**: Don't just count votes (10 vocal users ≠ real demand), weight by revenue/strategic value

### NPS/CSAT Drivers Analysis

**When to use**: Understanding which improvements drive customer satisfaction most

**Process**:
1. Collect NPS/CSAT scores
2. Ask open-ended: "What's the one thing we could improve?"
3. Categorize feedback (performance, features, support, etc.)
4. Correlate categories with NPS (which issues are mentioned by detractors most?)

**Example**:
- Detractors (NPS 0-6) mention "slow performance" 80% of time
- Passives (NPS 7-8) mention "missing integrations" 60%
- **Decision**: Fix performance first (bigger impact on promoter score)

---

## 5. Roadmap Optimization

### Dependency Mapping (Critical Path)

**Problem**: Items with dependencies can't start until prerequisites complete
**Solution**: Map dependency graph, identify critical path

**Process**:
1. List all items with dependencies (A depends on B, C depends on A and D)
2. Draw dependency graph (use tools: Miro, Mural, project management software)
3. Identify critical path (longest chain of dependencies)
4. Parallelize non-dependent work

**Example**:
- Quick Win A (2 weeks) → Big Bet B (8 weeks) → Quick Win C (1 week) = **11 week critical path**
- Quick Win D (2 weeks, no dependencies) can run in parallel with A
- **Optimized timeline**: 11 weeks instead of 13 weeks (if sequential)

### Team Velocity and Capacity Planning

**Problem**: Overcommitting to more work than team can deliver
**Solution**: Use historical velocity to forecast capacity

**Process**:
1. Measure past velocity (effort points completed per sprint/quarter)
2. Estimate total capacity (team size × utilization × time period)
3. Don't plan >70-80% of capacity (buffer for unknowns, support, bugs)

**Example**:
- Team completes 20 effort points/quarter historically
- Next quarter roadmap: 30 effort points planned
- **Problem**: 150% overcommitted
- **Fix**: Cut lowest-priority items (time sinks, fill-ins) to fit 16 effort points (80% of 20)

**Guardrail**: If you consistently complete <50% of roadmap, estimation is broken (not just overcommitted)

### Incremental Delivery (Break Big Bets into Phases)

**Problem**: Big Bet takes 6 months; no value delivery until end
**Solution**: Break into phases that deliver incremental value

**Example**:
- **Original**: "Rebuild reporting system" (6 months, Effort=5)
- **Phased**:
  - Phase 1: Migrate 3 most-used reports (1 month, Effort=2, Impact=3)
  - Phase 2: Add drill-down capability (1 month, Effort=2, Impact=4)
  - Phase 3: Real-time data (2 months, Effort=3, Impact=5)
  - Phase 4: Custom dashboards (2 months, Effort=3, Impact=3)
- **Benefit**: Ship value after 1 month (not 6), can adjust based on feedback

**Advantages**: Faster time-to-value, reduces risk, allows pivoting
**Disadvantages**: Requires thoughtful phasing (some work can't be incrementalized)

### Portfolio Balancing (Mix of Quick Wins and Big Bets)

**Problem**: Roadmap is all quick wins (no strategic depth) or all big bets (no momentum)
**Solution**: Balance portfolio across quadrants and time horizons

**Target distribution**:
- **70% Quick Wins + Fill-Ins** (short-term value, momentum)
- **30% Big Bets** (long-term strategic positioning)
- OR by time: **Now (0-3 months)**: 60%, **Next (3-6 months)**: 30%, **Later (6-12 months)**: 10%

**Example**:
- Q1: 5 quick wins + 1 big bet Phase 1
- Q2: 3 quick wins + 1 big bet Phase 2
- Q3: 4 quick wins + 1 new big bet start
- **Result**: Consistent value delivery (quick wins) + strategic progress (big bets)

---

## 6. Common Pitfalls and Solutions

### Pitfall 1: Solo Scoring (No Stakeholder Input)

**Problem**: PM scores everything alone, misses engineering effort or sales context
**Solution**: Multi-stakeholder scoring session (2-hour workshop)

**Workshop agenda**:
- 0-15min: Align on scoring scales (calibrate with examples)
- 15-60min: Silent voting on effort/impact for all items
- 60-90min: Discuss discrepancies, converge on consensus
- 90-120min: Plot matrix, identify quadrants, sequence roadmap

### Pitfall 2: Analysis Paralysis (Perfect Scores)

**Problem**: Spending days debating if item is Effort=3.2 or Effort=3.4
**Solution**: Good-enough > perfect; prioritization is iterative

**Guardrail**: Limit scoring session to 2 hours; if still uncertain, default to conservative (higher effort, lower impact)

### Pitfall 3: Ignoring Dependencies

**Problem**: Quick Win scored Effort=2, but depends on Effort=5 migration completing first
**Solution**: Score standalone effort AND prerequisite effort separately

**Example**:
- Item: "Add SSO login" (Effort=2 standalone)
- Depends on: "Migrate to new auth system" (Effort=5)
- **True effort**: 5 (for new roadmaps) or 2 (if migration already planned)

### Pitfall 4: Strategic Override ("CEO Wants It")

**Problem**: Exec declares item "high priority" without scoring, bypasses process
**Solution**: Make execs participate in scoring, apply same framework

**Response**: "Let's score this using our framework so we can compare to other priorities. If it's truly high impact and low effort, it'll naturally rise to the top."

### Pitfall 5: Sunk Cost Fallacy (Continuing Time Sinks)

**Problem**: "We already spent 2 months on X, we can't stop now" (even if impact is low)
**Solution**: Sunk costs are sunk; evaluate based on future effort/impact only

**Decision rule**: If you wouldn't start this project today knowing what you know, stop it now

### Pitfall 6: Neglecting Maintenance (Assuming 100% Project Capacity)

**Problem**: Roadmap plans 100% of team time, ignoring support/bugs/tech debt/meetings
**Solution**: Reduce capacity by 20-50% for non-project work

**Realistic capacity**:
- 100% time - 20% support/bugs - 10% meetings - 10% code review/pairing = **60% project capacity**
- If team is 5 people × 40 hrs/wk × 12 weeks = 2400 hrs, only 1440 hrs available for roadmap

### Pitfall 7: Ignoring User Research (Opinion-Based Scoring)

**Problem**: Impact scores based on team intuition, not user data
**Solution**: Validate impact with user research (surveys, interviews, usage data)

**Quick validation**:
- Survey 50 users: "How important is feature X?" (1-5)
- If <50% say 4-5, impact is not as high as assumed
- Adjust scores based on data

### Pitfall 8: Scope Creep During Execution

**Problem**: Quick Win (Effort=2) grows to Big Bet (Effort=5) during implementation
**Solution**: Timebox quick wins; if effort exceeds estimate, cut scope or defer

**Guardrail**: "If this takes >1 week, we stop and re-evaluate whether it's still worth it"

### Pitfall 9: Forgetting to Say "No"

**Problem**: Roadmap keeps growing (never remove items), becomes unexecutable
**Solution**: Explicitly cut time sinks, communicate what you're NOT doing

**Communication template**: "We prioritized X, Y, Z based on impact/effort. This means we're NOT doing A, B, C this quarter because [reason]. We'll revisit in [timeframe]."

### Pitfall 10: One-Time Prioritization (Never Re-Score)

**Problem**: Scores from 6 months ago are stale (context changed, new data available)
**Solution**: Re-score quarterly, adjust roadmap based on new information

**Triggers for re-scoring**:
- Quarterly planning cycles
- Major context changes (new competitor, customer churn, team size change)
- Big bets complete (update dependent items' scores)
- User research reveals new insights
