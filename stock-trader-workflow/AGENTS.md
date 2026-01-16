# Stock Trader Workflow - Agent Guide

This document describes how the AI agent should utilize the skills in this workflow.

## Skill Categories

### Market Analysis Skills

**US Market:**
- `us-stock-analysis` - Use for comprehensive US stock analysis (fundamentals + technicals)

**China A-Share Market:**
- `a-share-analysis` - Use for A-share analysis, considers T+1, price limits, northbound flow
- `a-share-screener` - Use for multi-criteria stock screening
- `china-macro-analyst` - Use for macro data and policy impact analysis
- `cross-border-flow-tracker` - Use for tracking northbound/southbound capital flows

**Hong Kong Market:**
- `hk-stock-analysis` - Use for HK stocks, includes AH premium analysis

### Technical Analysis Skills

- `technical-analyst` - Primary skill for chart analysis with scenario probability
- `breadth-chart-analyst` - Use for market breadth analysis
- `market-environment-analysis` - Use to assess overall market conditions

### Screening & Strategy Skills

- `canslim-screener` - Use for CANSLIM growth stock screening
- `value-dividend-screener` - Use for value + dividend screening
- `dividend-growth-pullback-screener` - Use for dividend stocks on pullback
- `pair-trade-screener` - Use for pair trading opportunities
- `sector-analyst` - Use for sector rotation analysis

### Portfolio & Risk Skills

- `portfolio-manager` - Use for portfolio analysis and rebalancing
- `scenario-analyzer` - Use for investment scenario analysis
- `options-strategy-advisor` - Use for options strategy recommendations
- `backtest-expert` - Use for strategy backtesting

### News & Calendar Skills

- `market-news-analyst` - Use for market news analysis
- `earnings-calendar` - Use to track earnings releases
- `economic-calendar-fetcher` - Use to track economic events

### Specialty Skills

- `institutional-flow-tracker` - Use for institutional positioning
- `stanley-druckenmiller-investment` - Use for macro-driven investing
- `us-market-bubble-detector` - Use to assess bubble risks
- `weekly-trade-strategy` - Use for weekly trading plan generation

## Routing Guide

### By User Query Language

**Chinese queries (中文):**
- Route to `a-share-analysis` for A-share stocks (600xxx, 000xxx, 300xxx, 688xxx)
- Route to `hk-stock-analysis` for HK stocks (xxx.HK, 港股)
- Route to `china-macro-analyst` for macro/policy questions
- Route to `cross-border-flow-tracker` for 北向资金/南向资金 questions
- Route to `a-share-screener` for 选股/筛选 requests

**English queries:**
- Route to `us-stock-analysis` for US stocks (AAPL, MSFT, etc.)
- Route to `technical-analyst` for chart analysis requests
- Route to `portfolio-manager` for portfolio-related questions

### By Query Type

**"Analyze [stock]" / "分析[股票]":**
1. Identify market (US/A-share/HK)
2. Use appropriate analysis skill
3. Consider combining fundamental + technical

**"Screen/filter stocks" / "选股/筛选":**
1. Use `a-share-screener` for A-shares
2. Use `canslim-screener` or `value-dividend-screener` for US

**"What's happening in the market" / "市场怎么样":**
1. Use `market-environment-analysis`
2. Supplement with `market-news-analyst`

**"Capital flow" / "资金流向":**
1. Use `cross-border-flow-tracker` for cross-border
2. Use `institutional-flow-tracker` for institutional

**"Portfolio" / "持仓/组合":**
1. Use `portfolio-manager`
2. Supplement with `scenario-analyzer` for planning

## Combination Strategies

### Comprehensive Stock Analysis
1. `us-stock-analysis` or `a-share-analysis` (fundamentals)
2. `technical-analyst` (chart analysis)
3. `institutional-flow-tracker` (smart money)

### Market Timing
1. `market-environment-analysis` (big picture)
2. `china-macro-analyst` (macro data)
3. `breadth-chart-analyst` (market breadth)

### Stock Selection Process
1. `a-share-screener` (initial filter)
2. `a-share-analysis` (deep dive on candidates)
3. `cross-border-flow-tracker` (capital flow confirmation)

### Weekly Planning
1. `economic-calendar-fetcher` (upcoming events)
2. `earnings-calendar` (earnings dates)
3. `weekly-trade-strategy` (actionable plan)

## Data Sources

Skills use web search to gather real-time data from:

**US Markets:**
- Yahoo Finance, MarketWatch, Seeking Alpha, Bloomberg, TradingView

**China A-Shares:**
- 东方财富 (eastmoney.com)
- 同花顺 (10jqka.com.cn)
- 雪球 (xueqiu.com)
- 巨潮资讯 (cninfo.com.cn)

**Hong Kong:**
- 港交所 (hkexnews.hk)
- 阿斯达克 (aastocks.com)

## Output Standards

1. **Use tables** for financial data and comparisons
2. **Include data sources** and dates
3. **Present both bull and bear cases**
4. **Provide specific price levels** for targets and stops
5. **Always include risk disclaimers**
6. **Use Chinese** when user queries in Chinese
7. **Quantify** wherever possible (percentages, ratios)
