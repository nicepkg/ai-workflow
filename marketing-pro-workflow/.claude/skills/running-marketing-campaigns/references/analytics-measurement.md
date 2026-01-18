# Analytics & Measurement

KPIs, GA4 configuration, attribution models, and ROI calculations for marketing performance.

## Contents

- [KPI Matrix by Channel](#kpi-matrix-by-channel)
- [Vanity vs Actionable Metrics](#vanity-vs-actionable-metrics)
- [Attribution Models](#attribution-models)
- [GA4 Setup Checklist](#ga4-setup-checklist)
- [Dashboard Design](#dashboard-design)
- [Reporting Cadence](#reporting-cadence)
- [ROI Calculations](#roi-calculations)

---

## KPI Matrix by Channel

### Paid Search Metrics

| Metric | Definition | 2024-2025 Benchmark |
|--------|------------|---------------------|
| CTR | Clicks / Impressions | 6.64% average |
| CPC | Cost / Clicks | $1.45 median |
| Conversion Rate | Conversions / Clicks | 4.40% average |
| ROAS | Revenue / Ad Spend | 2x-4x |
| Quality Score | Google's relevance rating | 7+ good |

### Social Media Metrics

| Metric | Definition | Benchmark by Platform |
|--------|------------|----------------------|
| Engagement Rate | (Likes+Comments+Shares) / Followers | LinkedIn 6.5%, Instagram 3-6%, Facebook 3.6% |
| Reach | Unique accounts who saw content | Varies by content type |
| CTR (ads) | Clicks / Impressions | Facebook 1.57%, LinkedIn 0.06% |

### Email Marketing Metrics

| Metric | Definition | Benchmark |
|--------|------------|-----------|
| Open Rate | Opens / Delivered | 43.46% average |
| CTR | Clicks / Delivered | 2.09% average |
| CTOR | Clicks / Opens | 6.81% average |
| Unsubscribe Rate | Unsubscribes / Delivered | < 0.3% healthy |

### SEO Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| Organic Traffic | Visitors from search | Month-over-month growth |
| Keyword Rankings | Position for target terms | Top 10, ideally top 3 |
| Core Web Vitals | Page experience scores | All "Good" |

---

## Vanity vs Actionable Metrics

### Vanity Metrics (Avoid as Primary KPIs)

| Metric | Why It's Vanity | Better Alternative |
|--------|-----------------|-------------------|
| Total pageviews | No quality context | Engaged sessions, conversions |
| Follower count | Doesn't indicate business value | Engagement rate, conversions |
| Raw impressions | Doesn't mean seen | Viewability, brand lift |
| Email list size | Size ≠ quality | Engaged subscribers, revenue per email |

### Actionable Metrics (Track These)

| Category | Actionable Metrics |
|----------|-------------------|
| Acquisition | CAC, qualified leads, conversion rate by channel |
| Revenue | ROAS, LTV, revenue per visitor, AOV |
| Engagement | Engaged sessions, goal completions, email CTR |
| Retention | Churn rate, repeat purchase rate, NPS |

### North Star Metric Framework

| Business Type | Example North Star |
|---------------|-------------------|
| E-commerce | Revenue per visitor |
| SaaS | Monthly recurring revenue (MRR) |
| Marketplace | Gross merchandise value (GMV) |
| Content/Media | Engaged time or subscribers |
| Lead Gen | Qualified leads or pipeline value |

---

## Attribution Models

### Model Comparison

| Model | Credit Distribution | Best For |
|-------|---------------------|----------|
| First-Touch | 100% to first interaction | Demand generation, brand awareness |
| Last-Touch | 100% to final interaction | Bottom-funnel optimization |
| Linear | Equal to all touchpoints | Simple multi-touch analysis |
| Time-Decay | More to recent touchpoints | Shorter sales cycles |
| Position-Based | 40% first, 40% last, 20% middle | Balanced view |
| Data-Driven | ML-based credit | Large datasets |

### When to Use Each Model

| Scenario | Recommended Model |
|----------|-------------------|
| Evaluating brand campaigns | First-touch |
| Optimizing conversion paths | Last-touch |
| Understanding full journey | Linear or Position-based |
| Short purchase cycles (< 7 days) | Time-decay |
| Complex B2B journeys | Position-based or Data-driven |

### GA4 Attribution Settings

**Default:** Data-driven attribution (if sufficient data), falls back to cross-channel last click.

**To change:** Admin → Attribution settings → Select model → Set lookback windows

---

## GA4 Setup Checklist

### Essential Configuration (14 Points)

#### 1. Data Retention
```
Admin → Data collection and modification → Data retention
→ Set to 14 months (default is 2 months)
```

#### 2. Internal Traffic Filter
```
Admin → Data streams → Configure tag settings → Define internal traffic
→ Add office IP addresses
→ Create filter: Admin → Data filters → Create → Set to Active
```

#### 3. Unwanted Referrals
```
Admin → Data streams → Configure tag settings → List unwanted referrals
→ Add: paypal.com, stripe.com, payment gateways
```

#### 4. Google Ads Linking
```
Admin → Product links → Google Ads links → Link
```

#### 5. Search Console Linking
```
Admin → Product links → Search Console links → Link
```

#### 6. BigQuery Linking (Free)
```
Admin → Product links → BigQuery links → Link
```

#### 7. Enhanced Measurement
```
Admin → Data streams → Enhanced measurement
→ Enable: Scrolls, Outbound clicks, Site search, Video engagement, File downloads
```

#### 8. Key Events (Conversions)
```
Admin → Key events → Mark as key event
Limit: 30 key events per property
```

**Recommended key events:**
- `purchase` or `generate_lead`
- `sign_up`
- `begin_checkout`
- `add_to_cart`
- Form submissions

#### 9. Google Signals
```
Admin → Data collection → Google signals → Turn on
```

#### 10. Verify Data Flow
```
Reports → Realtime → Test with your own session
```

### Post-Setup Verification

| Check | Where |
|-------|-------|
| Data retention set | Admin → Data retention |
| Internal traffic filtered | Data filters → Active |
| Key events marked | Key events list |
| Ads linked | Product links |
| Realtime data flowing | Realtime report |

---

## Dashboard Design

### Design Principles

**3-Second Rule:** Each visualization should tell a clear story within 3 seconds.

| Principle | Implementation |
|-----------|----------------|
| Limit KPIs | 5-7 metrics per view |
| Visual hierarchy | Most important top-left |
| Context | Include comparisons (vs. prior period, vs. goal) |
| Actionability | Every metric should inform a decision |

### Chart Selection

| Data Type | Best Chart |
|-----------|------------|
| Trend over time | Line chart |
| Comparison (categories) | Bar chart |
| Part of whole | Pie/donut (limit to 5 segments) |
| Single KPI | Scorecard with comparison |

### Tool Options

| Tool | Best For | Cost |
|------|----------|------|
| Looker Studio | GA4 native, free | Free |
| Tableau | Enterprise visualization | $70+/user/month |
| Power BI | Microsoft ecosystem | $10+/user/month |

---

## Reporting Cadence

### Cadence Framework

| Frequency | Focus | Metrics |
|-----------|-------|---------|
| **Daily** | Anomaly detection | Spend, impressions, major errors |
| **Weekly** | Performance direction | CTR, CPL, engagement, traffic |
| **Monthly** | Comprehensive analysis | Conversions, revenue, CAC, channel mix |
| **Quarterly** | Strategic review | ROI, LTV, market share, budget allocation |

### Weekly Report Template

```
## Week of [Date]

### Key Metrics vs. Prior Week
- Sessions: X (↑/↓ Y%)
- Conversions: X (↑/↓ Y%)
- Revenue: $X (↑/↓ Y%)

### Channel Performance
[Table: Channel, Sessions, Conversions, Conv Rate, WoW Change]

### Top Performers
- Best campaign: [Name] — [Result]
- Best content: [Title] — [Traffic/Conversions]

### Issues & Actions
- Issue: [Description]
- Action: [What we're doing]
```

---

## ROI Calculations

### Core Formulas

#### Marketing ROI
```
ROI = (Revenue - Marketing Cost) / Marketing Cost × 100

Example: ($50,000 - $10,000) / $10,000 × 100 = 400% ROI
```

#### Return on Ad Spend (ROAS)
```
ROAS = Revenue from Ads / Ad Spend

Example: $50,000 / $10,000 = 5x ROAS
```

#### Customer Acquisition Cost (CAC)
```
CAC = Total Marketing & Sales Expenses / New Customers Acquired

Example: $100,000 / 500 customers = $200 CAC
```

#### Customer Lifetime Value (LTV)
```
LTV = Average Purchase Value × Purchase Frequency × Customer Lifespan

Example: $50 × 4 purchases/year × 3 years = $600 LTV
```

#### LTV:CAC Ratio
```
LTV:CAC = Customer Lifetime Value / Customer Acquisition Cost

Example: $600 / $200 = 3:1 ratio
```

### Benchmark Targets

| Metric | Target | Excellent |
|--------|--------|-----------|
| LTV:CAC Ratio | 3:1 | 4:1+ |
| CAC Payback | < 12 months | < 6 months |
| Marketing ROI | 100%+ | 500%+ |
| ROAS (e-commerce) | 3x | 5x+ |

### Industry Benchmarks (2024-2025)

| Metric | Average |
|--------|---------|
| Average Conversion Rate | 2.9% |
| Average CPL | $70.11 |
| YoY CPL Change | +5.13% |

---

## Quick Reference

### Metric Calculation Cheat Sheet

| Metric | Formula |
|--------|---------|
| Conversion Rate | Conversions / Visitors × 100 |
| CTR | Clicks / Impressions × 100 |
| CPC | Cost / Clicks |
| CPM | (Cost / Impressions) × 1,000 |
| ROAS | Revenue / Ad Spend |
| ROI | (Revenue - Cost) / Cost × 100 |
| CAC | Marketing Spend / New Customers |
| LTV | Avg Purchase × Frequency × Lifespan |
| Engagement Rate | Engagements / Followers × 100 |

### GA4 Quick Navigation

| Need | Path |
|------|------|
| Real-time data | Reports → Realtime |
| Traffic sources | Reports → Acquisition |
| Conversions | Reports → Engagement → Conversions |
| User explorer | Explore → User explorer |
| Funnel analysis | Explore → Funnel exploration |

### Health Check Questions

- [ ] Is conversion tracking accurate?
- [ ] Are key events marked correctly?
- [ ] Is internal traffic filtered?
- [ ] Are UTMs consistent across campaigns?
- [ ] Is data retention set to 14 months?
