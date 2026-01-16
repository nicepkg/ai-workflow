# 股票交易工作流

为股票交易者打造的全面Claude Code工作流，覆盖美股、A股、港股三大市场。

## 适用人群

- 股票交易者和投资者
- 日内交易者和波段交易者
- 长期价值投资者
- 量化分析师
- 投资组合经理

## 功能特色

- **多市场覆盖**: 美股、A股、港股一站式分析
- **基本面分析**: 财务指标、估值分析、企业质量评估
- **技术面分析**: 指标、形态、趋势分析
- **资金流向追踪**: 北向/南向资金、机构持仓
- **宏观分析**: 经济数据解读、政策影响评估
- **投资组合管理**: 配置分析、风险评估、再平衡建议
- **智能选股**: 多种预设策略和自定义筛选

## 技能列表 (共25个)

### 市场专项分析

| 技能 | 描述 |
|------|------|
| `us-stock-analysis` | 美股综合基本面和技术面分析 |
| `a-share-analysis` | A股分析，考虑T+1、涨跌停、北向资金 |
| `hk-stock-analysis` | 港股分析，包含AH溢价、港股通 |

### 技术分析

| 技能 | 描述 |
|------|------|
| `technical-analyst` | 周线图技术分析，含场景概率 |
| `breadth-chart-analyst` | 市场广度和板块分析 |
| `market-environment-analysis` | 整体市场环境评估 |

### 基本面与估值

| 技能 | 描述 |
|------|------|
| `canslim-screener` | CANSLIM成长股筛选 |
| `value-dividend-screener` | 价值投资+股息策略 |
| `dividend-growth-pullback-screener` | 股息成长回调策略 |
| `pair-trade-screener` | 配对交易机会发现 |

### 资金流向与机构

| 技能 | 描述 |
|------|------|
| `cross-border-flow-tracker` | 北向/南向资金追踪 |
| `institutional-flow-tracker` | 机构资金流向分析 |

### 宏观与新闻

| 技能 | 描述 |
|------|------|
| `china-macro-analyst` | 中国宏观数据与政策分析 |
| `economic-calendar-fetcher` | 经济事件日历 |
| `earnings-calendar` | 财报发布日历 |
| `market-news-analyst` | 市场新闻分析 |

### 选股筛选

| 技能 | 描述 |
|------|------|
| `a-share-screener` | A股多条件选股器 |
| `sector-analyst` | 行业轮动分析 |

### 组合与策略

| 技能 | 描述 |
|------|------|
| `portfolio-manager` | 投资组合分析与再平衡 |
| `options-strategy-advisor` | 期权策略建议 |
| `scenario-analyzer` | 投资场景分析 |
| `weekly-trade-strategy` | 周度交易计划生成 |
| `backtest-expert` | 策略回测 |

### 特色策略

| 技能 | 描述 |
|------|------|
| `stanley-druckenmiller-investment` | 德鲁肯米勒风格宏观投资 |
| `us-market-bubble-detector` | 市场泡沫风险评估 |

## 快速开始

```bash
# 进入工作流目录
cd stock-trader-workflow

# 启动Claude Code，技能自动激活
claude

# 示例命令
"分析贵州茅台"
"帮我筛选低PE高ROE的股票"
"北向资金今天流入多少"
"analyze AAPL stock"
"当前宏观经济形势怎么样"
```

## 使用场景示例

### 美股分析
```
"分析英伟达NVDA"
"微软是否高估了"
"SPY技术面分析"
"compare TSLA vs BYD"
```

### A股分析
```
"分析宁德时代的基本面"
"茅台技术面怎么看"
"帮我筛选低估值高ROE的股票"
"北向资金重仓股有哪些"
"今天涨停的股票分析"
"给我一个价值投资选股结果"
```

### 港股分析
```
"分析腾讯港股"
"比亚迪AH溢价多少，买哪个合适"
"港股高息股推荐"
"南向资金最近买什么"
```

### 宏观分析
```
"最新CPI数据对股市的影响"
"央行降息利好什么板块"
"当前宏观经济形势分析"
"下周有什么重要经济数据"
```

### 资金流向
```
"今天北向资金流向如何"
"北向资金持股贵州茅台多少"
"外资连续加仓的股票"
"主力资金净流入最多的股票"
```

### 投资组合
```
"分析我的持仓配置"
"建议如何再平衡"
"我的组合风险敞口如何"
```

## 多AI工具支持

本工作流支持多种AI编程助手：

| 工具 | 路径 |
|-----|------|
| Claude Code | `.claude/skills/` |
| Codex | `.codex/skills/` |
| Cursor | `.cursor/skills/` |
| OpenCode | `.opencode/skill/` |

## 风险提示

本工作流仅供信息参考和学习使用，不构成投资建议。股票市场有风险，投资需谨慎。过往业绩不代表未来表现。在做出投资决策前，请自行研究并考虑咨询专业财务顾问。

## 许可证

MIT
