---
name: discovery-interviews-surveys
description: Use when validating product assumptions before building, discovering unmet user needs, understanding customer problems and workflows, testing concepts or positioning, researching target markets, identifying jobs-to-be-done and hiring triggers, uncovering pain points and workarounds, or when users mention user research, customer interviews, surveys, discovery interviews, validation studies, or voice of customer.
---
# Discovery Interviews & Surveys

## Table of Contents
- [Purpose](#purpose)
- [When to Use](#when-to-use)
- [What Is It?](#what-is-it)
- [Workflow](#workflow)
- [Common Patterns](#common-patterns)
- [Guardrails](#guardrails)
- [Quick Reference](#quick-reference)

## Purpose

Discovery Interviews & Surveys help you learn from users systematically to:

- **Validate assumptions** before investing in building
- **Discover real problems** users experience (not just stated needs)
- **Understand jobs-to-be-done** (what users "hire" your product to do)
- **Identify pain points** and current workarounds
- **Test concepts** and positioning with target audience
- **Uncover unmet needs** that users may not articulate directly

This moves from guessing to evidence-based product decisions.

## When to Use

Use this skill when:

- **Pre-build validation**: Testing product ideas before development
- **Problem discovery**: Understanding user pain points and workflows
- **Jobs-to-be-done research**: Identifying hiring/firing triggers and desired outcomes
- **Market research**: Understanding target audience, competitive landscape, willingness to pay
- **Concept testing**: Validating positioning, messaging, feature prioritization
- **Post-launch learning**: Understanding adoption barriers, churn reasons, expansion opportunities
- **Customer satisfaction research**: Identifying satisfaction/dissatisfaction drivers
- **UX research**: Mental models, task flows, usability issues
- **Voice of customer**: Gathering qualitative insights for roadmap prioritization

Trigger phrases: "user research", "customer interviews", "surveys", "discovery", "validation study", "voice of customer", "jobs-to-be-done", "JTBD", "user needs"

## What Is It?

Discovery Interviews & Surveys provide structured approaches to learn from users while avoiding common biases (leading questions, confirmation bias, selection bias).

**Key components**:
1. **Interview guides**: Open-ended questions that reveal problems and context
2. **Survey instruments**: Scaled questions for quantitative validation at scale
3. **JTBD probes**: Questions focused on hiring/firing triggers and desired outcomes
4. **Bias-avoidance techniques**: Past behavior focus, "show me" requests, avoiding hypotheticals
5. **Analysis frameworks**: Thematic coding, affinity mapping, statistical analysis

**Quick example:**

**Bad interview question** (leading, hypothetical):
"Would you pay $49/month for a tool that automatically backs up your files?"

**Good interview approach** (behavior-focused, problem-discovery):
1. "Tell me about the last time you lost important files. What happened?"
2. "What have you tried to prevent data loss? How's that working?"
3. "Walk me through your current backup process. Show me if possible."
4. "What would need to change for you to invest time/money in better backup?"

**Result**: Learn about actual problems, current solutions, willingness to change—not hypothetical preferences.

## Workflow

Copy this checklist and track your progress:

```
Discovery Research Progress:
- [ ] Step 1: Define research objectives and hypotheses
- [ ] Step 2: Identify target participants
- [ ] Step 3: Choose research method (interviews, surveys, or both)
- [ ] Step 4: Design research instruments
- [ ] Step 5: Conduct research and collect data
- [ ] Step 6: Analyze findings and extract insights
```

**Step 1: Define research objectives**

Specify what you're trying to learn, key hypotheses to test, success criteria for research, and decision to be informed. See [Common Patterns](#common-patterns) for typical objectives.

**Step 2: Identify target participants**

Define participant criteria (demographics, behaviors, firmographics), sample size needed, recruitment strategy, and screening questions. For sampling strategies, see [resources/methodology.md](resources/methodology.md#participant-recruitment).

**Step 3: Choose research method**

Based on objective and constraints:
- **For deep problem discovery (5-15 participants)** → Use [resources/template.md](resources/template.md#interview-guide-template) for in-depth interviews
- **For concept testing at scale (50-200+ participants)** → Use [resources/template.md](resources/template.md#survey-template) for quantitative validation
- **For JTBD research** → Use [resources/methodology.md](resources/methodology.md#jobs-to-be-done-interviews) for switch interviews
- **For mixed methods** → Interviews for discovery, surveys for validation

**Step 4: Design research instruments**

Create interview guide or survey with bias-avoidance techniques. Use [resources/template.md](resources/template.md) for structure. Avoid leading questions, focus on past behavior, use "show me" requests. For advanced question design, see [resources/methodology.md](resources/methodology.md#question-design-principles).

**Step 5: Conduct research**

Execute interviews (record with permission, take notes) or distribute surveys (pilot test first). Use proper techniques (active listening, follow-up probes, silence for thinking). See [Guardrails](#guardrails) for critical requirements.

**Step 6: Analyze findings**

For interviews: thematic coding, affinity mapping, quote extraction. For surveys: statistical analysis, cross-tabs, open-end coding. Create insights document with evidence. Self-assess using [resources/evaluators/rubric_discovery_interviews_surveys.json](resources/evaluators/rubric_discovery_interviews_surveys.json). **Minimum standard**: Average score ≥ 3.5.

## Common Patterns

**Pattern 1: Problem Discovery Interviews**
- **Objective**: Understand user pain points and current workflows
- **Approach**: 8-12 in-depth interviews, open-ended questions, focus on past behavior and actual solutions
- **Key questions**: "Tell me about the last time...", "Walk me through...", "What have you tried?", "How's that working?"
- **Output**: Problem themes, frequency estimates, current workarounds, willingness to change
- **Example**: B2B SaaS discovery—interview potential customers about current tools and pain points

**Pattern 2: Jobs-to-be-Done Research**
- **Objective**: Identify why users "hire" products and what triggers switching
- **Approach**: Switch interviews with recent adopters or switchers, focus on timeline and context
- **Key questions**: "What prompted you to look?", "What alternatives did you consider?", "What almost stopped you?", "What's different now?"
- **Output**: Hiring triggers, firing triggers, desired outcomes, anxieties, habits
- **Example**: SaaS churn research—interview recent churners about switch to competitor

**Pattern 3: Concept Testing (Qualitative)**
- **Objective**: Test product concepts, positioning, or messaging before launch
- **Approach**: 10-15 interviews showing concept (mockup, landing page, description), gather reactions
- **Key questions**: "In your own words, what is this?", "Who is this for?", "What would you use it for?", "How much would you expect to pay?"
- **Output**: Comprehension score, perceived value, target audience clarity, pricing anchors
- **Example**: Pre-launch validation—test landing page messaging with target audience

**Pattern 4: Survey for Quantitative Validation**
- **Objective**: Validate findings from interviews at scale or prioritize features
- **Approach**: 100-500 participants, mix of scaled questions (Likert, ranking) and open-ends
- **Key questions**: Satisfaction scores (CSAT, NPS), feature importance/satisfaction (Kano), usage frequency, demographics
- **Output**: Statistical significance, segmentation, prioritization (importance vs satisfaction matrix)
- **Example**: Product roadmap prioritization—survey 500 users on feature importance

**Pattern 5: Continuous Discovery**
- **Objective**: Ongoing learning, not one-time project
- **Approach**: Weekly customer conversations (15-30 min), rotating team members, shared notes
- **Key questions**: Varies by current focus (new features, onboarding, expansion, retention)
- **Output**: Continuous insight feed, early problem detection, relationship building
- **Example**: Product team does 3-5 customer calls weekly, logs insights in shared doc

## Guardrails

**Critical requirements:**

1. **Avoid leading questions**: Don't telegraph the "right" answer. Bad: "Don't you think our UI is confusing?" Good: "Walk me through using this feature. What happened?"

2. **Focus on past behavior, not hypotheticals**: What people did reveals truth; what they say they'd do is often wrong. Bad: "Would you use this feature?" Good: "Tell me about the last time you needed to do X."

3. **Use "show me" not "tell me"**: Actual behavior > described behavior. Ask to screen-share, demonstrate current workflow, show artifacts (spreadsheets, tools).

4. **Recruit right participants**: Screen carefully. Wrong participants = wasted time. Define inclusion/exclusion criteria, use screening survey.

5. **Sample size appropriate for method**: Interviews: 5-15 for themes to emerge. Surveys: 100+ for statistical significance, 30+ per segment if comparing.

6. **Avoid confirmation bias**: Actively look for disconfirming evidence. If 9/10 interviews support hypothesis, focus heavily on the 1 that doesn't.

7. **Record and transcribe (with permission)**: Memory is unreliable. Record interviews, transcribe for analysis. Take notes as backup.

8. **Analyze systematically**: Don't cherry-pick quotes that support preferred conclusion. Use thematic coding, count themes, present contradictory evidence.

**Common pitfalls:**

- ❌ **Asking "would you" questions**: Hypotheticals are unreliable. Focus on "have you", "tell me about when", "show me"
- ❌ **Small sample statistical claims**: "80% of users want feature X" from 5 interviews is not valid. Interviews = themes, surveys = statistics
- ❌ **Selection bias**: Interviewing only enthusiasts or only detractors skews results. Recruit diverse sample
- ❌ **Ignoring non-verbal cues**: Hesitation, confusion, workarounds during "show me" reveal truth beyond words
- ❌ **Stopping at surface answers**: First answer is often rationalization. Follow up: "Tell me more", "Why did that matter?", "What else?"

## Quick Reference

**Key resources:**

- **[resources/template.md](resources/template.md)**: Interview guide template, survey template, JTBD question bank, screening questions
- **[resources/methodology.md](resources/methodology.md)**: Advanced techniques (JTBD switch interviews, Kano analysis, thematic coding, statistical analysis, continuous discovery)
- **[resources/evaluators/rubric_discovery_interviews_surveys.json](resources/evaluators/rubric_discovery_interviews_surveys.json)**: Quality criteria for research design and execution

**Typical workflow time:**

- Interview guide design: 1-2 hours
- Conducting 10 interviews: 10-15 hours (including scheduling)
- Analysis and synthesis: 4-8 hours
- Survey design: 2-4 hours
- Survey distribution and collection: 1-2 weeks
- Survey analysis: 2-4 hours

**When to escalate:**

- Large-scale quantitative studies (1000+ participants)
- Statistical modeling or advanced segmentation
- Longitudinal studies (tracking over time)
- Ethnographic research (observing in natural setting)
→ Use [resources/methodology.md](resources/methodology.md) or consider specialist researcher

**Inputs required:**

- **Research objective**: What you're trying to learn
- **Hypotheses** (optional): Specific beliefs to test
- **Target persona**: Who to interview/survey
- **Job-to-be-done** (optional): Specific JTBD focus

**Outputs produced:**

- `discovery-interviews-surveys.md`: Complete research plan with interview guide or survey, recruitment criteria, analysis plan, and insights template
