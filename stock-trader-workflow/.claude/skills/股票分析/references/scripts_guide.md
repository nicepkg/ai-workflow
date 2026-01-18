# 脚本使用指南

本文档介绍三个核心 CLI 脚本的使用方法与集成示例。

## 1. longport_groups.py - 自选分组管理

**功能**：通过命令行管理 LongPort 自选分组，支持分组的增删改查与成员导出。

### longport_groups 使用示例

```bash
# 列出所有分组（显示 ID、名称、成员数）
python scripts/longport_groups.py list

# 创建分组
python scripts/longport_groups.py create --name tech_stocks --symbols 700.HK,AAPL.US,MSFT.US

# 更新分组成员
# 增加成员
python scripts/longport_groups.py update --id 1 --add-symbols 000001.SZ,000858.SZ

# 删除成员
python scripts/longport_groups.py update --id 1 --remove-symbols 700.HK

# 替换全部成员
python scripts/longport_groups.py update --id 1 --replace-symbols 600000.SH,600001.SH

# 导出分组成员列表（逐行一个符号）
python scripts/longport_groups.py get-symbols --id 1 --output symbols.txt

# 清空分组
python scripts/longport_groups.py delete --id 1
```

### Python 中导入使用（仅 CLI 可用）

本脚本**仅提供命令行入口**，不暴露库函数，应通过命令行调用。

## 2. longport_candlesticks.py - K 线数据获取

**功能**：从 LongPort 获取标的 K 线数据，支持多周期、自动前复权、输出 DataFrame 或 CSV。

### longport_candlesticks 使用示例

```bash
# 基本用法：查询日线 100 根，打印前后几行
python scripts/longport_candlesticks.py --symbol 700.HK

# 指定周期与数量，输出到 CSV
python scripts/longport_candlesticks.py --symbol 700.HK --period day --count 200 --output /tmp/700_day.csv

# 查询分钟级 K 线
python scripts/longport_candlesticks.py --symbol AAPL.US --period 1m --count 500

# 支持的周期：
# - 分钟：1m, 2m, 3m, 5m, 10m, 15m, 20m, 30m, 45m, 60m, 120m, 180m, 240m, 1h, 4h
# - 日线及以上：day, d, week, w, month, m, quarter, q, year, y
```

### Python 中导入使用

```python
from scripts.longport_candlesticks import fetch_candlesticks
from longport.openapi import Period

# 获取日线数据
df = fetch_candlesticks('700.HK', period=Period.Day, count=200)
# 返回 DataFrame，index 为 UTC datetime，列为 open/high/low/close/volume/turnover

# 指定周期获取
from longport.openapi import Period
df = fetch_candlesticks('AAPL.US', period=Period.Min_5, count=100)

# 前复权（默认）已自动应用
print(df.head())
# datetime      open  high   low      close    volume    turnover                                                        
# 2024-12-01    364.6  368.8  361.6  362.000  10853604  3954556819.0
```

## 3. talib_calculator.py - 技术指标计算

**功能**：基于 TA-Lib 计算多种技术指标，支持单个指标或完整套件一次性计算。

### Python 中使用

```python
from scripts.talib_calculator import IndicatorCalculator
import pandas as pd

# 假设已有 K 线 DataFrame
df = pd.read_csv('candlesticks.csv')

# 方案 1：一次性计算完整指标套件（推荐）
df = IndicatorCalculator.compute_full_suite(df)
# 包含：EMA(5,10,20,60) + MACD(12,26,9) + RSI(7,14) + ATR(3,14) + OBV + BBANDS(5,2.0)

# 方案 2：按需计算单个指标
df = IndicatorCalculator.compute_ema(df)          # 指数移动平均
df = IndicatorCalculator.compute_macd(df)         # MACD 与信号线
df = IndicatorCalculator.compute_rsi(df)          # 相对强弱指数
df = IndicatorCalculator.compute_atr(df)          # 真实波幅
df = IndicatorCalculator.compute_bbands(df)       # 布林带
df = IndicatorCalculator.compute_obv(df)          # 能量潮
df = IndicatorCalculator.compute_stoch(df)        # 随机指标

# 自定义参数
df = IndicatorCalculator.compute_ema(
    df, 
    ema_periods=(3, 6, 12)  # 自定义周期
)

df = IndicatorCalculator.compute_rsi(
    df,
    rsi_periods=(6, 12, 24)  # 自定义 RSI 周期
)

# 查看计算结果
print(df.columns)  # 包含所有新增指标列
print(df[['ema_5', 'macd', 'rsi_14', 'atr_14']].head())
```

## 完整工作流示例

```python
from scripts.longport_candlesticks import fetch_candlesticks
from scripts.talib_calculator import IndicatorCalculator
import pandas as pd

# 步骤 1：从 LongPort 获取 K 线
symbol = '700.HK'
df = fetch_candlesticks(symbol, count=250)

# 步骤 2：计算技术指标
df = IndicatorCalculator.compute_full_suite(df)

# 步骤 3：生成买卖点信号
# 基于 RSI 超买超卖
buy_signal = df[df['rsi_14'] < 30]
sell_signal = df[df['rsi_14'] > 70]

# 基于 MACD 金叉死叉
df['macd_signal'] = df['macd'] > df['macd_signal']  # True 为多头信号

# 步骤 4：统计并输出
print(f"买入信号数: {len(buy_signal)}")
print(f"卖出信号数: {len(sell_signal)}")
print(f"\n最近 10 条 K 线：")
print(df[['close', 'ema_5', 'ema_20', 'rsi_14', 'macd']].tail(10))

# 步骤 5：保存结果
df.to_csv(f'/tmp/{symbol}_with_indicators.csv')
```

## 环境要求

- `longport_groups.py`：需要 `.env` 文件配置 LongPort API 凭证
- `longport_candlesticks.py`：需要 `.env` 文件配置 LongPort API 凭证
- `talib_calculator.py`：需要安装 `talib` 包，参见 `indicators.md`

## 常见问题

### Q1：如何批量获取一个分组内所有标的的 K 线数据？

```bash
# 步骤 1：导出分组成员
python scripts/longport_groups.py get-symbols --id 1 --output symbols.txt

# 步骤 2：逐行读取并下载
while read symbol; do
  python scripts/longport_candlesticks.py --symbol "$symbol" --period day --count 200 --output "/tmp/${symbol}_day.csv"
done < symbols.txt
```

### Q2：如何在回测中使用计算好的指标？

参见完整工作流示例，计算指标后导出 CSV，回测脚本直接读取即可。

### Q3：TA-Lib 安装失败怎么办？

参见 `indicators.md` 中的安装与回退方案。
