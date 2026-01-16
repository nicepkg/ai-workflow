# CANSLIM Methodology - William O'Neil's Growth Stock Selection System

## Overview

CANSLIM is a proven growth stock selection methodology developed by William O'Neil, founder of Investor's Business Daily (IBD). Based on comprehensive analysis of the greatest winning stocks from 1953 to the present, CANSLIM identifies 7 common characteristics that multi-bagger stocks exhibit before their major price advances.

**Historical Performance**: IBD's studies show that stocks exhibiting all 7 CANSLIM traits delivered average gains of 100-300% over 1-3 year periods, with many producing returns exceeding 1,000%.

**Investment Philosophy**: CANSLIM focuses on identifying emerging growth leaders at the beginning of their major price advances - not after they've already run. The methodology emphasizes buying quality growth stocks during brief consolidations or pullbacks in confirmed market uptrends.

---

## The 7 CANSLIM Components

### C - Current Quarterly Earnings (15% Weight)

**O'Neil's Rule**: "Look for companies whose current quarterly earnings per share are up at least 18-20% compared to the same quarter the prior year."

#### Why It Matters

Earnings are the primary fundamental driver of stock prices. Companies with accelerating quarterly earnings signal business momentum, competitive advantages, and management execution. O'Neil's research found that 3 out of 4 winning stocks showed EPS growth of at least 70% in the quarter before their major price advance began.

#### Quantitative Criteria

- **Minimum**: 18% year-over-year (YoY) quarterly EPS growth
- **Preferred**: 25%+ YoY growth
- **Exceptional**: 50%+ YoY growth with accelerating trend

#### Scoring Formula (0-100 Points)

```
100 points: EPS growth >= 50% AND revenue growth >= 25% (explosive acceleration)
 80 points: EPS growth 30-49% AND revenue growth >= 15% (strong growth)
 60 points: EPS growth 18-29% AND revenue growth >= 10% (meets minimum)
 40 points: EPS growth 10-17% (below threshold)
  0 points: EPS growth < 10% or negative
```

#### Revenue Growth Verification

**Critical Check**: EPS growth must be supported by revenue growth. If EPS grows significantly faster than revenue, investigate whether growth is driven by cost-cutting, share buybacks, or accounting adjustments rather than genuine business expansion.

**Red Flag**: EPS growth > 30% while revenue growth < 10% suggests unsustainable earnings quality.

#### Historical Examples

- **AAPL (2009 Q3)**: EPS +45% YoY (iPhone 3GS launch), stock gained 200% over next 2 years
- **NFLX (2013 Q1)**: EPS +278% YoY (streaming acceleration), stock up 400% in 18 months
- **TSLA (2020 Q3)**: EPS turned positive (first sustained profitability), stock up 700% in 12 months
- **NVDA (2023 Q2)**: EPS +429% YoY (AI chip demand), stock up 240% YTD

---

### A - Annual Earnings Growth (20% Weight)

**O'Neil's Rule**: "Annual earnings per share should be up 25% or more in each of the last three years."

#### Why It Matters

While current quarterly earnings (C) signal near-term momentum, annual earnings growth (A) validates sustained competitive advantages and business model strength. One-quarter wonders rarely sustain price gains. Multi-year consistency separates authentic growth companies from cyclical or temporary winners.

#### Quantitative Criteria

- **Minimum**: 25% annual EPS CAGR over 3 years
- **Preferred**: 30-40% annual CAGR
- **Exceptional**: 40%+ annual CAGR with no down years

#### 3-Year CAGR Calculation

```python
# Compound Annual Growth Rate formula
EPS_CAGR = ((EPS_current / EPS_3_years_ago) ^ (1/3)) - 1

# Example: MSFT 2017-2020
# EPS: $3.25 (2017) → $5.76 (2020)
# CAGR = (5.76 / 3.25) ^ (1/3) - 1 = 21.0%
```

#### Scoring Formula (0-100 Points)

