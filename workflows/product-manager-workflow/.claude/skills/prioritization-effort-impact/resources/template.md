# Prioritization: Effort-Impact Matrix Template

## Table of Contents
1. [Workflow](#workflow)
2. [Prioritization Matrix Template](#prioritization-matrix-template)
3. [Scoring Table Template](#scoring-table-template)
4. [Prioritized Roadmap Template](#prioritized-roadmap-template)
5. [Guidance for Each Section](#guidance-for-each-section)
6. [Quick Patterns](#quick-patterns)
7. [Quality Checklist](#quality-checklist)

## Workflow

Copy this checklist and track your progress:

```
Prioritization Progress:
- [ ] Step 1: Gather items and clarify scoring
- [ ] Step 2: Score effort and impact
- [ ] Step 3: Plot matrix and identify quadrants
- [ ] Step 4: Create prioritized roadmap
- [ ] Step 5: Validate and communicate decisions
```

**Step 1:** Collect all items to prioritize and define scoring scales. See [Scoring Table Template](#scoring-table-template) for structure.

**Step 2:** Rate each item on effort (1-5) and impact (1-5) with stakeholder input. See [Guidance: Scoring](#guidance-scoring) for calibration tips.

**Step 3:** Plot items on 2x2 matrix and categorize into quadrants. See [Prioritization Matrix Template](#prioritization-matrix-template) for visualization.

**Step 4:** Sequence items into roadmap (Quick Wins → Big Bets → Fill-Ins, avoid Time Sinks). See [Prioritized Roadmap Template](#prioritized-roadmap-template) for execution plan.

**Step 5:** Self-check quality and communicate decisions with rationale. See [Quality Checklist](#quality-checklist) for validation.

---

## Prioritization Matrix Template

Copy this section to create your effort-impact matrix:

### Effort-Impact Matrix: [Context Name]

**Date**: [YYYY-MM-DD]
**Scope**: [e.g., Q1 Product Backlog, Technical Debt Items, Strategic Initiatives]
**Participants**: [Names/roles who contributed to scoring]

#### Matrix Visualization

```
High Impact │
         5  │  Big Bets           │  Quick Wins
            │  [Item names]       │  [Item names]
         4  │                     │
            │                     │
         3  │─────────────────────┼─────────────────
            │                     │
         2  │  Time Sinks         │  Fill-Ins
            │  [Item names]       │  [Item names]
         1  │                     │
Low Impact  │                     │
            └─────────────────────┴─────────────────
              5    4    3    2    1
            High Effort        Low Effort
```

**Visual Plotting** (if using visual tools):
- Create 2x2 grid (effort on X-axis, impact on Y-axis)
- Place each item at coordinates (effort, impact)
- Use color coding: Green=Quick Wins, Blue=Big Bets, Yellow=Fill-Ins, Red=Time Sinks
- Add item labels or numbers for reference

#### Quadrant Summary

**Quick Wins (High Impact, Low Effort)** - Do First! ✓
- [Item 1]: Impact=5, Effort=2 - [Brief rationale]
- [Item 2]: Impact=4, Effort=1 - [Brief rationale]
- **Total**: X items

**Big Bets (High Impact, High Effort)** - Do Second
- [Item 3]: Impact=5, Effort=5 - [Brief rationale]
- [Item 4]: Impact=4, Effort=4 - [Brief rationale]
- **Total**: X items

**Fill-Ins (Low Impact, Low Effort)** - Do During Downtime
- [Item 5]: Impact=2, Effort=1 - [Brief rationale]
- [Item 6]: Impact=1, Effort=2 - [Brief rationale]
- **Total**: X items

**Time Sinks (Low Impact, High Effort)** - Avoid/Defer ❌
- [Item 7]: Impact=2, Effort=5 - [Brief rationale for why low impact]
- [Item 8]: Impact=1, Effort=4 - [Brief rationale]
- **Total**: X items
- **Recommendation**: Cut scope, reject, or significantly descope these items

---

## Scoring Table Template

Copy this table to score all items systematically:

### Scoring Table: [Context Name]

| # | Item Name | Effort | Impact | Quadrant | Notes/Rationale |
|---|-----------|--------|--------|----------|-----------------|
| 1 | [Feature/initiative name] | 2 | 5 | Quick Win ✓ | [Why this score?] |
| 2 | [Another item] | 4 | 4 | Big Bet | [Why this score?] |
| 3 | [Another item] | 1 | 2 | Fill-In | [Why this score?] |
| 4 | [Another item] | 5 | 2 | Time Sink ❌ | [Why low impact?] |
| ... | ... | ... | ... | ... | ... |

**Scoring Scales:**

**Effort (1-5):**
- **1 - Trivial**: < 1 day, one person, no dependencies, no risk
- **2 - Small**: 1-3 days, one person or pair, minimal dependencies
- **3 - Medium**: 1-2 weeks, small team, some dependencies or moderate complexity
- **4 - Large**: 1-2 months, cross-team coordination, significant complexity or risk
- **5 - Massive**: 3+ months, major initiative, high complexity/risk/dependencies

**Impact (1-5):**
- **1 - Negligible**: <5% users affected, <$10K value, minimal pain relief
- **2 - Minor**: 5-20% users, $10-50K value, nice-to-have improvement
- **3 - Moderate**: 20-50% users, $50-200K value, meaningful pain relief
- **4 - Major**: 50-90% users, $200K-1M value, significant competitive advantage
- **5 - Transformative**: >90% users, $1M+ value, existential or strategic imperative

**Effort Dimensions (optional detail):**
| # | Item | Time | Complexity | Risk | Dependencies | **Avg Effort** |
|---|------|------|------------|------|--------------|----------------|
| 1 | [Item] | 2 | 2 | 1 | 2 | **2** |

**Impact Dimensions (optional detail):**
| # | Item | Users | Business Value | Strategy | Pain | **Avg Impact** |
|---|------|-------|----------------|----------|------|----------------|
| 1 | [Item] | 5 | 4 | 5 | 5 | **5** |

---

## Prioritized Roadmap Template

Copy this section to sequence items into execution plan:

### Prioritized Roadmap: [Context Name]

**Planning Horizon**: [e.g., Q1 2024, Next 6 months]
**Team Capacity**: [e.g., 3 engineers × 80% project time = 2.4 FTE, assumes 20% support/maintenance]
**Execution Strategy**: Quick Wins first to build momentum, then Big Bets for strategic impact

#### Phase 1: Quick Wins (Weeks 1-4)

**Objective**: Deliver visible value fast, build stakeholder confidence

| Priority | Item | Effort | Impact | Timeline | Owner | Dependencies |
|----------|------|--------|--------|----------|-------|--------------|
| 1 | [Quick Win 1] | 2 | 5 | Week 1-2 | [Name] | None |
| 2 | [Quick Win 2] | 1 | 4 | Week 2 | [Name] | None |
| 3 | [Quick Win 3] | 2 | 4 | Week 3-4 | [Name] | [Blocker if any] |

**Expected Outcomes**: [User impact, metrics improvement, stakeholder wins]

#### Phase 2: Big Bets (Weeks 5-16)

**Objective**: Tackle high-value strategic initiatives

| Priority | Item | Effort | Impact | Timeline | Owner | Dependencies |
|----------|------|--------|----------|----------|-------|--------------|
| 4 | [Big Bet 1] | 5 | 5 | Week 5-12 | [Team/Name] | Quick Win 1 complete |
| 5 | [Big Bet 2] | 4 | 4 | Week 8-14 | [Team/Name] | External API access |
| 6 | [Big Bet 3] | 4 | 5 | Week 12-18 | [Team/Name] | Phase 1 learnings |

**Expected Outcomes**: [Strategic milestones, competitive positioning, revenue impact]

#### Phase 3: Fill-Ins (Ongoing, Low Priority)

**Objective**: Batch small tasks during downtime, sprint buffers, or waiting periods

| Item | Effort | Impact | Timing | Notes |
|------|--------|--------|--------|-------|
| [Fill-In 1] | 1 | 2 | Sprint buffer | Do if capacity available |
| [Fill-In 2] | 2 | 1 | Between phases | Nice-to-have polish |
| [Fill-In 3] | 1 | 2 | Waiting on blocker | Quick task while blocked |

**Strategy**: Don't schedule these explicitly; fill gaps opportunistically

#### Deferred/Rejected Items (Time Sinks)

**Objective**: Communicate what we're NOT doing and why

| Item | Effort | Impact | Reason for Rejection | Reconsider When |
|------|--------|--------|----------------------|-----------------|
| [Time Sink 1] | 5 | 2 | Low ROI, niche use case | User demand increases 10× |
| [Time Sink 2] | 4 | 1 | Premature optimization | Performance becomes bottleneck |
| [Time Sink 3] | 5 | 2 | Edge case perfection | Core features stable for 6mo |

**Communication**: Explicitly tell stakeholders these are cut to focus resources on higher-impact work

#### Capacity Planning

**Total Planned Work**: [X effort points] across Quick Wins + Big Bets
**Available Capacity**: [Y effort points] (team size × time × utilization)
**Buffer**: [Z%] for unplanned work, support, bugs
**Risk**: [High/Medium/Low] - [Explanation of capacity risks]

**Guardrail**: Don't exceed 70-80% of available capacity to allow for unknowns

---

## Guidance for Each Section

### Guidance: Scoring

**Get diverse input**:
- **Engineering**: Estimates effort (time, complexity, risk, dependencies)
- **Product**: Estimates impact (user value, business value, strategic alignment)
- **Sales/CS**: Validates customer pain and business value
- **Design**: Assesses UX impact and design effort

**Calibration session**:
1. Score 3-5 reference items together to calibrate scale
2. Use these as anchors: "If X is a 3, then Y is probably a 2"
3. Document examples: "Effort=2 example: Add CSV export (2 days, one dev)"

**Avoid bias**:
- ❌ **Anchoring**: First person's score influences others → use silent voting, then discuss
- ❌ **Optimism bias**: Engineers underestimate effort → add 20-50% buffer
- ❌ **HIPPO (Highest Paid Person's Opinion)**: Exec scores override reality → anonymous scoring first
- ❌ **Recency bias**: Recent successes inflate confidence → review past estimates

**Differentiate scores**:
- If 80% of items are scored 3, you haven't prioritized
- Force distribution: Top 20% are 4-5, bottom 20% are 1-2, middle 60% are 2-4
- Use ranking if needed: "Rank all items, then assign scores based on distribution"

### Guidance: Quadrant Interpretation

**Quick Wins (High Impact, Low Effort)** - Rare, valuable
- ✓ Do these immediately
- ✓ Communicate early wins to build momentum
- ❌ Beware: If you have >5 quick wins, scores may be miscalibrated
- ❓ Ask: "If this is so easy and valuable, why haven't we done it already?"

**Big Bets (High Impact, High Effort)** - Strategic focus
- ✓ Schedule 1-2 big bets per quarter (don't overcommit)
- ✓ Break into phases/milestones for incremental value
- ✓ Start after quick wins to build team capability and stakeholder trust
- ❌ Don't start 3+ big bets simultaneously (thrashing, context switching)

**Fill-Ins (Low Impact, Low Effort)** - Opportunistic
- ✓ Batch together (e.g., "polish sprint" once per quarter)
- ✓ Do during downtime, sprint buffers, or while blocked
- ❌ Don't schedule explicitly (wastes planning time)
- ❌ Don't let these crowd out big bets

**Time Sinks (Low Impact, High Effort)** - Avoid!
- ✓ Explicitly reject or defer with clear rationale
- ✓ Challenge: Can we descope to make this lower effort?
- ✓ Communicate to stakeholders: "We're not doing X because..."
- ❌ Don't let these sneak into roadmap due to HIPPO or sunk cost fallacy

### Guidance: Roadmap Sequencing

**Phase 1: Quick Wins First**
- Builds momentum, team confidence, stakeholder trust
- Delivers early value while learning about systems/users
- Creates psychological safety for bigger risks later

**Phase 2: Big Bets Second**
- Team is warmed up, systems are understood
- Quick wins have bought goodwill for longer timeline items
- Learnings from Phase 1 inform Big Bet execution

**Phase 3: Fill-Ins Opportunistically**
- Don't schedule; do when capacity available
- Useful for onboarding new team members (low-risk tasks)
- Good for sprint buffers or while waiting on dependencies

**Dependencies:**
- Map explicitly (item X depends on item Y completing)
- Use critical path analysis for complex roadmaps
- Build slack/buffer before dependent items

---

## Quick Patterns

### By Context

**Product Backlog (50+ features)**:
- Effort: Engineering time + design + QA + deployment risk
- Impact: User reach × pain severity × business value
- Quick wins: UX fixes, config changes, small integrations
- Big bets: New workflows, platform changes, major redesigns

**Technical Debt (30+ items)**:
- Effort: Refactoring time + testing + migration risk
- Impact: Developer productivity + future feature velocity + incidents prevented
- Quick wins: Dependency upgrades, linting fixes, small refactors
- Big bets: Architecture overhauls, language migrations, monolith → microservices

**Bug Triage (100+ bugs)**:
- Effort: Debug time + fix complexity + regression risk + deployment
- Impact: User pain × frequency × business impact (revenue/support cost)
- Quick wins: High-frequency easy fixes, workarounds for critical bugs
- Big bets: Complex race conditions, performance issues, architectural bugs

**Strategic Initiatives (10-20 ideas)**:
- Effort: People × months + capital + dependencies
- Impact: Revenue/cost impact + strategic alignment + competitive advantage
- Quick wins: Process improvements, pilot programs, low-cost experiments
- Big bets: Market expansion, platform bets, major partnerships

### Common Scenarios

**All Big Bets, No Quick Wins**:
- Problem: Roadmap takes 6+ months for first value delivery
- Fix: Break big bets into phases; ship incremental value
- Example: Instead of "Rebuild platform" (6mo), do "Migrate auth" (1mo) + "Migrate users" (1mo) + ...

**All Quick Wins, No Strategic Depth**:
- Problem: Delivering small wins but losing competitive ground
- Fix: Schedule 1-2 big bets per quarter for strategic positioning
- Balance: 70% quick wins + fill-ins, 30% big bets

**Too Many Time Sinks**:
- Problem: Backlog clogged with low-value high-effort items
- Fix: Purge ruthlessly; if impact is low, effort doesn't matter
- Communication: "We're closing 20 low-value items to focus resources"

---

## Quality Checklist

Before finalizing, verify:

**Scoring Quality:**
- [ ] Diverse stakeholders contributed to scores (eng, product, sales, etc.)
- [ ] Scores are differentiated (not all 3s; use full 1-5 range)
- [ ] Extreme scores questioned ("Why haven't we done this quick win already?")
- [ ] Scoring rationale documented for transparency
- [ ] Effort includes time, complexity, risk, dependencies (not just time)
- [ ] Impact includes users, value, strategy, pain (not just one dimension)

**Matrix Quality:**
- [ ] 10-20% Quick Wins (if 0%, scores miscalibrated; if 50%, too optimistic)
- [ ] 20-30% Big Bets (strategic work, not just small tasks)
- [ ] Time Sinks identified and explicitly cut/deferred
- [ ] Items clustered around quadrant boundaries re-evaluated (e.g., Effort=2.5, Impact=2.5)
- [ ] Visual matrix created (not just table) for stakeholder communication

**Roadmap Quality:**
- [ ] Quick Wins scheduled first (Weeks 1-4)
- [ ] Big Bets scheduled second (after momentum built)
- [ ] Fill-Ins not explicitly scheduled (opportunistic)
- [ ] Time Sinks explicitly rejected with rationale communicated
- [ ] Dependencies mapped (item X depends on Y)
- [ ] Capacity buffer included (don't plan 100% of capacity)
- [ ] Timeline realistic (effort scores × team size = weeks)

**Communication Quality:**
- [ ] Prioritization decisions explained (not just "we're doing X")
- [ ] Trade-offs visible ("Doing X means not doing Y")
- [ ] Stakeholder concerns addressed ("Sales wanted Z, but impact is low because...")
- [ ] Success metrics defined (how will we know this roadmap succeeded?)
- [ ] Review cadence set (re-score quarterly, adjust roadmap monthly)

**Red Flags to Fix:**
- ❌ One person scored everything alone
- ❌ All scores are 2.5-3.5 (not differentiated)
- ❌ Zero quick wins identified
- ❌ Roadmap is 100% big bets (unrealistic)
- ❌ Time sinks included in roadmap (low ROI)
- ❌ No capacity buffer (planned at 100%)
- ❌ No rationale for why items were prioritized
- ❌ Stakeholders disagree on scores but no discussion happened
