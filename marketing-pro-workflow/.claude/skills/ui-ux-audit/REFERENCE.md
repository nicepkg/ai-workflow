# UI/UX Audit Reference Guide

**Purpose:** Detailed reference information for conducting comprehensive UI/UX audits. Read this when you need in-depth guidance beyond the core SKILL.md instructions.

---

## Table of Contents

1. [UX Research Principles](#ux-research-principles)
2. [WCAG 2.1 AA Requirements](#wcag-21-aa-requirements)
3. [Design Pattern Library](#design-pattern-library)
4. [Audit Methodology](#audit-methodology)
5. [Measurement Frameworks](#measurement-frameworks)
6. [Common Anti-Patterns](#common-anti-patterns)

---

## UX Research Principles

### Left-Attention Pattern (Nielsen Norman Group)

**Research Finding:** 80% of user attention falls on the LEFT half of the screen

**Source:** Nielsen Norman Group eye-tracking studies (multiple studies 2006-2024)

**Implementation Rules:**
- **LEFT HALF (high attention):**
  - Primary content and headlines
  - Key value propositions
  - Call-to-action buttons
  - Critical metrics and differentiators
  - Navigation elements
  - Important text content

- **RIGHT HALF (lower attention):**
  - Decorative images
  - Secondary information
  - Supporting visuals
  - Supplementary content

**Exception:** If critical content MUST be on right:
- Increase visual prominence (larger, bolder, higher contrast)
- Add discovery mechanisms on left side
- Use directional cues (arrows, layout flow)

**Audit Checklist:**
- [ ] Are primary CTAs in the left 50% of viewport?
- [ ] Are key value propositions left-aligned or left-positioned?
- [ ] Are critical metrics in high-attention zones?
- [ ] If important content is on right, is there a discovery mechanism?

---

### F-Pattern Reading (Nielsen Norman Group)

**Research Finding:** Users read web content in an F-shaped pattern

**Pattern Characteristics:**
1. Horizontal movement across top (top bar of F)
2. Move down, horizontal movement again (lower bar of F)
3. Vertical scan down left side (stem of F)

**Implementation Rules:**
- Most important information in first two paragraphs
- Start headlines and subheadlines with information-carrying words
- Left-align text for scanability
- Use bullet points and short paragraphs
- Front-load sentences with key information

**Audit Checklist:**
- [ ] Is key information in first two paragraphs?
- [ ] Do headlines start with information-carrying words?
- [ ] Is text left-aligned for easy scanning?
- [ ] Are bullet points used for lists?

---

### Cognitive Load Principles

**Miller's Law:** Average person can hold 7±2 items in working memory

**Implementation Rules:**
- Limit navigation items to 5-7 main options
- Break content into chunks of 5-9 items
- Use progressive disclosure for complex information
- Minimize simultaneous choices

**Hick's Law:** Decision time increases with number of choices

**Implementation Rules:**
- Limit CTAs to 1-2 primary actions per section
- Use visual hierarchy to prioritize options
- Group related choices together
- Remove unnecessary options

**Audit Checklist:**
- [ ] Are navigation items ≤7?
- [ ] Are content chunks ≤9 items?
- [ ] Are CTAs limited to 1-2 per section?
- [ ] Is information progressively disclosed?

---

### Visual Hierarchy Principles

**Size and Scale:**
- Headlines 2-3x body text size
- Subheads 1.5-2x body text size
- Body text 16-18px minimum

**Contrast and Color:**
- Important elements: high contrast
- Secondary elements: medium contrast
- Tertiary elements: low contrast

**Whitespace:**
- More whitespace = higher perceived importance
- Generous margins around key elements
- Breathing room between sections

**Audit Checklist:**
- [ ] Is there clear size hierarchy (headline > subhead > body)?
- [ ] Do important elements have high contrast?
- [ ] Is whitespace used strategically?
- [ ] Can users scan and find key information quickly?

---

## WCAG 2.1 AA Requirements

### Color Contrast

**Requirements:**
- **Normal text:** 4.5:1 contrast ratio minimum
- **Large text (18pt+):** 3:1 contrast ratio minimum
- **Interactive elements:** 3:1 contrast with adjacent colors

**Testing:**
- Use browser DevTools or online contrast checkers
- Test all text against backgrounds
- Verify button/link colors meet requirements

**Common Failures:**
- Light gray text on white (#999 on #FFF = 2.8:1 ❌)
- Low-contrast placeholders
- Subtle hover states

**Audit Checklist:**
- [ ] All text meets 4.5:1 contrast (or 3:1 for large text)?
- [ ] Interactive elements have 3:1 contrast?
- [ ] Hover/focus states are clearly visible?

---

### Keyboard Navigation

**Requirements:**
- All interactive elements keyboard accessible
- Visible focus indicators
- Logical tab order
- Skip links for main content

**Testing:**
- Tab through entire page
- Verify all clickable elements are reachable
- Ensure focus indicators are visible
- Test with keyboard only (no mouse)

**Common Failures:**
- Custom dropdowns not keyboard accessible
- Missing focus indicators
- Illogical tab order
- Keyboard traps (can't escape element)

**Audit Checklist:**
- [ ] Can all interactive elements be reached via Tab?
- [ ] Are focus indicators visible and clear?
- [ ] Is tab order logical (left-to-right, top-to-bottom)?
- [ ] Are there skip links for long navigation?

---

### ARIA Labels and Semantic HTML

**Requirements:**
- Use semantic HTML (nav, main, article, aside, etc.)
- ARIA labels for icon buttons
- Alt text for all meaningful images
- Form labels associated with inputs

**Implementation:**
```html
<!-- Good: Semantic HTML -->
<nav aria-label="Main navigation">
  <button aria-label="Menu">
    <IconMenu />
  </button>
</nav>

<!-- Good: Form labels -->
<label for="email">Email</label>
<input id="email" type="email" />

<!-- Good: Alt text -->
<img src="chart.png" alt="Portfolio value chart showing $156M total" />
```

**Audit Checklist:**
- [ ] Is semantic HTML used (nav, main, header, footer)?
- [ ] Do icon buttons have aria-label?
- [ ] Do all images have descriptive alt text?
- [ ] Are form labels properly associated?

---

### Motion and Animation

**Requirements:**
- Respect `prefers-reduced-motion` media query
- Animations ≤ 3 seconds duration
- Essential animations only
- Provide static alternatives

**Implementation:**
```css
/* Respect user preference */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Common Failures:**
- Auto-playing animations with no pause control
- Long animations (>3s) blocking content
- No reduced-motion alternative

**Audit Checklist:**
- [ ] Does site respect prefers-reduced-motion?
- [ ] Are animations ≤ 3 seconds?
- [ ] Can users pause auto-playing animations?
- [ ] Are essential functions available without animation?

---

## Design Pattern Library

### Clean, Minimal Design Patterns

**Characteristics:**
- Generous whitespace (40-60% of viewport)
- Limited color palette (2-4 colors)
- Typography hierarchy (2-3 font sizes)
- Single-column or simple grid layouts
- Focused content sections

**Examples:**
- Apple product pages
- Stripe documentation
- Linear app
- Notion marketing pages

**Anti-Patterns:**
- Dense information layouts
- Multiple sidebars
- Excessive animations
- Cluttered navigation
- Information overload

---

### Document-Style Pages

**Characteristics:**
- Single column, max-width 700-800px
- Text-focused with minimal decoration
- Clear typography hierarchy
- Scannable headings
- Strategic use of whitespace

**When to Use:**
- About pages
- Documentation
- Blog posts
- Case studies
- Long-form content

**What NOT to Add:**
- Dashboards or metrics
- Multiple CTAs throughout content
- Sidebars with unrelated info
- Auto-playing media
- Complex interactive elements

---

### Portfolio/Showcase Pages

**Best Practices:**
- Lead with impact/results
- Use data to tell stories
- Visual hierarchy: outcome > process
- Scannable sections with clear headers
- Strategic CTAs at conversion points

**Common Mistakes:**
- Burying results below process
- No quantifiable metrics
- Generic descriptions
- Missing CTAs
- Poor mobile optimization

---

## Audit Methodology

### Evidence-Based Audit Process

**Step 1: Establish Baseline**
1. Read all target files (pages, components, data)
2. Document what EXISTS (not assumptions)
3. Take screenshots for reference
4. Note current metrics (load time, bundle size)

**Step 2: Analyze Current State**
1. Map user flow through page
2. Identify conversion points
3. Note information hierarchy
4. Check for redundancy
5. Test accessibility

**Step 3: Identify Gaps**
1. Compare against best practices
2. Check for missing functionality
3. Verify WCAG compliance
4. Test across devices/browsers
5. Gather user feedback (if available)

**Step 4: Prioritize Recommendations**
1. **P0 (Critical):** Accessibility violations, broken functionality
2. **P1 (High):** Major UX improvements, clear value adds
3. **P2 (Medium):** Incremental improvements, polish
4. **P3 (Low):** Nice-to-haves, future considerations

**Step 5: Present Findings**
1. Current state summary
2. What exists (with evidence)
3. Redundancy check results
4. Prioritized recommendations
5. Expected impact for each

---

### Redundancy Detection Methodology

**Check for Duplicate Information:**
```markdown
1. List all data points displayed on page
2. Note location of each data point
3. Identify any repeated information
4. Flag redundancy with severity:
   - HIGH: Identical data in multiple locations
   - MEDIUM: Similar data in different formats
   - LOW: Related but not duplicate data
```

**Questions to Ask:**
- Is this data already shown elsewhere?
- Does this add new information or just repeat?
- If removed, would user lose critical info?
- Is there value in showing this twice?

**Example:**
```
Data Point: Portfolio Value ($156M)
Locations:
- Hero headline: "$156M in enterprise impact"
- Impact card: "Portfolio Value: $156M"
- About section: "Led $156M in products"

Analysis:
✅ Hero: Context-setting (appropriate)
✅ Impact card: Detailed metric (appropriate)
⚠️ About section: Redundant if also in impact cards
```

---

## Measurement Frameworks

### Before/After Metrics

**User Experience Metrics:**
- Time to first interaction
- Task completion rate
- Error rate
- User satisfaction score

**Technical Metrics:**
- Page load time
- First Contentful Paint (FCP)
- Largest Contentful Paint (LCP)
- Cumulative Layout Shift (CLS)
- Bundle size

**Business Metrics:**
- Conversion rate
- Bounce rate
- Time on page
- Click-through rate

**How to Measure Impact:**
1. Establish baseline metrics
2. Implement changes
3. Measure after changes
4. Calculate delta (% improvement)
5. Validate statistical significance

---

### Severity Classification

**Critical (Fix Immediately):**
- WCAG violations preventing access
- Broken functionality
- Security vulnerabilities
- Data loss issues

**High (Fix This Sprint):**
- Poor UX blocking primary tasks
- Performance issues affecting users
- Missing critical features
- Significant accessibility gaps

**Medium (Fix Within Month):**
- Incremental UX improvements
- Minor accessibility issues
- Code quality improvements
- Non-critical feature gaps

**Low (Backlog):**
- Nice-to-have features
- Visual polish
- Edge case fixes
- Future enhancements

---

## Common Anti-Patterns

### Pattern 1: Kitchen Sink Dashboard

**Description:** Adding every possible metric/visualization to a page

**Why It's Bad:**
- Overwhelms users with information
- Dilutes focus from key metrics
- Increases cognitive load
- Slows page performance

**Instead:**
- Show 3-5 key metrics maximum
- Use progressive disclosure for details
- Provide filtering/customization options
- Link to detailed analytics if needed

---

### Pattern 2: Redundant Data Display

**Description:** Showing same data in multiple formats/locations

**Why It's Bad:**
- Wastes screen real estate
- Creates maintenance burden
- Confuses users (which is correct?)
- Adds no new information

**Instead:**
- Show each data point once
- Choose most effective format
- Use context to determine placement
- Link to details rather than duplicating

---

### Pattern 3: Premature Feature Addition

**Description:** Adding features without validating need

**Why It's Bad:**
- Clutters interface unnecessarily
- Adds maintenance burden
- May not solve actual user problems
- Increases complexity

**Instead:**
- Validate need first (user research, data)
- Start with minimal viable solution
- Test with users before full build
- Add complexity only when justified

---

### Pattern 4: Ignoring Mobile Experience

**Description:** Desktop-first design without mobile consideration

**Why It's Bad:**
- 50%+ traffic is mobile for most sites
- Poor mobile UX drives users away
- Responsive design is easier to fix early
- Accessibility suffers

**Instead:**
- Mobile-first or mobile-concurrent design
- Test on actual devices
- Consider touch targets (44x44px min)
- Optimize for thumb zones

---

### Pattern 5: Animation Overload

**Description:** Excessive animations that slow or distract

**Why It's Bad:**
- Frustrates users in a hurry
- Accessibility issue (motion sensitivity)
- Performance impact
- Delays content access

**Instead:**
- Animations ≤ 0.3s for UI feedback
- Respect prefers-reduced-motion
- Make animations purposeful
- Allow users to skip/disable

---

## Usage Notes

**When to Read This File:**
- Conducting comprehensive audit (not quick check)
- Need detailed WCAG requirements
- Validating design decisions with research
- Explaining recommendations to stakeholders
- Learning UX best practices

**When to Use SKILL.md Instead:**
- Quick audits (< 30 minutes)
- Standard workflow execution
- Need step-by-step process
- Want audit output template

**When to Use FORMS.md Instead:**
- Need pre-filled templates
- Want standardized checklists
- Quick reference formats
- Copy-paste audit structures

---

**Last Updated:** October 29, 2025
**Version:** 1.0
**Maintained by:** Madina Gbotoe
