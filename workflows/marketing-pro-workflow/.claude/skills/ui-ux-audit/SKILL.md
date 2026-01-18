---
name: ui-ux-audit
description: Mandatory audit workflow for UI/UX changes that reads current state FIRST, checks for redundancy, respects clean design philosophy, and identifies genuine gaps before implementation. Auto-invoked when user mentions UI, UX, design, layout, homepage, page improvements, visual changes, or interface modifications.
---

<!--
Created by: Madina Gbotoe (https://madinagbotoe.com/)
Project: Claude Code Skills - Professional Development Toolkit
Version: 1.0
Created: October 28, 2025
Last Updated: October 29, 2025
License: MIT License
Attribution Required: Yes - Include author name and link when sharing/modifying
GitHub: https://github.com/mgbotoe/claude-code-share
Find latest version: https://github.com/mgbotoe/claude-code-share/tree/main/claude-code-skills/ui-ux-audit

Purpose: UI/UX Audit skill - Prevents redundant implementations by auditing current state before UI/UX changes
-->

# UI/UX Audit Skill

## 🚨 CRITICAL: This Skill Runs BEFORE Implementation

**Purpose:** Prevent redundant implementations and cluttered designs by auditing current state FIRST.

**When to invoke:** Automatically when user mentions:
- UI/UX work: "improve UI", "enhance UX", "better design", "update layout"
- Page work: "fix homepage", "improve page", "update interface", "redesign"
- Visual changes: "add visual elements", "enhance visuals", "improve appearance"
- Component work: "add component", "new feature", "improve section"
- General improvements: "make it better", "improve experience", "enhance site"

**Order of execution:**
1. ✅ This skill runs FIRST (audit phase)
2. Then present findings to user
3. Then optionally invoke ui-ux-designer agent (design critique)
4. Then implement approved changes

---

## Mandatory Audit Process (READ FIRST, IMPLEMENT SECOND)

### Step 1: Read Current State (Non-Negotiable)

**Before making ANY recommendations, read these files:**

```bash
# Target page file
Read: src/app/[target-page]/page.tsx

# Related components (if modifying existing sections)
Read: src/components/sections/[component].tsx

# Related data files
Read: src/data/[related-data].tsx
Read: src/data/page-content/[page]-content.ts

# Check for existing similar functionality
Grep: Search for keywords related to proposed feature
```

**Example:**
```markdown
User: "Improve homepage"

MUST READ FIRST:
- src/app/page.tsx
- src/components/sections/Hero.tsx
- src/data/page-content/home-content.ts

THEN analyze what EXISTS before proposing anything
```

### Step 2: Document What EXISTS (Evidence-Based)

**Create inventory of current state:**

```markdown
## Current State Audit: [Page Name]

### Existing Components
- Component 1: [Description, location, purpose]
- Component 2: [Description, location, purpose]

### Existing Data Display
- Portfolio metrics: [Where shown, format]
- CTAs: [Location, text, purpose]
- Content sections: [List all sections]

### Design Characteristics
- Layout: [Grid, flex, columns]
- White space: [Generous, tight, balanced]
- Information density: [Minimal, moderate, dense]
- Visual style: [Clean, busy, colorful, minimal]

### Evidence
[Show actual code snippets proving what exists]
```

### Step 3: Redundancy Check (Critical)

**Before proposing ANY addition, verify:**

- [ ] Is this data already displayed elsewhere on the page?
- [ ] Does similar functionality exist in different form?
- [ ] Would this duplicate existing content?
- [ ] Would this clutter a clean design?
- [ ] Is information shown more than once?

**Anti-Patterns to Avoid (from October 2025 lessons):**

❌ **Portfolio Visualization** when impact cards already show portfolio breakdown
❌ **Large AI Assistant card** when primary CTAs already exist in hero
❌ **Metric sidebars** on document-style pages (like /brief)
❌ **Dashboards** on intentionally minimal pages (like /ai-lab)
❌ **Duplicate data displays** in multiple sections
❌ **Bulk additions** without clear value proposition

### Step 4: Identify GENUINE Gaps (Not Assumed Gaps)

**Only propose additions for:**

✅ **Missing functionality** (proven by code audit)
✅ **Genuine UX problems** (demonstrated, not assumed)
✅ **Clear value add** (specific benefit articulated)
✅ **Respects clean design** (doesn't add bulk)

**Template:**
```markdown
## Genuine Gaps Identified

### Gap 1: [Specific missing element]
- Evidence: [Code shows this doesn't exist]
- User need: [Why user needs this]
- Value: [Specific benefit]
- Simple solution: [Minimal approach]
- No redundancy: [Confirmed doesn't duplicate X]

### Gap 2: [Next gap]
...
```

### Step 5: Design Philosophy Check

**This portfolio has a CLEAN, MINIMAL aesthetic by design:**

Check against these principles:
- [ ] Simple, scannable layouts
- [ ] Strategic use of white space
- [ ] Information shown ONCE, not repeated
- [ ] Document-style pages stay document-like
- [ ] No bulk additions without clear need

**Questions to ask:**
- Does this ADD value or just ADD BULK?
- Is this the SIMPLEST solution?
- Does this respect the existing clean design?
- Would this survive user review or get reverted?

---

## Audit Output Template

**Present findings in this format:**

```markdown
# UI/UX Audit Report: [Page Name]

## Current State Summary
[2-3 sentences describing current design]

## What Already EXISTS
1. [Component/feature]: [Description with code location]
2. [Component/feature]: [Description with code location]
3. [Component/feature]: [Description with code location]

Evidence: [Code snippets proving these exist]

## Redundancy Check Results
✅ No redundancy detected: [Explain]
OR
⚠️ Potential redundancy: [Show what duplicates what]

## Genuine Gaps Identified
### Priority 1: [Most important gap]
- Evidence: [Why this is missing]
- User impact: [Specific problem it solves]
- Proposed solution: [Minimal approach]
- No redundancy: [Confirmed]

### Priority 2: [Next gap]
...

## NOT Recommended (Would Create Redundancy)
❌ [Proposed feature]: Already exists as [existing feature]
❌ [Proposed feature]: Would duplicate [existing data]

## Design Philosophy Compliance
✅ Respects clean, minimal aesthetic
✅ Adds value without adding bulk
✅ No information duplication
OR
⚠️ Concerns: [List any design philosophy violations]

## Recommendation
**Recommended:** Implement Priority 1 gap ([brief description])
**Not Recommended:** [List features that would add redundancy]

**Next Steps:**
1. User review of findings
2. (Optional) Invoke ui-ux-designer agent for design critique
3. Implement approved changes incrementally
```

---

## Verification Checklist

**Before completing audit, verify:**

- [ ] Did I read all target page/component files FIRST?
- [ ] Did I document what EXISTS (not what I assume is missing)?
- [ ] Did I check for redundancy systematically?
- [ ] Did I identify GENUINE gaps (not assumed gaps)?
- [ ] Did I verify no information duplication?
- [ ] Does recommendation respect clean, minimal design?
- [ ] Did I propose SIMPLEST solution?
- [ ] Would this survive user review?

**If any answer is NO, STOP and reassess.**

---

## Example: Good vs. Bad Audit

### ❌ BAD Audit (What NOT to do)

```markdown
User: "Improve homepage"

Bad Response:
"I recommend adding:
1. Portfolio visualization showing $156M breakdown
2. Large dashboard with metrics
3. Section transitions between content
4. Enhanced testimonials with animations"

Problem: Didn't read current state, didn't check for redundancy
```

### ✅ GOOD Audit (What TO do)

```markdown
User: "Improve homepage"

Good Response:
"Let me audit the current homepage first..."

[Reads src/app/page.tsx]

"Current State Audit:

What EXISTS:
- Impact cards already display portfolio breakdown ($156M, $91M, etc.)
- Hero has primary CTAs (View Work, See Skills, Get In Touch)
- Testimonials section exists
- EKG dividers separate sections

Redundancy Check:
⚠️ Adding portfolio visualization would DUPLICATE impact card data

GENUINE Gap:
✅ No CTA after testimonials section (natural conversion point)

Recommendation:
- Add single strategic CTA after testimonials
- Do NOT add portfolio visualization (redundant)
- Keep clean, minimal design

Would you like to proceed with the CTA addition?"
```

---

## Integration with CLAUDE.md Rules

This skill enforces the mandatory rules from CLAUDE.md:

1. ✅ READ FIRST, IMPLEMENT SECOND (enforced by Step 1)
2. ✅ REDUNDANCY CHECK (enforced by Step 3)
3. ✅ RESPECT DESIGN PHILOSOPHY (enforced by Step 5)
4. ✅ MANDATORY AUDIT BEFORE UI/UX WORK (this entire skill)
5. ✅ VERIFICATION CHECKLIST (enforced by final checklist)

---

## Trigger Keywords Reference

**Auto-invoke this skill when user says:**

**UI/UX Terms:**
- improve UI, enhance UX, better design, update layout
- improve user experience, enhance interface, better visuals
- redesign, refactor UI, update design, modernize
- make it look better, improve appearance, visual improvements

**Page Terms:**
- fix homepage, improve page, update page, enhance page
- homepage improvements, page redesign, layout changes
- improve landing page, better home screen

**Component Terms:**
- add component, new feature, improve section
- enhance hero, update header, improve footer
- add visualization, add dashboard, add metrics
- new UI element, add interface component

**General Improvement:**
- make it better, improve experience, enhance site
- improve portfolio, better showcase, enhance presentation
- improve conversion, better engagement, increase impact

**Question Form:**
- "How can I improve X?"
- "What should I add to X?"
- "Should I add X to the page?"

---

## Remember: This Skill Prevents the October 2025 Session Mistakes

**What went wrong that day:**
- Implemented Phase 3 UI/UX recommendations without reading pages
- Added PortfolioVisualization despite impact cards showing same data
- Added large AI Assistant card overshadowing primary CTAs
- Added bulk to AI Lab page making it "look like two pages in one"
- User had to revert everything

**This skill prevents those mistakes by:**
- Reading current state FIRST (always)
- Checking for redundancy BEFORE proposing
- Respecting clean, minimal design philosophy
- Identifying genuine gaps (not assumed gaps)
- Presenting evidence-based findings to user BEFORE implementing

---

## Supporting Files & Resources

This skill includes additional resources for comprehensive audits:

### REFERENCE.md - Detailed UX Research
**When to read:**
- Need detailed WCAG 2.1 AA requirements
- Want UX research citations (Nielsen Norman Group, etc.)
- Understanding design patterns and anti-patterns
- Deep dive into audit methodology

**Contains:**
- Left-attention pattern research (80/20 rule)
- F-pattern reading principles
- Cognitive load principles (Miller's Law, Hick's Law)
- Complete WCAG 2.1 AA requirements
- Design pattern library
- Measurement frameworks

**Read with:** `Read: [skill-directory]/REFERENCE.md`

---

### FORMS.md - Pre-Filled Templates
**When to read:**
- Starting a new audit (copy template)
- Need structured checklist format
- Want standardized audit output

**Contains:**
- Quick Audit Template (5-10 min)
- Comprehensive Audit Template (30+ min)
- Redundancy Checklist
- Gap Analysis Template
- WCAG Compliance Checklist
- Mobile Optimization Checklist
- Performance Audit Template

**Read with:** `Read: [skill-directory]/FORMS.md`

---

### resources/ - Examples & Case Studies
**When to read:**
- First-time conducting UI/UX audit
- Unsure if approach is correct
- Learning from real examples
- Training others

**Contains:**
- `examples/good-audit-example.md` - Gold standard audit
- `examples/bad-audit-example.md` - What NOT to do
- `case-studies/october-2025-incident.md` - Real incident that inspired this skill
- `README.md` - Navigation guide

**Read with:** `Read: [skill-directory]/resources/[filename]`

---

## Usage Guide for Supporting Files

### Quick Audit (< 10 minutes):
1. Use **SKILL.md** (this file) for process
2. Copy template from **FORMS.md** (Quick Audit Template)
3. Follow 5 steps, fill in template

### Comprehensive Audit (30+ minutes):
1. Use **SKILL.md** for overall process
2. Copy template from **FORMS.md** (Comprehensive Audit Template)
3. Reference **REFERENCE.md** for detailed requirements
4. Compare your work to **resources/examples/good-audit-example.md**

### Learning/Training:
1. Read **resources/examples/good-audit-example.md** (see gold standard)
2. Read **resources/examples/bad-audit-example.md** (learn what to avoid)
3. Read **resources/case-studies/october-2025-incident.md** (understand why this skill exists)
4. Practice using **FORMS.md** templates

---

## Final Note

**This is not optional.** When user mentions UI/UX work, this skill MUST run first to audit current state before any implementation begins.

The goal: Prevent redundant implementations, respect existing design, propose targeted improvements only.

**New to UI/UX audits?** Start with `resources/examples/good-audit-example.md` to see the process in action.
