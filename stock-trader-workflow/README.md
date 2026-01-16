# Stock Trader Workflow

A comprehensive Claude Code workflow for stock traders covering US stocks, China A-shares, and Hong Kong stocks.

[中文文档](./README_cn.md)

## Target Users

- Stock traders and investors
- Day traders and swing traders
- Long-term value investors
- Quantitative analysts
- Portfolio managers

## Features

- **Multi-Market Coverage**: US stocks, China A-shares, Hong Kong stocks
- **Fundamental Analysis**: Financial metrics, valuation, business quality
- **Technical Analysis**: Indicators, patterns, trend analysis
- **Capital Flow Tracking**: Northbound/southbound flows, institutional positioning
- **Macro Analysis**: Economic data interpretation, policy impact
- **Portfolio Management**: Allocation, risk assessment, rebalancing
- **Stock Screening**: Multiple preset strategies and custom filters

## Skills (25 total)

### Market-Specific Analysis

| Skill | Description |
|-------|-------------|
| `us-stock-analysis` | Comprehensive US stock fundamental & technical analysis |
| `a-share-analysis` | China A-share analysis with T+1, price limits, northbound flow |
| `hk-stock-analysis` | Hong Kong stock analysis with AH premium, Stock Connect |

### Technical Analysis

| Skill | Description |
|-------|-------------|
| `technical-analyst` | Weekly chart technical analysis with scenarios |
| `breadth-chart-analyst` | Market breadth and sector analysis |
| `market-environment-analysis` | Overall market condition assessment |

### Fundamental & Valuation

| Skill | Description |
|-------|-------------|
| `canslim-screener` | CANSLIM growth stock screening |
| `value-dividend-screener` | Value investing with dividend focus |
| `dividend-growth-pullback-screener` | Dividend growth on pullback strategy |
| `pair-trade-screener` | Pair trading opportunity finder |

### Capital Flow & Institutional

| Skill | Description |
|-------|-------------|
| `cross-border-flow-tracker` | Northbound/southbound capital tracking |
| `institutional-flow-tracker` | Institutional money flow analysis |

### Macro & News

| Skill | Description |
|-------|-------------|
| `china-macro-analyst` | China macro data & policy analysis |
| `economic-calendar-fetcher` | Economic event calendar |
| `earnings-calendar` | Earnings release tracking |
| `market-news-analyst` | Market news analysis |

### Stock Screening

| Skill | Description |
|-------|-------------|
| `a-share-screener` | A-share multi-criteria screening |
| `sector-analyst` | Sector rotation analysis |

### Portfolio & Strategy

| Skill | Description |
|-------|-------------|
| `portfolio-manager` | Portfolio analysis & rebalancing |
| `options-strategy-advisor` | Options strategy recommendations |
| `scenario-analyzer` | Investment scenario analysis |
| `weekly-trade-strategy` | Weekly trading plan generator |
| `backtest-expert` | Strategy backtesting |

### Special Strategies

| Skill | Description |
|-------|-------------|
| `stanley-druckenmiller-investment` | Druckenmiller-style macro investing |
| `us-market-bubble-detector` | Market bubble risk assessment |

## Quick Start

```bash
# Navigate to workflow directory
cd stock-trader-workflow

# Launch Claude Code - skills activate automatically
claude

# Example commands
"analyze AAPL stock"
"分析贵州茅台"
"compare TSLA vs BYD"
"北向资金今天流入多少"
"screen for undervalued dividend stocks"
"what's the current market environment"
```

## Example Use Cases

### US Stock Analysis
```
"Give me a comprehensive analysis of NVDA"
"Is Microsoft overvalued?"
"Technical analysis of SPY"
```

### A-Share Analysis
```
"分析宁德时代的基本面"
"茅台技术面怎么看"
"帮我筛选低估值高ROE的股票"
"北向资金重仓股有哪些"
```

### Hong Kong Stock Analysis
```
"分析腾讯港股"
"比亚迪AH溢价多少，买哪个合适"
"港股高息股推荐"
```

### Macro Analysis
```
"最新CPI数据对股市的影响"
"央行降息利好什么板块"
"当前宏观经济形势分析"
```

### Portfolio Management
```
"analyze my portfolio allocation"
"suggest rebalancing for my holdings"
"what's my portfolio's risk exposure"
```

## Multi-AI Tool Support

This workflow supports multiple AI coding assistants:

| Tool | Path |
|------|------|
| Claude Code | `.claude/skills/` |
| Codex | `.codex/skills/` |
| Cursor | `.cursor/skills/` |
| OpenCode | `.opencode/skill/` |

## Disclaimer

This workflow is for informational and educational purposes only. It does not constitute investment advice. Stock market investments carry risk, and past performance does not guarantee future results. Always do your own research and consider consulting a financial advisor before making investment decisions.

## License

MIT
