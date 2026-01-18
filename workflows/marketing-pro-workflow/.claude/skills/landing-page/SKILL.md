---
name: landing-page
description: Create high-converting landing pages with persuasive copy, clear CTAs, social proof, and optimized structure. Use when building sales pages, product pages, lead capture pages, or conversion-focused pages.
---

# Landing Page Skill

## Instructions

When creating landing pages:

### 1. Page Structure

```
┌─────────────────────────────────────┐
│           HERO SECTION              │
│  Headline + Subheadline + CTA       │
│           + Hero Image              │
├─────────────────────────────────────┤
│         SOCIAL PROOF BAR            │
│    Logos / "As seen in" / Stats     │
├─────────────────────────────────────┤
│         PROBLEM SECTION             │
│     Pain points your audience has   │
├─────────────────────────────────────┤
│         SOLUTION SECTION            │
│    How your product solves it       │
├─────────────────────────────────────┤
│         FEATURES/BENEFITS           │
│    3-6 key features with benefits   │
├─────────────────────────────────────┤
│         HOW IT WORKS                │
│       3-step process                │
├─────────────────────────────────────┤
│         TESTIMONIALS                │
│    Customer quotes + photos         │
├─────────────────────────────────────┤
│         PRICING                     │
│    Clear pricing options            │
├─────────────────────────────────────┤
│            FAQ                      │
│    Objection handling               │
├─────────────────────────────────────┤
│         FINAL CTA                   │
│    Last push with urgency           │
├─────────────────────────────────────┤
│           FOOTER                    │
│    Trust badges, links, legal       │
└─────────────────────────────────────┘
```

### 2. Hero Section

**Headline Formulas:**
- [Achieve outcome] without [pain point]
- The [adjective] way to [desired result]
- [Product] that [key benefit]
- Stop [bad thing]. Start [good thing].
- [Number] [people] use [Product] to [outcome]

**Subheadline:**
- Expand on the headline
- Add specificity
- Include secondary benefit

**Example:**
```html
<section class="hero">
  <h1>Build WordPress Themes 10x Faster</h1>
  <p class="subheadline">
    The developer toolkit that eliminates repetitive coding
    so you can focus on what matters — shipping great themes.
  </p>
  <a href="#" class="cta-button">Start Free Trial</a>
  <p class="microcopy">No credit card required • 14-day trial</p>
</section>
```

### 3. Social Proof Types

**Logo Bar:**
```html
<section class="social-proof">
  <p>Trusted by 10,000+ developers at</p>
  <div class="logos">
    <img src="logo1.svg" alt="Company 1">
    <img src="logo2.svg" alt="Company 2">
    ...
  </div>
</section>
```

**Stats Bar:**
```html
<div class="stats">
  <div class="stat">
    <span class="number">50,000+</span>
    <span class="label">Active Users</span>
  </div>
  <div class="stat">
    <span class="number">4.9/5</span>
    <span class="label">Average Rating</span>
  </div>
  <div class="stat">
    <span class="number">99.9%</span>
    <span class="label">Uptime</span>
  </div>
</div>
```

**Testimonials:**
```html
<blockquote class="testimonial">
  <p>"Quote that highlights specific results..."</p>
  <footer>
    <img src="avatar.jpg" alt="Name">
    <cite>
      <strong>Name</strong>
      <span>Title, Company</span>
    </cite>
  </footer>
</blockquote>
```

### 4. Features Section

**Format: Feature → Benefit**
```html
<div class="feature">
  <div class="feature-icon">🚀</div>
  <h3>One-Click Deployment</h3>
  <p>Deploy to production in seconds, not hours.
     Spend more time building, less time configuring.</p>
</div>
```

### 5. Pricing Section

```html
<div class="pricing-card popular">
  <span class="badge">Most Popular</span>
  <h3>Pro Plan</h3>
  <div class="price">
    <span class="currency">$</span>
    <span class="amount">49</span>
    <span class="period">/month</span>
  </div>
  <ul class="features">
    <li>✓ Feature 1</li>
    <li>✓ Feature 2</li>
    <li>✓ Feature 3</li>
  </ul>
  <a href="#" class="cta-button">Get Started</a>
  <p class="guarantee">30-day money-back guarantee</p>
</div>
```

### 6. CTA Best Practices

**Button Copy:**
- Start Free Trial
- Get Started Now
- Download Free Guide
- Join 10,000+ Users
- Claim Your Discount

**Supporting Elements:**
- Risk reducers (money-back guarantee)
- Urgency (limited time)
- Scarcity (only X left)
- Social proof (join X others)

### 7. FAQ Section

```html
<details class="faq-item">
  <summary>Common objection as a question?</summary>
  <p>Answer that overcomes the objection with
     specifics and reassurance.</p>
</details>
```

**Common FAQ Topics:**
- Pricing/refunds
- Technical requirements
- Support availability
- Comparison to alternatives
- Getting started process

### 8. Conversion Optimization

**Above the Fold:**
- Clear value proposition
- Primary CTA visible
- Trust indicator

**Throughout Page:**
- Multiple CTAs (same action)
- Progressive disclosure
- Visual hierarchy
- Mobile optimization

**Reduce Friction:**
- Minimal form fields
- Clear next steps
- Fast page load
- No distractions

### 9. Copywriting Tips

**Power Words:**
- Free, New, Proven, Easy
- Instant, Guaranteed, Limited
- Exclusive, Premium, Ultimate

**Avoid:**
- Jargon and buzzwords
- Vague claims
- Walls of text
- Multiple CTAs

### 10. Landing Page Checklist

- [ ] Clear, benefit-focused headline
- [ ] Single, focused CTA
- [ ] Social proof present
- [ ] Mobile responsive
- [ ] Fast loading (<3s)
- [ ] Trust signals visible
- [ ] FAQ addresses objections
- [ ] Analytics tracking set up
