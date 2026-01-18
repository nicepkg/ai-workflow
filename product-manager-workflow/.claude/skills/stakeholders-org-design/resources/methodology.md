# Advanced Organizational Design Methodology

## Workflow

```
Advanced Org Design Progress:
- [ ] Step 1: Conway's Law analysis and reverse Conway maneuver
- [ ] Step 2: Team Topologies design
- [ ] Step 3: Domain-Driven Design alignment
- [ ] Step 4: Advanced stakeholder techniques
- [ ] Step 5: Organizational change patterns
```

**Step 1**: Conway's Law analysis - Understand current architecture-team misalignment. See [1. Conway's Law & Reverse Conway Maneuver](#1-conways-law--reverse-conway-maneuver).

**Step 2**: Team Topologies - Apply 4 fundamental types + 3 interaction modes. See [2. Team Topologies Framework](#2-team-topologies-framework).

**Step 3**: Domain-Driven Design - Align bounded contexts with team boundaries. See [3. Domain-Driven Design Alignment](#3-domain-driven-design-alignment).

**Step 4**: Advanced stakeholder techniques - Influence networks, coalition building. See [4. Advanced Stakeholder Techniques](#4-advanced-stakeholder-techniques).

**Step 5**: Organizational change - Transformation patterns, resistance management. See [5. Organizational Change Patterns](#5-organizational-change-patterns).

---

## 1. Conway's Law & Reverse Conway Maneuver

### Conway's Law Statement

**"Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations."** — Melvin Conway, 1967

**Practical Implications:**
- If you have 4 teams, you'll produce a system with 4 major components
- If backend and frontend are separate teams, you'll get a clear backend/frontend split (potentially with API bloat)
- If teams don't communicate, systems won't integrate well

### Reverse Conway Maneuver

**Principle**: Design team structure to match desired system architecture, not current org structure.

**Process:**
1. **Design target architecture** (microservices, modular monolith, etc.)
2. **Identify system boundaries** (services, modules, domains)
3. **Create teams matching boundaries** (one team per service/domain)
4. **Define clear interfaces** (APIs between teams = APIs between systems)

**Example: Microservices Transition**

**Current State (misaligned):**
- Monolithic team structure: Frontend team, Backend team, Database team, QA team
- Want: Microservices architecture (User Service, Payment Service, Notification Service)
- Problem: No team owns end-to-end service

**Target State (aligned):**
- User Service Team (owns frontend + backend + DB + deployment)
- Payment Service Team (owns frontend + backend + DB + deployment)
- Notification Service Team (owns frontend + backend + DB + deployment)
- Platform Team (provides shared infrastructure, monitoring, deployment tools)

**Result**: Teams naturally build microservices because that's their ownership boundary.

### Architecture-Team Alignment Matrix

| Architecture Style | Recommended Team Structure | Anti-pattern |
|--------------------|---------------------------|--------------|
| Monolith | Single cross-functional team (if <50 people) | Functional silos (FE/BE/QA teams) |
| Modular Monolith | Teams per module with clear interfaces | Shared code ownership across teams |
| Microservices | Teams per service, full-stack ownership | Shared service ownership |
| Microfrontends | Teams per micro-app + platform team | Single frontend team for all micro-apps |
| Platform/API | Product teams (consumers) + Platform team (provider) | Product teams building own platforms |

### Detecting Conway's Law Violations

**Symptoms:**
- Architecture constantly diverging from intended design
- Excessive coordination needed for simple changes
- Modules/services tightly coupled despite supposed independence
- Teams unable to deploy independently

**Diagnostic Questions:**
1. Do team boundaries match system boundaries?
2. Can teams deploy without coordinating with other teams?
3. Do frequent changes require cross-team sync meetings?
4. Are interfaces well-defined or constantly renegotiated?

**Fix**: Realign teams to match desired architecture OR redesign architecture to match practical team constraints.

---

## 2. Team Topologies Framework

### Four Fundamental Team Types

**1. Stream-Aligned Teams** (Product/Feature Teams)
- **Purpose**: Aligned with flow of business change (features, products, user journeys)
- **Characteristics**: Cross-functional, close to customer, fast flow
- **Size**: 5-9 people
- **Cognitive Load**: 1 product area, 1-2 user journeys
- **Example**: Checkout Team (owns entire checkout experience), Search Team, Recommendations Team

**2. Platform Teams** (Internal Product Teams)
- **Purpose**: Reduce cognitive load of stream-aligned teams by providing internal services
- **Characteristics**: Treat stream-aligned teams as customers, self-service, clear SLAs
- **Size**: Larger (10-15 people) or multiple smaller platform teams
- **Examples**: Developer Experience Platform (CI/CD, testing frameworks), Data Platform (analytics, ML infrastructure), Infrastructure Platform (AWS, Kubernetes)

**3. Enabling Teams** (Capability Building)
- **Purpose**: Build capability in stream-aligned teams (temporary, not permanent dependency)
- **Characteristics**: Coaches not doers, time-boxed engagements (3-6 months), transfer knowledge then leave
- **Size**: Small (2-5 people), specialists
- **Examples**: Security Enablement (teach teams secure coding), Accessibility Enablement, Performance Optimization Enablement

**4. Complicated-Subsystem Teams** (Specialists)
- **Purpose**: Own complex subsystems requiring deep expertise
- **Characteristics**: Specialist knowledge, reduce cognitive load on stream teams
- **Size**: Small (3-8 people), domain experts
- **Examples**: ML/AI team, Video encoding team, Payment processing team, Cryptography team

### Three Team Interaction Modes

**1. Collaboration Mode** (High Interaction)
- **When**: Discovery, rapid innovation, solving novel problems
- **Duration**: Temporary (weeks to months)
- **Example**: Stream team collaborates with enabling team to learn new capability
- **Characteristics**: High overlap, pair programming, joint problem-solving
- **Warning**: Don't make permanent—high cognitive load

**2. X-as-a-Service Mode** (Low Interaction)
- **When**: Clear interface, stable requirements, proven solution
- **Duration**: Permanent
- **Example**: Stream team consumes platform team's CI/CD service
- **Characteristics**: Self-service, clear SLA, API-first, minimal meetings
- **Goal**: Reduce cognitive load, enable autonomy

**3. Facilitating Mode** (Temporary Support)
- **When**: Building new capability, unblocking stream team
- **Duration**: Time-boxed (weeks to months)
- **Example**: Enabling team teaches stream team performance testing
- **Characteristics**: Knowledge transfer, workshops, pairing, then exit
- **Goal**: Leave stream team self-sufficient

### Team Topology Evolution

**Stage 1: Single Team** (Startup, <10 people)
- One stream-aligned team owns everything
- No platform team yet (premature optimization)

**Stage 2: Multiple Stream Teams** (Scale-up, 10-30 people)
- 2-4 stream-aligned teams
- Start seeing duplication (deployment, monitoring, data)
- Platform team emerges from common pain

**Stage 3: Stream + Platform** (Growth, 30-100 people)
- 4-10 stream-aligned teams
- 1-2 platform teams (developer experience, data, infrastructure)
- Possibly 1 enabling team for critical capability gaps

**Stage 4: Mature Topology** (Large, 100+ people)
- Many stream-aligned teams (organized by value stream)
- Multiple platform teams (federated platforms)
- Enabling teams for strategic capabilities
- Complicated-subsystem teams for deep specialties

### Team API Design

**Every team should document their "Team API":**

1. **Code API**: What services/libraries do we provide? (Endpoints, SDKs, packages)
2. **Documentation API**: What docs are available? (README, runbooks, architecture diagrams)
3. **Communication API**: How to reach us? (Slack, email, office hours, on-call)
4. **Collaboration API**: How to work with us? (Interaction mode, meeting cadence, decision process)

**Template:**
```
Team: [Name]
Type: [Stream-Aligned / Platform / Enabling / Complicated-Subsystem]

Services Provided:
- Service A: [Description] - SLA: [99.9% uptime]
- Service B: [Description] - SLA: [<100ms p95]

Documentation:
- Architecture: [Link]
- API Docs: [Link]
- Runbooks: [Link]

Communication:
- Slack: #team-name
- Email: team@company.com
- Office Hours: Tuesdays 2-3pm
- On-call: [PagerDuty link]

Interaction Modes:
- X-as-a-Service: Use our APIs (preferred)
- Collaboration: For new integrations (time-boxed to 2 weeks)
- Facilitation: We can teach your team [capability] (3-month engagement)
```

---

## 3. Domain-Driven Design Alignment

### Bounded Contexts & Team Boundaries

**Principle**: Align team boundaries with bounded contexts (not just technical layers).

**Bounded Context**: A conceptual boundary within which a domain model is consistent. Different contexts may have different models for same concept.

**Example: E-commerce**
- **Shopping Context**: Product (SKU, description, price, inventory)
- **Fulfillment Context**: Product (tracking number, shipping address, delivery status)
- **Analytics Context**: Product (page views, conversion rate, revenue)

**Same entity ("Product"), different models, different teams.**

### Context Mapping Patterns

**1. Partnership** (Two teams collaborate closely)
- Symmetric relationship, joint planning
- Example: Checkout team + Payment team for new payment flow

**2. Shared Kernel** (Small shared code/data)
- Minimal shared model, high coordination cost
- Example: Shared customer ID schema across all teams
- Warning: Keep tiny—big shared kernels become bottlenecks

**3. Customer-Supplier** (Upstream provides to Downstream)
- Asymmetric relationship, SLA-based
- Example: User Auth service (upstream) provides to all product teams (downstream)
- Supplier responsible for meeting customer needs

**4. Conformist** (Downstream conforms to Upstream)
- Downstream has no influence on upstream
- Example: Product teams conform to external payment provider API
- Necessary when integrating third-party services

**5. Anti-Corruption Layer** (Translation Layer)
- Protect your model from external complexity
- Example: Wrapper around legacy system to present clean API
- Use when upstream is messy but you can't change it

**6. Separate Ways** (No integration)
- Contexts too different to integrate economically
- Example: HR system and product analytics—no overlap

### Team-to-Context Alignment

**Rule**: One team per bounded context (ideally).

**Options if context too large for one team:**
1. **Split context**: Find natural seam within bounded context
2. **Multiple teams share**: Requires tight coordination (expensive)
3. **Sub-teams within**: Maintain as one logical team, sub-teams for focus areas

**Options if team owns multiple contexts:**
1. **OK if contexts small** and tightly related
2. **Watch cognitive load**: Max 2-3 simple contexts per team

---

## 4. Advanced Stakeholder Techniques

### Influence Network Analysis

**Social Network Analysis for Organizations:**

1. **Identify nodes**: All stakeholders
2. **Map edges**: Who influences whom? (direction matters)
3. **Calculate centrality**:
   - **Degree centrality**: Number of connections (who's most connected?)
   - **Betweenness centrality**: Who bridges disconnected groups? (critical connectors)
   - **Closeness centrality**: Who can reach everyone quickly? (efficient communicators)

**Application:**
- **High betweenness**: Critical bridges—if they leave or resist, networks fragment
- **High degree**: Opinion leaders—influence many directly
- **Low centrality but critical domain**: Hidden experts—engage directly

### Coalition Building

**For Major Organizational Change:**

**Phase 1: Identify Minimum Winning Coalition**
- What's minimum set of stakeholders needed to approve change?
- Who has veto power? (must include)
- Who has high influence? (prioritize)

**Phase 2: Address WIIFM (What's In It For Me)**
- For each coalition member: What do they gain from this change?
- If nothing: Can we adjust proposal to create gains?
- Document value proposition per stakeholder

**Phase 3: Sequence Engagement**
- Start with champions (easy wins)
- Then bridges (access to networks)
- Then high-power neutrals (sway with champion support)
- Finally address blockers (after coalition established)

**Phase 4: Manage Defection**
- Monitor for coalition members changing stance
- Regular check-ins, address concerns early
- Adjust proposal if needed to maintain coalition

### Resistance Management

**Kotter's 8-Step Change Model:**
1. Create urgency (burning platform)
2. Form guiding coalition (power + credibility)
3. Develop vision (clear future state)
4. Communicate vision (over-communicate 10x)
5. Empower action (remove obstacles)
6. Generate short-term wins (momentum)
7. Consolidate gains (don't declare victory early)
8. Anchor changes (make it "how we do things")

**Resistance Patterns:**

| Resistance Type | Symptom | Root Cause | Strategy |
|-----------------|---------|------------|----------|
| Rational | "This won't work because [data]" | Legitimate concerns | Address with analysis, pilot to test |
| Emotional | "I don't like this" | Fear, loss of status/control | Empathy, involvement, WIIFM |
| Political | "I'll block this" | Power play, competing agenda | Coalition, escalation, negotiation |
| Cultural | "Not how we do things here" | Clashes with norms/values | Small wins, demonstrate compatibility |

---

## 5. Organizational Change Patterns

### Spotify Model (Modified)

**Squads** (Stream-aligned teams, 5-9 people)
- Cross-functional, autonomous, long-lived
- Own features end-to-end
- Aligned with product areas

**Tribes** (Collection of related squads, 40-150 people)
- Share mission, loosely coordinated
- Tribe lead facilitates, doesn't dictate
- Regular tribe gatherings (demos, planning)

**Chapters** (Functional expertise groups within tribe)
- Engineers from different squads, same skill
- Led by chapter lead (line manager)
- Knowledge sharing, standards, career development

**Guilds** (Communities of practice across tribes)
- Voluntary, interest-based
- Share knowledge org-wide (security, testing, frontend)
- No formal authority, influence through expertise

**When to Use:**
- Large product orgs (100+ people)
- Need autonomy + alignment
- Strong engineering culture

**When NOT to Use:**
- Small orgs (<50 people) - too much overhead
- Weak engineering culture - guilds/chapters won't self-organize
- Highly regulated - too much autonomy

### Amazon's Two-Pizza Teams

**Principles:**
- Team size: 5-9 people (can feed with 2 pizzas)
- Fully autonomous: Own service end-to-end
- APIs only: Teams communicate via documented APIs
- You build it, you run it: Own production operations

**Supporting Infrastructure:**
- Service-oriented architecture (technical enabler)
- Self-service platform (AWS, deployment tools)
- Clear metrics (each team has dashboard)

**Results:**
- Reduced coordination overhead
- Faster innovation
- Clear accountability

**Challenges:**
- Requires mature platform (or teams duplicate infrastructure)
- API versioning complexity
- Potential for silos if over-isolated

### Platform Team Extraction

**When to Extract Platform Team:**
- **Signal 1**: 3+ stream teams duplicating infrastructure work
- **Signal 2**: Stream teams slowed by infrastructure
 tasks (>20% time)
- **Signal 3**: Infrastructure quality suffering (monitoring gaps, deployment issues)

**How to Extract:**
1. **Identify common pain** across stream teams (deployment, monitoring, data)
2. **Form platform team** (pull volunteers from stream teams who enjoy infrastructure)
3. **Define charter**: What platform provides, what it doesn't
4. **Set SLAs**: Treat stream teams as customers
5. **Build self-service**: Documentation, automation, APIs
6. **Iterate**: Start small, expand based on demand

**Staffing Ratio:**
- **Rule of thumb**: 1 platform engineer per 7-10 product engineers
- **Too many platform**: Over-engineering, bloat
- **Too few platform**: Can't keep up with demand

**Success Metrics:**
- Stream team velocity (should increase after platform stabilizes)
- Time to deploy (should decrease)
- Platform adoption (% of stream teams using platform services)
- Platform team satisfaction survey (NPS from stream teams)

### Organizational Refactoring Patterns

**Pattern 1: Cell Division** (Split large team)
- **When**: Team >12 people, communication overhead high
- **How**: Identify natural seam in ownership, split into 2 teams
- **Example**: E-commerce team → Catalog team + Checkout team

**Pattern 2: Merging** (Combine small teams)
- **When**: Teams <4 people, lack skill diversity, too much coordination
- **How**: Merge related teams, clarify combined ownership
- **Example**: Frontend team + Backend team → Full-stack product team

**Pattern 3: Extraction** (Pull out specialists)
- **When**: Specialized need emerging across teams
- **How**: Form complicated-subsystem or platform team
- **Example**: Extract data engineers from product teams → Data Platform team

**Pattern 4: Embedding** (Integrate specialists)
- **When**: Specialist team bottleneck, stream teams need capability
- **How**: Embed specialists into stream teams, dissolve central team
- **Example**: Embed QA engineers into product teams, close central QA team

---

## 6. Measuring Organizational Effectiveness

**Accelerate Metrics (beyond DORA):**
- **Team autonomy**: % decisions made without escalation
- **Psychological safety**: Team survey (Edmondson scale)
- **Documentation quality**: % questions answerable via docs
- **Cognitive load**: % time on primary mission vs toil/coordination

**Org Design Quality Indicators:**
- [ ] <10% time in cross-team coordination meetings
- [ ] Teams can deploy independently (>80% deploys don't require sync)
- [ ] Clear ownership (anyone can name team owning any component in <30 seconds)
- [ ] Fast onboarding (new hire productive in <2 weeks)
- [ ] Low turnover (voluntary attrition <10%/year)
- [ ] High engagement (survey scores ≥4/5)

**Anti-patterns:**
- Conway's Law violations (architecture ≠ team structure)
- Shared code ownership (nobody accountable)
- Teams too large (>12) or too small (<3)
- Matrix hell (dual reporting, unclear decision rights)
- Platform teams building for themselves (not customer-focused)
- Permanent collaboration mode (high cognitive load, burnout)
