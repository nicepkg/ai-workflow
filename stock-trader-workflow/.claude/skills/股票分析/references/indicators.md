# 技术指标计算

## 基础使用

```python
import talib
import pandas as pd

# 假设 df 有 'close', 'high', 'low', 'volume' 列
df['ema_20'] = talib.EMA(df['close'], timeperiod=20)
df['rsi_14'] = talib.RSI(df['close'], timeperiod=14)
df['atr_14'] = talib.ATR(df['high'], df['low'], df['close'], timeperiod=14)
```

## Skill 中使用

本 Skill 提供 `IndicatorCalculator` 完整套件，一次性计算所有指标：

```python
from scripts.talib_calculator import IndicatorCalculator

df = IndicatorCalculator.compute_full_suite(df)
# 返回：EMA(5,10,20,60) + MACD(12,26,9) + RSI(7,14) + ATR(3,14) + OBV + BBANDS(5,2.0)
```

详见 `scripts_guide.md` 或脚本文件中的 docstring。

## 在回测中使用指标的注意点

- TA-Lib 返回 numpy 数组，可能包含 NaN 值，应与原 DataFrame 按索引对齐。
- 小时线与日线的指标计算方式相同，但时间对齐与缺失值处理需注意。
- 对于多周期（例如同时使用日线和小时线）的策略，需确保指标在同一基准时间轴上进行回测时的对齐。

## 指标介绍

**ROCR**: 多周期涨幅，衡量价格变动比例。
**EMA**: 指数移动平均线，反映价格趋势。
**VWMA**: 成交量加权移动平均线，结合价格与成交量。
**ADX**: 平均趋向指标，衡量趋势强度。
**MACD**: 指数平滑异同移动平均线，衡量价格动量。
**RSI**: 相对强弱指数，评估价格变动速度和变化。
**CCI**: 顺势指标，衡量价格偏离均值的程度。
**STOCH**: KDJ随机指标，反映价格在一定周期内的相对位置。
**ATR**: 平均真实波幅，衡量市场波动性。
**OBV**: 能量潮指标，结合价格与成交量分析买卖压力。
**BBANDS**: 布林带，显示价格的波动范围。
**AD**: 累积/派发指标，评估资金流入流出。
**VOLUME_SMA**: 成交量的简单移动平均。