```
90 points: EPS CAGR >= 40% AND stable (no down years) AND revenue CAGR >= 20%
70 points: EPS CAGR 30-39% AND stable
50 points: EPS CAGR 25-29% (meets CANSLIM minimum)
30 points: EPS CAGR 15-24% (below threshold)
 0 points: EPS CAGR < 15% or erratic (down years present)

Bonus: +10 points if all 3 years show year-over-year growth (stability bonus)
Penalty: -20% of score if revenue CAGR < 50% of EPS CAGR (buyback-driven growth)
```

#### Growth Stability Assessment

**Stable Growth** (preferred): EPS increases every year over the 3-year period
- Example: $1.00 → $1.30 → $1.69 → $2.20 (consistent 30% growth)

**Erratic Growth** (penalty): One or more years show declining EPS
- Example: $1.00 → $1.50 → $1.20 → $1.80 (volatile, uncertain)

**O'Neil's Insight**: "It's better to see three years of 25% growth than one year of 80% followed by two years of 10%."

#### Revenue Growth Validation

**Healthy Growth**: EPS CAGR and Revenue CAGR both strong (within 10 percentage points)
- Example: EPS 30% CAGR + Revenue 25% CAGR = Sustainable

**Warning Sign**: EPS CAGR >> Revenue CAGR (gap > 15 percentage points)
- Likely driven by margin expansion, buybacks, or cost cuts (less sustainable)
- Example: EPS 35% CAGR + Revenue 10% CAGR = Investigate quality

#### Historical Examples

- **V (2015-2018)**: EPS CAGR 29%, Revenue CAGR 18% → 180% stock gain
- **MA (2014-2017)**: EPS CAGR 33%, Revenue CAGR 14% → 200% stock gain
- **MSFT (2017-2020)**: EPS CAGR 21%, Revenue CAGR 13% → 280% stock gain
- **NVDA (2020-2023)**: EPS CAGR 76%, Revenue CAGR 52% → 450% stock gain

---

### N - New Products, Management, or Highs (15% Weight)

**O'Neil's Rule**: "Stocks making new price highs have no overhead supply (resistance), signaling strong demand. New products, services, or management can catalyze major moves."

#### Why It Matters

Price action near 52-week highs indicates institutional accumulation and investor demand. New products create earnings catalysts. New management brings strategic changes. The "N" component combines technical momentum (new highs) with fundamental catalysts (newness).

**Key Insight**: 95% of CANSLIM winning stocks made new all-time highs before their major advance. Stocks far from highs face resistance and lack sponsorship.

#### Quantitative Criteria

**Price Position**:
- **Ideal**: Within 5% of 52-week high
- **Acceptable**: Within 15% of 52-week high
- **Caution**: 15-25% below 52-week high
- **Avoid**: >25% below 52-week high (lacks momentum)

**Breakout Pattern** (bonus):
- New 52-week high achieved on volume 40-50%+ above average
- Signals institutional buying (large orders driving price)

#### Scoring Formula (0-100 Points)

```python
# Distance from 52-week high
distance_pct = ((current_price / week_52_high) - 1) * 100

# Base score from price position
100 points: distance <= 5% from high AND breakout detected AND new product/catalyst
 80 points: distance <= 10% from high AND breakout detected
 60 points: distance <= 15% from high OR breakout detected
 40 points: distance <= 25% from high
 20 points: distance > 25% from high (insufficient momentum)

# Bonus for new product/catalyst signals (from news)
+10-20 points: Keywords detected - "FDA approval", "new product", "patent granted", "breakthrough"
```

#### New Product/Catalyst Detection (Supplementary)

**High-Impact Catalysts**:
- FDA drug approvals (pharmaceuticals)
- New platform/service launches (technology)
- Patent grants (defensive moat)
- Strategic acquisitions (expansion)
- New management from successful companies

**Data Source**: Keyword search in recent news headlines (FMP news API)
- "FDA approval" → +20 points
- "new product", "product launch" → +10 points
- "acquisition", "expansion" → +10 points

