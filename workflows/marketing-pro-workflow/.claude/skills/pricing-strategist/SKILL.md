---
name: pricing-strategist
description: Design and optimize pricing strategies for SaaS products including tiering, packaging, value metrics, and experimentation. Use when setting initial pricing, optimizing conversion, expanding revenue, or when users ask about pricing strategy, monetization, or revenue optimization.
license: Complete terms in LICENSE.txt
---

# Pricing Strategist

Design pricing strategies that maximize revenue while keeping customers happy.

## Core Principles

1. **Pricing is a growth lever**: 1% improvement in pricing = 11% improvement in profit (McKinsey)
2. **Price to value, not cost**: Charge based on value delivered, not what it costs you
3. **Simple > Clever**: 3 tiers beats 5 tiers; clear packaging beats complex
4. **Experiment continuously**: A/B test, iterate, optimize

## Pricing Strategy Framework

### Step 1: Determine Your Value Metric

**Value metric** = What you charge for (users, projects, API calls, etc.)

**Good value metrics**:

- Align with customer value (as they get more value, they pay more)
- Easy to understand and predict
- Grow naturally with usage

**Examples**:

```yaml
Slack: Per active user
  ✅ Grows with team size
  ✅ Easy to understand
  ✅ Aligns with value

Twilio: Per API call
  ✅ Grows with usage
  ✅ Predictable for users
  ✅ Direct value correlation

Dropbox: Storage size
  ✅ Clear metric
  ✅ Grows with needs
  ⚠️ Can be gamed (compression)

AWS: Everything (CPU, storage, bandwidth, etc.)
  ⚠️ Complex but accurate
  ⚠️ Hard to predict costs
  ✅ Pay for what you use
```

**Value Metric Decision Matrix**:

| Metric       | Alignment to Value | Simplicity | Predictability | Growth Potential |
| ------------ | ------------------ | ---------- | -------------- | ---------------- |
| Per User     | High               | High       | High           | Medium           |
| Per Feature  | Medium             | High       | High           | Low              |
| Usage-Based  | High               | Medium     | Low            | High             |
| Storage      | Low                | High       | Medium         | Medium           |
| Transactions | High               | Medium     | Medium         | High             |

### Step 2: Choose Your Pricing Model

**Flat Rate**:

```
$99/month - unlimited everything
```

- ✅ Simple to understand
- ✅ Easy to sell
- ❌ Leaves money on table
- ❌ Doesn't scale with value

**Tiered Pricing**:

```
Starter: $29/mo  - 5 users
Pro:     $99/mo  - 20 users
Business: $299/mo - Unlimited users
```

- ✅ Captures different customer segments
- ✅ Upsell path clear
- ⚠️ Anchor pricing matters

**Usage-Based**:

```
$0.01 per API call
First 10,000 free
```

- ✅ Perfect alignment with value
- ✅ Low barrier to entry
- ❌ Unpredictable for customers
- ❌ Hard to forecast revenue

**Hybrid** (Best of both):

```
Base: $49/mo + $0.50 per extra user
```

- ✅ Predictable base + scales with value
- ✅ Lower barrier than pure per-seat
- ⚠️ More complex to explain

### Step 3: Create Your Pricing Tiers

**The Rule of 3**:

- **Starter/Basic**: Get them in the door (50-60% of customers)
- **Professional/Pro**: Sweet spot (30-40% of customers)
- **Business/Enterprise**: High value, high support (5-10% of customers)

**Tier Design Template**:

```yaml
Tier 1 - Starter ($29/mo):
  Target: Individuals, tiny teams, trying it out
  Value Limit: 5 users, 10 projects
  Features: ✅ Core features
    ✅ Basic support (email)
    ❌ Advanced features
    ❌ Integrations
    ❌ Custom anything

Tier 2 - Professional ($99/mo):
  Target: Small-medium teams, main product
  Value Limit: 20 users, 100 projects
  Features: ✅ Everything in Starter
    ✅ Advanced features
    ✅ Integrations (Slack, etc.)
    ✅ Priority support
    ✅ API access
    ❌ Custom SLA
    ❌ SSO

Tier 3 - Business ($299/mo):
  Target: Larger teams, mission-critical
  Value Limit: Unlimited users, unlimited projects
  Features: ✅ Everything in Professional
    ✅ Advanced security (SSO, SAML)
    ✅ Custom SLA
    ✅ Dedicated support
    ✅ Custom integrations
    ✅ Training & onboarding
```

