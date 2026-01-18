# ROI Analyzer Reference Guide

## Core Formulas

### 1. ROI (Return on Investment)

```
ROI = (Net Profit / Total Investment) × 100%

Where:
Net Profit = Revenue - Total Costs
Total Costs = Investment + Operating Costs

Example:
- Investment: 100M KRW
- Revenue: 200M KRW
- Operating Costs: 50M KRW
- Net Profit: 200M - 50M - 100M = 50M KRW
- ROI: (50M / 100M) × 100% = 50%
```

### 2. Break-Even Point (BEP)

**For Project Investment**:
```
Break-Even Point = Total Investment / (Revenue per Unit - Variable Cost per Unit)

Or for subscription:
Break-Even Months = Total Investment / Monthly Net Profit

Example:
- Investment: 120M KRW
- Monthly Revenue: 20M KRW
- Monthly Costs: 10M KRW
- Monthly Net Profit: 10M KRW
- BEP: 120M / 10M = 12 months
```

**For Conversion-Based Projects**:
```
Break-Even Conversion Rate = Investment / Potential Revenue

Example (Phase 0 → Phase 1):
- Investment: 50M KRW
- Phase 1 Contract: 200M KRW
- BEP: 50M / 200M = 25% conversion needed
```

### 3. Payback Period

```
Payback Period = Investment / Annual Net Cash Flow

Or monthly:
Payback Months = Investment / Monthly Net Profit

Example:
- Investment: 240M KRW
- Monthly Profit: 20M KRW
- Payback: 240M / 20M = 12 months
```

### 4. Net Present Value (NPV)

For multi-year projects:
```
NPV = Σ (Cash Flow_t / (1 + r)^t) - Investment

Where:
- t = year (1, 2, 3...)
- r = discount rate (typically 10-15%)

Example (3 years, 10% discount):
- Y0: -200M (investment)
- Y1: +50M / 1.1 = 45.5M
- Y2: +100M / 1.21 = 82.6M
- Y3: +150M / 1.33 = 112.8M
- NPV: 45.5 + 82.6 + 112.8 - 200 = 40.9M KRW ✅
```

---

## Scenario Analysis Framework

### 3-Scenario Template

| Scenario | Probability | Key Assumptions | ROI | Assessment |
|----------|------------|-----------------|-----|------------|
| **Worst** | 10-20% | [List pessimistic] | | Risk level |
| **Realistic** | 60-70% | [List expected] | | Target |
| **Best** | 10-20% | [List optimistic] | | Upside |

### Variable Selection (Top 5)

For each scenario, vary these 5 variables:

1. **Revenue Growth Rate**
   - Worst: 50% of target
   - Realistic: Target
   - Best: 150% of target

2. **Customer Acquisition Cost (CAC)**
   - Worst: 2x budget
   - Realistic: Budget
   - Best: 0.5x budget

3. **Churn Rate**
   - Worst: 10%/month
   - Realistic: 5%/month
   - Best: 2%/month

4. **Pricing / ARPU**
   - Worst: -20% (discounts needed)
   - Realistic: Target price
   - Best: +20% (premium positioning)

5. **Time to Market / Launch Delay**
   - Worst: +3 months
   - Realistic: On time
   - Best: -1 month

### Example: B2B SaaS 3-Year Scenarios

**Assumptions**:
- Investment: 200M KRW
- Target MRR: Y1: 10M, Y2: 30M, Y3: 60M
- Monthly Costs: 15M KRW

**Worst Case** (50% revenue, 2x CAC, 10% churn):
```
| Year | MRR | ARR | Churn Impact | Net ARR | Costs | Profit |
|------|-----|-----|--------------|---------|-------|--------|
| Y1 | 5M | 60M | -20M (churn) | 40M | 180M | -140M |
| Y2 | 15M | 180M | -60M | 120M | 180M | -60M |
| Y3 | 30M | 360M | -120M | 240M | 180M | +60M |

3-Year Total: -140M (ROI: -70%) ❌
Payback: 36+ months
```

**Realistic Case** (target):
```
| Year | MRR | ARR | Churn (5%) | Net ARR | Costs | Profit |
|------|-----|-----|-----------|---------|-------|--------|
| Y1 | 10M | 120M | -6M | 114M | 180M | -66M |
| Y2 | 30M | 360M | -18M | 342M | 180M | +162M |
| Y3 | 60M | 720M | -36M | 684M | 180M | +504M |

3-Year Total: +600M (ROI: +300%) ✅
Payback: 18 months
```

**Best Case** (150% revenue, 0.5x CAC, 2% churn):
```
| Year | MRR | ARR | Churn (2%) | Net ARR | Costs | Profit |
|------|-----|-----|-----------|---------|-------|--------|
| Y1 | 15M | 180M | -4M | 176M | 180M | -4M |
| Y2 | 45M | 540M | -11M | 529M | 180M | +349M |
| Y3 | 90M | 1080M | -22M | 1058M | 180M | +878M |

3-Year Total: +1223M (ROI: +612%) ✅
Payback: 13 months
```

---

## Sensitivity Analysis

### Single-Variable Sensitivity

Test each variable independently (hold others constant):

**Example: Revenue Growth Rate Sensitivity**

| Growth Rate | Y3 ARR | 3-Year Profit | ROI | Payback |
|-------------|--------|---------------|-----|---------|
| -50% | 360M | -140M | -70% | Never |
| -25% | 540M | +240M | +120% | 30 months |
| **Target** | **720M** | **+600M** | **+300%** | **18 months** |
| +25% | 900M | +960M | +480% | 12 months |
| +50% | 1080M | +1320M | +660% | 10 months |