**Note**: Price action (new highs) is the primary signal (80% of N score). New product detection is supplementary (20% of N score).

#### Historical Examples

**New Highs + New Products**:
- **AAPL (2007)**: iPhone launch + new highs → 600% gain in 5 years
- **TSLA (2020)**: Model 3 production scale + new highs → 700% gain in 12 months
- **NVDA (2023)**: AI chip (H100) demand + new highs → 240% YTD gain

**New Highs After Consolidation**:
- **MSFT (2018)**: Azure cloud growth + breakout from 3-year consolidation → 350% gain in 3 years
- **META (2023)**: AI efficiency gains + breakout from 2022 bear market → 200% gain in 12 months

**Caution - Stocks Far from Highs**:
- Stocks 30-50% below highs rarely lead; they often become "dead money" for years
- Exception: Deep pullbacks in bear markets can reset; wait for new highs in next bull market

---

### M - Market Direction (5% Weight)

**O'Neil's Rule**: "You can be right about a stock but wrong about the market, and still lose money. Three out of four stocks follow the market's trend."

#### Why It Matters

CANSLIM doesn't work in bear markets. Even the best growth stocks decline 20-50% in sustained downtrends. O'Neil's research shows:
- **Bull markets**: 75% of stocks move with market direction
- **Bear markets**: Profitable stock picking nearly impossible
- **Market timing**: Staying in cash during corrections preserves capital for next bull phase

**Critical Insight**: "The most important decision is not which stock to buy, but whether to be invested at all."

#### Quantitative Criteria

**Primary Signal**: S&P 500 vs. 50-day Exponential Moving Average (EMA)
- **Uptrend**: S&P 500 closes above 50-day EMA for 3+ consecutive days
- **Choppy/Neutral**: S&P 500 oscillating around 50-day EMA (±2%)
- **Downtrend**: S&P 500 closes below 50-day EMA for 3+ consecutive days

**Secondary Signal**: VIX (Fear Gauge)
- **Low Fear**: VIX < 15 (complacent, supportive environment)
- **Normal**: VIX 15-20 (healthy market)
- **Elevated**: VIX 20-30 (caution, potential volatility)
- **Panic**: VIX > 30 (sell signal, go to cash)

#### Scoring Formula (0-100 Points)

```python
# Calculate distance from 50-day EMA
distance_from_ema = (sp500_price / sp500_ema_50) - 1

# Market trend scoring
100 points: sp500 > EMA by 2%+ AND VIX < 15 AND follow-through day detected
 80 points: sp500 > EMA by 1-2% AND VIX < 20
 60 points: sp500 > EMA by 0-1% (early uptrend)
 40 points: sp500 within ±2% of EMA (choppy, neutral)
 20 points: sp500 < EMA by 1-3% (early downtrend)
  0 points: sp500 < EMA by 3%+ OR VIX > 30 (bear market - DO NOT BUY)
```

#### Follow-Through Day (FTD) - O'Neil's Bull Market Confirmation

**Definition**: A day when a major index (S&P 500, Nasdaq) rallies 1.25%+ on volume higher than the previous day, occurring on Day 4-10 of an attempted rally after a correction.

**Significance**:
- Signals institutional buying has resumed
- Confirms market bottoming process complete
- Green light to begin buying leading growth stocks

**Without FTD**: Rally attempts often fail; premature buying leads to losses

#### Market Direction Interpretation

**100 Points (Strong Uptrend)**:
- S&P 500 well above 50-day EMA
- VIX low (complacent)
- Follow-through day confirmed
- **Action**: Aggressively buy leading growth stocks (CANSLIM candidates)

**60 Points (Early Uptrend)**:
- S&P 500 just crossed above 50-day EMA
- Market still establishing trend
- **Action**: Start small positions (25-50% allocation)

**40 Points (Choppy/Neutral)**:
- S&P 500 oscillating around 50-day EMA
- Direction unclear
- **Action**: Reduce exposure to 25-50%, wait for confirmation

