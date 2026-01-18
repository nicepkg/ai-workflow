# Postmortem Methodology

## Table of Contents
1. [Blameless Culture](#1-blameless-culture)
2. [Root Cause Analysis Techniques](#2-root-cause-analysis-techniques)
3. [Corrective Action Frameworks](#3-corrective-action-frameworks)
4. [Incident Response Patterns](#4-incident-response-patterns)
5. [Postmortem Facilitation](#5-postmortem-facilitation)
6. [Organizational Learning](#6-organizational-learning)

---

## 1. Blameless Culture

### Core Principles

**Humans Err, Systems Should Be Resilient**
- Assumption: People will make mistakes. Design systems to tolerate errors.
- Example: Deployment requires 2 approvals → reduces error likelihood
- Example: Canary deployments → limits error blast radius

**Second Victim Phenomenon**
- First victim: Customers affected by incident
- Second victim: Engineer who made triggering action (guilt, anxiety, fear)
- Blameful culture: Second victim punished → hides future issues, leaves company
- Blameless culture: Learn together → transparency, improvement

**Just Culture vs Blameless**
- **Blameless**: Focus on system improvements, not individual accountability
- **Just Culture**: Distinguish reckless behavior (punish) from honest mistakes (learn)
- Example Reckless: Intentionally bypassing safeguards, ignoring warnings
- Example Honest: Misunderstanding, reasonable decision with information at hand

### Language Patterns

**Blameful → Blameless Reframing**:
- ❌ "Engineer X caused outage" → ✓ "Deployment process allowed bad config to reach production"
- ❌ "PM didn't validate" → ✓ "Requirements validation process was missing"
- ❌ "Designer made error" → ✓ "Design review didn't catch accessibility issue"
- ❌ "Careless mistake" → ✓ "System lacked error detection at this step"

**System-Focused Questions**:
- "What allowed this to happen?" (not "Who did this?")
- "What gaps in our process enabled this?" (not "Why didn't you check?")
- "How can we prevent recurrence?" (not "How do we prevent X from doing this again?")

### Building Blameless Culture

**Leadership Modeling**:
- Leaders admit own mistakes publicly
- Leaders ask "How did our systems fail?" not "Who messed up?"
- Leaders reward transparency (sharing incidents, near-misses)

**Psychological Safety**:
- Safe to raise concerns, report issues, admit mistakes
- No punishment for honest errors (distinguish from recklessness)
- Celebrate learning, not just success

**Metrics to Track**:
- Near-miss reporting rate (high = good, means people feel safe reporting)
- Postmortem completion rate (all incidents get postmortem)
- Action item completion rate (learnings turn into improvements)
- Repeat incident rate (same root cause recurring = not learning)

---

## 2. Root Cause Analysis Techniques

### 5 Whys

**Process**:
1. State problem clearly
2. Ask "Why?" → Answer
3. Ask "Why?" on answer → Next answer
4. Repeat until root cause (fixable at system/org level)
5. Typically 5 iterations, but can be 3-7

**Example**:
Problem: Website down
1. Why? Database connection failed
2. Why? Connection pool exhausted
3. Why? Pool size too small (10 vs 100 needed)
4. Why? Config template had wrong value
5. Why? No validation in deployment pipeline

**Root Cause**: Deployment pipeline lacked config validation (fixable!)

**Tips**:
- Avoid "human error" as answer - keep asking why error possible
- Stop when you reach actionable system change
- Multiple paths may emerge - explore all

### Fishbone Diagram (Ishikawa)

**Structure**: Fish skeleton with problem at head, causes as bones

**Categories** (6M):
- **Methods** (Processes): Missing step, unclear procedure, no validation
- **Machines** (Technology): System limits, infrastructure failures, bugs
- **Materials** (Data/Inputs): Bad data, missing info, incorrect assumptions
- **Measurements** (Monitoring): Blind spots, delayed detection, wrong metrics
- **Mother Nature** (Environment): External dependencies, third-party failures, regulations
- **Manpower** (People): Training gaps, staffing, knowledge silos (careful - focus on systemic issues)

**When to Use**: Complex incidents with multiple contributing factors

**Process**:
1. Draw fish skeleton with problem at head
2. Brainstorm causes in each category
3. Vote on most likely root causes
4. Investigate top 3-5 causes
5. Confirm with evidence (logs, metrics)

### Fault Tree Analysis

**Structure**: Tree with failure at top, causes below, gates connecting

**Gates**:
- **AND Gate**: All inputs required for failure (redundancy protects)
- **OR Gate**: Any input sufficient for failure (single point of failure)

**Example**:
```
Service Down (OR gate)
├── Database Failure (AND gate)
│   ├── Primary DB down
│   └── Replica promotion failed
└── Application Crash (OR gate)
    ├── Memory leak
    ├── Uncaught exception
    └── OOM killer triggered
```

**Use**: Identify single points of failure, prioritize redundancy

### Swiss Cheese Model

**Concept**: Layers of defense (safeguards) with holes (gaps)

**Incident occurs when**: Holes align across all layers

**Example Layers**:
1. Design: Architecture with failover
2. Training: Team knows how to respond
3. Process: Peer review required
4. Technology: Automated tests
5. Monitoring: Alerts fire when issue occurs

**Analysis**: Identify which layers had holes for this incident, plug holes

### Contributing Factors Framework

**Categorize causes**:

**Immediate Cause**: Proximate trigger
- Example: Config with wrong value deployed

**Enabling Causes**: Allowed immediate cause
- Example: No config validation, no peer review

**Systemic Causes**: Organizational issues
- Example: Pressure to ship fast, understaffed team, no time for rigor

**Action**: Address all levels, not just immediate

---

## 3. Corrective Action Frameworks

### Hierarchy of Controls

**From Most to Least Effective**:

1. **Elimination**: Remove hazard entirely
   - Example: Deprecate risky feature, sunset legacy system
   - Most effective but often not feasible

2. **Substitution**: Replace with safer alternative
   - Example: Use managed service vs self-hosted database
   - Reduces risk substantially

3. **Engineering Controls**: Add safeguards
   - Example: Rate limits, circuit breakers, automated testing, canary deployments
   - Effective and feasible

4. **Administrative Controls**: Improve processes
   - Example: Runbooks, checklists, peer review, approval gates
   - Relies on compliance

5. **Training**: Educate people
   - Example: Onboarding, workshops, documentation
   - Least effective alone, use with other controls

**Apply**: Start at top of hierarchy, work down until feasible solution found

### SMART Actions

**Criteria**:
- **Specific**: "Add config validation" not "Improve deployments"
- **Measurable**: "Reduce MTTR from 2hr to 30min" not "Faster response"
- **Assignable**: Name person, not "team" or "we"
- **Realistic**: Given constraints (time, budget, skills)
- **Time-bound**: Explicit deadline

**Bad**: "Improve monitoring"
**Good**: "Add alert for connection pool >80% utilization by Mar 15 (Owner: Alex)"

### Prevention vs Detection vs Mitigation

**Prevention**: Stop incident from occurring
- Example: Config validation, automated testing, peer review
- Best ROI but can't prevent everything

**Detection**: Identify incident quickly
- Example: Monitoring, alerting, anomaly detection
- Reduces time to mitigation

**Mitigation**: Limit impact when incident occurs
- Example: Circuit breakers, graceful degradation, failover, rollback
- Reduces blast radius

**Balanced Portfolio**: Invest in all three

### Action Prioritization

**Impact vs Effort Matrix**:
- **High Impact, Low Effort**: Do immediately (Quick wins)
- **High Impact, High Effort**: Schedule as project (Strategic)
- **Low Impact, Low Effort**: Do if capacity (Fill-ins)
- **Low Impact, High Effort**: Skip (Not worth it)

**Risk-Based**: Prioritize by: Likelihood × Impact of recurrence
- Critical incident (total outage) likely to recur → Top priority
- Minor issue (UI glitch) unlikely to recur → Lower priority

---

## 4. Incident Response Patterns

### Incident Severity Levels

**Sev 1 (Critical)**:
- Total outage, data loss, security breach, >50% users affected
- Response: Immediate, all-hands, exec notification
- SLA: Acknowledge <15min, resolve <4hr

**Sev 2 (High)**:
- Partial outage, degraded performance, 10-50% users affected
- Response: On-call team, incident commander assigned
- SLA: Acknowledge <30min, resolve <24hr

**Sev 3 (Medium)**:
- Minor degradation, <10% users affected, non-critical feature down
- Response: On-call investigates, may defer to business hours
- SLA: Acknowledge <2hr, resolve <48hr

**Sev 4 (Low)**:
- Minimal impact, cosmetic issues, internal tools only
- Response: Create ticket, prioritize in backlog
- SLA: No SLA, best-effort

### Incident Command Structure (ICS)

**Roles**:
- **Incident Commander (IC)**: Coordinates response, makes decisions, external communication
- **Technical Lead**: Diagnoses issue, implements fix, coordinates engineers
- **Communication Lead**: Status updates, stakeholder briefing, customer communication
- **Scribe**: Documents timeline, decisions, actions in incident log

**Why Structure**: Prevents chaos, clear ownership, scales to large incidents

**Rotation**: IC role rotates across senior engineers (training, burnout prevention)

### Communication Patterns

**Internal Updates** (Slack, incident channel):
- Frequency: Every 15-30 min
- Format: Status, progress, next steps, blockers
- Example: "Update 14:30: Root cause identified (bad config). Initiating rollback. ETA resolution: 15:00."

**External Updates** (Status page, social media):
- Frequency: At detection, every hour, at resolution
- Tone: Transparent, apologetic, no technical jargon
- Example: "We're currently experiencing issues with login. Our team is actively working on a fix. We'll update every hour."

**Executive Updates**:
- Trigger: Sev 1/2 within 30 min
- Format: Impact, root cause (if known), ETA, what we're doing
- Frequency: Every 30-60 min until resolved

### Postmortem Timing

**When to Conduct**:
- **Immediately** (within 48 hours): Sev 1/2 incidents
- **Weekly batching**: Sev 3 incidents (batch review)
- **Monthly**: Sev 4 or pattern analysis (recurring issues)
- **Pre-mortem**: Before major launch (imagine failure, identify risks)

**Who Attends**:
- All incident responders
- Service owners
- Optional: Stakeholders, leadership (for major incidents)

---

## 5. Postmortem Facilitation

### Facilitation Tips

**Set Tone**:
- Open: "We're here to learn, not blame. Everything shared is blameless."
- Emphasize: Focus on systems and processes, not individuals
- Encourage: Transparency, even uncomfortable truths

**Structure Meeting** (60-90 min):
1. **Recap timeline** (10 min): Walk through what happened
2. **Impact review** (5 min): Quantify damage
3. **Root cause brainstorm** (20 min): Fishbone or 5 Whys as group
4. **Corrective actions** (20 min): Brainstorm actions for each root cause
5. **Prioritization** (10 min): Vote on top 5 actions
6. **Assign owners** (5 min): Who owns what, by when

**Facilitation Techniques**:
- **Round-robin**: Everyone speaks, no dominance
- **Silent brainstorm**: Write ideas on sticky notes, then share (prevents groupthink)
- **Dot voting**: Each person gets 3 votes for top priorities
- **Parking lot**: Capture off-topic items for later

**Red Flags** (intervene if you see):
- Blame language ("X caused this") → Reframe to system focus
- Defensiveness ("I had to rush because...") → Acknowledge pressure, focus on fixing system
- Rabbit holes (long technical debates) → Park for offline discussion

### Follow-Up

**Document**: Assign someone to write up postmortem (usually IC or Technical Lead)
**Share**: Distribute to team, stakeholders, company-wide (transparency)
**Present**: 10-min presentation in all-hands or team meeting (visibility)
**Track**: Add action items to project tracker, review weekly in standup
**Close**: Postmortem marked complete when all actions done

### Postmortem Review Meetings

**Monthly Postmortem Review** (Team-level):
- Review all postmortems from last month
- Identify patterns (repeated root causes)
- Assess action item completion rate
- Celebrate improvements

**Quarterly Postmortem Review** (Org-level):
- Aggregate data: Incident frequency, severity, MTTR
- Trends: Are we getting better? (MTTR decreasing? Repeat incidents decreasing?)
- Investment decisions: Where to invest in reliability

---

## 6. Organizational Learning

### Learning Metrics

**Track**:
- **Incident frequency**: Total incidents per month (decreasing over time?)
- **MTTR (Mean Time To Resolve)**: Average time from detection to resolution (improving?)
- **Repeat incidents**: Same root cause recurring (learning gap if high)
- **Action completion rate**: % of postmortem actions completed (accountability)
- **Near-miss reporting**: # of near-misses reported (psychological safety indicator)

**Goals**:
- Reduce incident frequency: -10% per quarter
- Reduce MTTR: -20% per quarter
- Reduce repeat incidents: <5% of total
- Action completion: >90%
- Near-miss reporting: Increasing (good sign)

### Knowledge Sharing

**Postmortem Database**:
- Centralized repository (Confluence, Notion, wiki)
- Searchable by: Date, service, root cause category, severity
- Template: Consistent format for easy scanning

**Learning Sessions**:
- Monthly "Failure Fridays": Review interesting postmortems
- Quarterly "Top 10 Incidents": Review worst incidents, learnings
- Blameless tone: Celebrate transparency, not success

**Cross-Team Sharing**:
- Share postmortems beyond immediate team
- Tag related teams (if payment incident, notify fintech team)
- Prevent: Team A repeats Team B's mistake

### Continuous Improvement

**Feedback Loops**:
- Postmortem → Corrective actions → Completion → Measure impact → Repeat
- Quarterly review: Are actions working? (MTTR decreasing? Repeats decreasing?)

**Runbook Updates**:
- After every incident: Update runbook with learnings
- Quarterly: Review all runbooks, refresh stale content
- Metric: Runbook age (>6 months old = needs refresh)

**Process Evolution**:
- Learn from postmortem process itself
- Survey: "Was this postmortem useful? What would improve it?"
- Iterate: Improve template, facilitation, tracking

---

## Quick Reference

### Blameless Language Patterns
- ❌ "Person caused" → ✓ "Process allowed"
- ❌ "Didn't check" → ✓ "Validation missing"
- ❌ "Mistake" → ✓ "Gap in system"

### Root Cause Techniques
- **5 Whys**: Simple incidents, single cause
- **Fishbone**: Complex incidents, multiple causes
- **Fault Tree**: Identify single points of failure
- **Swiss Cheese**: Multiple safeguard failures

### Corrective Action Hierarchy
1. Eliminate (remove hazard)
2. Substitute (safer alternative)
3. Engineering controls (safeguards)
4. Administrative (processes)
5. Training (education)

### Incident Response
- **Sev 1**: Total outage, <15min ack, <4hr resolve
- **Sev 2**: Partial, <30min ack, <24hr resolve
- **Sev 3**: Minor, <2hr ack, <48hr resolve

### Success Metrics
- ✓ Incident frequency decreasing
- ✓ MTTR improving
- ✓ Repeat incidents <5%
- ✓ Action completion >90%
- ✓ Near-miss reporting increasing