**Key Insight**: Revenue growth is THE critical variable (high sensitivity)

### Multi-Variable Sensitivity Matrix

Test combinations of top 2 variables:

|  | CAC -50% | CAC Target | CAC +100% |
|--|----------|-----------|-----------|
| **Revenue +50%** | ROI 800% | ROI 660% | ROI 480% |
| **Revenue Target** | ROI 400% | ROI 300% | ROI 180% |
| **Revenue -50%** | ROI 0% | ROI -70% | ROI -150% |

**Key Insight**: If CAC doubles AND revenue misses by 50%, project fails

---

## Industry Benchmarks

### SaaS Metrics (B2B)

| Metric | Seed | Series A | Series B+ |
|--------|------|----------|-----------|
| **ARR Growth** | 3x YoY | 2.5x YoY | 2x YoY |
| **CAC** | < 6mo LTV | < 12mo LTV | < 18mo LTV |
| **Churn (Annual)** | <30% | <20% | <10% |
| **Gross Margin** | 50%+ | 70%+ | 80%+ |
| **Payback Period** | <12mo | <18mo | <24mo |
| **ROI (3 years)** | 200%+ | 300%+ | 400%+ |

### E-commerce

| Metric | Target |
|--------|--------|
| **Gross Margin** | 30-50% |
| **CAC Payback** | 3-6 months |
| **Repeat Rate** | 30%+ |
| **LTV:CAC Ratio** | 3:1 minimum |
| **ROI (1 year)** | 100%+ |

### Hardware / Physical Products

| Metric | Target |
|--------|--------|
| **Gross Margin** | 40-60% |
| **Inventory Turns** | 6-12x/year |
| **Payback Period** | 6-12 months |
| **ROI (2 years)** | 150%+ |

---

## Advanced Analysis

### Customer Lifetime Value (LTV)

```
LTV = ARPU × Gross Margin % × (1 / Monthly Churn Rate)

Example (B2B SaaS):
- ARPU: 50,000 KRW/month
- Gross Margin: 80%
- Monthly Churn: 5%
- LTV: 50,000 × 0.8 × (1/0.05) = 800,000 KRW

Target: LTV:CAC ≥ 3:1
```

### Customer Acquisition Cost (CAC)

```
CAC = (Marketing Spend + Sales Spend) / New Customers

Example:
- Marketing: 10M KRW/month
- Sales: 5M KRW/month
- New Customers: 50/month
- CAC: 15M / 50 = 300,000 KRW

Target: CAC Payback < 12 months
```

### Cohort Analysis

Track each monthly cohort separately:

| Signup Month | M0 | M1 | M2 | M3 | M6 | M12 |
|--------------|----|----|----|----|----|----|
| Jan 2024 | 100% | 80% | 70% | 65% | 55% | 45% |
| Feb 2024 | 100% | 85% | 75% | 70% | 60% | ? |
| Mar 2024 | 100% | 90% | 80% | 75% | ? | ? |

**Insight**: Retention improving (Feb/Mar > Jan at same stages)

---

## Risk Assessment Framework

### Risk Scoring

| Risk Factor | Weight | Score (1-5) | Weighted Score |
|-------------|--------|-------------|----------------|
| Market Size | 20% | | |
| Competition | 15% | | |
| Technical Feasibility | 15% | | |
| Team Experience | 15% | | |
| Funding Runway | 15% | | |
| Regulatory | 10% | | |
| Economic Conditions | 10% | | |
| **Total** | **100%** | | **?/5** |

**Interpretation**:
- 4.0+: Low risk ✅
- 3.0-4.0: Moderate risk ⚠️
- <3.0: High risk ❌

### Contingency Planning

For each major risk (score ≤2), define:

```
Risk: [Description]
Likelihood: [%]
Impact: [Financial impact if occurs]
Mitigation: [Preventive actions]
Contingency: [Plan B if it happens]
Owner: [Responsible person]
```

---

## Decision Trees

### Investment Decision Tree

```
Start
├─ ROI (realistic) ≥ 100%?
│  ├─ Yes → Continue
│  └─ No → ❌ REJECT
│
├─ Payback ≤ 18 months?
│  ├─ Yes → Continue
│  └─ No → ⚠️ REVIEW (require strong strategic value)
│
├─ Break-even achievable at <50% of target?
│  ├─ Yes → Continue
│  └─ No → ⚠️ REVIEW (high execution risk)
│
├─ Worst-case ROI ≥ 0%?
│  ├─ Yes → ✅ INVEST
│  └─ No → ⚠️ REVIEW (potential loss)
```

### Phase Progression Decision (0→1→2)

```
Phase 0 Complete
├─ Conversion ≥ 70%?
│  ├─ Yes → ✅ Proceed to Phase 1
│  └─ No → Check conversion
│     ├─ 50-70%? → ⚠️ Improve & retry
│     └─ <50%? → ❌ Cancel or pivot
│
Phase 1 Complete
├─ ROI ≥ 150%?
│  ├─ Yes → ✅ Proceed to Phase 2
│  └─ No → Check metrics
│     ├─ 100-150%? → ⚠️ Optimize first
│     └─ <100%? → ❌ Pause expansion
```

---

**See Skill.md for**: Quick examples, templates, common use cases