**0 Points (Downtrend/Bear Market)**:
- S&P 500 below 50-day EMA and declining
- VIX elevated or spiking
- **Action**: Sell all stocks, raise 80-100% cash, wait for FTD

#### Historical Examples

**Bull Market Phases (M Score 80-100)**:
- 2009-2011: Post-financial crisis recovery (AAPL, PCLN major winners)
- 2013-2015: QE-driven rally (NFLX, FB explosive gains)
- 2016-2018: Tax reform bull run (NVDA, AMD, FANG stocks)
- 2020-2021: Pandemic recovery (TSLA, NVDA, growth stocks)
- 2023-2024: AI boom (NVDA, META, MAG7)

**Bear Market Phases (M Score 0-20)**:
- 2008 (Financial Crisis): Even best stocks fell 40-60%
- 2011 (Debt Ceiling Crisis): 20% correction
- 2015-2016 (China Devaluation): Growth stocks down 20-30%
- 2018 (Fed Tightening): Nasdaq down 23%
- 2022 (Inflation/Fed): Nasdaq down 33%, growth stocks down 50-80%

**Key Takeaway**: In bear markets (M score < 20), CANSLIM candidates still decline despite strong fundamentals. Market direction trumps stock selection.

---

### S - Supply and Demand (15% Weight)

**O'Neil's Rule**: "Volume is the gas in the tank of a stock. Without gas, the car doesn't go anywhere. Look for stocks where volume expands on up days and contracts on down days."

#### Why It Matters

Volume patterns reveal institutional accumulation (buying) or distribution (selling). Individual investors trade in small lots (100-1,000 shares), but institutions move millions of shares. When institutions accumulate, volume surges on up days. When they distribute, volume spikes on down days. Volume precedes price - smart money moves before the crowd notices.

**Key Principle**: UP-DAY VOLUME > DOWN-DAY VOLUME = Accumulation (bullish)

#### Quantitative Criteria

**Accumulation/Distribution Analysis** (60-day period):
- Classify each day as up-day (close > previous close) or down-day (close < previous close)
- Calculate average volume for up-days vs. down-days
- **Accumulation Ratio** = Avg Up-Day Volume / Avg Down-Day Volume

**Thresholds**:
- **Strong Accumulation**: Ratio ≥ 2.0 (institutions aggressively buying)
- **Accumulation**: Ratio 1.5-2.0 (bullish volume pattern)
- **Neutral**: Ratio 1.0-1.5 (slightly positive)
- **Distribution**: Ratio 0.5-0.7 (institutions selling)
- **Strong Distribution**: Ratio < 0.5 (heavy selling pressure)

#### Scoring Formula (0-100 Points)

```python
# Calculate accumulation/distribution ratio
up_days_volume = [volume for day in last_60_days if close > prev_close]
down_days_volume = [volume for day in last_60_days if close < prev_close]

avg_up_volume = sum(up_days_volume) / len(up_days_volume)
avg_down_volume = sum(down_days_volume) / len(down_days_volume)

ratio = avg_up_volume / avg_down_volume

# Scoring
100 points: ratio >= 2.0 (Strong Accumulation)
 80 points: ratio 1.5-2.0 (Accumulation)
 60 points: ratio 1.0-1.5 (Neutral/Weak Accumulation)
 40 points: ratio 0.7-1.0 (Neutral/Weak Distribution)
 20 points: ratio 0.5-0.7 (Distribution)
  0 points: ratio < 0.5 (Strong Distribution)
```

#### Historical Examples

- **NVDA (2023)**: Up/down ratio 2.3 before 500% run (massive institutional accumulation)
- **META (2023)**: Up/down ratio 1.8 during recovery from 2022 lows
- **TSLA (2019-2020)**: Ratio 2.1 during Model 3 production ramp
- **AAPL (2019)**: Ratio 1.7 before iPhone 11 cycle launched

**Red Flag**: Ratio < 0.7 signals distribution - institutions are selling into strength. Avoid or exit positions.

