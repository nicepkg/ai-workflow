# Developer Product Metrics

Comprehensive guide to measuring success for technical products, developer tools, and APIs.

---

## Why Developer Metrics Are Different

Developer products have unique characteristics:
- **High technical barriers** to adoption
- **Longer evaluation** periods
- **Community-driven** growth
- **Usage-based** pricing models
- **Quality over quantity** (one great developer > 100 casual users)

Traditional B2B SaaS metrics don't always apply directly.

---

## The Developer Funnel

```
Awareness → Interest → Evaluation → Activation → Engagement → Retention → Monetization
```

Each stage has specific metrics.

---

## 1. Awareness Metrics

### Top-of-Funnel

**Website Traffic:**
- Documentation page views
- Landing page visits
- Blog traffic
- GitHub repository views

**Search & Discovery:**
- Organic search rankings (for key terms)
- GitHub stars
- Stack Overflow mentions
- Social media mentions

**Community Presence:**
- Discord/Slack members
- Reddit subscribers
- Newsletter subscribers
- Conference attendance

**Targets (vary by company):**
- 50K monthly docs views (early stage)
- 500K monthly docs views (growth stage)
- 1K+ GitHub stars (open source component)

---

## 2. Interest Metrics

### Consideration Stage

**Engagement:**
- Time on documentation
- Pages per session
- Video views (tutorials)
- GitHub README views

**Content Consumption:**
- Blog post reads
- Tutorial completion rate
- Demo video watch time
- Webinar registrations

**Social Proof:**
- Case study views
- Customer testimonials read
- Comparison page visits

**Targets:**
- 5+ minute average session duration
- 4+ pages per session
- 50%+ video completion rate

---

## 3. Evaluation Metrics

### Trial/Sandbox Stage

**Sign-Up:**
- Developer sign-ups
- API key requests
- Sandbox activations
- Free tier activations

**Time to Value:**
- **Time to first API call** (target: < 10 minutes)
- **Time to "Hello World"** (target: < 15 minutes)
- **Time to integration** (target: < 1 hour)

**Documentation Engagement:**
- Getting started guide views
- Code sample copies
- SDK downloads
- Postman collection imports

**Targets:**
- 1K+ sign-ups per month (early stage)
- 60% make first API call within 24 hours
- 10 minutes median time to first call

---

## 4. Activation Metrics

### First Value Realized

**Critical Activation Events:**
- **First successful API call**
- **First integration deployed**
- **First production request**
- **SDK installed and used**
- **Sandbox → production migration**

**Activation Rate:**
```
Activation Rate = (Users who complete activation event) / (Total sign-ups)
```

**Depth of Activation:**
- Features explored
- Endpoints called
- SDKs used
- Integrations enabled

**Targets:**
- 50-70% activation rate (first API call)
- 30-40% activation rate (production deployment)
- 80%+ complete getting started guide

---

## 5. Engagement Metrics

### Active Usage

**Daily/Weekly/Monthly Active Developers (DAD/WAD/MAD):**
```
DAD = Unique developers making API calls daily
WAD = Unique developers active weekly
MAD = Unique developers active monthly
```

**Stickiness:**
```
Stickiness = DAD / MAD
```
- Target: > 20% (good)
- Target: > 40% (excellent)

**API Usage:**
- **Total API calls** per day/week/month
- **API calls per developer**
- **Endpoints used** per developer
- **Error rate** (target: < 1%)

**Feature Adoption:**
- % of developers using key features
- Time to feature adoption
- Feature depth (how many features per user)

**Targets:**
- 40%+ stickiness (DAD/MAD)
- 1K+ API calls per active developer per month
- < 1% error rate
- 3+ features adopted per developer

---

## 6. Retention Metrics

### Developer Retention

**Cohort Retention:**
```
Day 1 Retention = Developers active on Day 1 / Total sign-ups
Day 7 Retention = Developers active on Day 7 / Total sign-ups
Day 30 Retention = Developers active on Day 30 / Total sign-ups
```

