# Roadmap Backcast: Advanced Methodologies

## Table of Contents
1. [Critical Path Method (CPM) Mathematics](#1-critical-path-method-cpm-mathematics)
2. [Advanced Dependency Patterns](#2-advanced-dependency-patterns)
3. [Buffer Management Techniques](#3-buffer-management-techniques)
4. [Multi-Track Roadmaps](#4-multi-track-roadmaps)
5. [Risk-Adjusted Timeline Planning](#5-risk-adjusted-timeline-planning)
6. [Resource Optimization](#6-resource-optimization)

## 1. Critical Path Method (CPM) Mathematics

### Forward Pass (Earliest Start/Finish)

**Process**:
1. Start at beginning, assign ES=0 to first milestone
2. For each milestone: EF = ES + Duration
3. For dependent milestones: ES = max(EF of all prerequisites)
4. Continue until end milestone

**Example**:
```
Milestone A: ES=0, Duration=4, EF=4
Milestone B (depends on A): ES=4, Duration=6, EF=10
Milestone C (depends on A): ES=4, Duration=3, EF=7
Milestone D (depends on B, C): ES=max(10,7)=10, Duration=2, EF=12
```

**Project duration**: EF of final milestone = 12 weeks

### Backward Pass (Latest Start/Finish)

**Process**:
1. Start at end, assign LF = EF of final milestone
2. For each milestone: LS = LF - Duration
3. For prerequisites: LF = min(LS of all dependents)
4. Continue until start milestone

**Example** (working backward from D):
```
Milestone D: LF=12, Duration=2, LS=10
Milestone B (enables D): LF=10, Duration=6, LS=4
Milestone C (enables D): LF=10, Duration=3, LS=7
Milestone A (enables B, C): LF=min(4,7)=4, Duration=4, LS=0
```

### Slack Calculation

**Slack** (or Float) = LS - ES = LF - EF

**Milestones with zero slack are on critical path**:
- Milestone A: 0-0=0 ✓ Critical
- Milestone B: 4-4=0 ✓ Critical
- Milestone C: 7-4=3 (3 weeks slack, non-critical)
- Milestone D: 10-10=0 ✓ Critical

**Critical path**: A → B → D (12 weeks)

### Using Slack for Scheduling

**Milestones with slack**:
- Can be delayed up to slack amount without impacting project
- Use slack to smooth resource utilization
- Delay non-critical work to free resources for critical path

**Example**: Milestone C has 3 weeks slack
- Can start as early as week 4 (ES=4)
- Must start no later than week 7 (LS=7)
- Flexibility to schedule based on resource availability

## 2. Advanced Dependency Patterns

### Soft Dependencies vs Hard Dependencies

**Hard dependency** (cannot proceed without):
- Example: Cannot test code until code is written
- Enforce strictly in schedule

**Soft dependency** (preferable but not required):
- Example: Prefer to have design complete before engineering, but can start with partial design
- Allow overlap if timeline pressure, accept rework risk

### Lag and Lead Time

**Lag**: Mandatory delay between dependent tasks
- Example: "Concrete must cure 7 days after pouring before building on it"
- Add lag to dependency: A → [+7 days lag] → B

**Lead**: Task can start before prerequisite fully completes
- Example: "Can start integration testing when 80% of code complete"
- Negative lag or start-to-start dependency with offset

### Conditional Dependencies

**Branching dependencies**:
```
Design Complete → [If design approved] → Engineering
                → [If design rejected] → Redesign → Engineering
```

**Include in backcast**: Plan for expected path, note contingency branches

### External Dependencies (Outside Team Control)

**Vendor deliveries, regulatory approvals, partner integration**:
- Identify early (longest lead time often on critical path)
- Add extra buffer (40-50% for external dependencies)
- Establish contract penalties for delays
- Plan alternative paths where possible

**Example**:
- Primary path: Vendor delivers component → Integration (4 weeks lead time, +50% buffer = 6 weeks)
- Backup path: Build in-house (8 weeks, more reliable) - evaluate cost/benefit

## 3. Buffer Management Techniques

### Critical Chain Project Management (CCPM)

**Concept**: Remove buffers from individual tasks, aggregate into project buffer at end

**Traditional approach**:
- Task A: 4 weeks + 20% buffer = 4.8 weeks
- Task B: 6 weeks + 30% buffer = 7.8 weeks
- Total: 12.6 weeks

**CCPM approach**:
- Task A: 4 weeks (aggressive estimate)
- Task B: 6 weeks (aggressive estimate)
- Project buffer: 50% of critical path = 5 weeks
- Total: 15 weeks (4+6+5)

**Benefits**: Prevents Parkinson's Law (work expands to fill time), focuses on project completion not task completion

### Buffer Placement

**Project buffer**: At end of critical path (protects project deadline)

**Feeding buffer**: Where non-critical path joins critical path (prevents non-critical delays from impacting critical)

**Example**:
```
Critical: A (4w) → B (6w) → D (2w) → [Project Buffer: 3w]
Non-critical: C (3w) → [Feeding Buffer: 1w] → D
```

**Feeding buffer protects against C delaying D's start**

### Buffer Consumption Monitoring

**Traffic light system**:
- **Green** (0-33% buffer consumed): On track
- **Yellow** (33-67% buffer consumed): Warning, monitor closely
- **Red** (67-100% buffer consumed): Crisis, corrective action needed

**Example**: 12-week critical path, 3-week buffer
- Week 8 complete, 1 week delay → 1/3 buffer consumed → Green
- Week 10 complete, 3 weeks delay → 3/3 buffer consumed → Red (need to accelerate or extend deadline)

## 4. Multi-Track Roadmaps

### Parallel Workstreams

**Identify independent tracks**:
- Track 1 (Frontend): Design → Frontend dev → Frontend testing
- Track 2 (Backend): API design → Backend dev → Backend testing
- Track 3 (Infrastructure): Cloud setup → CI/CD → Monitoring

**Synchronization points** (all tracks must converge):
- Integration testing (requires all 3 tracks complete)
- Deploy to production (requires integration testing + infrastructure ready)

**Managing multi-track**:
- Assign clear owners to each track
- Identify longest track (determines overall timeline)
- Monitor convergence points closely (often become critical)

### Portfolio Backcasting (Multiple Initiatives)

**Scenario**: Launch Products A, B, C by Q4 2025

**Approach**:
1. Backcast each product independently
2. Identify resource conflicts (same people/budget needed)
3. Sequence to resolve conflicts (stagger starts, prioritize critical path work)
4. Re-assess portfolio feasibility

**Resource smoothing**: Adjust non-critical task timing to avoid resource over-allocation

## 5. Risk-Adjusted Timeline Planning

### Monte Carlo Simulation for Timelines

**Process**:
1. For each milestone, estimate optimistic/likely/pessimistic duration (3-point estimate)
2. Run 1000+ simulations, randomly sampling from distributions
3. Generate probability distribution of project completion dates

**Example**:
```
Milestone A: Optimistic=3w, Likely=4w, Pessimistic=6w
Milestone B: Optimistic=4w, Likely=6w, Pessimistic=10w
Milestone D: Optimistic=1w, Likely=2w, Pessimistic=4w
```

**Simulation results**:
- P50 (median): 12 weeks (50% chance complete by week 12)
- P80: 15 weeks (80% chance complete by week 15)
- P95: 18 weeks (95% chance complete by week 18)

**Use P80 or P90 for deadline setting** (realistic buffer)

### PERT (Program Evaluation and Review Technique)

**Expected duration formula**:
```
Expected = (Optimistic + 4×Likely + Pessimistic) / 6
```

**Example**:
```
Milestone A: (3 + 4×4 + 6) / 6 = 4.17 weeks
Milestone B: (4 + 4×6 + 10) / 6 = 6.33 weeks
Milestone D: (1 + 4×2 + 4) / 6 = 2.17 weeks
Critical path: 4.17 + 6.33 + 2.17 = 12.67 weeks
```

**Standard deviation** (measures uncertainty):
```
σ = (Pessimistic - Optimistic) / 6
```

**Example**:
```
Milestone B: σ = (10 - 4) / 6 = 1 week
```

**68% chance B completes within 6.33 ± 1 week = 5.33 to 7.33 weeks**

### Risk-Driven Milestone Sequencing

**Identify highest-risk milestones** (technical unknowns, novel work, external dependencies)

**De-risk early**: Sequence high-risk work toward beginning of roadmap
- Learn quickly if infeasible
- Maximize time to pivot if needed
- Avoid sunk cost trap (months invested before discovering blocker)

**Example**:
- High risk: "Integrate with Partner X API" (never done before, unknown technical constraints)
- **Do early**: Spike integration in month 1, not month 6 (discover blockers sooner)

## 6. Resource Optimization

### Resource Leveling

**Problem**: Resource over-allocation (need 10 engineers, have 5)

**Solution**:
1. Identify over-allocated periods
2. Delay non-critical tasks (use slack)
3. If still over-allocated, extend critical path

**Example**:
```
Weeks 1-4: Tasks A + C = 10 engineers needed, have 5
Task C has 3 weeks slack → Delay C to weeks 5-7
Result: Weeks 1-4 (Task A: 5 engineers), Weeks 5-7 (Task C: 5 engineers)
```

### Resource Smoothing

**Goal**: Minimize resource fluctuations (avoid hire/fire cycles)

**Approach**: Shift non-critical tasks within slack to create steady resource demand

**Example**:
```
Original: Weeks 1-4 (10 eng), Weeks 5-8 (2 eng), Weeks 9-12 (8 eng)
Smoothed: Weeks 1-4 (6 eng), Weeks 5-8 (6 eng), Weeks 9-12 (6 eng)
```

### Fast-Tracking (Overlapping Phases)

**Concept**: Start dependent task before prerequisite fully completes

**Example**:
- Traditional: Design complete (week 4) → Engineering starts (week 5)
- Fast-track: Engineering starts week 3 with 75% design complete → Risk of rework if design changes

**When to fast-track**:
- Timeline pressure, small slack margin
- Low risk of design changes (stable requirements)
- Acceptable rework cost (10-20% likely)

**When NOT to fast-track**:
- High design uncertainty (rework >50% likely)
- Regulatory work (cannot afford rework)
- Critical path already has adequate buffer

### Crashing (Adding Resources)

**Concept**: Shorten critical path by adding resources

**Example**: Task B (6 weeks, 1 engineer) → Add 2nd engineer → Completes in 4 weeks

**Constraints**:
- **Diminishing returns**: 9 women can't make a baby in 1 month (Brooks's Law)
- **Communication overhead**: Adding people initially slows down (ramp-up time)
- **Indivisible tasks**: Some work cannot be parallelized

**When to crash**:
- Critical path task, high priority to accelerate
- Task is parallelizable (coding yes, architecture design harder)
- Resources available (budget, hiring pipeline)
- Early in project (time to onboard)

**Cost-benefit**:
```
Crashing cost: 2nd engineer for 4 weeks = $40K
Benefit: 2 weeks earlier → Capture market window worth $200K
ROI: ($200K - $40K) / $40K = 400% → Crash
```

---

## Workflow Integration

**When to use advanced techniques**:

**CPM mathematics** → Complex roadmaps (>10 milestones), need precise critical path
**Advanced dependencies** → Multi-team coordination, conditional paths, external dependencies
**Buffer management** → High-uncertainty projects, regulatory timelines, want buffer visibility
**Multi-track roadmaps** → Cross-functional initiatives, parallel product development
**Risk-adjusted planning** → Novel work, high stakes, leadership wants confidence intervals
**Resource optimization** → Constrained resources, want to minimize hiring/layoffs

**Start simple, add complexity as needed**:
1. **Basic backcast**: Target → Milestones → Dependencies → Critical path (visual/intuitive)
2. **Moderate complexity**: Add buffers, resource constraints, risk register
3. **Advanced**: CPM calculations, Monte Carlo, CCPM, resource leveling

**Tools**:
- **Simple** (5-10 milestones): Spreadsheet, Gantt chart, whiteboard
- **Moderate** (10-30 milestones): Asana, Monday.com, Jira with dependencies
- **Complex** (30+ milestones): MS Project, Primavera, dedicated project management software with CPM/PERT

---

## Case Study: Product Launch Backcast

**Target**: SaaS product live with 1000 paying customers by Dec 31, 2024

**Milestones** (working backward):
1. **Dec 31**: 1000 customers (Target)
2. **Dec 1**: GA launch, marketing campaign, 100 customers
3. **Nov 1**: Beta complete, pricing finalized, sales ready
4. **Oct 1**: Feature complete, QA passed, beta started (50 users)
5. **Sep 1**: MVP built, alpha testing with 10 users
6. **Aug 1**: Design finalized, APIs defined, engineering staffed
7. **Jul 1**: Requirements locked, design started
8. **Jun 1** (Today): Project approved, team forming

**Dependencies**:
- Sequential: Requirements → Design → Engineering → QA → Beta → GA
- Parallel: Marketing (starts Sep 1) ∥ Sales training (starts Oct 1)

**Critical path**: Requirements → Design → Engineering → QA → Beta → GA = 30 weeks
- Requirements: 4 weeks
- Design: 4 weeks
- Engineering: 12 weeks
- QA: 4 weeks
- Beta: 4 weeks
- GA ramp: 4 weeks
- **Total**: 32 weeks

**Feasibility**:
- Available: Jun 1 to Dec 31 = 30 weeks
- Required (with 20% buffer): 32 × 1.2 = 38 weeks
- **Verdict**: Infeasible by 8 weeks

**Options**:
1. **Extend deadline**: Launch Feb 28, 2025 (+8 weeks)
2. **Reduce scope**: Cut features, launch MVP-only → Engineering 8 weeks instead of 12 → Saves 4 weeks, still need +4
3. **Accelerate**: Add 2 engineers to shorten Engineering 12→10 weeks → Costs $80K, saves 2 weeks, still need +6
4. **Combination**: Reduce scope (-4 weeks) + Accelerate (-2 weeks) + 10% risk acceptance (+2 weeks buffer removed) = 30 weeks → **Feasible**

**Decision**: Reduce scope to MVP, add 1 engineer, accept 10% risk → Launch Dec 31 with 70% confidence
