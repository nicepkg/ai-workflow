<div align="center">

# 📋 Product Manager Workflow

### **Your AI-Powered Product Team**

[← Back to AI Workflow](../README.md)

[简体中文](./README_cn.md) | English

</div>

---

## 🎯 Who Is This For?

- **Product Managers** - Full product lifecycle management
- **Product Owners** - Agile delivery and backlog management
- **Head of Product / VP** - Strategy and portfolio planning
- **Technical Program Managers** - Cross-functional execution

---

## ⚡ Quick Install

```bash
# Install all 23 skills with one command
npx add-skill nicepkg/ai-workflow/product-manager-workflow

# Or install specific skills
npx add-skill nicepkg/ai-workflow/product-manager-workflow --skill prd-generator
```

---

## 📦 Skills Included (23)

### 0️⃣ Intake & Triage
| Skill | What It Does |
|:------|:-------------|
| `work-intake` | Convert any request into trackable work items with scope, goals, constraints |

### 1️⃣ Discovery & Research
| Skill | What It Does |
|:------|:-------------|
| `user-research` | User interviews, surveys, problem validation methods |
| `discovery-interviews-surveys` | Discovery phase interview and survey design |
| `customer-feedback-analyzer` | Multi-channel feedback analysis → pattern extraction → prioritization |
| `user-persona-creation` | Create detailed user personas based on research |
| `competitive-analysis` | Market and competitor analysis framework |

### 2️⃣ Definition & Specification
| Skill | What It Does |
|:------|:-------------|
| `prd-generator` | Generate structured PRDs with industry-standard format |
| `writing-product-specs` | Feature specs with context, requirements, success metrics, boundaries |
| `requirements` | Requirements gathering, acceptance criteria, scope control |
| `writing-user-stories` | Standard format user stories with acceptance criteria |

### 3️⃣ Prioritization & Planning
| Skill | What It Does |
|:------|:-------------|
| `prioritization-effort-impact` | Effort-Impact 2x2 matrix for quick prioritization (quick wins / big bets) |
| `roadmap` | Roadmap planning with timeline and resource allocation |
| `roadmap-backcast` | Backcast planning from target outcomes to milestones |
| `strategy` | Product strategy, OKRs, vision alignment |
| `stakeholders-org-design` | Stakeholder mapping and organizational alignment |

### 4️⃣ Delivery & Execution
| Skill | What It Does |
|:------|:-------------|
| `feature-planning` | Implementation plans with tasks, dependencies, validation steps |
| `agile` | Agile methodology, sprint planning, velocity tracking |
| `agile-sprint-planning` | Sprint planning with story points and capacity |

### 5️⃣ Launch & Release
| Skill | What It Does |
|:------|:-------------|
| `launch` | Product launch coordination and checklist |
| `technical-launch-planner` | Technical launch planning: timeline, assets, GA/beta checklist |

### 6️⃣ Metrics & Review
| Skill | What It Does |
|:------|:-------------|
| `analytics` | Product analytics, KPIs, data-driven decisions |
| `forecast-premortem` | Pre-launch risk analysis and mitigation planning |
| `postmortem` | Post-launch review and lessons learned |

---

## 🔄 Complete PM Pipeline (7 Stages)

```
Stage 0: Intake
└── work-intake → Structure any request into trackable work items

Stage 1: Discovery
├── user-research → Plan and conduct user interviews
├── discovery-interviews-surveys → Design interview guides and surveys
├── customer-feedback-analyzer → Analyze existing feedback data
├── user-persona-creation → Synthesize findings into personas
└── competitive-analysis → Understand market landscape

Stage 2: Definition
├── prd-generator → Create comprehensive PRDs
├── writing-product-specs → Write detailed feature specs
├── requirements → Define acceptance criteria
└── writing-user-stories → Break down into user stories

Stage 3: Prioritization
├── prioritization-effort-impact → Quick wins vs big bets analysis
├── roadmap → Timeline and resource planning
├── roadmap-backcast → Work backwards from goals
├── strategy → OKR alignment and vision
└── stakeholders-org-design → Stakeholder buy-in

Stage 4: Delivery
├── feature-planning → Implementation planning
├── agile → Sprint methodology
└── agile-sprint-planning → Capacity planning

Stage 5: Launch
├── forecast-premortem → Pre-launch risk analysis
├── technical-launch-planner → Technical checklist
└── launch → Launch coordination

Stage 6: Review
├── analytics → Metrics tracking
└── postmortem → Lessons learned
```

---

## 💡 Example Workflows

### New Product Initiative
```
1. "I have a new feature request for user data export, run work-intake"
2. "Plan user research to validate this need"
3. "Analyze customer feedback about data export"
4. "Generate a PRD for the data export feature"
5. "Prioritize against current backlog using effort-impact"
6. "Create implementation plan"
```

### Quarterly Planning
```
1. "Review our product strategy and OKRs"
2. "Analyze competitor landscape"
3. "Prioritize Q2 initiatives using effort-impact matrix"
4. "Create quarterly roadmap with milestones"
5. "Get stakeholder alignment on roadmap"
```

### Sprint Kickoff
```
1. "Break this epic into user stories with acceptance criteria"
2. "Plan sprint capacity and velocity"
3. "Create implementation plan for top stories"
```

### Product Launch
```
1. "Run premortem analysis for launch risks"
2. "Create technical launch checklist"
3. "Coordinate launch activities"
4. "Set up analytics tracking for success metrics"
```

### Post-Launch Review
```
1. "Analyze launch metrics vs success criteria"
2. "Run postmortem on the launch"
3. "Extract lessons learned and action items"
```

### Backlog Grooming
```
1. "Review and prioritize feature requests"
2. "Write user stories for top items"
3. "Define acceptance criteria"
4. "Estimate effort for sprint planning"
```

---

## 🔗 Skill Combinations

| Goal | Skill Chain |
|:-----|:------------|
| **New Feature** | work-intake → user-research → prd-generator → prioritization-effort-impact → feature-planning |
| **Quarterly Planning** | strategy → competitive-analysis → roadmap-backcast → roadmap → stakeholders-org-design |
| **Sprint Planning** | writing-user-stories → requirements → agile-sprint-planning |
| **Product Launch** | forecast-premortem → technical-launch-planner → launch → analytics |
| **Discovery** | user-research → customer-feedback-analyzer → user-persona-creation |
| **Documentation** | prd-generator → writing-product-specs → writing-user-stories → requirements |
| **Weekly Review** | analytics → postmortem → prioritization-effort-impact |

---

## 📄 License

MIT © [nicepkg](https://github.com/nicepkg)

<div align="center">

**[⬆ Back to Main Project](../README.md)**

</div>