**Anchor Pricing Strategy**:

```
Starter:  $29/mo  (entry point)
Pro:      $99/mo  (3.4x - where you want most people) 👈 Sweet spot
Business: $299/mo (3x - makes Pro look reasonable)
```

Most customers choose the middle tier when:

- Middle tier is 3-4x the starter price
- Top tier is 2-3x the middle tier

### Step 4: Feature Packaging

**Good Feature Distribution**:

```yaml
Starter Tier (60% features):
  - All core CRUD operations
  - Basic reporting
  - Email support
  - Mobile app
  Goal: Get them using the product successfully

Pro Tier (85% features):
  - Everything in Starter
  - Advanced analytics
  - Integrations (Slack, Zapier, etc.)
  - API access
  - Priority support
  - Collaboration features
  Goal: Make this irresistible for growing teams

Business Tier (100% features):
  - Everything in Pro
  - SSO/SAML
  - Advanced security & compliance
  - Custom SLA
  - Dedicated support
  - Training & onboarding
  - Custom contracts
  Goal: Remove all objections for enterprise buyers
```

**Gating Strategy**:

- **Gate by volume**: 5 users → 20 users → unlimited
- **Gate by features**: Basic → Advanced → Enterprise
- **Gate by support**: Email → Priority → Dedicated
- **Gate by integrations**: None → Standard → Custom

❌ **Don't gate core value**: If your product's main value is X, don't gate X
✅ **Gate advanced/power features**: Analytics, integrations, admin features

## Pricing Psychology

### Charm Pricing

```
$99/mo > $100/mo  (1% cheaper, feels 20% cheaper)
$29/mo > $30/mo
```

### Anchoring

```
❌ Bad:
  Basic:    $50
  Premium:  $75  (only 50% more, but not 50% more value?)

✅ Good:
  Basic:    $50
  Premium:  $150  (3x price for 2x value = good deal)
  Enterprise: $500  (makes Premium look reasonable)
```

### Annual Discounts

```
Monthly:  $99/mo  ($1,188/year)
Annual:   $990/year  (Save $198 = 17% discount)
```

**Why offer annual?**:

- Cash flow upfront
- Higher LTV (less churn)
- 15-20% discount is standard

**When to offer**:

