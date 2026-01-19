<div align="center">

# 📊 Stock Trader Workflow

### **Your AI Investment Research Team**

[← Back to AI Workflow](../../README.md)

[简体中文](./README_cn.md) | English

</div>

---

## 🎯 Who Is This For?

- **Stock Traders** - Day trading & swing trading
- **Value Investors** - Long-term fundamentals
- **Quant Analysts** - Data-driven strategies
- **Portfolio Managers** - Allocation & risk

---

## ⚡ Quick Install

```bash
# Install all 29 skills with one command
npx add-skill nicepkg/ai-workflow/workflows/stock-trader-workflow

# Or install specific skills
npx add-skill nicepkg/ai-workflow/workflows/stock-trader-workflow --skill a-share-analysis
```

---

## 🌍 Multi-Market Coverage

| Market | Skills | Features |
|:-------|:------:|:---------|
| 🇺🇸 **US Stocks** | 10 | Fundamental, Technical, Options, Bubble Detection |
| 🇨🇳 **A-Shares** | 9 | T+1, Price limits, Northbound flow, AKShare Data |
| 🇭🇰 **HK Stocks** | 4 | AH Premium, Stock Connect |
| 🇹🇼 **TW Stocks** | 1 | Shioaji Trading API |

---

## 📦 Skills Included (29)

### 1️⃣ Market Data & Foundation
| Skill | What It Does |
|:------|:-------------|
| `akshare` | China market data foundation (A-shares, futures, funds) |
| `股票分析` | A/HK stock analysis with technical indicators |

### 2️⃣ Market Analysis
| Skill | What It Does |
|:------|:-------------|
| `us-stock-analysis` | US stock fundamental & technical analysis |
| `a-share-analysis` | China A-share with T+1, price limits |
| `hk-stock-analysis` | Hong Kong with AH premium analysis |
| `technical-analyst` | Weekly chart analysis with scenarios |
| `market-environment-analysis` | Overall market condition assessment |
| `breadth-chart-analyst` | Market breadth and internals |

### 3️⃣ Capital Flow Tracking
| Skill | What It Does |
|:------|:-------------|
| `cross-border-flow-tracker` | Northbound/southbound capital tracking |
| `institutional-flow-tracker` | Institutional money flow |

### 4️⃣ Stock Screening
| Skill | What It Does |
|:------|:-------------|
| `stock-screener` | General multi-criteria stock screening |
| `a-share-screener` | A-share specific screening |
| `canslim-screener` | CANSLIM growth stock screening |
| `value-dividend-screener` | Value + dividend strategy |
| `dividend-growth-pullback-screener` | Dividend stocks on pullback |
| `pair-trade-screener` | Pair trading opportunities |

### 5️⃣ Sector & Macro Analysis
| Skill | What It Does |
|:------|:-------------|
| `sector-analyst` | Sector rotation analysis |
| `china-macro-analyst` | China macro data & policy |
| `economic-calendar-fetcher` | Economic events calendar |
| `earnings-calendar` | Earnings releases tracking |
| `market-news-analyst` | News impact analysis |

### 6️⃣ Portfolio & Risk Management
| Skill | What It Does |
|:------|:-------------|
| `portfolio-manager` | Allocation & rebalancing |
| `options-strategy-advisor` | Options strategies |
| `backtest-expert` | Strategy backtesting |
| `scenario-analyzer` | Investment scenario analysis |

### 7️⃣ Strategy & Trading
| Skill | What It Does |
|:------|:-------------|
| `weekly-trade-strategy` | Weekly trading plan generation |
| `stanley-druckenmiller-investment` | Macro-driven investment approach |
| `us-market-bubble-detector` | Bubble risk assessment |
| `shioaji` | Taiwan market trading API integration |

---

## 🔄 Professional Trading Pipeline

```
Stage 1: Pre-Market Research
├── economic-calendar-fetcher → Upcoming economic events
├── earnings-calendar → Earnings releases this week
├── market-environment-analysis → Market conditions
└── china-macro-analyst → Macro outlook

Stage 2: Stock Screening
├── stock-screener → Initial broad filtering
├── a-share-screener → A-share specific criteria
├── canslim-screener → Growth stock identification
└── value-dividend-screener → Value stock identification

Stage 3: Deep Analysis
├── us-stock-analysis / a-share-analysis → Fundamental analysis
├── technical-analyst → Chart patterns & levels
├── institutional-flow-tracker → Smart money tracking
└── cross-border-flow-tracker → Capital flow confirmation

Stage 4: Risk Assessment
├── scenario-analyzer → Bull/bear/base cases
├── us-market-bubble-detector → Bubble risk check
├── options-strategy-advisor → Hedging strategies
└── portfolio-manager → Position sizing

Stage 5: Execution
├── shioaji → Taiwan market orders
└── weekly-trade-strategy → Actionable trading plan

Stage 6: Post-Market Review
├── market-news-analyst → News impact review
├── breadth-chart-analyst → Market breadth analysis
└── portfolio-manager → Performance tracking
```

---

## 💡 Example Workflows

### Pre-Market Prep
```
1. "What economic events are scheduled this week?"
2. "Any major earnings releases to watch?"
3. "What's the current market environment?"
4. "Analyze northbound capital flow trends"
```

### Growth Stock Discovery (US)
```
1. "Run CANSLIM screener for US stocks"
2. "Analyze NVDA fundamentals and technicals"
3. "What's the institutional positioning in NVDA?"
4. "Is NVDA at bubble risk levels?"
5. "Create a weekly trading plan for NVDA"
```

### A-Share Value Investing
```
1. "Screen A-shares with low PE and high ROE"
2. "Analyze Kweichow Moutai fundamentals"
3. "What's the recent northbound capital flow trend?"
4. "Give me a value investing portfolio recommendation"
5. "What's the trading plan for this week?"
```

### Hong Kong Arbitrage
```
1. "Analyze Tencent HK stock"
2. "BYD AH premium analysis"
3. "Which HK sectors are southbound funds flowing into?"
4. "Give me AH premium arbitrage opportunities"
```

### Macro-Driven Trading
```
1. "Analyze current macro environment"
2. "Which sectors benefit from rate cuts?"
3. "Run Druckenmiller-style macro analysis"
4. "What's the scenario analysis for a recession?"
```

### Risk Management
```
1. "Analyze my portfolio for risk exposure"
2. "What options strategies can hedge my positions?"
3. "Backtest this strategy on historical data"
4. "Run scenario analysis for 20% market drop"
```

---

## 🔧 Prerequisites

| Skill | Requirement |
|-------|-------------|
| `akshare` | Python + AKShare library |
| `shioaji` | Shioaji API credentials (Taiwan market) |
| `股票分析` | Web search access |
| `stock-screener` | Web search access |

```bash
# For akshare skill
pip install akshare

# For shioaji skill (Taiwan market)
pip install shioaji
```

---

## 📊 Data Sources

| Market | Sources |
|:-------|:--------|
| US | Yahoo Finance, MarketWatch, Seeking Alpha, Bloomberg, TradingView |
| A-Shares | East Money, Tonghuashun, Xueqiu, CNINFO, AKShare |
| Hong Kong | HKEX, AASTOCKS |
| Taiwan | Shioaji API, TWSE |

---

## ⚠️ Disclaimer

This workflow is for **informational and educational purposes only**. It does not constitute investment advice. Stock market investments carry risk. Always do your own research.

---

## 📄 License

MIT © [nicepkg](https://github.com/nicepkg)

<div align="center">

**[⬆ Back to Main Project](../../README.md)**

</div>
