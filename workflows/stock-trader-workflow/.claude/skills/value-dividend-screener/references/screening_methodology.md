# Value Dividend Stock Screening Methodology

## Overview

This screening methodology identifies high-quality dividend stocks that combine:
- **Value characteristics**: Reasonable valuations (low P/E, P/B)
- **Income generation**: Attractive dividend yields (>=3.5%)
- **Growth profile**: Consistent dividend, revenue, and EPS growth
- **Quality metrics**: Strong profitability, financial health, and dividend sustainability

## Screening Criteria

### Phase 1: Initial Quantitative Filters

#### 1. Dividend Yield >= 3.5%
**Rationale**: Provides meaningful income above typical market yields (S&P 500 average: ~1.5-2%)

**Calculation**:
```
Dividend Yield = (Annual Dividends per Share / Current Stock Price) × 100
```

**Threshold Logic**:
- 3.5%+ provides attractive income
- Not so high as to signal dividend risk (>8% often unsustainable)
- Balances income and growth potential

#### 2. P/E Ratio <= 20
**Rationale**: Identifies stocks trading at reasonable multiples relative to earnings

**Calculation**:
```
P/E Ratio = Market Price per Share / Earnings per Share (TTM)
```

**Threshold Logic**:
- S&P 500 historical average: ~15-18x
- P/E <= 20 indicates value territory
- Excludes overvalued growth stocks
- Focuses on mature, profitable companies

#### 3. P/B Ratio <= 2.0
**Rationale**: Ensures stock price is reasonable relative to book value

**Calculation**:
```
P/B Ratio = Market Price per Share / Book Value per Share
```

**Threshold Logic**:
- P/B <= 2.0 suggests reasonable valuation
- Avoids paying excessive premium over net assets
- Particularly relevant for asset-heavy businesses

### Phase 2: Growth Quality Filters

#### 4. Dividend Growth: 3-Year CAGR >= 5%
**Rationale**: Identifies companies with consistent dividend-raising track record

**Calculation**:
```
Dividend CAGR = [(End Dividend / Start Dividend)^(1/3) - 1] × 100
```

**Threshold Logic**:
- 5% annual growth compounds meaningfully over time
- Demonstrates management confidence in cash flows
- Protects against inflation (long-term average: 2-3%)
- Signals business health and shareholder commitment

**Consistency Check**:
- No dividend cuts in the period
- Allows one year of flat dividends (economic cycles)
- Cuts signal financial stress or strategy changes

#### 5. Revenue Growth: Positive 3-Year Trend
**Rationale**: Confirms top-line growth supports dividend sustainability

**Evaluation**:
- Revenue in Year 3 > Revenue in Year 1
- Allows one year of decline (cyclical businesses, one-time events)
- Overall upward trajectory required

**Why Not a Fixed %**:
- Different industries have different growth rates
- Mature dividend stocks may have modest but stable growth
- Focus is on **trend direction** rather than absolute rate

#### 6. EPS Growth: Positive 3-Year Trend
**Rationale**: Ensures earnings power is expanding, not eroding

**Evaluation**:
- EPS in Year 3 > EPS in Year 1
- Allows one year of decline
- Overall upward trajectory required

**Significance**:
- Earnings fund dividends
- EPS growth = potential for future dividend increases
- Distinguishes quality companies from dividend traps

### Phase 3: Quality & Sustainability Analysis

#### 7. Dividend Sustainability Metrics

**A. Payout Ratio**
```
Payout Ratio = (Dividends Paid / Net Income) × 100
```

**Healthy Range**: 30-70%
- < 30%: Conservative, room for growth
- 30-70%: Balanced, sustainable
- > 80%: Caution, limited flexibility

**B. Free Cash Flow Payout Ratio**
```
FCF Payout Ratio = (Dividends Paid / Free Cash Flow) × 100
where FCF = Operating Cash Flow - Capital Expenditures
```

**Healthy Range**: < 100%
- FCF is the true source of sustainable dividends
- < 100%: Dividends covered by actual cash generation
- > 100%: Unsustainable, funded by debt or asset sales

**Sustainability Flag**: ✅ if Payout Ratio < 80% AND FCF Payout Ratio < 100%

#### 8. Financial Health Metrics

**A. Debt-to-Equity Ratio**
```
D/E Ratio = Total Debt / Shareholders' Equity
```

**Healthy Range**: < 2.0
- Lower is generally better
- Varies by industry (utilities typically higher)
- < 2.0: Reasonable leverage, not overleveraged

**B. Current Ratio**
```
Current Ratio = Current Assets / Current Liabilities
```

**Healthy Range**: > 1.0 (ideally > 1.5)
- > 1.0: Can cover short-term obligations
- > 1.5: Strong liquidity cushion
- < 1.0: Liquidity risk

**Health Flag**: ✅ if D/E < 2.0 AND Current Ratio > 1.0

#### 9. Quality Score (0-100)

**Components**:

**A. Return on Equity (ROE)** - Max 50 points
```
ROE = Net Income / Shareholders' Equity

Points = min((ROE% / 20%) × 50, 50)
```

- 20%+ ROE = 50 points (excellent capital efficiency)
- 10% ROE = 25 points (average)
- < 5% ROE = poor capital returns

**B. Net Profit Margin** - Max 50 points
```
Profit Margin = (Net Income / Revenue) × 100

Points = min((Margin% / 15%) × 50, 50)
```

