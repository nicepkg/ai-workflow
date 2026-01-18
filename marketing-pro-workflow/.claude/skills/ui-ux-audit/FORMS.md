# UI/UX Audit Templates and Forms

**Purpose:** Pre-filled templates for conducting UI/UX audits. Copy the appropriate template and fill in the details.

---

## Table of Contents

1. [Quick Audit Template](#quick-audit-template) (5-10 minutes)
2. [Comprehensive Audit Template](#comprehensive-audit-template) (30+ minutes)
3. [Redundancy Checklist](#redundancy-checklist)
4. [Gap Analysis Template](#gap-analysis-template)
5. [WCAG Compliance Checklist](#wcag-compliance-checklist)
6. [Mobile Optimization Checklist](#mobile-optimization-checklist)
7. [Performance Audit Template](#performance-audit-template)

---

## Quick Audit Template

**Use when:** Need fast assessment (< 10 minutes)

**Template:**

```markdown
# Quick UI/UX Audit: [Page Name]

**Date:** [Date]
**Auditor:** Claude
**Estimated Time:** 5-10 minutes

---

## Current State (What EXISTS)

### Components Present:
- [ ] Component 1: [Name] - [Purpose]
- [ ] Component 2: [Name] - [Purpose]
- [ ] Component 3: [Name] - [Purpose]

### Key Features:
- [ ] Feature 1: [Description]
- [ ] Feature 2: [Description]

### CTAs Present:
- [ ] CTA 1: "[Text]" - [Location]
- [ ] CTA 2: "[Text]" - [Location]

---

## Quick Redundancy Check

- [ ] No duplicate data displays detected
- [ ] Each metric shown once
- [ ] CTAs not repeated unnecessarily
- [ ] Content sections distinct

**Redundancy Found:**
[List any redundant elements]

---

## Top 3 Gaps Identified

1. **[Gap Name]**
   - Impact: [High/Medium/Low]
   - Quick Fix: [Yes/No]

2. **[Gap Name]**
   - Impact: [High/Medium/Low]
   - Quick Fix: [Yes/No]

3. **[Gap Name]**
   - Impact: [High/Medium/Low]
   - Quick Fix: [Yes/No]

---

## Recommendation

**Priority Action:** [What to do first]

**Avoid:** [What NOT to add]

**Next Steps:** [User action required]
```

---

## Comprehensive Audit Template

**Use when:** Need thorough assessment (30+ minutes)

**Template:**

```markdown
# Comprehensive UI/UX Audit: [Page Name]

**Date:** [Date]
**Auditor:** Claude
**Page URL/Path:** [Path]
**Estimated Time:** 30-45 minutes

---

## 1. Executive Summary

### Current State:
[2-3 sentence overview of page current state]

### Overall Assessment:
- Design Quality: [Excellent/Good/Needs Improvement/Poor]
- User Experience: [Excellent/Good/Needs Improvement/Poor]
- Accessibility: [WCAG AA Compliant/Partial/Non-Compliant]
- Performance: [Fast/Moderate/Slow]

### Key Finding:
[Most important discovery from audit]

---

## 2. What EXISTS (Evidence-Based Inventory)

### 2.1 Components and Sections

**Component 1: [Name]**
- Location: [File path:line number]
- Purpose: [What it does]
- Data displayed: [List data points]
- CTAs present: [List CTAs]
- Status: [Working/Broken/Needs improvement]

**Component 2: [Name]**
- Location: [File path:line number]
- Purpose: [What it does]
- Data displayed: [List data points]
- CTAs present: [List CTAs]
- Status: [Working/Broken/Needs improvement]

[Continue for all components...]

### 2.2 Data Points Displayed

| Data Point | Location(s) | Format | Redundant? |
|------------|-------------|--------|------------|
| [Data 1] | [Component] | [Text/Chart/Icon] | [Yes/No] |
| [Data 2] | [Component] | [Text/Chart/Icon] | [Yes/No] |

### 2.3 Call-to-Actions (CTAs)

| CTA Text | Location | Type | Prominence |
|----------|----------|------|------------|
| "[CTA 1]" | [Section] | [Primary/Secondary] | [High/Medium/Low] |
| "[CTA 2]" | [Section] | [Primary/Secondary] | [High/Medium/Low] |

### 2.4 Design Characteristics

**Layout:**
- Structure: [Grid/Flex/Single-column]
- Columns: [Number]
- Max-width: [Value]
- Responsive: [Yes/No/Partial]

**Whitespace:**
- Density: [Generous/Moderate/Tight]
- Section spacing: [Appropriate/Too much/Too little]
- Content breathing room: [Yes/No]

**Visual Style:**
- Aesthetic: [Minimal/Modern/Traditional/Busy]
- Color palette: [Limited/Moderate/Extensive]
- Typography: [1-2/3-4/5+ font sizes]
- Consistency: [High/Medium/Low]

**Information Hierarchy:**
- Scanability: [Excellent/Good/Poor]
- Visual flow: [Clear/Confusing]
- Priority clarity: [Obvious/Unclear]

---

## 3. Redundancy Analysis

### 3.1 Duplicate Data Displays

**Finding 1:**
- Data point: [What's duplicated]
- Location 1: [Where]
- Location 2: [Where]
- Severity: [High/Medium/Low]
- Recommendation: [Keep one, remove other]

**Finding 2:**
[Continue pattern...]

### 3.2 Redundancy Checklist

- [ ] No data shown in multiple formats
- [ ] No repeated CTAs
- [ ] No duplicate content sections
- [ ] Each metric displayed once
- [ ] No overlapping functionality

**Summary:**
- Total redundancies found: [Number]
- High severity: [Number]
- Medium severity: [Number]
- Low severity: [Number]

---

## 4. Gap Analysis

### 4.1 Missing Functionality

**Gap 1: [Name]**
- **Evidence:** [Code shows this doesn't exist - cite file/line]
- **User need:** [Why users need this]
- **Impact:** [High/Medium/Low]
- **Proposed solution:** [Minimal approach]
- **Effort:** [Low/Medium/High]
- **Redundancy check:** ✅ Confirmed doesn't duplicate [X]

**Gap 2: [Name]**
[Continue pattern...]

### 4.2 UX Issues

**Issue 1: [Description]**
- **Severity:** [Critical/High/Medium/Low]
- **User impact:** [How it affects users]
- **Suggested fix:** [Specific solution]
- **Effort:** [Low/Medium/High]

**Issue 2: [Description]**
[Continue pattern...]

### 4.3 Accessibility Gaps

**Gap 1: [WCAG Criterion]**
- **Criterion:** [e.g., 1.4.3 Contrast (Minimum)]
- **Current state:** [What fails]
- **Required fix:** [What needs to change]
- **Priority:** [Critical/High/Medium]

**Gap 2: [WCAG Criterion]**
[Continue pattern...]

---

## 5. Design Philosophy Compliance

### Clean, Minimal Design Check:

- [ ] Simple, scannable layouts
- [ ] Strategic use of whitespace
- [ ] Information shown ONCE, not repeated
- [ ] Document-style pages stay document-like
- [ ] No bulk additions without clear need

**Violations Found:**
[List any violations of design philosophy]

**Compliance Score:** [X/5 principles met]

---

## 6. Prioritized Recommendations

### P0 - Critical (Fix Immediately)
1. **[Recommendation]**
   - Why: [Justification]
   - Impact: [Expected outcome]
   - Effort: [Hours/days]

### P1 - High Priority (This Sprint)
1. **[Recommendation]**
   - Why: [Justification]
   - Impact: [Expected outcome]
   - Effort: [Hours/days]

### P2 - Medium Priority (Next Sprint)
1. **[Recommendation]**
   - Why: [Justification]
   - Impact: [Expected outcome]
   - Effort: [Hours/days]

### P3 - Low Priority (Backlog)
1. **[Recommendation]**
   - Why: [Justification]
   - Impact: [Expected outcome]
   - Effort: [Hours/days]

---

## 7. What NOT to Implement (Redundancy Prevention)

❌ **[Feature/Component]**
- Reason: Already exists as [existing feature]
- Would duplicate: [What it duplicates]

❌ **[Feature/Component]**
- Reason: Would clutter clean design
- Alternative: [Better approach]

---

## 8. Expected Impact

### If P0-P1 Recommendations Implemented:

**User Experience:**
- [Expected improvement 1]
- [Expected improvement 2]

**Accessibility:**
- [Expected improvement]

**Business Metrics:**
- [Expected change in conversion/engagement]

**Technical:**
- [Performance impact]
- [Maintenance impact]

---

## 9. Next Steps

1. **User Review:** [What user should review/approve]
2. **Design Critique:** [Should ui-ux-designer agent review?]
3. **Implementation:** [Which recommendations to start with]
4. **Testing:** [What to test after changes]

---

## 10. Appendix

### Evidence (Code Snippets):
```tsx
// [Component/file name]
// Lines [X-Y]
[Relevant code snippet]
```

### Screenshots:
[If applicable, note where screenshots were taken]

---

**Audit Completed:** [Date/Time]
**Total Time Spent:** [Minutes]
**Follow-up Required:** [Yes/No - what needs follow-up]
```

---

## Redundancy Checklist

**Use when:** Specifically checking for duplicate content

**Template:**

```markdown
# Redundancy Checklist: [Page Name]

**Date:** [Date]

---

## Data Point Inventory

List all data points displayed on the page:

1. **[Data Point 1]** (e.g., Portfolio Value)
   - Location 1: [Component/section]
   - Location 2: [Component/section] (if shown multiple times)
   - Location 3: [Component/section] (if shown multiple times)
   - Format: [Text/Chart/Icon/Card]
   - Redundant: [Yes/No]

2. **[Data Point 2]**
   [Continue pattern...]

---

## CTA Inventory

List all CTAs on the page:

1. **"[CTA Text 1]"**
   - Location 1: [Section]
   - Location 2: [Section] (if repeated)
   - Purpose: [What it does]
   - Redundant: [Yes/No]

2. **"[CTA Text 2]"**
   [Continue pattern...]

---

## Redundancy Detection

### High Severity (Identical Content)
- [ ] [Data point] shown identically in [location 1] and [location 2]
- [ ] [CTA] repeated in [location 1] and [location 2]

### Medium Severity (Similar Content)
- [ ] [Data point] shown in different formats (text + chart)
- [ ] [Information] paraphrased in multiple sections

### Low Severity (Related Content)
- [ ] [Topic] referenced in multiple contexts (acceptable)

---

## Redundancy Summary

**Total redundancies:** [Number]
- High: [Number] - Remove immediately
- Medium: [Number] - Consider consolidating
- Low: [Number] - Acceptable

**Recommendation:**
[What to keep, what to remove]
```

---

## Gap Analysis Template

**Use when:** Identifying missing features/content

**Template:**

```markdown
# Gap Analysis: [Page Name]

**Date:** [Date]

---

## Methodology

1. ✅ Read all target files
2. ✅ Documented what exists
3. ✅ Compared against best practices
4. ✅ Identified missing elements

---

## Gap Categories

### 1. Functionality Gaps

**Gap: [Missing Feature]**
- **Evidence:** [File checked, feature not found]
- **User need:** [Why needed]
- **Priority:** [Critical/High/Medium/Low]
- **Effort:** [Hours/days estimate]
- **Proposed solution:** [Minimal approach]
- **Not redundant:** ✅ Confirmed doesn't duplicate [X]

[Repeat for each gap...]

---

### 2. Content Gaps

**Gap: [Missing Content]**
- **Evidence:** [What's missing]
- **User need:** [Why needed]
- **Priority:** [Critical/High/Medium/Low]
- **Proposed solution:** [What to add]

[Repeat for each gap...]

---

### 3. UX Gaps

**Gap: [UX Issue]**
- **Current problem:** [What's broken/missing]
- **User impact:** [How it affects users]
- **Priority:** [Critical/High/Medium/Low]
- **Proposed fix:** [Solution]

[Repeat for each gap...]

---

### 4. Accessibility Gaps

**Gap: [WCAG Issue]**
- **WCAG Criterion:** [Number and name]
- **Current failure:** [What doesn't comply]
- **Priority:** [Critical/High/Medium]
- **Required fix:** [Solution]

[Repeat for each gap...]

---

## Genuine Gaps (Verified)

Total gaps identified: [Number]
- Critical: [Number]
- High: [Number]
- Medium: [Number]
- Low: [Number]

**Top 3 Priorities:**
1. [Gap name] - [Why it's priority 1]
2. [Gap name] - [Why it's priority 2]
3. [Gap name] - [Why it's priority 3]

---

## NOT Gaps (Already Exists)

❌ [Assumed gap] - Actually exists as [existing feature]
❌ [Assumed gap] - Already covered by [existing content]

---

## Recommendation

**Implement:** [Top priority gaps]
**Don't implement:** [What would be redundant]
**Consider for future:** [Lower priority gaps]
```

---

## WCAG Compliance Checklist

**Use when:** Checking accessibility compliance

**Template:**

```markdown
# WCAG 2.1 AA Compliance Checklist: [Page Name]

**Date:** [Date]

---

## 1. Perceivable

### 1.1 Text Alternatives
- [ ] All images have alt text
- [ ] Decorative images have empty alt ("")
- [ ] Icon buttons have aria-label

### 1.2 Time-based Media
- [ ] Video has captions (if applicable)
- [ ] Audio has transcripts (if applicable)

### 1.3 Adaptable
- [ ] Semantic HTML used (nav, main, article, etc.)
- [ ] Heading hierarchy logical (h1 → h2 → h3)
- [ ] Form labels properly associated

### 1.4 Distinguishable
- [ ] Text contrast ≥ 4.5:1 (normal text)
- [ ] Text contrast ≥ 3:1 (large text 18pt+)
- [ ] Interactive elements contrast ≥ 3:1
- [ ] Text resizable to 200% without loss
- [ ] No images of text (except logos)

**Violations Found:**
[List any 1.x violations]

---

## 2. Operable

### 2.1 Keyboard Accessible
- [ ] All functionality keyboard accessible
- [ ] No keyboard traps
- [ ] Skip links provided
- [ ] Logical tab order

### 2.2 Enough Time
- [ ] No time limits (or user can extend)
- [ ] Auto-updating content can be paused

### 2.3 Seizures and Physical Reactions
- [ ] No flashing content (or < 3 flashes/second)

### 2.4 Navigable
- [ ] Page title descriptive
- [ ] Focus order logical
- [ ] Link purpose clear
- [ ] Multiple navigation methods
- [ ] Headings and labels descriptive
- [ ] Focus visible

### 2.5 Input Modalities
- [ ] Pointer gestures have alternatives
- [ ] No motion-based activation required
- [ ] Touch targets ≥ 44x44px
- [ ] Label in name matches accessible name

**Violations Found:**
[List any 2.x violations]

---

## 3. Understandable

### 3.1 Readable
- [ ] Page language identified
- [ ] Language changes marked

### 3.2 Predictable
- [ ] Focus doesn't change context unexpectedly
- [ ] Input doesn't change context unexpectedly
- [ ] Navigation consistent across pages
- [ ] Components identified consistently

### 3.3 Input Assistance
- [ ] Error messages descriptive
- [ ] Labels or instructions for inputs
- [ ] Error prevention (confirmation for important actions)

**Violations Found:**
[List any 3.x violations]

---

## 4. Robust

### 4.1 Compatible
- [ ] Valid HTML (no parsing errors)
- [ ] Name, role, value for all UI components
- [ ] Status messages use aria-live

**Violations Found:**
[List any 4.x violations]

---

## Summary

**Total Violations:** [Number]
- Critical (blocks access): [Number]
- High (significant barrier): [Number]
- Medium (moderate barrier): [Number]
- Low (minor issue): [Number]

**Compliance Level:** [WCAG AA Compliant / Partial / Non-Compliant]

**Priority Fixes:**
1. [Top issue]
2. [Second issue]
3. [Third issue]
```

---

## Mobile Optimization Checklist

**Use when:** Checking mobile experience

**Template:**

```markdown
# Mobile Optimization Checklist: [Page Name]

**Date:** [Date]
**Tested on:** [Device/browser]

---

## Viewport and Responsive Design

- [ ] Viewport meta tag present
- [ ] Content fits within viewport (no horizontal scroll)
- [ ] Text readable without zooming (≥ 16px)
- [ ] Images scale appropriately
- [ ] Layout adapts to screen size

**Issues Found:**
[List responsive design issues]

---

## Touch Targets

- [ ] All buttons ≥ 44x44px
- [ ] Links spaced adequately (no accidental taps)
- [ ] Form inputs large enough to tap
- [ ] Spacing between interactive elements ≥ 8px

**Issues Found:**
[List touch target issues]

---

## Performance

- [ ] Page loads < 3 seconds on 3G
- [ ] Images optimized for mobile
- [ ] Lazy loading implemented
- [ ] Critical CSS inlined
- [ ] JavaScript deferred/async

**Metrics:**
- Load time: [Seconds]
- FCP: [Seconds]
- LCP: [Seconds]

**Issues Found:**
[List performance issues]

---

## Navigation

- [ ] Mobile menu accessible
- [ ] Hamburger menu works correctly
- [ ] Navigation items large enough
- [ ] Can navigate with one hand
- [ ] Thumb-friendly zones used

**Issues Found:**
[List navigation issues]

---

## Content

- [ ] Text readable at mobile size
- [ ] Line length appropriate (45-75 chars)
- [ ] Headings scale down appropriately
- [ ] Tables handled gracefully
- [ ] No tiny text

**Issues Found:**
[List content issues]

---

## Forms

- [ ] Input types appropriate (email, tel, etc.)
- [ ] Auto-complete enabled
- [ ] Labels visible
- [ ] Error messages clear
- [ ] Submit button easy to tap

**Issues Found:**
[List form issues]

---

## Summary

**Mobile-Friendly:** [Yes/Partial/No]

**Critical Issues:** [Number]

**Top Priorities:**
1. [Issue 1]
2. [Issue 2]
3. [Issue 3]
```

---

## Performance Audit Template

**Use when:** Checking page performance

**Template:**

```markdown
# Performance Audit: [Page Name]

**Date:** [Date]
**Tools:** [Chrome DevTools/Lighthouse/WebPageTest]

---

## Core Web Vitals

### LCP (Largest Contentful Paint)
- **Current:** [Seconds]
- **Target:** < 2.5s
- **Status:** [Good/Needs Improvement/Poor]
- **Element:** [What's the LCP element]

### FID (First Input Delay)
- **Current:** [Milliseconds]
- **Target:** < 100ms
- **Status:** [Good/Needs Improvement/Poor]

### CLS (Cumulative Layout Shift)
- **Current:** [Score]
- **Target:** < 0.1
- **Status:** [Good/Needs Improvement/Poor]
- **Causes:** [What's shifting]

---

## Load Performance

- **First Contentful Paint:** [Seconds]
- **Time to Interactive:** [Seconds]
- **Speed Index:** [Score]
- **Total Blocking Time:** [Milliseconds]

---

## Resource Analysis

### JavaScript
- **Bundle size:** [KB]
- **Unused JS:** [KB / %]
- **Long tasks:** [Number]

### CSS
- **Stylesheet size:** [KB]
- **Unused CSS:** [KB / %]
- **Blocking CSS:** [Yes/No]

### Images
- **Total size:** [MB]
- **Unoptimized:** [Number]
- **Missing dimensions:** [Number]

---

## Opportunities

1. **[Opportunity]** - [Potential savings]
2. **[Opportunity]** - [Potential savings]
3. **[Opportunity]** - [Potential savings]

---

## Recommendations

**P0:**
- [Critical performance fix]

**P1:**
- [High-impact optimization]

**P2:**
- [Incremental improvement]
```

---

## Usage Guidelines

**Choose the right template:**
- **Quick Audit:** Time-sensitive, basic assessment needed
- **Comprehensive Audit:** Thorough review, detailed documentation
- **Redundancy Checklist:** Specifically checking for duplicates
- **Gap Analysis:** Identifying what's missing
- **WCAG Checklist:** Accessibility compliance check
- **Mobile Checklist:** Mobile experience review
- **Performance Audit:** Speed and optimization review

**Tips for using templates:**
1. Copy entire template to start
2. Fill in bracketed placeholders [like this]
3. Check/uncheck boxes as you audit
4. Delete sections not applicable
5. Add evidence (code snippets, screenshots)
6. Be specific in findings and recommendations

---

**Last Updated:** October 29, 2025
**Version:** 1.0
**Maintained by:** Madina Gbotoe
