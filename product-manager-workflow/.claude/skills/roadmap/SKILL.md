---
name: roadmap-prioritization-planning
version: "2.0.0"
description: Master prioritization frameworks, roadmap planning, timeline estimation, and resource allocation. Create executable roadmaps that drive focus and alignment.
sasmp_version: "1.3.0"
bonded_agent: 04-roadmap-prioritization
bond_type: PRIMARY_BOND
parameters:
  - name: backlog
    type: array
    required: true
    description: Feature list to prioritize
  - name: framework
    type: string
    enum: [rice, moscow, kano, ice, wsjf]
retry_logic:
  max_attempts: 3
  backoff: exponential
logging:
  level: info
  hooks: [start, complete, error]
---

# Roadmap & Prioritization Skill

Master the art of saying "no". Create focused roadmaps that align your organization, drive strategic outcomes, and maximize impact with limited resources.

## RICE Scoring System (Complete)

### Formula
```
RICE Score = (Reach × Impact × Confidence) / Effort

Reach: How many users affected? (1-100+)
- 10+ = 10
- 100+ = 100
- 1000+ = 1000

Impact: Per-user impact (3, 2, 1, 0.5)
- 3 = Massive (10x improvement)
- 2 = High (significant improvement)
- 1 = Medium (noticeable improvement)
- 0.5 = Low (minor improvement)

Confidence: How confident? (0.25-1.0)
- 1.0 = High (research backed)
- 0.8 = Medium (some validation)
- 0.5 = Low (minimal validation)
- 0.25 = Very low (assumption)

Effort: Engineer-weeks needed (1-20+)
```

### Scoring Example Matrix

```
Feature          Reach Impact Confidence Effort RICE Score
────────────────────────────────────────────────────────
User Onboarding   50    3      0.8      8      (50×3×0.8)/8 = 15.0
Dark Mode         200   1      0.9      4      (200×1×0.9)/4 = 45.0
API Limits        500   2      0.7      10     (500×2×0.7)/10 = 70.0
Performance Fix   1000  0.5    1.0      5      (1000×0.5×1)/5 = 100.0
Custom Fields     30    3      0.6      12     (30×3×0.6)/12 = 4.5

PRIORITIZE: Performance > API Limits > Dark Mode > Onboarding > Custom Fields
```

### RICE Confidence Levels

**High (1.0) - Research-backed**
- Customer interviews conducted
- Data from analytics
- Customer support tickets confirming
- Clear customer demand

**Medium (0.8) - Some validation**
- Logical assumption
- One or two customers requesting
- Industry trends suggest it
- Similar features successful elsewhere

**Low (0.5) - Minimal validation**
- Educated guess
- Competitive pressure (they have it)
- Opportunity emerged
- Needs deeper validation

**Very Low (0.25) - Pure assumption**
- "Seems like good idea"
- No customer feedback
- No validation whatsoever
- High risk of waste

## Alternative Prioritization Methods

### Value vs Effort Matrix

```
           Low Effort      High Effort
High Value  QUICK WINS      STRATEGIC
           (Do first)      (Plan carefully)

Low Value   FILL-INS        AVOID
           (If time)       (Skip)
```

**Quick Wins:** High value, low effort
- Implement first for momentum
- Build confidence
- Show stakeholders progress
- Examples: Bug fixes, small features

**Strategic:** High value, high effort
- Long-term competitive advantage
- Requires planning and resources
- Examples: New platform, architecture

**Fill-Ins:** Low value, low effort
- Polish features
- Technical debt
- Do when capacity available

**Avoid:** Low value, high effort
- Waste of resources
- Say "no" clearly

### MoSCoW Method (Simpler)

**Must Have** (Non-negotiable for launch)
- Core functionality
- Without these: launch doesn't happen
- Usually 40% of work

**Should Have** (Important but deferrable)
- Significant value
- Could launch without but less attractive
- Usually 30% of work

**Could Have** (Nice to have)
- Polish, nice features
- Do if budget/time allows
- Usually 20% of work

**Won't Have** (Explicitly out of scope)
- Clearly deferred
- Helps stakeholders understand priorities
- Usually 10% of work

### Kano Model (Customer Satisfaction)

Three feature categories:

**Basic Factors** (Threshold)
- Expected to be present
- Absence = very dissatisfied
- Presence = satisfied (not delighted)
- Example: Core app functionality
- No competitive advantage

**Performance Factors** (Linear)
- More = more satisfaction
- Less = less satisfaction
- Competitive advantage
- Examples: Speed, customization options
- Scales continuously

**Delighters** (Excitement)
- Unexpected features
- Presence = delighted
- Absence = neutral
- High competitive advantage
- Examples: Surprising UX, hidden features

**Strategy:** Must haves first, then performance, then delighters for differentiation

## Roadmap Planning Process

### 12-Month Strategic Roadmap

