# Stakeholders & Organizational Design Template

## Workflow

Copy this checklist and track your progress:

```
Org Design Progress:
- [ ] Step 1: Map stakeholders and influence
- [ ] Step 2: Define team structure and boundaries
- [ ] Step 3: Specify team interfaces and contracts
- [ ] Step 4: Assess capability maturity
- [ ] Step 5: Create transition plan with governance
```

**Step 1: Map stakeholders** - Power-interest matrix, RACI, influence networks. See [Section 1](#1-stakeholder-mapping).

**Step 2: Define teams** - Team topology, size, ownership boundaries. See [Section 2](#2-team-structure-design).

**Step 3: Specify interfaces** - API contracts, SLAs, handoffs, decision rights. See [Section 3](#3-team-interface-contracts).

**Step 4: Assess maturity** - DORA, CMM, custom capability assessments. See [Section 4](#4-capability-maturity-assessment).

**Step 5: Create transition plan** - Migration path, governance, review cadence. See [Section 5](#5-transition-plan).

---

## 1. Stakeholder Mapping

### Organization Context

**Domain/Initiative:**
- **Name**: [What are we designing/changing]
- **Scope**: [Boundaries of design/change]
- **Timeline**: [When does this need to happen]
- **Drivers**: [Why now? What triggered this?]

### Stakeholder Inventory

List all stakeholders (individuals or groups):

| Stakeholder | Role | Power | Interest | Quadrant |
|-------------|------|-------|----------|----------|
| [Name/Group] | [What they do] | High/Low | High/Low | [See below] |
| [Name/Group] | [What they do] | High/Low | High/Low | [See below] |
| [Name/Group] | [What they do] | High/Low | High/Low | [See below] |

**Power**: Ability to influence outcome (budget, authority, veto, resources)
**Interest**: Engagement level, stake in outcome

### Power-Interest Quadrants

**High Power, High Interest** (Manage Closely):
- [ ] Stakeholder 1: [Name] - [Engagement strategy]
- [ ] Stakeholder 2: [Name] - [Engagement strategy]

**High Power, Low Interest** (Keep Satisfied):
- [ ] Stakeholder 3: [Name] - [How to keep satisfied]
- [ ] Stakeholder 4: [Name] - [How to keep satisfied]

**Low Power, High Interest** (Keep Informed):
- [ ] Stakeholder 5: [Name] - [How to engage]
- [ ] Stakeholder 6: [Name] - [How to engage]

**Low Power, Low Interest** (Monitor):
- [ ] Stakeholder 7: [Name] - [When to update]

### Influence Network

**Champions** (Advocates for change):
- [Name]: Why champion? What do they gain?
- [Name]: Why champion? What do they gain?

**Blockers** (Resistors to change):
- [Name]: Why blocking? What concerns?
- [Name]: Why blocking? What concerns?

**Bridges** (Connect groups):
- [Name]: Connects [Group A] to [Group B]
- [Name]: Connects [Group C] to [Group D]

**Gatekeepers** (Control access):
- [Name]: Controls access to [Key stakeholder/resource]

### RACI for Key Decisions

| Decision | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| Team structure | [Who] | [One person] | [Who,Who] | [Who,Who,Who] |
| Interface contracts | [Who] | [One person] | [Who,Who] | [Who,Who,Who] |
| Migration timeline | [Who] | [One person] | [Who,Who] | [Who,Who,Who] |
| [Custom decision] | [Who] | [One person] | [Who,Who] | [Who,Who,Who] |

**Rule**: Exactly one Accountable per decision. Consulted = provide input before. Informed = notified after.

---

## 2. Team Structure Design

### Current State

**Existing Teams:**

| Team Name | Size | Responsibilities | Problems |
|-----------|------|------------------|----------|
| [Team 1] | [#] | [What they own] | [Pain points] |
| [Team 2] | [#] | [What they own] | [Pain points] |
| [Team 3] | [#] | [What they own] | [Pain points] |

**Current Structure Type:** [Functional / Product / Matrix / Hybrid]

**Key Problems:**
- [ ] Problem 1: [Describe]
- [ ] Problem 2: [Describe]
- [ ] Problem 3: [Describe]

### Target State

**Team Topology:** [Choose one or hybrid]
- [ ] **Functional**: Teams organized by skill (Frontend, Backend, QA, DevOps)
- [ ] **Product/Feature**: Cross-functional teams owning features/products
- [ ] **Platform**: Product teams + Platform team providing shared services
- [ ] **Team Topologies**: Stream-aligned + Platform + Enabling + Complicated-subsystem

**Proposed Teams:**

| Team Name | Type | Size | Responsibilities | Owner |
|-----------|------|------|------------------|-------|
| [Team A] | [Stream/Platform/Enabling/Subsystem] | [5-9] | [What they own] | [Lead] |
| [Team B] | [Stream/Platform/Enabling/Subsystem] | [5-9] | [What they own] | [Lead] |
| [Team C] | [Stream/Platform/Enabling/Subsystem] | [5-9] | [What they own] | [Lead] |

**Team Sizing Principles:**
- **2-pizza rule**: 5-9 people per team (Amazon model)
- **Dunbar's number**: 5-15 close working relationships max
- **Cognitive load**: 1 simple domain, 2-3 related domains, or max 1 complex domain per team

### Team Boundaries & Ownership

**Ownership Model:** [Choose one]
- [ ] **Full-stack ownership**: Team owns frontend, backend, database, infrastructure for their domain
- [ ] **Service ownership**: Team owns specific microservices
- [ ] **Feature ownership**: Team owns features across shared codebase
- [ ] **Platform ownership**: Team provides internal products/tools to other teams

**Domain Boundaries** (using Domain-Driven Design):

| Bounded Context | Owning Team | Responsibilities | Dependencies |
|-----------------|-------------|------------------|--------------|
| [Context A] | [Team X] | [What's in scope] | [Other contexts] |
| [Context B] | [Team Y] | [What's in scope] | [Other contexts] |
| [Context C] | [Team Z] | [What's in scope] | [Other contexts] |

### Conway's Law Alignment

**Desired System Architecture:**
- [Describe target architecture: microservices, modular monolith, etc.]

**Team Structure Alignment:**
- [How team boundaries map to system boundaries]
- [Example: Team A owns Service A, Team B owns Service B with well-defined APIs]

**Anti-patterns to Avoid:**
- [ ] Monolithic team creating microservices (coordination nightmare)
- [ ] Fragmented teams with shared code ownership (merge conflicts, unclear responsibility)

---

## 3. Team Interface Contracts

### Technical Interfaces (APIs)

**For each team providing services:**

**Service: [Name]**
- **Owner Team**: [Team name]
- **Purpose**: [What problem does it solve for consumers?]
- **Consumers**: [Which teams depend on this?]

**API Contract:**
- **Endpoints**: [List key endpoints or link to API docs]
- **Data Format**: [JSON, Protocol Buffers, GraphQL, etc.]
- **Authentication**: [OAuth, API keys, mTLS, etc.]
- **Rate Limits**: [Requests per second/minute]
- **Versioning**: [Semantic versioning, backward compatibility policy]
- **Documentation**: [Link to API docs, Swagger/OpenAPI spec]

**SLA:**
- **Availability**: [99.9%, 99.95%, 99.99%]
- **Performance**: [p50: Xms, p95: Yms, p99: Zms]
- **Support**: [Critical: 1hr response, High: 4hr, Medium: 1 day]
- **On-call**: [Rotation schedule, escalation path]

**Contact:**
- **Slack**: [#team-channel]
- **Email**: [team@company.com]
- **On-call**: [PagerDuty link / escalation policy]

### Organizational Interfaces (Workflows)

**Cross-Team Workflows:**

**Workflow: Design → Engineering**
- **Trigger**: [When does handoff happen?]
- **Inputs**: [What does Engineering need from Design?]
  - [ ] Design specs (Figma/Sketch)
  - [ ] User flows
  - [ ] Design review sign-off
  - [ ] Asset exports
- **Outputs**: [What does Design get back?]
  - [ ] Implementation feedback
  - [ ] Edge cases discovered
- **Timeline**: [How long for handoff? Review cycles?]

**Workflow: Engineering → QA**
- **Trigger**: Feature complete
- **Inputs**: Test plan, staging environment, feature documentation
- **Outputs**: QA report, bugs filed, sign-off for release
- **Timeline**: 2-3 days QA cycle

**Workflow: Engineering → Support**
- **Trigger**: Feature launch
- **Inputs**: Documentation, runbook, training session
- **Outputs**: Support readiness confirmation
- **Timeline**: 1 week before launch

### Decision Rights (DACI)

**For each cross-team decision type:**

**Decision Type: [e.g., Architectural changes affecting multiple teams]**
- **Driver**: [Who runs the decision process] - Example: Tech Lead from Team A
- **Approver**: [Who makes final call - exactly one] - Example: Principal Architect
- **Contributors**: [Who provides input] - Example: Team leads from Teams B, C, D
- **Informed**: [Who is notified] - Example: Engineering VP, all engineers

**Process:**
1. Driver documents proposal
2. Contributors review and provide feedback (deadline: X days)
3. Approver makes decision (deadline: Y days)
4. Informed stakeholders notified

---

## 4. Capability Maturity Assessment

### DORA Metrics (DevOps Maturity)

| Metric | Current | Target | Gap | Actions |
|--------|---------|--------|-----|---------|
| Deployment Frequency | [X/day, /week, /month] | [Elite: Multiple/day] | [Describe gap] | [How to improve] |
| Lead Time | [X hours/days/weeks] | [Elite: <1 hour] | [Describe gap] | [How to improve] |
| MTTR | [X hours/days] | [Elite: <1 hour] | [Describe gap] | [How to improve] |
| Change Failure Rate | [X%] | [Elite: 0-15%] | [Describe gap] | [How to improve] |

**DORA Performance Level**: [Elite / High / Medium / Low]

### Custom Capability Assessments

**Capability: [e.g., Testing Maturity]**

**Current State** (Level 1-5):
- **Level**: [1-5]
- **Evidence**: [Metrics, artifacts, observations proving current level]
- **Description**: [What does maturity look like at this level?]

**Target State**:
- **Level**: [Target 1-5]
- **Rationale**: [Why this target? Business value?]

**Gap Analysis**:
- **Missing**: [What capabilities/processes/tools are missing?]
- **Needed**: [What needs to change to reach target?]

**Action Items**:
- [ ] Action 1: [Specific, measurable action] - Owner: [Name] - Deadline: [Date]
- [ ] Action 2: [Specific, measurable action] - Owner: [Name] - Deadline: [Date]
- [ ] Action 3: [Specific, measurable action] - Owner: [Name] - Deadline: [Date]

**Repeat for each capability:**
- [ ] Security maturity
- [ ] Design maturity
- [ ] Data maturity
- [ ] Agile/process maturity
- [ ] [Custom capability]

---

## 5. Transition Plan

### Migration Path

**Approach:** [Choose one]
- [ ] **Big Bang**: Switch all at once (risky, fast)
- [ ] **Incremental**: Migrate team by team (safer, slower)
- [ ] **Pilot**: Start with one team, learn, then roll out (recommended)
- [ ] **Hybrid**: Different approaches for different teams

**Phases:**

**Phase 1: [Name] (Timeline: [Dates])**
- **Goal**: [What we're achieving]
- **Teams Affected**: [Which teams]
- **Changes**: [Specific changes happening]
- **Success Criteria**: [How we know it worked]
- **Risks**: [What could go wrong]
- **Mitigations**: [How to reduce risks]

**Phase 2: [Name] (Timeline: [Dates])**
- [Same structure as Phase 1]

**Phase 3: [Name] (Timeline: [Dates])**
- [Same structure as Phase 1]

### Governance & Review

**Decision Authority:**
- **Steering Committee**: [Who makes go/no-go decisions] - Meets: [Frequency]
- **Working Group**: [Who executes day-to-day] - Meets: [Frequency]
- **Escalation Path**: [Issue → Working Group → Steering Committee → Executive]

**Review Cadence:**
- **Weekly**: Working group sync (30 min) - Review progress, blockers
- **Biweekly**: Stakeholder update (1 hr) - Demos, metrics, ask for help
- **Monthly**: Steering committee review (1 hr) - Go/no-go gates, course corrections
- **Quarterly**: Retrospective (2 hr) - What's working, what to adjust

**Communication Plan:**

| Audience | What | When | Channel |
|----------|------|------|---------|
| All employees | High-level update | Monthly | All-hands, email |
| Affected teams | Detailed changes | Weekly | Team meetings, Slack |
| Leadership | Metrics, risks | Biweekly | Email, slides |
| Stakeholders | Progress, asks | Monthly | Stakeholder meeting |

### Success Metrics

**Process Metrics:**
- [ ] Migration timeline: [On track / X weeks ahead/behind]
- [ ] Teams transitioned: [X / Y teams complete]
- [ ] Interfaces defined: [X / Y contracts documented]

**Outcome Metrics** (measure 3-6 months post-transition):
- [ ] Deployment frequency: [Baseline] → [Current] (Target: [X]) | Lead time: [Baseline] → [Current] (Target: [X])
- [ ] Team satisfaction: [Survey before] → [After] (Target: ≥7/10) | Cross-team dependencies: [Baseline] → [Current] (Target: -30%)
- [ ] Incident response: [Baseline] → [Current] (Target: +50% faster)

**Qualitative**: Teams feel ownership | Interfaces clear | Stakeholders know who to contact | Faster decisions | Less coordination overhead

---

## Quality Checklist

Before finalizing, verify:

**Stakeholder Mapping:**
- [ ] All stakeholders identified (didn't miss any groups)
- [ ] Power-interest assessed for each
- [ ] Champions and blockers identified
- [ ] RACI defined for key decisions with exactly one Accountable per decision
- [ ] Engagement strategy per quadrant

**Team Structure:**
- [ ] Team boundaries align with desired architecture (Conway's Law)
- [ ] Team sizes reasonable (5-9 people, 2-pizza rule)
- [ ] Cognitive load per team manageable (1-3 domains)
- [ ] Ownership clear (no shared ownership anti-patterns)
- [ ] Team types appropriate (stream/platform/enabling/subsystem)

**Interfaces:**
- [ ] API contracts documented (endpoints, SLA, contact)
- [ ] SLAs realistic and measurable
- [ ] Handoff protocols clear (design→eng, eng→QA, etc.)
- [ ] Decision rights explicit (DACI for each decision type)
- [ ] Every interface has one clear owner

**Maturity:**
- [ ] Current state assessed with evidence (not aspirations)
- [ ] Gaps identified between current and target
- [ ] Action items specific, assigned, with deadlines
- [ ] Benchmarks used where available (DORA, CMMC, etc.)

**Transition:**
- [ ] Migration path chosen (big bang, incremental, pilot)
- [ ] Phases defined with success criteria
- [ ] Governance structure established (steering, working group)
- [ ] Review cadence set (weekly, monthly, quarterly)
- [ ] Success metrics baselined and targets set
- [ ] Communication plan covers all audiences

**Overall:**
- [ ] Assumptions documented explicitly
- [ ] Risks identified with mitigations
- [ ] Conway's Law alignment checked
- [ ] Design survives "Would this work in practice?" test