**Typical Developer Product Retention:**
- Day 1: 60-70%
- Day 7: 30-50%
- Day 30: 20-40%
- Day 90: 15-30%

**Why Developer Retention Is Lower:**
- Evaluation period (many are just testing)
- Project-based usage (finish project, stop using)
- This is normal and expected

**Churn Rate:**
```
Monthly Churn = Developers who stopped using / Active developers at month start
```

**Resurrection Rate:**
```
Resurrection = Churned developers who return / Total churned developers
```

**Targets:**
- < 5% monthly churn (paid users)
- 40%+ Day 7 retention
- 25%+ Day 30 retention

---

## 7. Monetization Metrics

### Revenue Metrics

**Conversion Metrics:**
```
Free → Paid Conversion Rate = Paid users / Total active users
```
- Target: 3-10% (varies widely by product)

**Revenue Metrics:**
- **MRR** (Monthly Recurring Revenue)
- **ARR** (Annual Recurring Revenue)
- **ARPU** (Average Revenue Per User)
- **Net Revenue Retention** (NRR)

**Usage-Based Pricing Metrics:**
- **Average API calls per paid user**
- **Tier distribution** (how many in each pricing tier)
- **Upgrade rate** (free → paid, basic → pro)
- **Expansion revenue** (existing customers spending more)

**Targets:**
- 5%+ free-to-paid conversion
- 110%+ Net Revenue Retention
- $50-$500 ARPU (varies by product)

---

## Developer-Specific Metrics

### Code Quality Metrics

**SDK Quality:**
- **Downloads** per month
- **GitHub stars**
- **Issues opened** vs. closed
- **PR acceptance** rate
- **Time to resolve** issues

