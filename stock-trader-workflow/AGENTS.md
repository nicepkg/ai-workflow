# Stock Trader Workflow - AI Instructions

AI execution guide for stock trader workflow with 29 skills for professional trading and investment analysis.

## Available Skills (29)

### 1. Market Data & Foundation
| Skill | Trigger |
|-------|---------|
| akshare | AKShare data, China market data, A-share data, futures data, fund data |
| 股票分析 | 股票分析, A股分析, 港股分析, technical indicators, 技术指标 |

### 2. Market Analysis
| Skill | Trigger |
|-------|---------|
| us-stock-analysis | US stocks, AAPL, MSFT, NVDA, American stocks, analyze [ticker] |
| a-share-analysis | A股, A-share, 600xxx, 000xxx, 300xxx, 688xxx, 沪深, 分析[股票] |
| hk-stock-analysis | 港股, HK stocks, xxx.HK, 腾讯, 阿里, Hong Kong |
| technical-analyst | chart analysis, technicals, support, resistance, patterns, 技术面 |
| market-environment-analysis | market conditions, overall market, 市场环境, big picture |
| breadth-chart-analyst | market breadth, advance/decline, internals, 市场广度 |

### 3. Capital Flow Tracking
| Skill | Trigger |
|-------|---------|
| cross-border-flow-tracker | northbound, southbound, 北向资金, 南向资金, Stock Connect |
| institutional-flow-tracker | institutional, smart money, 机构资金, hedge fund, 主力 |

### 4. Stock Screening
| Skill | Trigger |
|-------|---------|
| stock-screener | screen stocks, filter, find stocks, multi-criteria, 筛选股票 |
| a-share-screener | A股选股, A-share screen, 选股, 筛选A股 |
| canslim-screener | CANSLIM, growth stocks, CAN SLIM, William O'Neil |
| value-dividend-screener | value stocks, dividends, low PE, high ROE, 价值股, 股息 |
| dividend-growth-pullback-screener | dividend growth, pullback, 股息成长, 回调买入 |
| pair-trade-screener | pair trade, spread, arbitrage, 配对交易, 套利 |

### 5. Sector & Macro Analysis
| Skill | Trigger |
|-------|---------|
| sector-analyst | sector, industry, rotation, 行业, 板块, 轮动 |
| china-macro-analyst | China macro, policy, 宏观, 政策, 央行, GDP, PMI |
| economic-calendar-fetcher | economic calendar, events, 经济日历, 数据发布 |
| earnings-calendar | earnings, 财报, quarterly report, 季报, 业绩 |
| market-news-analyst | news, headlines, impact, 新闻, 消息面 |

### 6. Portfolio & Risk Management
| Skill | Trigger |
|-------|---------|
| portfolio-manager | portfolio, allocation, rebalance, 持仓, 组合, 配置 |
| options-strategy-advisor | options, calls, puts, hedge, 期权, 对冲 |
| backtest-expert | backtest, historical test, 回测, 历史测试 |
| scenario-analyzer | scenario, what if, bull case, bear case, 情景分析 |

### 7. Strategy & Trading
| Skill | Trigger |
|-------|---------|
| weekly-trade-strategy | weekly plan, trading plan, 周度计划, 交易计划 |
| stanley-druckenmiller-investment | Druckenmiller, macro trading, 宏观交易 |
| us-market-bubble-detector | bubble, overvalued, frothy, 泡沫, 高估 |
| shioaji | Taiwan, 台股, TW market, Shioaji API, 台湾 |

## Professional Trading Pipeline

```
Stage 1: Pre-Market Research (盘前研判)
├── economic-calendar-fetcher → Check economic events
├── earnings-calendar → Track earnings releases
├── market-environment-analysis → Assess market conditions
├── china-macro-analyst → Review macro data
└── market-news-analyst → Scan important news

Stage 2: Stock Screening (选股扫描)
├── stock-screener → Broad multi-criteria filtering
├── a-share-screener → A-share specific criteria
├── canslim-screener → Growth stock identification
├── value-dividend-screener → Value stock identification
└── pair-trade-screener → Arbitrage opportunities

Stage 3: Deep Analysis (深度分析)
├── us-stock-analysis → US stock fundamentals
├── a-share-analysis → A-share fundamentals
├── hk-stock-analysis → HK stock analysis
├── 股票分析 → Chinese stock with technicals
├── technical-analyst → Chart patterns & levels
├── institutional-flow-tracker → Smart money tracking
└── cross-border-flow-tracker → Capital flow confirmation

Stage 4: Risk Assessment (风险评估)
├── scenario-analyzer → Bull/bear/base cases
├── us-market-bubble-detector → Bubble risk check
├── options-strategy-advisor → Hedging strategies
└── portfolio-manager → Position sizing

Stage 5: Execution (下单执行)
├── shioaji → Taiwan market orders
└── weekly-trade-strategy → Actionable trading plan

Stage 6: Post-Market Review (盘后复盘)
├── market-news-analyst → News impact review
├── breadth-chart-analyst → Market breadth analysis
└── portfolio-manager → Performance tracking
```