- At signup
- After 2-3 months (they're hooked)
- During renewal
- Seasonal promotions

### Free Trial vs Freemium

**Free Trial**:

```yaml
Type: 14-day free trial, no credit card required
When: Product has clear "aha moment" quickly
Pros:
  - Everyone experiences full product
  - Clear conversion point
  - No freeloaders
Cons:
  - Friction at signup
  - Have to convert them quickly
```

**Freemium**:

```yaml
Type: Forever free tier with limitations
When: High viral coefficient, network effects
Pros:
  - No friction at signup
  - Build large user base
  - Word of mouth
Cons:
  - Many users never pay
  - High infrastructure costs
  - Harder to monetize
```

**Decision Matrix**:

- **B2B SaaS**: Free trial (14 days)
- **Viral products** (Slack, Zoom): Freemium
- **High touch sales**: Free trial + demo
- **Self-serve products**: Freemium

## Pricing Experiments

### A/B Testing Pricing

**What to test**:

1. **Price points**: $99 vs $149
2. **Packaging**: Features in each tier
3. **Billing frequency**: Monthly vs annual
4. **Free trial length**: 7 vs 14 vs 30 days
5. **Anchor pricing**: Add expensive tier to make middle tier look good

**How to test**:

```javascript
// Example: Test pricing pages
const pricingVariants = {
  control: {
    starter: 29,
    pro: 99,
    business: 299
  },
  test: {
    starter: 39,
    pro: 129,
    business: 349
  }
}

// Show different prices to 50% of visitors
const variant = Math.random() < 0.5 ? 'control' : 'test'

// Track which converts better
analytics.track('pricing_page_viewed', {
  variant: variant,
  prices: pricingVariants[variant]
})
```

**Metrics to track**:

- Conversion rate (trial → paid)
- Average revenue per user (ARPU)
- Customer acquisition cost (CAC)
- Lifetime value (LTV)
- Payback period

**Sample size calculator**:

```
Need ~1,000 visitors per variant to detect 10% change
Need ~5,000 visitors per variant to detect 5% change
```

### Grandfather Pricing

When raising prices, grandfather existing customers:

```yaml
Scenario: Raising Pro from $99 → $129

Option 1: Grandfather forever
  - Existing: Stay at $99/mo forever
  - New: Pay $129/mo
  - Pros: Great for retention
  - Cons: Growing discount over time

Option 2: Grandfather for 12 months
  - Existing: Stay at $99 for 1 year, then $129
  - New: Pay $129/mo immediately
  - Pros: Balanced approach
  - Cons: Still have to communicate increase

Option 3: No grandfathering, small increase
  - Everyone: Goes to $129/mo
  - Give 30 days notice
  - Offer annual deal to lock in current price
  - Pros: Simplest
  - Cons: Some churn risk
```

### Price Increases

**When to raise prices**:

- Product significantly improved
- Demand exceeds supply
- Customer acquisition costs increased
- Competitors charge more
- Every 12-18 months (keep up with inflation)

**How to communicate**:

```markdown
Subject: [Product] pricing update - your plan is increasing

Hi [Name],

Good news: We've shipped [impressive features] over the last
year, including [X, Y, Z].

Starting [Date, 30+ days away], we're updating our pricing:

- Pro: $99 → $129/mo (+30%)
- Business: $299 → $349/mo (+17%)

Your current pricing:

- You'll stay at $99/mo for the next 12 months
- To lock in $99/mo permanently, switch to annual: $990/year

Why we're increasing prices:

- [Specific value adds]
- [New features]
- [Better support]

Questions? Reply to this email.

Thanks for being with us,
[Founder Name]
```

## Revenue Expansion

### Upsell Strategies

**When to prompt upgrades**:

```javascript
// Hit limit
if (user.projectCount >= user.plan.projectLimit) {
  showUpgradePrompt({
    message: "You've hit your 10 project limit",
    cta: 'Upgrade to Pro for 100 projects',
    timing: 'when_blocked'
  })
}

// Feature discovery
if (user.clickedAdvancedFeature && !user.hasAccess) {
  showUpgradePrompt({
    message: 'This feature is available on Pro',
    cta: 'Upgrade now for $99/mo',
    timing: 'moment_of_value'
  })
}

// Usage-based trigger
if (user.daysActive > 30 && user.plan === 'starter') {
  showUpgradePrompt({
    message: "You're a power user! Unlock more with Pro",
    cta: 'See Pro features',
    timing: 'established_user'
  })
}
```

**Upgrade Incentives**:

- Prorated credit for current plan
- Feature preview (7-day trial of Pro features)
- Bundle discount (annual save 20%)
- Limited-time offer (20% off if you upgrade this week)

### Add-Ons

```yaml
Base Product: $99/mo

Add-ons (à la carte):
  - Extra users: +$10/user/mo
  - Advanced analytics: +$49/mo
  - White label: +$99/mo
  - Priority support: +$199/mo
  - API rate limit increase: +$49/mo

Example Bill:
  Pro plan: $99
  +5 extra users: $50
  +Advanced analytics: $49
  Total: $198/mo
```

**When to use add-ons**:

- Feature has clear standalone value
- Not every customer needs it
- Significant cost to provide
- Clear pricing (not complex calculations)

## Pricing by Market Segment

### Small Business (SMB)

```yaml
Price Point: $29-99/mo
Sales Motion: Self-serve
Features: Simple, easy to use
Support: Email, docs
Decision Maker: End user or team lead
Sales Cycle: Minutes to days
```

### Mid-Market

```yaml
Price Point: $99-999/mo
Sales Motion: Self-serve + light touch
Features: Integrations, collaboration
Support: Priority email, chat
Decision Maker: Department head
Sales Cycle: Days to weeks
```

### Enterprise

```yaml
Price Point: $1,000+/mo (often $10k-100k+)
Sales Motion: High-touch sales
Features: SSO, custom, security, SLA
Support: Dedicated account manager
Decision Maker: VP, C-level, procurement
Sales Cycle: Weeks to months
```

## Pricing Metrics

### Key Metrics to Track

```typescript
interface PricingMetrics {
  // Revenue metrics
  mrr: number // Monthly Recurring Revenue
  arr: number // Annual Recurring Revenue
  arpu: number // Average Revenue Per User

  // Conversion
  trial_to_paid_rate: number // %
  free_to_paid_rate: number // % (if freemium)

  // Expansion
  expansion_mrr: number // New revenue from existing customers
  contraction_mrr: number // Lost revenue from downgrades
  net_revenue_retention: number // (Expansion - Contraction) / Starting MRR

  // Efficiency
  cac: number // Customer Acquisition Cost
  ltv: number // Lifetime Value
  ltv_cac_ratio: number // Should be > 3x
  payback_period_months: number // Should be < 12 months

  // Distribution
  customers_by_tier: {
    starter: number
    pro: number
    business: number
  }
}
```

### Healthy SaaS Benchmarks

```yaml
Good SaaS Company:
  Trial → Paid: > 15%
  MRR Growth: > 10% month-over-month (early stage)
  Churn Rate: < 5% per month (SMB) or < 1% (enterprise)
  LTV:CAC: > 3:1
  Payback Period: < 12 months
  Net Revenue Retention: > 100% (expansion covers churn)
  Annual Contract Value:
    - SMB: $1k-10k
    - Mid-market: $10k-100k
    - Enterprise: $100k+
```

## Pricing Page Best Practices

### Structure

```
Hero Section:
  Headline: "Pricing that grows with you"
  Subheadline: "Start free, upgrade anytime"

Comparison Table:
  [Starter]  [Pro - Most Popular]  [Business]

  Feature comparison rows

  [CTA Button]  [CTA Button]  [CTA Button]

FAQ Section:
  - Can I change plans?
  - What payment methods do you accept?
  - Do you offer refunds?
  - Can I cancel anytime?

Trust Signals:
  - Testimonials
  - Logos of customers
  - Money-back guarantee
```

### Psychological Tricks

```html
<!-- Highlight most popular tier -->
<div class="pricing-card" data-popular="true">
  <div class="badge">Most Popular</div>
  <h3>Pro</h3>
  <div class="price">
    <span class="amount">$99</span>
    <span class="period">/month</span>
  </div>
  <!-- Larger button, different color -->
  <button class="cta-primary-large">Start Free Trial</button>
</div>

<!-- Show annual savings -->
<div class="billing-toggle">
  <span>Monthly</span>
  <toggle />
  <span>Annual <badge>Save 20%</badge></span>
</div>

<!-- Social proof -->
<div class="testimonial">
  "We increased revenue by 40% after upgrading to Pro" - Jane Doe, Acme Corp
</div>
```

## Quick Start Checklist

### Launching Pricing (MVP)

- [ ] Pick value metric (per-user, usage, etc.)
- [ ] Design 3 tiers (Starter, Pro, Business)
- [ ] Set anchor prices (3-4x between tiers)
- [ ] Package features (60%, 85%, 100%)
- [ ] Create simple pricing page
- [ ] Set up billing (Stripe)
- [ ] Offer 14-day trial

### Optimizing Pricing (Post-Launch)

- [ ] Track conversion rates by tier
- [ ] Survey customers on pricing perception
- [ ] A/B test price points
- [ ] Add annual billing option (15-20% discount)
- [ ] Create upgrade prompts in-app
- [ ] Monitor NRR (expansion vs churn)
- [ ] Review pricing every 6-12 months

## Common Pitfalls

❌ **Pricing too low**: Harder to raise than lower; leaves money on table
❌ **Too many tiers**: 5+ tiers is confusing; stick to 3
❌ **Gating core features**: Don't lock essential value behind highest tier
❌ **Complex value metric**: Users shouldn't need calculator to predict their bill
❌ **Never raising prices**: Customers expect prices to increase over time
❌ **Charging for support**: Support should be included, vary by response time

## Summary

Great pricing strategy:

- ✅ Aligns with customer value (value metric)
- ✅ Simple to understand (3 tiers, clear packaging)
- ✅ Room for expansion (upgrade path, add-ons)
- ✅ Regularly optimized (experiments, data-driven)
- ✅ Increases over time (annual raises as you add value)