**Documentation Quality:**
- **Search success** rate (did they find what they needed?)
- **Time on page** (too short = unclear, too long = can't find)
- **Bounce rate** on docs
- **Feedback** (thumbs up/down on docs pages)

**Targets:**
- 90%+ search success rate
- < 40% bounce rate on docs
- 80%+ positive feedback on docs

---

### Developer Experience Metrics

**Time-Based:**
- Time to first API call
- Time to production
- Time to integrate
- Time to debug

**Friction Points:**
- Authentication failures
- API errors
- SDK install issues
- Documentation gaps

**Support Metrics:**
- Support tickets per MAD
- Time to first response
- Time to resolution
- Community forum response time

**Targets:**
- < 5 minutes to first API call
- < 1 support ticket per 100 MAD
- < 4 hours first response time
- 90%+ questions answered by community

---

## Developer Satisfaction

### Net Promoter Score (NPS)

Survey question: "How likely are you to recommend [product] to other developers?"

**Scale:** 0-10

**Calculation:**
```
NPS = % Promoters (9-10) - % Detractors (0-6)
```

**Developer Product Benchmarks:**
- **Excellent:** NPS > 50
- **Good:** NPS 30-50
- **Needs Work:** NPS < 30

### Developer Sentiment

**Qualitative Indicators:**
- Social media sentiment
- Community forum tone
- GitHub issue sentiment
- Review site ratings (G2, Capterra)
- Stack Overflow sentiment

**Quantitative Tracking:**
- Positive vs. negative mentions
- Sentiment score (automated analysis)
- Review ratings (1-5 stars)

---

## Launch-Specific Metrics

### Launch Day Metrics

**Day 1:**
- Sign-ups / API keys
- First API calls
- Documentation views
- Blog post views
- Social media impressions
- Email open rate
- Email click rate

**Targets (Tier 1 launch):**
- 5K+ sign-ups
- 50%+ activation rate (first call)
- 100K+ docs views
- 50K+ blog views

---

### Week 1 Metrics

- Total sign-ups
- Day 7 retention rate
- Active developers
- API calls made
- Support tickets
- Community questions
- Social mentions

**Targets (Tier 1):**
- 10K+ total sign-ups
- 40%+ Day 7 retention
- 5K+ active developers
- 1M+ API calls
- < 50 support tickets

---

### Month 1 Metrics

- Monthly Active Developers (MAD)
- Free → paid conversion
- NPS score
- Documentation coverage (no major gaps)
- Community health
- Feature adoption

**Targets (Tier 1):**
- 25K+ MAD
- 3-5% paid conversion
- NPS > 40
- 80%+ positive doc feedback

---

## Metrics Dashboard Template

### Executive Dashboard

**Adoption:**
- Total Developers: [X]
- MAD: [X]
- Growth Rate: [X%]

**Engagement:**
- DAD/MAD: [X%]
- API Calls/Day: [X]
- Error Rate: [X%]

**Retention:**
- Day 7: [X%]
- Day 30: [X%]
- Churn: [X%]

**Revenue:**
- MRR: $[X]
- ARPU: $[X]
- NRR: [X%]

**Quality:**
- NPS: [X]
- Support Tickets/MAD: [X]

---

### Product Team Dashboard

**This Week:**
- New Developers: [X]
- Activation Rate: [X%]
- Features Adopted: [X]
- Top API Endpoints: [List]

**Trends:**
- MAD (7-day trend): [Graph]
- API Calls (7-day): [Graph]
- Error Rate (7-day): [Graph]

**Health:**
- Documentation Gaps: [Count]
- Open Issues: [Count]
- P0 Bugs: [Count]

---

## Metric Collection

### Where to Track

**Product Analytics:**
- Amplitude
- Mixpanel
- Heap
- PostHog

**API Analytics:**
- Moesif
- API metrics (custom)
- CloudWatch / Datadog

**Documentation Analytics:**
- Google Analytics
- Readme.io analytics
- GitBook analytics

**Developer Feedback:**
- Intercom
- Zendesk
- Community forum analytics
- Survey tools (Delighted, SurveyMonkey)

---

## Setting Targets

### Early Stage (0-1 year)

Focus on **activation** and **engagement**:
- Sign-ups: 1K-10K/month
- Activation: 50%+
- MAD: 500-5K
- Day 7 Retention: 30%+

### Growth Stage (1-3 years)

Focus on **scale** and **retention**:
- Sign-ups: 10K-50K/month
- MAD: 10K-100K
- Day 30 Retention: 25%+
- Free→Paid: 5%+

### Mature Stage (3+ years)

Focus on **efficiency** and **expansion**:
- MAD: 100K+
- NRR: 110%+
- ARPU: Increasing
- CAC Payback: < 12 months

---

## Common Pitfalls

### Vanity Metrics

**Avoid:**
- Total registered users (most are inactive)
- Total API calls (could be from one user)
- GitHub stars alone (may not use product)

**Focus on:**
- Active users (making API calls)
- Retained users (coming back)
- Engaged users (using multiple features)

### Wrong Benchmarks

Don't compare developer product metrics to:
- B2C social apps (much higher DAU/MAU)
- Enterprise SaaS (lower volume, higher ACV)
- E-commerce (transactional, not sustained use)

Use developer product benchmarks instead.

---

## Summary: Key Metrics to Track

**Must Track:**
1. Monthly Active Developers (MAD)
2. Activation Rate (first API call)
3. Day 7 & Day 30 Retention
4. Stickiness (DAD/MAD)
5. API Error Rate
6. NPS

**Should Track:**
7. Free → Paid Conversion
8. Time to First API Call
9. Documentation Effectiveness
10. Support Ticket Volume

**Nice to Have:**
11. GitHub Stars/Activity
12. Community Engagement
13. Social Sentiment
14. Feature Adoption Depth

Start with the must-track metrics, then expand.

---

## Developer Metric Formulas

Quick reference:

```
Activation Rate = Activated Users / Sign-ups
Stickiness = DAD / MAD
Churn Rate = Users Lost / Total Users
NRR = (MRR + Expansion - Churn) / Starting MRR
LTV = ARPU / Churn Rate
CAC Payback = CAC / (ARPU * Gross Margin)
```

**Remember:** Metrics should drive action, not just reporting. If a metric doesn't change behavior, don't track it.