---

### I - Institutional Sponsorship (10% Weight)

**O'Neil's Rule**: "You need some of the big boys on your side. Look for stocks with increasing institutional sponsorship, but not too much. The sweet spot is 50-100 institutional holders with 30-60% ownership."

#### Why It Matters

Institutional investors (mutual funds, pension funds, hedge funds) have research teams, long time horizons, and large capital pools. Their sponsorship provides:
1. **Liquidity**: Enables smooth trading without excessive slippage
2. **Price Support**: Large holders defend positions during pullbacks
3. **Discovery**: Attracts additional institutional and retail capital
4. **Validation**: Smart money confirms the investment thesis

**Key Insight**: Too little institutional ownership (< 20%) means the stock is neglected. Too much (> 80%) means institutions have already bought - no buying power left to drive future gains.

#### Quantitative Criteria

**Holder Count**:
- **Sweet Spot**: 50-100 institutional holders
- **Good**: 30-50 holders (building interest)
- **Acceptable**: 100-150 holders (getting crowded)
- **Avoid**: < 30 holders (underowned) or > 150 holders (overcrowded)

**Ownership Percentage**:
- **Ideal Range**: 30-60% institutional ownership
- **Acceptable**: 20-30% or 60-80%
- **Caution**: < 20% (neglected) or > 80% (saturated)

**Quality Signal**: Superinvestor Presence (bonus)
- Holdings by legendary investors: Berkshire Hathaway, Baupost Group, Pershing Square, Greenlight Capital, Third Point, Appaloosa Management

#### Scoring Formula (0-100 Points)

```python
# Calculate institutional ownership %
total_shares_held = sum(holder.shares for holder in institutional_holders)
ownership_pct = (total_shares_held / shares_outstanding) * 100

# Scoring logic
if 50 <= num_holders <= 100 and 30 <= ownership_pct <= 60:
    score = 100  # O'Neil's sweet spot

elif superinvestor_present and 30 <= num_holders <= 150:
    score = 90  # Superinvestor quality signal

elif (30 <= num_holders < 50 and 20 <= ownership_pct <= 40) or \
     (100 < num_holders <= 150 and 40 <= ownership_pct <= 70):
    score = 80  # Good ranges

elif (20 <= num_holders < 30 and 20 <= ownership_pct <= 50) or \
     (50 <= num_holders <= 150 and 20 <= ownership_pct <= 70):
    score = 60  # Acceptable

elif ownership_pct < 20 or ownership_pct > 80:
    score = 40  # Suboptimal ownership

elif ownership_pct < 10 or ownership_pct > 90:
    score = 20  # Extreme ownership (avoid)

else:
    score = 50  # Default

# Superinvestor bonus
if superinvestor_present and score < 100:
    score = min(score + 10, 100)
```

#### Interpretation

**100 Points (Ideal)**:
- 50-100 holders, 30-60% ownership
- **Action**: Perfect institutional backing - proceed with confidence

**90 Points (Quality Signal)**:
- Superinvestor holding + good holder count
- **Action**: Quality investors provide margin of safety

**60 Points (Acceptable)**:
- Decent institutional interest, but not optimal
- **Action**: Proceed cautiously, monitor for changes

**40 Points (Suboptimal)**:
- Either underowned (< 20%) or overcrowded (> 80%)
- **Action**: Investigate why institutions are avoiding or have saturated

**20 Points (Avoid)**:
- Extreme ownership levels (< 10% or > 90%)
- **Action**: Pass - either neglected or no buying power left

#### Historical Examples

- **NVDA (2023 Q2)**: 74 holders, 44% ownership → 240% gain YTD
- **META (2023 Q1)**: 68 holders, 51% ownership → 194% recovery
- **TSLA (2020)**: Increased from 35 to 89 holders during 700% run
- **AAPL (2019)**: Berkshire Hathaway holding (superinvestor) → confidence signal