**Structure:**
```
Q1 2025: Initiative Theme
├─ Goal: Business outcome
├─ Key Features: 2-3 major features
├─ Success Metrics: How you measure
└─ Resource: Team size needed

Q2 2025: Initiative Theme
Q3 2025: Initiative Theme
Q4 2025: Initiative Theme
```

### Quarterly Planning Process

**Timeline:** Plan month before quarter starts

**Week 1: Data Gathering**
- Customer feedback from last quarter
- Support tickets and issues
- Competitive landscape changes
- Team retrospective learnings
- Metrics review vs targets

**Week 2: Prioritization**
- Apply RICE scoring
- Consider strategic goals
- Assess resource availability
- Get engineering estimates
- Map dependencies

**Week 3: Planning**
- Break stories into sprints
- Allocate resources
- Identify risks
- Plan communication

**Week 4: Alignment & Launch**
- Present roadmap to stakeholders
- Engineering team commitment
- Executive buy-in
- All hands announcement

### Sprint Planning (Weekly)

**Monday: Planning**
- Pick features for sprint
- Break into user stories
- Estimate effort
- Assign owners
- Identify blockers

**Daily: Standups**
- What did you do?
- What's blocking you?
- What's next?
- 15 minutes max

**Friday: Retrospective**
- What went well?
- What needs improvement?
- Velocity tracking
- Plan adjustments for next sprint

## Resource Allocation

### Team Capacity Planning

```
Team Size: 5 engineers
Sprint Length: 2 weeks
Typical Capacity: 40-50 story points

Planning Reality:
- 50% unplanned work (bugs, interrupts)
- 20% operational tasks
- 30% feature development

Result: 50 points × 30% = 15 points for features
→ Add MUST have items first
→ Fill remaining capacity with SHOULD/COULD
```

### Resource Distribution

**Engineering Team:**
- 60-70% new features (roadmap)
- 20-30% bug fixes & optimization
- 10-15% technical debt
- 5-10% operations/support

**Product Manager:**
- 60% planning and discovery
- 20% communication and alignment
- 10% analysis and metrics
- 10% team leadership

**Design Team:**
- 70% feature design
- 15% design system maintenance
- 15% research and testing

## Dependencies & Sequencing

### Dependency Types

**Hard Dependency**
- Feature B can't start until Feature A done
- Example: Payment system before subscription plans
- Impacts timeline significantly

**Soft Dependency**
- Feature B better if Feature A done first
- Example: Mobile app after web fully tested
- Flexible on timing

**Cross-Team Dependency**
- Requires other team completion
- Longest lead time
- Must surface early

### Risk Management

**Common Risks:**

1. **Scope Creep**
   - Mitigation: Say "no" often, defer to future
   - Owner: Product Manager
   - Plan: Weekly scope review

2. **Key Person Leaves**
   - Mitigation: Cross-training, documentation
   - Owner: Engineering Manager
   - Plan: Onboarding process

3. **Timeline Pressure**
   - Mitigation: Plan with buffer, manage expectations
   - Owner: Product Manager
   - Plan: Transparent communication

4. **Technical Challenges Emerge**
   - Mitigation: Spike time, proof of concepts
   - Owner: Engineering Lead
   - Plan: 20% contingency in estimates

## Roadmap Communication

### For Executives
- Focus on business outcomes
- Show how each quarter builds toward vision
- Highlight competitive differentiation
- Revenue/growth impact

### For Engineering
- Detailed specs and requirements
- Technical complexity and dependencies
- Effort estimates and risks
- Resource needs

### For Customers
- User-focused benefits
- Timeline (quarter, not date)
- Most-requested features highlighted
- Under-promise, over-deliver

### For Sales
- "Coming soon" messaging
- What they can sell against
- Customer feedback incorporated
- Competitive differentiation

## Roadmap Review & Adjustment

**Weekly:** Sprint progress
**Monthly:** Quarterly progress vs plan
**Quarterly:** Full roadmap refresh
**Annually:** Strategic direction review

**Triggers for Reprioritization:**
- Major customer churn
- Competitive threat
- Market shift
- Unexpected technical blocker
- Resource availability change

## Troubleshooting

### Yaygın Hatalar & Çözümler

| Hata | Olası Sebep | Çözüm |
|------|-------------|-------|
| Roadmap sürekli kayıyor | Unrealistic estimates | 30% buffer ekle |
| Priority debates | Unclear criteria | RICE workshop |
| Resource contention | Over-commitment | Capacity planning |
| Dependencies blocking | Late identification | Sprint 0 mapping |

### Debug Checklist

```
[ ] RICE scoring consistent mi?
[ ] Capacity realistic mi? (20% buffer)
[ ] Dependencies mapped mi?
[ ] Stakeholder alignment var mı?
[ ] Risk mitigation planı var mı?
```

### Recovery Procedures

1. **Roadmap Slip** → Re-prioritize, cut scope
2. **Resource Conflict** → Trade-off matrix
3. **Priority Disagreement** → Data-driven RICE

---

**Master prioritization and create roadmaps that drive real outcomes!**
