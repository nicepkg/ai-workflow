# Postmortem Template

## Table of Contents
1. [Workflow](#workflow)
2. [Postmortem Document Template](#postmortem-document-template)
3. [Guidance for Each Section](#guidance-for-each-section)
4. [Quick Patterns](#quick-patterns)
5. [Quality Checklist](#quality-checklist)

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

Fill out [Incident Summary](#incident-summary) and [Timeline](#timeline) sections. Quantify impact in [Impact](#impact) section. Gather logs, metrics, alerts, and witness accounts.

**Step 2: Conduct root cause analysis**

Use 5 Whys or fishbone diagram to identify root causes. Fill out [Root Cause Analysis](#root-cause-analysis) section. See [Guidance: Root Cause](#root-cause) for techniques.

**Step 3: Define corrective and preventive actions**

For each root cause, identify actions. Fill out [Corrective Actions](#corrective-actions) section with SMART actions (specific, measurable, assigned, realistic, time-bound).

**Step 4: Document and share postmortem**

Complete [What Went Well](#what-went-well) and [Lessons Learned](#lessons-learned) sections. Share with team, stakeholders, and broader organization. Present in meeting for discussion.

**Step 5: Track action items to completion**

Add actions to project tracker. Assign owners, set deadlines. Review progress weekly. Close postmortem when all actions complete. Use [Quality Checklist](#quality-checklist) to validate.

---

## Postmortem Document Template

### Incident Summary

**Incident ID**: [Unique identifier, e.g., INC-2024-001]
**Date**: [When incident occurred, e.g., 2024-03-05]
**Duration**: [How long, e.g., 2 hours 15 minutes]
**Severity**: [Critical / High / Medium / Low]
**Status**: [Resolved / Investigating / Monitoring]

**Summary**: [1-2 sentence description of what happened]

**Impact Summary**:
- **Users Affected**: [Number or percentage]
- **Duration**: [Downtime or degradation period]
- **Revenue Impact**: [Estimated $ loss, if applicable]
- **SLA Impact**: [SLA breach? Refunds owed?]
- **Reputation Impact**: [Customer complaints, social media, press]

**Owner**: [Postmortem author]
**Contributors**: [Who participated in postmortem]
**Date Written**: [When postmortem was created]

---

### Timeline

**Detection to Resolution**: [14:05 - 16:05 UTC (2 hours)]

| Time (UTC) | Event | Source | Action Taken |
|------------|-------|--------|--------------|
| 14:00 | [Normal operation] | - | - |
| 14:05 | [Deployment started] | CI/CD | [Config change deployed] |
| 14:07 | [Error spike detected] | Monitoring | [Errors jumped from 0 to 500/min] |
| 14:10 | [Alert fired] | PagerDuty | [On-call engineer paged] |
| 14:15 | [Engineer joins incident] | Slack | [Investigation begins] |
| 14:20 | [Root cause identified] | Logs | [Bad config found] |
| 14:25 | [Mitigation attempt #1] | Manual | [Tried config hotfix - failed] |
| 14:45 | [Mitigation attempt #2] | Manual | [Scaled up instances - no effect] |
| 15:30 | [Rollback decision] | Incident Commander | [Decided to rollback deployment] |
| 15:45 | [Rollback executed] | CI/CD | [Rolled back to previous version] |
| 16:05 | [Service restored] | Monitoring | [Errors returned to 0, traffic normal] |
| 16:30 | [All-clear declared] | Incident Commander | [Incident closed] |

**Key Observations**:
- Detection lag: [X minutes between occurrence and detection]
- Response time: [X minutes from alert to engineer joining]
- Diagnosis time: [X minutes to identify root cause]
- Mitigation time: [X minutes from mitigation start to resolution]
- Total incident duration: [X hours Y minutes]

---

### Impact

**User Impact**: [50K users (20%), complete unavailability, global]
**Business**: [$20K revenue loss, SLA breach (99.9% → 2hr down), $15K credits]
**Operational**: [150 support tickets, 10 person-hours incident response]
**Reputation**: [50 negative tweets, 3 Enterprise escalations]

| Metric | Baseline | During | Post |
|--------|----------|--------|------|
| Uptime | 99.99% | 0% | 99.99% |
| Errors | <0.1% | 100% | <0.1% |
| Users | 250K | 0 | 240K |

---

### Root Cause Analysis

#### 5 Whys

**Problem Statement**: Database connection pool exhausted, causing 2-hour service outage affecting 50K users.

1. **Why did the service go down?**
   - Database connection pool exhausted (all connections in use, new requests rejected)

2. **Why did the connection pool exhaust?**
   - Connection pool size was set to 10, but traffic required 100+ connections

3. **Why was the pool size set to 10?**
   - Configuration template had wrong value (10 instead of 100)

4. **Why did the template have the wrong value?**
   - New team member created template without referencing production values

5. **Why didn't anyone catch this before deployment?**
   - No staging environment with production-like load to test configs
   - No automated config validation in deployment pipeline
   - No peer review required for configuration changes

**Root Causes Identified**:
1. **Primary**: Missing config validation in deployment pipeline
2. **Contributing**: No staging environment with prod-like load
3. **Contributing**: Unclear onboarding process for infrastructure changes
4. **Contributing**: No peer review requirement for config changes

#### Contributing Factors

**Technical**:
- Deployment pipeline lacks config validation
- No staging environment matching production scale
- Monitoring detected symptom (errors) but not root cause (pool exhaustion)

**Process**:
- Onboarding doesn't cover production config management
- No peer review process for infrastructure changes
- Runbook for rollback was outdated, delayed recovery by 45 minutes

**Organizational**:
- Pressure to deploy quickly (feature deadline) led to skipping validation steps
- Team understaffed (3 people covering on-call for 50-person engineering org)

---

### Corrective Actions

**Immediate Fixes** (Completed or in-flight):
- [x] Rollback to previous config (Completed 16:05 UTC)
- [x] Manually set connection pool to 100 on all instances (Completed 16:30 UTC)
- [ ] Update deployment runbook with rollback steps (Owner: Sam, Due: Mar 8)

**Short-Term Improvements** (Next 2-4 weeks):
- [ ] Add config validation to deployment pipeline (Owner: Alex, Due: Mar 15)
  - Validate connection pool size is between 50-500
  - Validate all required config keys present
  - Fail deployment if validation fails
- [ ] Create staging environment with production-like load (Owner: Jordan, Due: Mar 30)
  - 10% of prod traffic
  - Same config as prod
  - Automated smoke tests after each deployment
- [ ] Require peer review for all infrastructure changes (Owner: Morgan, Due: Mar 10)
  - Update GitHub settings to require 1 approval
  - Add CODEOWNERS for infra configs
- [ ] Improve monitoring to detect pool exhaustion (Owner: Casey, Due: Mar 20)
  - Alert when pool utilization >80%
  - Dashboard showing pool metrics

**Long-Term Investments** (Next 1-3 months):
- [ ] Implement canary deployments (Owner: Alex, Due: May 1)
  - Deploy to 5% of traffic first
  - Auto-rollback if error rate >0.5%
- [ ] Expand on-call rotation (Owner: Morgan, Due: Apr 15)
  - Hire 2 more SREs
  - Train 3 backend engineers for on-call
  - Reduce on-call burden from 1:3 to 1:8
- [ ] Onboarding program for infrastructure changes (Owner: Jordan, Due: Apr 30)
  - Checklist for new team members
  - Buddy system for first 3 infra changes
  - Production access granted after completion

**Tracking**:
- Actions added to JIRA project: INCIDENT-2024-001
- Reviewed in weekly engineering standup
- Postmortem closed when all actions complete (target: May 1)

---

### What Went Well

**Detection & Alerting**:
- ✓ Monitoring detected error spike within 3 minutes of occurrence
- ✓ PagerDuty alert fired correctly, paged on-call within 5 minutes
- ✓ Escalation path worked (on-call → senior eng → incident commander)

**Incident Response**:
- ✓ Team assembled quickly (5 engineers joined within 10 minutes)
- ✓ Clear incident commander (Morgan) coordinated response
- ✓ Regular status updates posted to #incidents Slack channel every 15 min
- ✓ Stakeholder communication: Execs notified within 20 min, status page updated

**Communication**:
- ✓ Blameless tone maintained throughout (no finger-pointing)
- ✓ External communication transparent (status page, Twitter updates)
- ✓ Customer support briefed on issue and talking points provided

**Technical**:
- ✓ Rollback process worked once initiated (though delayed by unclear runbook)
- ✓ No data loss or corruption during incident
- ✓ Automated alerts prevented longer outage (if manual detection, could be hours)

---

### Lessons Learned

**What We Learned**:
1. **Staging environments matter**: Could have caught this with prod-like staging
2. **Config is code**: Needs same rigor as code (validation, review, testing)
3. **Runbooks rot**: Outdated runbook delayed recovery by 45 min - need to keep fresh
4. **Pressure kills quality**: Rushing to hit deadline led to skipping validation
5. **Monitoring gaps**: Detected symptom (errors) but not cause (pool exhaustion) - need better metrics

**Knowledge Gaps Identified**:
- New team members don't know production config patterns
- Not everyone knows how to rollback deployments
- Connection pool sizing not well understood across team

**Process Improvements Needed**:
- Peer review for all infrastructure changes (not just code)
- Automated config validation before deployment
- Regular runbook review/update (quarterly)
- Staging environment for all changes

**Cultural Observations**:
- Team responded well under pressure (good collaboration, clear roles)
- Blameless culture held up (no one blamed new team member)
- But: Pressure to ship fast is real and leads to shortcuts

---

### Appendix

**Related Incidents**:
- [INC-2024-002]: Similar config error 2 weeks later (different service)
- [INC-2023-045]: Previous database connection issue (6 months ago)

**References**:
- Logs: [Link to log aggregator query]
- Metrics: [Link to Grafana dashboard]
- Incident Slack thread: [#incidents, Mar 5 14:10-16:30]
- Status page: [Link to status.company.com incident #123]
- Customer impact: [Link to support ticket analysis]

**Contacts**:
- Incident Commander: Morgan (morgan@company.com)
- Postmortem Author: Alex (alex@company.com)
- Escalation: VP Engineering (vpe@company.com)

---

## Guidance for Each Section

### Incident Summary
- **Severity Levels**:
  - Critical: Total outage, data loss, security breach
  - High: Partial outage, significant degradation, many users affected
  - Medium: Minor degradation, limited users affected
  - Low: Minimal impact, caught before customer impact
- **Summary**: 1-2 sentences max. Example: "Database connection pool exhaustion caused 2-hour outage affecting 50K users due to incorrect config deployment."

### Timeline
- **Timestamps**: Use UTC or clearly state timezone. Be specific (14:05, not "afternoon").
- **Key Events**: Detection, escalation, investigation milestones, mitigation attempts, resolution.
- **Sources**: Where info came from (monitoring, logs, person X, Slack, etc.).
- **Objectivity**: Facts only, no blame. "Engineer X deployed" not "Engineer X mistakenly deployed".

### Impact
- **Quantify**: Numbers > adjectives. "50K users" not "many users". "$20K" not "significant".
- **Multiple Dimensions**: Users, revenue, SLA, reputation, team time, opportunity cost.
- **Metrics Table**: Before/during/after for key metrics shows impact clearly.

### Root Cause
- **5 Whys**: Stop when you reach fixable systemic issue, not "person made mistake".
- **Multiple Causes**: Most incidents have >1 cause. List primary + contributing.
- **System Focus**: "Deployment pipeline allowed bad config" not "Person deployed bad config".

### Corrective Actions
- **SMART**: Specific (what exactly), Measurable (how verify), Assigned (who owns), Realistic (achievable), Time-bound (when done).
- **Categorize**: Immediate (days), Short-term (weeks), Long-term (months).
- **Prioritize**: High impact, low effort first. Don't create >10 actions (won't get done).
- **Track**: Add to project tracker, review weekly, don't let languish.

### What Went Well
- **Balance**: Postmortems aren't just about failures, recognize what worked.
- **Examples**: Good communication, fast response, effective teamwork, working alerting.
- **Build On**: These are strengths to maintain and amplify.

### Lessons Learned
- **Generalize**: Extract principles applicable beyond this incident.
- **Share**: These are org-wide learnings, share broadly.
- **Action**: Connect lessons to corrective actions.

---

## Quick Patterns

### Production Outage Postmortem
```
Summary: [Service] down for [X hours] affecting [Y users] due to [root cause]
Timeline: Detection → Investigation → Mitigation attempts → Resolution
Impact: Users, revenue, SLA, reputation
Root Cause: 5 Whys to system issue
Actions: Immediate fixes, monitoring improvements, process changes, long-term infrastructure
```

### Security Incident Postmortem
```
Summary: [Breach type] exposed [data/systems] due to [vulnerability]
Timeline: Breach → Detection (often delayed) → Containment → Remediation → Recovery
Impact: Data exposed, compliance risk, reputation, remediation cost
Root Cause: Missing security controls, access management, unpatched vulnerabilities
Actions: Security audit, access review, patch management, training, compliance reporting
```

### Product Launch Failure Postmortem
```
Summary: [Feature] launched to [<X% adoption] vs [Y% expected] due to [reasons]
Timeline: Planning → Development → Launch → Metrics review → Pivot decision
Impact: Revenue miss, wasted effort, opportunity cost, team morale
Root Cause: Poor problem validation, wrong solution, inadequate testing, misaligned expectations
Actions: Improve discovery, user research, validation, stakeholder alignment
```

### Project Deadline Miss Postmortem
```
Summary: [Project] delivered [X months late] due to [root causes]
Timeline: Kickoff → Milestones → Delays → Delivery
Impact: Customer impact, revenue delay, team burnout, opportunity cost
Root Cause: Poor estimation, scope creep, technical challenges, resource constraints
Actions: Improve estimation, scope control, technical spikes, resource planning
```

---

## Quality Checklist

Before finalizing postmortem, verify:

**Completeness**:
- [ ] Incident summary with severity, impact summary, dates
- [ ] Timeline with timestamps, events, actions taken
- [ ] Impact quantified (users, duration, revenue, metrics)
- [ ] Root cause analysis (5 Whys or equivalent)
- [ ] Corrective actions with SMART criteria (specific, measurable, assigned, realistic, time-bound)
- [ ] What went well section
- [ ] Lessons learned documented

**Quality**:
- [ ] Blameless tone (focus on systems, not individuals)
- [ ] Timeline uses specific timestamps (not vague times)
- [ ] Impact quantified with numbers (not adjectives like "many")
- [ ] Root cause goes beyond surface symptoms (asked "Why?" 5 times)
- [ ] Actions are specific, owned, and time-bound (not vague "improve X")
- [ ] Actions tracked in project management tool

**Timeliness**:
- [ ] Postmortem written within 48 hours of incident resolution
- [ ] Shared with team and stakeholders within 72 hours
- [ ] Presented in team meeting for discussion
- [ ] Action items in tracker with owners and deadlines

**Learning**:
- [ ] Lessons learned extracted and generalized
- [ ] Shared broadly for organizational learning
- [ ] Action items address root causes (not just symptoms)
- [ ] Follow-up review scheduled (2-4 weeks) to check progress

**Overall Assessment**:
- [ ] Would prevent similar incident if all actions completed?
- [ ] Are we attacking root causes or just symptoms?
- [ ] Is tone blameless and constructive?
- [ ] Will team actually complete these actions? (realistic, prioritized)