**Warning**: Stocks with > 150 holders and > 80% ownership often underperform - institutions have already bought, creating selling pressure during any weakness.

---

## Phase 2 Implementation Notes

This Phase 2 implementation includes **C, A, N, S, I, M** components, covering 80% of the full CANSLIM methodology weight. Phase 2 adds two critical components to Phase 1:

1. **S (Supply/Demand)**: Volume-based accumulation/distribution analysis - reveals institutional buying/selling
2. **I (Institutional Sponsorship)**: Holder count and ownership percentage - validates "smart money" backing

**Key Improvements Over Phase 1**:
- More accurate filtering: Volume patterns (S) eliminate stocks with distribution
- Quality validation: Institutional backing (I) confirms investment thesis
- Better ranking: Stocks with both strong fundamentals AND institutional support rise to top
- API efficient: Phase 2 requires ~203 calls for 40 stocks (81% of free tier)

### Component Weights (Phase 2 - Renormalized)

| Component | Original Weight | Phase 2 Weight | Rationale |
|-----------|-----------------|----------------|-----------|
| C - Current Earnings | 15% | **19%** | Core fundamental - quarterly momentum |
| A - Annual Growth | 20% | **25%** | Validates sustainability |
| N - Newness | 15% | **19%** | Momentum confirmation |
| S - Supply/Demand | 15% | **19%** | Institutional accumulation signal |
| I - Institutional | 10% | **13%** | Smart money validation |
| M - Market Direction | 5% | **6%** | Gating filter |
| **Subtotal (Phase 2)** | **80%** | **100%** | Renormalized to 100% (excluding L) |

**Future Phases**:
- **Phase 3**: Add L (Leadership/RS Rank) → 100% complete CANSLIM
- **Phase 4**: FINVIZ Elite integration for 10x speed improvement

### Interpretation for Phase 2 Scores

Phase 2 implements 6 of 7 components (80% weight), providing substantially more accurate screening than Phase 1:

- **90-100 points** (Phase 2): Exceptional+ (Rare multi-bagger setup with institutional backing)
- **80-89 points** (Phase 2): Exceptional (Outstanding fundamentals + accumulation)
- **70-79 points** (Phase 2): Strong (High-quality CANSLIM stock)
- **60-69 points** (Phase 2): Above Average (Watchlist - monitor for improvement)
- **<60 points** (Phase 2): Below CANSLIM standards

**Minimum Thresholds (Phase 2)**:
All 6 components must meet baseline criteria:
- C ≥ 60 (18%+ quarterly EPS growth)
- A ≥ 50 (25%+ annual CAGR)
- N ≥ 40 (within 15% of 52-week high)
- S ≥ 40 (accumulation pattern, ratio ≥ 1.0)
- I ≥ 40 (30+ holders OR 20%+ ownership)
- M ≥ 40 (market in uptrend)

**Key Difference from Phase 1**: Phase 2 scores reflect institutional validation (S, I). A stock with great fundamentals (C, A) but distribution pattern (S < 40) will score poorly, protecting against false positives.

---

## Investment Philosophy and Best Practices

### When CANSLIM Works Best

1. **Confirmed Bull Markets**: S&P 500 above 50-day and 200-day moving averages
2. **Growth-Favoring Environment**: Low interest rates, economic expansion, innovation cycles
3. **Sector Rotation into Growth**: Technology, healthcare, consumer discretionary leading
4. **Positive Market Breadth**: Majority of stocks in uptrends (>50% above 200-day MA)

### When to Avoid CANSLIM

1. **Bear Markets**: Major indices below 200-day MA, VIX > 30
2. **Value-Favoring Markets**: High inflation, rising rates favor defensive stocks
3. **Sector Rotation into Defensives**: Utilities, consumer staples, REITs leading
4. **Negative Breadth**: Majority of stocks in downtrends, breadth deteriorating

### Position Management Rules

