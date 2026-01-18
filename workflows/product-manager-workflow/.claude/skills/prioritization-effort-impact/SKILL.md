---
name: prioritization-effort-impact
description: Use when ranking backlogs, deciding what to do first based on effort vs impact (quick wins vs big bets), prioritizing feature roadmaps, triaging bugs or technical debt, allocating resources across initiatives, identifying low-hanging fruit, evaluating strategic options with 2x2 matrix, or when user mentions prioritization, quick wins, effort-impact matrix, high-impact low-effort, big bets, or asks "what should we do first?".
---
# Prioritization: Effort-Impact Matrix

## Table of Contents
1. [Purpose](#purpose)
2. [When to Use](#when-to-use)
3. [What Is It?](#what-is-it)
4. [Workflow](#workflow)
5. [Common Patterns](#common-patterns)
6. [Scoring Frameworks](#scoring-frameworks)
7. [Guardrails](#guardrails)
8. [Quick Reference](#quick-reference)

## Purpose

Transform overwhelming backlogs and option lists into clear, actionable priorities by mapping items on a 2x2 matrix of effort (cost/complexity) vs impact (value/benefit). Identify quick wins (high impact, low effort) and distinguish them from big bets (high impact, high effort), time sinks (low impact, high effort), and fill-ins (low impact, low effort).

## When to Use

**Use this skill when:**

- **Backlog overflow**: You have 20+ items (features, bugs, tasks, ideas) and need to decide execution order
- **Resource constraints**: Limited time, budget, or people force trade-off decisions
- **Strategic planning**: Choosing between initiatives, projects, or investments for quarterly/annual roadmaps
- **Quick wins needed**: Stakeholders want visible progress fast; you need high-impact low-effort items
- **Trade-off clarity**: Team debates "should we do A or B?" without explicit effort/impact comparison
- **Alignment gaps**: Different stakeholders (eng, product, sales, exec) have conflicting priorities
- **Context switching**: Too many simultaneous projects; need to focus on what matters most
- **New PM/leader**: Taking over a backlog and need systematic prioritization approach

**Common triggers:**
- "We have 50 feature requests, where do we start?"
- "What are the quick wins?"
- "Should we do the migration or the new feature first?"
- "How do we prioritize technical debt vs new features?"
- "What gives us the most bang for our buck?"

## What Is It?

**Effort-Impact Matrix** (also called Impact-Effort Matrix, Quick Wins Matrix, or 2x2 Prioritization) plots each item on two dimensions:

- **X-axis: Effort** (time, cost, complexity, risk, dependencies)
- **Y-axis: Impact** (value, revenue, user benefit, strategic alignment, risk reduction)

**Four quadrants:**

```
High Impact │
            │  Big Bets       │  Quick Wins
            │  (do 2nd)       │  (do 1st!)
            │─────────────────┼─────────────
            │  Time Sinks     │  Fill-Ins
            │  (avoid)        │  (do last)
Low Impact  │
            └─────────────────┴─────────────
              High Effort       Low Effort
```

**Example:** Feature backlog with 12 items

| Item | Effort | Impact | Quadrant |
|------|--------|--------|----------|
| Add "Export to CSV" button | Low (2d) | High (many users) | **Quick Win** ✓ |
| Rebuild entire auth system | High (3mo) | High (security) | Big Bet |
| Perfect pixel alignment on logo | High (1wk) | Low (aesthetic) | Time Sink ❌ |
| Fix typo in footer | Low (5min) | Low (trivial) | Fill-In |

**Decision:** Do "Export to CSV" first (quick win), schedule auth rebuild next (big bet), skip logo perfection (time sink), batch typo fixes (fill-ins).

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

**Step 1: Gather items and clarify scoring**

Collect all items to prioritize (features, bugs, initiatives, etc.) and define scoring scales for effort and impact. See [Scoring Frameworks](#scoring-frameworks) for effort and impact definitions. Use [resources/template.md](resources/template.md) for structure.

**Step 2: Score effort and impact**

Rate each item on effort (1-5: trivial to massive) and impact (1-5: negligible to transformative). Involve subject matter experts for accuracy. See [resources/methodology.md](resources/methodology.md) for advanced scoring techniques like Fibonacci, T-shirt sizes, or RICE.

**Step 3: Plot matrix and identify quadrants**

Place items on 2x2 matrix and categorize into Quick Wins (high impact, low effort), Big Bets (high impact, high effort), Fill-Ins (low impact, low effort), and Time Sinks (low impact, high effort). See [Common Patterns](#common-patterns) for typical quadrant distributions.

**Step 4: Create prioritized roadmap**

Sequence items: Quick Wins first, Big Bets second (after quick wins build momentum), Fill-Ins during downtime, avoid Time Sinks unless required. See [resources/template.md](resources/template.md) for roadmap structure.

**Step 5: Validate and communicate decisions**

Self-check using [resources/evaluators/rubric_prioritization_effort_impact.json](resources/evaluators/rubric_prioritization_effort_impact.json). Ensure scoring is defensible, stakeholder perspectives included, and decisions clearly explained with rationale.

## Common Patterns

**By domain:**

- **Product backlogs**: Quick wins = small UX improvements, Big bets = new workflows, Time sinks = edge case perfection
- **Technical debt**: Quick wins = config fixes, Big bets = architecture overhauls, Time sinks = premature optimizations
- **Bug triage**: Quick wins = high-impact easy fixes, Big bets = complex critical bugs, Time sinks = cosmetic issues
- **Strategic initiatives**: Quick wins = process tweaks, Big bets = market expansion, Time sinks = vanity metrics
- **Marketing campaigns**: Quick wins = email nurture, Big bets = brand overhaul, Time sinks = minor A/B tests

**By stakeholder priority:**

- **Execs want**: Quick wins (visible progress) + Big bets (strategic impact)
- **Engineering wants**: Technical debt quick wins + Big bets (platform work)
- **Sales wants**: Quick wins that unblock deals + Big bets (major features)
- **Customers want**: Quick wins (pain relief) + Big bets (transformative value)

**Typical quadrant distribution:**
- Quick Wins: 10-20% (rare, high-value opportunities)
- Big Bets: 20-30% (strategic, resource-intensive)
- Fill-Ins: 40-50% (most backlogs have many low-value items)
- Time Sinks: 10-20% (surprisingly common, often disguised as "polish")

**Red flags:**
- ❌ **No quick wins**: Likely overestimating effort or underestimating impact
- ❌ **All quick wins**: Scores probably not calibrated correctly
- ❌ **Many time sinks**: Cut scope or reject these items
- ❌ **Effort/impact scores all 3**: Need more differentiation (use 1-2 and 4-5)

## Scoring Frameworks

**Effort dimensions (choose relevant ones):**
- **Time**: Engineering/execution hours (1=hours, 2=days, 3=weeks, 4=months, 5=quarters)
- **Complexity**: Technical difficulty (1=trivial, 5=novel/unprecedented)
- **Risk**: Failure probability (1=safe, 5=high-risk)
- **Dependencies**: External blockers (1=none, 5=many teams/approvals)
- **Cost**: Financial investment (1=$0-1K, 2=$1-10K, 3=$10-100K, 4=$100K-1M, 5=$1M+)

**Impact dimensions (choose relevant ones):**
- **Users affected**: Reach (1=<1%, 2=1-10%, 3=10-50%, 4=50-90%, 5=>90%)
- **Business value**: Revenue/savings (1=$0-10K, 2=$10-100K, 3=$100K-1M, 4=$1-10M, 5=$10M+)
- **Strategic alignment**: OKR contribution (1=tangential, 5=critical to strategy)
- **User pain**: Problem severity (1=nice-to-have, 5=blocker/crisis)
- **Risk reduction**: Mitigation value (1=minor, 5=existential risk)

**Composite scoring:**
- **Simple**: Average of dimensions (Effort = avg(time, complexity), Impact = avg(users, value))
- **Weighted**: Multiply by importance (Effort = 0.6×time + 0.4×complexity)
- **Fibonacci**: Use 1, 2, 3, 5, 8 instead of 1-5 for exponential differences
- **T-shirt sizes**: S/M/L/XL mapped to 1/2/3/5

**Example scoring (feature: "Add dark mode"):**
- Effort: Time=3 (2 weeks), Complexity=2 (CSS), Risk=2 (minor bugs), Dependencies=1 (no blockers) → **Avg = 2.0 (Low)**
- Impact: Users=4 (80% want it), Value=2 (retention, not revenue), Strategy=3 (design system goal), Pain=3 (eye strain) → **Avg = 3.0 (Medium-High)**
- **Result**: Medium-High Impact, Low Effort → **Quick Win!**

## Guardrails

**Ensure quality:**

1. **Include diverse perspectives**: Don't let one person score alone (eng overestimates effort, sales overestimates impact)
   - ✓ Get engineering, product, sales, customer success input
   - ❌ PM scores everything solo

2. **Differentiate scores**: If everything is scored 3, you haven't prioritized
   - ✓ Force rank or use wider scale (1-10)
   - ✓ Aim for distribution: few 1s/5s, more 2s/4s, many 3s
   - ❌ All items scored 2.5-3.5

3. **Question extreme scores**: High-impact low-effort items are rare (if you have 10, something's wrong)
   - ✓ "Why haven't we done this already?" test for quick wins
   - ❌ Wishful thinking (underestimating effort, overestimating impact)

4. **Make scoring transparent**: Document why each score was assigned
   - ✓ "Effort=4 because requires 3 teams, new infrastructure, 6-week timeline"
   - ❌ "Effort=4" with no rationale

5. **Revisit scores periodically**: Effort/impact change as context evolves
   - ✓ Re-score quarterly or after major changes (new tech, new team size)
   - ❌ Use 2-year-old scores

6. **Don't ignore dependencies**: Low-effort items blocked by high-effort prerequisites aren't quick wins
   - ✓ "Effort=2 for task, but depends on Effort=5 migration"
   - ❌ Score task in isolation

7. **Beware of "strategic" override**: Execs calling everything "high impact" defeats prioritization
   - ✓ "Strategic" is one dimension, not a veto
   - ❌ "CEO wants it" → auto-scored 5

## Quick Reference

**Resources:**
- **Quick start**: [resources/template.md](resources/template.md) - 2x2 matrix template and scoring table
- **Advanced techniques**: [resources/methodology.md](resources/methodology.md) - RICE, MoSCoW, Kano, weighted scoring
- **Quality check**: [resources/evaluators/rubric_prioritization_effort_impact.json](resources/evaluators/rubric_prioritization_effort_impact.json) - Evaluation criteria

**Success criteria:**
- ✓ Identified 1-3 quick wins to execute immediately
- ✓ Sequenced big bets into realistic roadmap (don't overcommit)
- ✓ Cut or deferred time sinks (low ROI items)
- ✓ Scoring rationale is transparent and defensible
- ✓ Stakeholders aligned on priorities
- ✓ Roadmap has capacity buffer (don't schedule 100% of time)

**Common mistakes:**
- ❌ Scoring in isolation (no stakeholder input)
- ❌ Ignoring effort (optimism bias: "everything is easy")
- ❌ Ignoring impact (building what's easy, not what's valuable)
- ❌ Analysis paralysis (perfect scores vs good-enough prioritization)
- ❌ Not saying "no" to time sinks
- ❌ Overloading roadmap (filling every week with big bets)
- ❌ Forgetting maintenance/support time (assuming 100% project capacity)

**When to use alternatives:**
- **Weighted scoring (RICE)**: When you need more nuance than 2x2 (Reach × Impact × Confidence / Effort)
- **MoSCoW**: When prioritizing for fixed scope/deadline (Must/Should/Could/Won't)
- **Kano model**: When evaluating customer satisfaction (basic/performance/delight features)
- **ICE score**: Simpler than RICE (Impact × Confidence × Ease)
- **Value vs complexity**: Same as effort-impact, different labels
- **Cost of delay**: When timing matters (revenue lost by delaying)
