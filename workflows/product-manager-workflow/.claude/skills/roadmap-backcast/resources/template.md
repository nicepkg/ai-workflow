# Roadmap Backcast Template

## Workflow

Copy this checklist and track your progress:

```
Roadmap Backcast Progress:
- [ ] Step 1: Define target outcome
- [ ] Step 2: Work backward to milestones
- [ ] Step 3: Map dependencies
- [ ] Step 4: Identify critical path
- [ ] Step 5: Assess feasibility
```

**Step 1: Define target outcome**

State specific outcome, date, success criteria. See [Target Definition](#target-definition).

**Step 2: Work backward to milestones**

Ask "what must be true just before?" iteratively. See [Milestone Backcasting](#milestone-backcasting-process).

**Step 3: Map dependencies**

Identify sequential vs parallel work. See [Dependency Mapping](#dependency-mapping).

**Step 4: Identify critical path**

Find longest dependent chain. See [Critical Path](#critical-path-identification).

**Step 5: Assess feasibility**

Check time available, add buffers, identify risks. See [Feasibility Assessment](#feasibility-assessment).

---

## Roadmap Backcast Template

### Target Definition

**Target Outcome**: [Specific, measurable end state]

**Target Date**: [Fixed deadline - DD/MM/YYYY]

**Success Criteria**:
- [Criterion 1]: [Quantifiable measure of success]
- [Criterion 2]: [...]
- [Criterion 3]: [...]

**Why this matters**: [Business impact, strategic importance, consequences if missed]

**Constraints**:
- **Budget**: [Available resources]
- **Team**: [Available capacity, FTEs]
- **Dependencies**: [External constraints, vendor timelines, regulatory deadlines]
- **Scope**: [Must-haves vs nice-to-haves]

---

### Milestone Backcasting Process

**Working backward from target date:**

#### Milestone 0: Target Outcome (T+0)
**Date**: [Target date]
**Deliverable**: [Final outcome achieved]
**Owner**: [Name/Role]
**Dependencies**: [What must be complete for this to happen]

#### Milestone 1: [Name] (T-[X weeks/months])
**Date**: [Date]
**Deliverable**: [Specific output, not activity]
**Owner**: [Name/Role]
**Duration**: [X weeks/months]
**Dependencies**: [Requires milestone 2, 3 complete]
**What must be true before**: [State of world needed to start this milestone]

#### Milestone 2: [Name] (T-[X weeks/months])
**Date**: [Date]
**Deliverable**: [...]
**Owner**: [...]
**Duration**: [...]
**Dependencies**: [...]
**What must be true before**: [...]

#### Milestone 3: [Name] (T-[X weeks/months])
**Date**: [Date]
**Deliverable**: [...]
**Owner**: [...]
**Duration**: [...]
**Dependencies**: [...]
**What must be true before**: [...]

#### Milestone N: Starting Point (Today)
**Date**: [Today's date]
**Deliverable**: [Current state, what we have now]
**Owner**: [...]
**What we need to begin**: [Resources, approvals, information to start milestone N-1]

---

### Dependency Mapping

**Dependency Graph**:

```
[Milestone A] ──→ [Milestone B] ──→ [Milestone D] ──→ [Target]
                                      ↑
[Milestone C] ────────────────────────┘
```

**Dependency Table**:

| Milestone | Depends On (Prerequisites) | Enables (Downstream) | Type | Can Parallelize? |
|-----------|---------------------------|----------------------|------|------------------|
| [Milestone A] | None (start) | [B] | Sequential | No (on critical path) |
| [Milestone B] | [A] | [D] | Sequential | No (on critical path) |
| [Milestone C] | [A] | [D] | Parallel with B | Yes (non-critical) |
| [Milestone D] | [B, C] | [Target] | Converging | No (on critical path) |

**Parallel workstreams** (can happen simultaneously):
- [Milestone X] ∥ [Milestone Y]: [Why these can be parallel]
- [Milestone Z] ∥ [Milestone W]: [...]

**Converging points** (multiple prerequisites):
- [Milestone M] requires both [A] AND [B]: [Coordination needed]

**Diverging points** (one enables multiple):
- [Milestone N] enables [X], [Y], [Z]: [Handoff process]

---

### Critical Path Identification

**Critical path** (longest dependent chain):

```
[Start] → [Milestone A: 4 weeks] → [Milestone B: 6 weeks] → [Milestone D: 2 weeks] → [Target]
Total: 12 weeks
```

**Alternative paths** (non-critical, have slack):

```
[Start] → [Milestone A: 4 weeks] → [Milestone C: 3 weeks] → [Milestone D: 2 weeks] → [Target]
Total: 9 weeks (3 weeks slack)
```

**Critical path milestones** (zero slack, delays directly impact target):
- [Milestone A]: [Why on critical path, impact if delayed]
- [Milestone B]: [Why on critical path, impact if delayed]
- [Milestone D]: [Why on critical path, impact if delayed]

**Non-critical milestones** (have slack, can absorb delays):
- [Milestone C]: [X weeks slack, latest finish date without impacting target]

**Critical path management**:
- **Monitor**: [How will we track critical path progress? Weekly reviews, dashboards]
- **Accelerate**: [Can we add resources to shorten critical path? Cost/benefit]
- **Buffer**: [20-30% buffer on critical path tasks built in? Where?]

---

### Feasibility Assessment

**Time Analysis**:

| Component | Estimate (weeks) | Buffer (%) | Buffered (weeks) |
|-----------|------------------|------------|------------------|
| [Milestone A] | [4] | [20%] | [4.8] |
| [Milestone B] | [6] | [30%] | [7.8] |
| [Milestone D] | [2] | [20%] | [2.4] |
| **Total (critical path)** | **12** | - | **15** |

**Available time**: [Target date - Today = X weeks]

**Required time** (with buffer): [15 weeks]

**Feasibility verdict**:
- ✓ **Feasible** if Available ≥ Required (with X weeks margin)
- ⚠ **Tight** if Available ≈ Required (±10%)
- ✗ **Infeasible** if Available < Required

**If infeasible, options**:
1. **Extend deadline**: Move target date to [new date] (need X additional weeks)
2. **Reduce scope**: Cut [feature Y], defer [feature Z] to post-launch
3. **Add resources**: Hire [N contractors/FTEs], cost $[X], reduces timeline by [Y weeks]
4. **Accept risk**: Proceed with [X%] probability of missing deadline

---

### Risk Register

**Risks to timeline**:

| Risk | Probability (H/M/L) | Impact (H/M/L) | Mitigation | Contingency |
|------|---------------------|----------------|------------|-------------|
| [Vendor delay on component X] | H | H | Contract penalties, alternate vendor identified | Built 4-week buffer in milestone B |
| [Key engineer leaves] | M | H | Cross-train team, document tribal knowledge | Contractor bench available |
| [Scope creep from stakeholder Y] | H | M | Requirements freeze by milestone 2, change control process | Reserve 2 weeks flex time |
| [Technical unknowns in integration] | M | H | Technical spike in milestone 3, architecture review | Parallel path with simpler approach |

**Triggers for re-planning**:
- Critical path milestone delayed >1 week → Escalate, re-assess feasibility
- Scope change >20% → Re-run backcast, adjust target or timeline
- Resource loss >25% → Revisit parallelization, extend timeline

---

### Resource Allocation

**Team capacity**:

| Role | Available FTEs | Required FTEs (peak) | Gap | Mitigation |
|------|----------------|----------------------|-----|------------|
| [Engineering] | [5] | [7] | [-2] | [Hire 2 contractors by milestone 2] |
| [Design] | [2] | [2] | [0] | [Sufficient] |
| [QA] | [1] | [3] | [-2] | [Outsource testing for milestone 4] |

**Budget**:
- **Total required**: $[X]
- **Allocated**: $[Y]
- **Gap**: $[X-Y] → [Source: reallocation, additional funding, scope reduction]

---

### Communication Plan

**Stakeholder alignment**:
- **Weekly updates**: [To whom, what format, starting when]
- **Milestone reviews**: [After each milestone, with stakeholders X, Y, Z]
- **Go/No-Go gates**: [At milestones A, C before committing to next phase]

**Escalation path**:
- **Level 1** (delays <1 week): Team lead resolves
- **Level 2** (delays 1-2 weeks): Product manager adjusts plan
- **Level 3** (delays >2 weeks or feasibility threat): Executive decision on scope/date

---

## Guidance for Each Section

### Target Definition

**Good target outcomes** (specific, measurable):
- ✓ "1000 paying customers using product by Jan 31, 2025"
- ✓ "SOC 2 Type II certification achieved by regulatory deadline Sept 1, 2025"
- ✓ "Conference with 500 attendees, NPS >40, on Oct 15, 2024"

**Bad target outcomes** (vague, unmeasurable):
- ❌ "Launch product soon"
- ❌ "Improve compliance"
- ❌ "Hold successful event"

### Milestone Backcasting

**Ask iteratively**: "What must be true just before [current milestone]?"

**Example (Product Launch)**:
- **Target**: 1000 customers using product
- **T-2 weeks**: Product in production, scaling, monitoring working
- **T-6 weeks**: Beta complete, critical bugs fixed, ready for GA
- **T-10 weeks**: MVP feature complete, QA passed
- **T-14 weeks**: Design finalized, APIs defined
- **T-18 weeks**: Requirements locked, team staffed
- **Today** (T-20 weeks): Feasible if starting now

**Milestone quality**:
- **Clear deliverable**: "Design finalized" not "working on design"
- **Verifiable**: Can objectively check if done
- **Owned**: Named person responsible
- **Estimated**: Duration in days/weeks/months

### Dependency Mapping

**Identify dependencies by asking**:
- "Can this start before [X] completes?" (sequential vs parallel)
- "What does this milestone need to begin?" (prerequisites)
- "What can't start until this finishes?" (downstream dependencies)

**Common patterns**:
- **Waterfall phases** (design → build → test): Sequential, little parallelization
- **Workstreams** (frontend ∥ backend ∥ infrastructure): Parallel, converge for integration
- **Approvals/Reviews**: Often converging (need multiple sign-offs)

### Critical Path Identification

**Shortcuts for small roadmaps** (<10 milestones):
1. Draw dependency graph
2. Visually trace longest path
3. Sum durations on that path

**For complex roadmaps** (>10 milestones):
- Use project management tools (MS Project, Asana, Jira with dependencies)
- Critical path method (CPM) calculation (forward/backward pass)

**Interpreting critical path**:
- Critical path length = minimum project duration
- Slack on non-critical tasks = flexibility
- Delays on critical path directly delay target

### Feasibility Assessment

**Buffer guidance by uncertainty**:
- **Low uncertainty** (done similar work before): 10-20% buffer
- **Medium uncertainty** (some unknowns, dependencies): 20-30% buffer
- **High uncertainty** (novel work, many risks): 30-50% buffer
- **Regulatory/Compliance**: 40%+ buffer (risk intolerant)

**Feasibility decision tree**:
```
Available time ≥ Required time (with buffer)?
├─ Yes → Proceed, monitor critical path closely
├─ Within 10% → Proceed with risk acknowledgment, escalation plan
└─ No → Re-plan (extend date, reduce scope, or add resources)
```

---

## Common Patterns by Context

**Product Launch**:
- Critical path: Design → Engineering → Testing (usually 60-70% of timeline)
- Buffer: 20-30% on engineering, 20% on testing
- Risks: Scope creep, technical unknowns, vendor delays

**Compliance/Regulatory**:
- Critical path: Gap analysis → Remediation → Audit
- Buffer: 40%+ (cannot miss regulatory deadline)
- Risks: Audit findings require rework, controls take longer than expected

**Event Planning**:
- Critical path: Venue booking (long lead time), content creation, speaker coordination
- Buffer: 10-20% (hard deadline, less flexible)
- Risks: Speaker cancellations, venue issues, low registration

**Strategic Transformation**:
- Critical path: Foundation work (pilot, learnings) before scaling
- Buffer: 30%+ per phase (unknowns compound)
- Risks: Organizational resistance, scope expansion, funding cuts

---

## Quality Checklist

- [ ] Target outcome is specific and measurable
- [ ] Target date is fixed (not flexible)
- [ ] Success criteria are quantifiable
- [ ] 5-10 major milestones identified working backward
- [ ] Each milestone has clear deliverable (not activity)
- [ ] Each milestone has owner assigned
- [ ] Dependencies explicitly mapped (prerequisites identified)
- [ ] Parallel workstreams identified where possible
- [ ] Critical path identified (longest dependent chain)
- [ ] Duration estimates include 20-30% buffer
- [ ] Feasibility assessed: required time ≤ available time
- [ ] Risks to timeline documented with mitigations
- [ ] Resource constraints identified (team, budget)
- [ ] Communication plan for stakeholder updates
- [ ] Escalation path defined for delays
- [ ] If infeasible, options provided (extend date, reduce scope, add resources)
