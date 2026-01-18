<div align="center">

# 📊 股票交易工作流

### **你的 AI 投研团队**

[← 返回 AI Workflow](../README_cn.md)

简体中文 | [English](./README.md)

</div>

---

## 🎯 适合谁？

- **股票交易者** - 日内交易、波段交易
- **价值投资者** - 长期基本面
- **量化分析师** - 数据驱动策略
- **组合经理** - 配置与风险管理

---

## ⚡ 快速安装

```bash
# 一键安装全部 29 个技能
npx add-skill nicepkg/ai-workflow/stock-trader-workflow

# 或安装单个技能
npx add-skill nicepkg/ai-workflow/stock-trader-workflow --skill a-share-analysis
```

---

## 🌍 多市场覆盖

| 市场 | 技能数 | 特色功能 |
|:-----|:------:|:---------|
| 🇺🇸 **美股** | 10 | 基本面、技术面、期权、泡沫检测 |
| 🇨🇳 **A股** | 9 | T+1、涨跌停、北向资金、AKShare数据 |
| 🇭🇰 **港股** | 4 | AH溢价、港股通 |
| 🇹🇼 **台股** | 1 | Shioaji交易API |

---

## 📦 包含技能 (29个)

### 1️⃣ 市场数据底座
| 技能 | 功能描述 |
|:-----|:---------|
| `akshare` | 中国市场数据底座（A股、期货、基金） |
| `股票分析` | A股/港股分析（含技术指标） |

### 2️⃣ 市场分析
| 技能 | 功能描述 |
|:-----|:---------|
| `us-stock-analysis` | 美股基本面和技术面分析 |
| `a-share-analysis` | A股分析（T+1、涨跌停） |
| `hk-stock-analysis` | 港股分析（AH溢价） |
| `technical-analyst` | 周线图技术分析 |
| `market-environment-analysis` | 整体市场环境评估 |
| `breadth-chart-analyst` | 市场广度分析 |

### 3️⃣ 资金流向
| 技能 | 功能描述 |
|:-----|:---------|
| `cross-border-flow-tracker` | 北向/南向资金追踪 |
| `institutional-flow-tracker` | 机构资金流向 |

### 4️⃣ 选股筛选
| 技能 | 功能描述 |
|:-----|:---------|
| `stock-screener` | 通用多条件选股 |
| `a-share-screener` | A股专用选股 |
| `canslim-screener` | CANSLIM成长股筛选 |
| `value-dividend-screener` | 价值+股息策略 |
| `dividend-growth-pullback-screener` | 股息成长回调筛选 |
| `pair-trade-screener` | 配对交易机会 |

### 5️⃣ 行业与宏观
| 技能 | 功能描述 |
|:-----|:---------|
| `sector-analyst` | 行业轮动分析 |
| `china-macro-analyst` | 中国宏观数据与政策 |
| `economic-calendar-fetcher` | 经济事件日历 |
| `earnings-calendar` | 财报发布日历 |
| `market-news-analyst` | 新闻影响分析 |

### 6️⃣ 组合与风险
| 技能 | 功能描述 |
|:-----|:---------|
| `portfolio-manager` | 配置与再平衡 |
| `options-strategy-advisor` | 期权策略 |
| `backtest-expert` | 策略回测 |
| `scenario-analyzer` | 情景分析 |

### 7️⃣ 策略与执行
| 技能 | 功能描述 |
|:-----|:---------|
| `weekly-trade-strategy` | 周度交易计划 |
| `stanley-druckenmiller-investment` | 德鲁肯米勒宏观投资 |
| `us-market-bubble-detector` | 泡沫风险评估 |
| `shioaji` | 台湾市场交易API |

---

## 🔄 专业交易流水线（6阶段）

```
阶段 1: 盘前研判
├── economic-calendar-fetcher → 本周经济事件
├── earnings-calendar → 财报发布日程
├── market-environment-analysis → 市场环境评估
└── china-macro-analyst → 宏观数据分析

阶段 2: 选股扫描
├── stock-screener → 初步筛选
├── a-share-screener → A股多条件筛选
├── canslim-screener → 成长股筛选
└── value-dividend-screener → 价值股筛选

阶段 3: 深度分析
├── us-stock-analysis / a-share-analysis → 基本面分析
├── technical-analyst → 技术面分析
├── institutional-flow-tracker → 机构资金追踪
└── cross-border-flow-tracker → 北向资金确认

阶段 4: 风险评估
├── scenario-analyzer → 多情景分析
├── us-market-bubble-detector → 泡沫风险检测
├── options-strategy-advisor → 对冲策略
└── portfolio-manager → 仓位管理

阶段 5: 下单执行
├── shioaji → 台湾市场下单
└── weekly-trade-strategy → 本周交易计划

阶段 6: 盘后复盘
├── market-news-analyst → 新闻复盘
├── breadth-chart-analyst → 市场广度分析
└── portfolio-manager → 持仓跟踪
```

---

## 💡 使用示例

### 盘前准备
```
1. "本周有哪些重要经济数据发布"
2. "有哪些公司本周发财报"
3. "当前市场环境如何"
4. "北向资金最近的流向趋势"
```

### 美股成长股发现
```
1. "用CANSLIM方法筛选美股"
2. "分析NVDA基本面和技术面"
3. "NVDA的机构持仓情况"
4. "NVDA是否有泡沫风险"
5. "制定NVDA本周交易计划"
```

### A股价值投资
```
1. "帮我筛选低PE高ROE的A股"
2. "分析贵州茅台基本面"
3. "北向资金最近的流向趋势"
4. "给我一个价值投资组合建议"
5. "本周交易计划是什么"
```

### 港股套利
```
1. "分析腾讯港股"
2. "比亚迪AH溢价分析"
3. "南向资金流向港股哪些板块"
4. "给我AH溢价套利机会"
```

### 宏观驱动交易
```
1. "分析当前宏观环境"
2. "降息利好哪些板块"
3. "用德鲁肯米勒风格分析市场"
4. "经济衰退情景分析"
```

### 风险管理
```
1. "分析我的持仓风险敞口"
2. "有什么期权策略可以对冲"
3. "回测这个策略的历史表现"
4. "市场下跌20%的情景分析"
```

---

## 🔧 前置要求

| 技能 | 需要 |
|------|------|
| `akshare` | Python + AKShare库 |
| `shioaji` | Shioaji API凭证（台湾市场） |
| `股票分析` | 网络搜索权限 |
| `stock-screener` | 网络搜索权限 |

```bash
# 安装 akshare
pip install akshare

# 安装 shioaji（台湾市场）
pip install shioaji
```

---

## 📊 数据来源

| 市场 | 数据源 |
|:-----|:-------|
| 美股 | Yahoo Finance, MarketWatch, Seeking Alpha, Bloomberg, TradingView |
| A股 | 东方财富, 同花顺, 雪球, 巨潮资讯, AKShare |
| 港股 | 港交所, 阿斯达克 |
| 台股 | Shioaji API, 台湾证交所 |

---

## ⚠️ 风险提示

本工作流**仅供信息参考和学习使用**，不构成投资建议。股票市场有风险，投资需谨慎。请自行研究。

---

## 📄 开源协议

MIT © [nicepkg](https://github.com/nicepkg)

<div align="center">

**[⬆ 返回主项目](../README_cn.md)**

</div>