- 15%+ margin = 50 points (highly profitable)
- 7.5% margin = 25 points (average)
- < 3% margin = low profitability

**Quality Score Interpretation**:
- 80-100: Excellent quality (high profitability, efficiency)
- 60-79: Good quality
- 40-59: Average quality
- < 40: Below average quality

## Composite Scoring System

### Purpose
Rank stocks by overall attractiveness, balancing value, growth, and quality.

### Score Components (Total: 100 points)

1. **Dividend Growth** (Max 20 points)
   - 10%+ CAGR = 20 points
   - 5% CAGR = 10 points
   - Linear scaling

2. **Revenue Growth** (Max 15 points)
   - 10%+ CAGR = 15 points
   - 5% CAGR = 7.5 points
   - Linear scaling

3. **EPS Growth** (Max 15 points)
   - 15%+ CAGR = 15 points
   - 7.5% CAGR = 7.5 points
   - Linear scaling

4. **Dividend Sustainability** (10 points)
   - Pass (sustainable) = 10 points
   - Fail = 0 points

5. **Financial Health** (10 points)
   - Pass (healthy) = 10 points
   - Fail = 0 points

6. **Quality Score** (Max 30 points)
   - Quality Score × 0.3
   - 100 quality = 30 points
   - 50 quality = 15 points

### Interpretation

- **80-100**: Exceptional (high growth, quality, sustainability)
- **60-79**: Strong (solid all-around profile)
- **40-59**: Good (meets criteria, some trade-offs)
- **20-39**: Acceptable (passes filters but lower quality)
- **< 20**: Marginal (barely meets criteria)

## Investment Philosophy

### Why This Approach Works

1. **Value + Growth + Quality**: Combines three proven factor premiums
2. **Dividend Focus**: Signals management discipline and cash generation
3. **Sustainability Screen**: Avoids dividend traps and value traps
4. **Growth Requirements**: Ensures businesses are healthy, not declining
5. **Quality Filters**: Identifies durable competitive advantages

### What This Strategy Avoids

1. **Dividend Traps**: High yields from struggling companies (growth filters catch these)
2. **Value Traps**: Cheap stocks that stay cheap (quality metrics catch these)
3. **Overvaluation**: Growth stocks trading at expensive multiples (P/E, P/B filters)
4. **Financial Risk**: Overleveraged or illiquid companies (health metrics)

### Ideal Candidate Profile

A stock scoring highly in this screen typically:
- Operates in stable, mature industry
- Has sustainable competitive advantage (moat)
- Generates consistent free cash flow
- Committed to shareholder returns (dividends)
- Trades at reasonable valuation (not hyped)
- Growing modestly but consistently
- Strong balance sheet and profitability

Examples: Dividend Aristocrats, quality REITs (if included), stable utilities, consumer staples leaders

## Usage Notes

### Limitations

1. **Market Cap Bias**: Typically finds large/mid-cap stocks (small-caps less likely to meet all criteria)
2. **Sector Bias**: May overweight certain sectors (utilities, consumer staples, REITs)
3. **Excludes High Growth**: Tech and growth stocks generally won't qualify (by design)
4. **Historical Performance**: Past growth doesn't guarantee future results
5. **Economic Sensitivity**: Some qualified stocks may be cyclical

### Best Practices

1. **Diversification**: Don't concentrate in top 5; spread across top 20
2. **Sector Balance**: Monitor sector exposure, avoid overconcentration
3. **Rescreen Regularly**: Quarterly or semi-annually; fundamentals change
4. **Valuation Check**: Just because it passed doesn't mean buy at any price
5. **Dividend Safety**: Monitor payout ratios and cash flows quarterly
6. **Hold for Long Term**: This is a quality dividend growth strategy, not trading

### When to Sell

1. **Dividend Cut**: Immediate red flag; review business health
2. **Deteriorating Fundamentals**: Revenue/EPS declining multiple quarters
3. **Payout Ratio > 100%**: Dividend unsustainable
4. **Debt Spike**: Leverage increasing significantly without clear reason
5. **Better Opportunities**: Capital allocation to higher-scoring stocks
6. **Valuation Extreme**: Stock becomes significantly overvalued (P/E > 30, for example)

## Historical Context

### Why 3.5% Yield Threshold?

- **US 10-Year Treasury**: Historically 2-4%
- **S&P 500 Dividend Yield**: 1.5-2%
- **Equity Risk Premium**: 3.5% provides ~1.5-2% premium over Treasuries
- **Tax Efficiency**: Qualified dividends taxed favorably vs. bonds

### Why P/E <= 20?

- **S&P 500 Historical Average**: ~15-18x
- **Fair Value Range**: 15-20x for mature, stable businesses
- **Margin of Safety**: Leaves room for multiple compression
- **Cyclically Adjusted**: Not overpaying at peak earnings

### Why 5% Dividend CAGR?

- **Inflation Protection**: Beats long-term inflation (2-3%)
- **Real Income Growth**: Provides rising purchasing power
- **Achievable**: Sustainable for quality companies
- **Compound Power**: 5% doubles in 14.4 years

## References

- Benjamin Graham: "The Intelligent Investor" (value investing principles)
- Jeremy Siegel: "The Future for Investors" (dividend growth research)
- CFA Institute: Equity Valuation standards
- S&P Dow Jones Indices: Dividend Aristocrats methodology
- Morningstar: Dividend Sustainability Research