**Entry**:
- Buy stocks scoring 80+ (Phase 1) or 140+ (Full CANSLIM)
- Enter on pullback to 10-week moving average (best risk/reward)
- Position size: 10-20% of portfolio per stock, 5-10 total positions

**Stops**:
- Initial stop loss: 7-8% below entry (O'Neil's strict rule)
- Move to breakeven once stock up 15%
- Trail stop 10-15% below peak as stock advances

**Profit Taking**:
- Sell 20-25% of position when up 20-25% (lock in partial gains)
- Sell another 20-25% when up 50%
- Let winners run if still in Stage 2 uptrend (hold final 50%)

**Sell Signals**:
1. Stop loss hit (7-8% loss) - no exceptions
2. Market enters correction (M score drops to 0-20)
3. Fundamental deterioration (C or A component score drops below 40)
4. Climax top (parabolic move on extreme volume, then reversal)
5. Distribution (heavy volume on down days, institutional selling)

---

## Common Mistakes and How to Avoid Them

### Mistake 1: Ignoring Market Direction (M Component)

**Error**: Buying CANSLIM stocks in bear markets because "they have great fundamentals"

**Reality**: 75% of stocks follow market direction. Even perfect CANSLIM candidates decline 20-50% in sustained downtrends.

**Solution**:
- Check M component FIRST before analyzing individual stocks
- If M score < 40, raise cash to 80-100% and wait
- "Being right about a stock but wrong about the market still loses money"

### Mistake 2: Chasing Stocks Far from Highs

**Error**: Buying stocks 30-50% below 52-week highs because "they're on sale"

**Reality**: Stocks trading far from highs lack institutional sponsorship and face overhead resistance. They rarely lead the next advance.

**Solution**:
- Focus on N component: stocks within 15% of 52-week high
- Wait for proper base breakout (7-8 weeks minimum consolidation)
- "Leaders of the last bull market rarely lead the next one"

### Mistake 3: Overweighting Quarterly Earnings, Ignoring Annual Growth

**Error**: Buying stocks with explosive Q1 EPS growth (C) but erratic 3-year history (A)

**Reality**: One-quarter wonders often revert. Sustainable winners show consistent multi-year growth.

**Solution**:
- Require BOTH C >= 60 AND A >= 50 (Phase 1 scoring)
- View A component as validation of C component
- "Consistency beats volatility in long-term wealth building"

### Mistake 4: Not Cutting Losses Quickly

**Error**: Holding losing positions hoping they "come back"

**Reality**: O'Neil's studies show that cutting losses at 7-8% prevents small losses from becoming large disasters.

**Solution**:
- Set stop loss at entry (7-8% below buy price)
- No exceptions: stop hit = sell immediately
- "Your first loss is your smallest loss - take it"

---

## Conclusion

CANSLIM is a time-tested, quantitative methodology for identifying emerging growth leaders before major price advances. The system combines fundamental analysis (C, A) with technical confirmation (N, M) to filter for stocks with institutional sponsorship and momentum.

**Phase 1 MVP (C, A, N, M)** provides immediate value by screening for stocks with:
- Accelerating quarterly earnings (C)
- Consistent multi-year growth (A)
- Price momentum near new highs (N)
- Confirmation of market uptrend (M)

**Future Phases** will add supply/demand analysis (S), institutional sponsorship tracking (I), and relative strength leadership ranking (L) to create a complete implementation of O'Neil's system.

**Remember**: CANSLIM is a growth stock methodology best applied during confirmed bull markets. In bear markets, the best action is to raise cash and wait for the next follow-through day signaling institutional buying has resumed.

---

## References and Further Reading

- **"How to Make Money in Stocks"** by William J. O'Neil (4th Edition, 2009)
- **"The Successful Investor"** by William J. O'Neil (2004)
- **IBD (Investor's Business Daily)** - Daily CANSLIM stock screens and market analysis
- **MarketSmith** - IBD's institutional-grade stock analysis platform with official RS Ranks
- **Historical Studies**: IBD's analysis of 600+ winning stocks (1953-2008) validating CANSLIM