## Skill Combinations

### Comprehensive Stock Analysis
```
akshare → a-share-analysis → technical-analyst
→ institutional-flow-tracker → portfolio-manager
```

### Growth Stock Discovery (CANSLIM)
```
canslim-screener → us-stock-analysis → technical-analyst
→ us-market-bubble-detector → weekly-trade-strategy
```

### A-Share Value Investing
```
value-dividend-screener → a-share-analysis → cross-border-flow-tracker
→ portfolio-manager → weekly-trade-strategy
```

### Macro-Driven Trading
```
china-macro-analyst → sector-analyst → a-share-screener
→ 股票分析 → scenario-analyzer
```

### AH Arbitrage
```
hk-stock-analysis + a-share-analysis → cross-border-flow-tracker
→ pair-trade-screener → portfolio-manager
```

### Weekly Planning
```
economic-calendar-fetcher → earnings-calendar → market-environment-analysis
→ weekly-trade-strategy
```

## Routing Guide

### By User Query Language

**Chinese queries (中文):**
- Route to `a-share-analysis` for A-share stocks (600xxx, 000xxx, 300xxx, 688xxx)
- Route to `hk-stock-analysis` for HK stocks (xxx.HK, 港股)
- Route to `china-macro-analyst` for macro/policy questions
- Route to `cross-border-flow-tracker` for 北向资金/南向资金 questions
- Route to `a-share-screener` for 选股/筛选 requests
- Route to `股票分析` for technical analysis requests

**English queries:**
- Route to `us-stock-analysis` for US stocks (AAPL, MSFT, etc.)
- Route to `technical-analyst` for chart analysis requests
- Route to `portfolio-manager` for portfolio-related questions
- Route to `stock-screener` for general screening

### By Query Type

**"Analyze [stock]" / "分析[股票]":**
1. Identify market (US/A-share/HK)
2. Use appropriate analysis skill
3. Consider combining fundamental + technical

**"Screen/filter stocks" / "选股/筛选":**
1. Use `stock-screener` for general filtering
2. Use `a-share-screener` for A-shares
3. Use `canslim-screener` or `value-dividend-screener` for specific strategies

**"What's happening in the market" / "市场怎么样":**
1. Use `market-environment-analysis`
2. Supplement with `market-news-analyst`
3. Check `breadth-chart-analyst` for internals

**"Capital flow" / "资金流向":**
1. Use `cross-border-flow-tracker` for cross-border
2. Use `institutional-flow-tracker` for institutional

**"Portfolio" / "持仓/组合":**
1. Use `portfolio-manager`
2. Supplement with `scenario-analyzer` for planning

**"Weekly plan" / "本周计划":**
1. Start with `economic-calendar-fetcher`
2. Check `earnings-calendar`
3. Generate with `weekly-trade-strategy`

## Quality Gates

1. **Before Stock Selection**: Run market-environment-analysis
2. **After Screening**: Deep dive with analysis skills
3. **Before Entry**: Run scenario-analyzer for risk assessment
4. **Position Sizing**: Use portfolio-manager
5. **Weekly Review**: Run breadth-chart-analyst + market-news-analyst

## Output Standards

### Stock Analysis
- Use tables for financial data
- Include both bull and bear cases
- Provide specific price levels (support, resistance, targets)
- Show PE, PB, ROE, revenue growth
- Include data sources and dates

### Screening Results
- Top 10-20 candidates
- Key metrics in table format
- Brief rationale for each
- Next steps for deep dive

### Trading Plans
- Clear entry/exit levels
- Position size recommendations
- Stop loss levels
- Time horizon
- Risk/reward ratio

### Macro Analysis
- Key data points
- Policy implications
- Sector impact
- Historical comparison

## Data Sources

**US Markets:**
- Yahoo Finance, MarketWatch, Seeking Alpha, Bloomberg, TradingView

**China A-Shares:**
- AKShare (akshare skill)
- 东方财富 (eastmoney.com)
- 同花顺 (10jqka.com.cn)
- 雪球 (xueqiu.com)
- 巨潮资讯 (cninfo.com.cn)

**Hong Kong:**
- 港交所 (hkexnews.hk)
- 阿斯达克 (aastocks.com)

**Taiwan:**
- Shioaji API
- 台湾证交所

## Prerequisites

| Skill | Requirement |
|-------|-------------|
| akshare | Python + `pip install akshare` |
| shioaji | Shioaji API credentials + `pip install shioaji` |
| 股票分析 | Web search access |
| stock-screener | Web search access |

## Risk Disclaimer

All skills in this workflow are for **informational and educational purposes only**. They do not constitute investment advice. Always do your own research and consult with qualified financial advisors before making investment decisions.
