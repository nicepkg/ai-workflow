---
name: postmortem
description: Use when analyzing failures, outages, incidents, or negative outcomes, conducting blameless postmortems, documenting root causes with 5 Whys or fishbone diagrams, identifying corrective actions with owners and timelines, learning from near-misses, establishing prevention strategies, or when user mentions postmortem, incident review, failure analysis, RCA, lessons learned, or after-action review.
---
# Postmortem

## Table of Contents
1. [Purpose](#purpose)
2. [When to Use](#when-to-use)
3. [What Is It?](#what-is-it)
4. [Workflow](#workflow)
5. [Common Patterns](#common-patterns)
6. [Guardrails](#guardrails)
7. [Quick Reference](#quick-reference)

## Purpose

Conduct blameless postmortems that transform failures into learning opportunities by documenting what happened, why it happened, impact quantification, root cause analysis, and actionable preventions with clear ownership.

## When to Use

**Use this skill when:**

### Incident Context
- Production outage, system failure, or service degradation occurred
- Security breach, data loss, or compliance violation happened
- Product launch failed, project missed deadline, or initiative underperformed
- Customer-impacting bug, quality issue, or support crisis arose
- Near-miss incident that could have caused serious harm (proactive postmortem)

### Learning Goals
- Need to understand root cause (not just symptoms) to prevent recurrence
- Want to identify systemic issues vs. individual mistakes
- Must document timeline and impact for stakeholders or auditors
- Aim to improve processes, systems, or practices based on failure insights
- Building organizational learning culture (celebrate transparency, not blame)

### Timing
- **Immediately after** incident resolution (while memory fresh, within 48 hours)
- **Scheduled reviews** for recurring issues or chronic problems
- **Quarterly reviews** of all incidents to identify patterns
- **Pre-mortem** style: Before major launch, imagine it failed and write postmortem

**Do NOT use when:**
- Incident still ongoing (focus on resolution first, postmortem second)
- Looking to assign blame or punish individuals (antithesis of blameless culture)
- Issue is trivial with no learning value (reserved for significant incidents)

## What Is It?

**Postmortem** is a structured, blameless analysis of failures that answers:
- **What happened?** Timeline of events from detection to resolution
- **What was the impact?** Quantified harm (users affected, revenue lost, duration)
- **Why did it happen?** Root cause analysis using 5 Whys, fishbone, or fault trees
- **How do we prevent recurrence?** Actionable items with owners and deadlines
- **What went well?** Positive aspects of incident response

**Key Principles**:
- **Blameless**: Focus on systems/processes, not individuals. Humans err; systems should be resilient.
- **Actionable**: Corrective actions must be specific, owned, and tracked
- **Transparent**: Share widely to enable organizational learning
- **Timely**: Conduct while memory fresh (within 48 hours of resolution)

**Quick Example:**

**Incident**: Database outage, 2-hour downtime, 50K users affected

**Timeline**:
- 14:05 - Automated deployment started (config change)
- 14:07 - Database connection pool exhausted, errors spike
- 14:10 - Alerts fired, on-call paged
- 14:15 - Engineer investigates, identifies bad config
- 15:30 - Rollback initiated (delayed by unclear runbook)
- 16:05 - Service restored

**Impact**: 2-hour outage, 50K users unable to access, estimated $20K revenue loss

**Root Cause** (5 Whys):
1. Why outage? Bad config deployed
2. Why bad config? Connection pool size set to 10 (should be 100)
3. Why wrong value? Config templated incorrectly
4. Why template wrong? New team member unfamiliar with prod values
5. Why no catch? No staging environment testing of configs

**Corrective Actions**:
- [ ] Add config validation to deployment pipeline (Owner: Alex, Due: Mar 15)
- [ ] Create staging env with prod-like load (Owner: Jordan, Due: Mar 30)
- [ ] Update runbook with rollback steps (Owner: Sam, Due: Mar 10)
- [ ] Onboarding checklist: Review prod configs (Owner: Morgan, Due: Mar 5)

**What Went Well**: Alerts fired quickly, team responded within 5 minutes, good communication

## Workflow

Copy this checklist and track your progress:

```
Postmortem Progress:
- [ ] Step 1: Assemble timeline and quantify impact
- [ ] Step 2: Conduct root cause analysis
- [ ] Step 3: Define corrective and preventive actions
- [ ] Step 4: Document and share postmortem
- [ ] Step 5: Track action items to completion
```

**Step 1: Assemble timeline and quantify impact**

Gather facts: when detected, when started, key events, when resolved. Quantify impact: users affected, duration, revenue/SLA impact, customer complaints. For straightforward incidents use [resources/template.md](resources/template.md). For complex incidents with multiple causes or cascading failures, study [resources/methodology.md](resources/methodology.md) for advanced timeline reconstruction techniques.

**Step 2: Conduct root cause analysis**

Ask "Why?" 5 times to get from symptom to root cause, or use fishbone diagram for complex incidents with multiple contributing factors. See [Root Cause Analysis Techniques](#root-cause-analysis-techniques) for guidance. Focus on system failures (process gaps, missing safeguards) not human errors.

**Step 3: Define corrective and preventive actions**

For each root cause, identify actions to prevent recurrence. Must be specific (not "improve testing"), owned (named person), and time-bound (deadline). Categorize as immediate fixes vs. long-term improvements. See [Corrective Actions](#corrective-actions-framework) for framework.

**Step 4: Document and share postmortem**

Create postmortem document using template. Include timeline, impact, root cause, actions, what went well. Share widely (engineering, product, leadership) to enable learning. Present in team meeting for discussion. Archive in knowledge base.

**Step 5: Track action items to completion**

Assign owners, set deadlines, add to project tracker. Review progress in standups or weekly meetings. Close postmortem only when all actions complete. Self-assess quality using [resources/evaluators/rubric_postmortem.json](resources/evaluators/rubric_postmortem.json). Minimum standard: ≥3.5 average score.

## Common Patterns

### By Incident Type

**Production Outages** (system failures, downtime):
- Timeline: Detection → Investigation → Mitigation → Resolution
- Impact: Users affected, duration, SLA breach, revenue loss
- Root cause: Often config errors, deployment issues, infrastructure limits
- Actions: Improve monitoring, runbooks, rollback procedures, capacity planning

**Security Incidents** (breaches, vulnerabilities):
- Timeline: Breach occurrence → Detection (often delayed) → Containment → Remediation
- Impact: Data exposed, compliance risk, reputation damage
- Root cause: Missing security controls, access management gaps, unpatched vulnerabilities
- Actions: Security audits, access reviews, patch management, training

**Product/Project Failures** (launches, deadlines):
- Timeline: Planning → Execution → Launch/Deadline → Outcome vs. Expectations
- Impact: Revenue miss, user churn, wasted effort, opportunity cost
- Root cause: Poor requirements, unrealistic estimates, misalignment, inadequate testing
- Actions: Improve discovery, estimation, stakeholder alignment, validation processes

**Process Failures** (operational, procedural):
- Timeline: Process initiation → Breakdown point → Impact realization
- Impact: Delays, quality issues, rework, team frustration
- Root cause: Unclear process, missing steps, handoff failures, tooling gaps
- Actions: Document processes, automate workflows, improve communication, training

### By Root Cause Category

**Human Error** (surface cause, dig deeper):
- Don't stop at "person made mistake"
- Ask: Why was mistake possible? Why not caught? Why no safeguard?
- Actions: Reduce error likelihood (checklists, automation), increase error detection (testing, reviews), mitigate error impact (rollback, redundancy)

**Process Gap** (missing or unclear procedures):
- Symptoms: "Didn't know to do X", "Not in runbook", "First time"
- Actions: Document process, create checklist, formalize approval gates, onboarding

**Technical Debt** (deferred maintenance):
- Symptoms: "Known issue", "Fragile system", "Workaround failed"
- Actions: Prioritize tech debt, allocate 20% capacity, refactor, replace legacy systems

**External Dependencies** (third-party failures):
- Symptoms: "Vendor down", "API failed", "Partner issue"
- Actions: Add redundancy, circuit breakers, graceful degradation, SLA monitoring, vendor diversification

**Systemic Issues** (organizational, cultural):
- Symptoms: "Always rushed", "No time to test", "Pressure to ship"
- Actions: Address root organizational issues (unrealistic deadlines, resource constraints, incentive misalignment)

## Root Cause Analysis Techniques

**5 Whys**:
1. Start with problem statement
2. Ask "Why did this happen?" → Answer
3. Ask "Why did that happen?" → Answer
4. Repeat 5 times (or until root cause found)
5. Root cause: Fixable at organizational/system level

**Example**: Database outage → Why? Bad config → Why? Wrong value → Why? Template error → Why? New team member unfamiliar → Why? No config review in onboarding

**Fishbone Diagram** (Ishikawa):
- Categories: People, Process, Technology, Environment
- Brainstorm causes in each category
- Identify most likely root causes for investigation
- Useful for complex incidents with multiple contributing factors

**Fault Tree Analysis**:
- Top: Failure event (e.g., "System down")
- Gates: AND (all required) vs OR (any sufficient)
- Leaves: Base causes (e.g., "Config error" OR "Network failure")
- Trace path from failure to root causes

## Corrective Actions Framework

**Types of Actions**:
- **Immediate Fixes**: Deployed within days (hotfix, manual process, workaround)
- **Short-term Improvements**: Completed within weeks (better monitoring, updated runbook, process change)
- **Long-term Investments**: Completed within months (architecture changes, new systems, cultural shifts)

**SMART Actions**:
- **Specific**: "Add config validation" not "Improve deploys"
- **Measurable**: "Reduce MTTR from 2hr to 30min" not "Faster response"
- **Assignable**: Named owner, not "team"
- **Realistic**: Given capacity and constraints
- **Time-bound**: Explicit deadline

**Prioritization**:
1. **High impact, low effort**: Do immediately
2. **High impact, high effort**: Schedule as strategic project
3. **Low impact, low effort**: Do if spare capacity
4. **Low impact, high effort**: Consider skipping (cost > benefit)

**Prevention Hierarchy** (from most to least effective):
1. **Eliminate**: Remove hazard entirely (e.g., deprecate risky feature)
2. **Substitute**: Replace with safer alternative (e.g., use managed service vs self-host)
3. **Engineering controls**: Add safeguards (e.g., rate limits, circuit breakers, automated testing)
4. **Administrative controls**: Improve processes (e.g., runbooks, checklists, reviews)
5. **Training**: Educate people (least effective alone, combine with others)

## Guardrails

**Blameless Culture**:
- ❌ "Engineer caused outage by deploying bad config" → ✓ "Deployment pipeline allowed bad config to reach production"
- ❌ "PM didn't validate requirements" → ✓ "Requirements validation process missing"
- ❌ "Designer made mistake" → ✓ "Design review process didn't catch issue"
- Focus: What system/process failed? Not who made error.

**Root Cause Depth**:
- ❌ Stopping at surface: "Bug caused outage" → ✓ Deep analysis: "Bug deployed because testing gap, no staging env, rushed release pressure"
- ❌ Single cause: "Database failure" → ✓ Multiple causes: "Database + no failover + alerting delay + unclear runbook"
- Rule: Keep asking "Why?" until you reach actionable systemic improvements

**Actionability**:
- ❌ Vague: "Improve testing", "Better communication", "More careful" → ✓ Specific: "Add E2E test suite covering top 10 user flows by Apr 1 (Owner: Alex)"
- ❌ No owner: "Team should document" → ✓ Owned: "Sam documents incident response runbook by Mar 15"
- ❌ No deadline: "Eventually migrate" → ✓ Time-bound: "Complete migration by Q2 end"

**Impact Quantification**:
- ❌ Qualitative: "Many users affected", "Significant downtime" → ✓ Quantitative: "50K users (20% of base), 2-hour outage, $20K revenue loss"
- ❌ No metrics: "Bad customer experience" → ✓ Metrics: "NPS dropped from 50 to 30, 100 support tickets, 5 churned customers ($50K ARR)"

**Timeliness**:
- ❌ Wait 2 weeks → Memory fades, urgency lost → ✓ Conduct within 48 hours while fresh
- ❌ Never follow up → Actions forgotten → ✓ Track actions, review weekly, close when complete

## Quick Reference

**Resources**:
- [resources/template.md](resources/template.md) - Postmortem document structure and sections
- [resources/methodology.md](resources/methodology.md) - Blameless culture, root cause analysis techniques, corrective action frameworks
- [resources/evaluators/rubric_postmortem.json](resources/evaluators/rubric_postmortem.json) - Quality criteria for postmortems

**Success Criteria**:
- ✓ Timeline clear with timestamps and key events
- ✓ Impact quantified (users, duration, revenue, metrics)
- ✓ Root cause identified (systemic, not individual blame)
- ✓ Corrective actions SMART (specific, measurable, assigned, realistic, time-bound)
- ✓ Blameless tone (focus on systems/processes)
- ✓ Documented and shared within 48 hours
- ✓ Action items tracked to completion

**Common Mistakes**:
- ❌ Blame individuals → culture of fear, hide future issues
- ❌ Superficial root cause → doesn't prevent recurrence
- ❌ Vague actions → nothing actually improves
- ❌ No follow-through → actions never completed, same incident repeats
- ❌ Delayed postmortem → details forgotten, less useful
- ❌ Not sharing → no organizational learning
- ❌ Defensive tone → misses opportunity to improve
