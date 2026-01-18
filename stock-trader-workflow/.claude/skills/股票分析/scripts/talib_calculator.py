"""技术指标计算工具，基于 TA-Lib 提供多类型行情指标计算。

Main Functions:
  - compute_change: 多周期涨幅 (ROCR)
  - compute_ema: 指数移动平均 (EMA)
  - compute_macd: 趋势转换 (MACD)
  - compute_adx: 趋势力度 (ADX)
  - compute_rsi: 超买超卖 (RSI)
  - compute_cci: 极端偏离 (CCI)
  - compute_stoch: 随机指标 (KDJ)
  - compute_atr: 波动幅度 (ATR)
  - compute_bbands: 布林带 (Bollinger Bands)
  - compute_obv: 资金流向 (OBV)
  - compute_ad: 吸筹派发 (A/D)
  - compute_volume_sma: 成交量移动平均
  - compute_vwma: 成交量加权均线
  - compute_full_suite: 完整指标套件 (EMA+MACD+RSI+ATR+OBV+BBANDS)

Usage:
  df = pd.read_csv('candlesticks.csv')
  df = IndicatorCalculator.compute_ema(df)
  df = IndicatorCalculator.compute_macd(df)
  df = IndicatorCalculator.compute_full_suite(df)
"""

from collections.abc import Sequence
from typing import cast

import numpy as np
import pandas as pd
import talib


class IndicatorCalculator:
    """技术指标计算器,按功能分类组织指标计算。

    指标分类:
    1. 基础指标: ROCR(涨幅), MIDPRICE(中间价)
    2. 趋势方向: EMA(指数移动平均), MACD(趋势转换)
    3. 趋势强度: ADX(趋势力度评估)
    4. 动量指标: CCI(极端偏离), RSI(超买超卖), STOCH(区间扫点)
    5. 波动指标: ATR(波动幅度), BBANDS(震荡区间)
    6. 成交量: OBV(资金流向), AD(吸筹与派发)
    """

    DEFAULT_CLOSE_COLUMN = "close"
    DEFAULT_HIGH_COLUMN = "high"
    DEFAULT_LOW_COLUMN = "low"
    DEFAULT_CHANGE_PERIODS = (1, 5, 10, 20)
    DEFAULT_EMA_PERIODS = (5, 10, 20, 60)
    DEFAULT_MACD_PERIODS = (12, 26, 9)
    DEFAULT_ADX_PERIODS = (14, 7)
    DEFAULT_RSI_PERIODS = (7, 14)
    DEFAULT_CCI_PERIODS = (14, 7)
    DEFAULT_STOCH_PERIODS = (9, 3, 3)
    DEFAULT_ATR_PERIODS = (3, 14)
    DEFAULT_BBANDS_PARAMS = (5, 2.0, 2.0, talib.MA_Type.SMA)
    DEFAULT_VOLUME_SMA_PERIODS = (5, 10, 20)
    DEFAULT_VWMA_PERIODS = (5, 10)
    # ==================== 基础指标 ====================

    @staticmethod
    def compute_change(
        frame: pd.DataFrame,
        *,
        change_periods: Sequence[int] | None = None,
        close_column: str = DEFAULT_CLOSE_COLUMN,
    ) -> pd.DataFrame:
        """计算多周期涨幅 (ROCR)

        衡量价格波动速度,突破 1.0 动量增强,低于 1.0 减弱。
        """

        periods = tuple(change_periods or IndicatorCalculator.DEFAULT_CHANGE_PERIODS)
        IndicatorCalculator._ensure_columns(frame, [close_column])
        result = frame.copy()
        close = IndicatorCalculator._column_as_ndarray(result, close_column)
        for period in periods:
            result[f"change_pct_{period}"] = talib.ROCP(close, timeperiod=period)
        return result

    @staticmethod
    def compute_mid_price(
        frame: pd.DataFrame,
        *,
        high_column: str = DEFAULT_HIGH_COLUMN,
        low_column: str = DEFAULT_LOW_COLUMN,
    ) -> pd.DataFrame:
        """计算高低价均值,生成中间价列."""

        IndicatorCalculator._ensure_columns(frame, [high_column, low_column])
        result = frame.copy()
        high = IndicatorCalculator._column_as_ndarray(result, high_column)
        low = IndicatorCalculator._column_as_ndarray(result, low_column)
        result["mid_price"] = talib.MIDPRICE(high, low, timeperiod=2)
        return result

    # ==================== 趋势方向 ====================
    @staticmethod
    def compute_ema(
        frame: pd.DataFrame,
        *,
        ema_periods: Sequence[int] | None = None,
        close_column: str = DEFAULT_CLOSE_COLUMN,
    ) -> pd.DataFrame:
        """使用 TA-Lib 计算多周期 EMA, 返回附加指标列后的 DataFrame."""

        periods = tuple(ema_periods or IndicatorCalculator.DEFAULT_EMA_PERIODS)
        IndicatorCalculator._ensure_columns(frame, [close_column])
        result = frame.copy()
        close = IndicatorCalculator._column_as_ndarray(result, close_column)
        for period in periods:
            column_name = f"ema_{period}"
            result[column_name] = talib.EMA(close, timeperiod=period)
        return result

    @staticmethod
    def compute_macd(
        frame: pd.DataFrame,
        *,
        macd_periods: Sequence[int] | None = None,
        close_column: str = DEFAULT_CLOSE_COLUMN,
    ) -> pd.DataFrame:
        """计算 MACD 及其 signal/histogram."""

        periods = tuple(macd_periods or IndicatorCalculator.DEFAULT_MACD_PERIODS)
        if len(periods) != 3:
            raise ValueError("MACD 参数必须是 (fast, slow, signal) 三个整数")
        IndicatorCalculator._ensure_columns(frame, [close_column])
        result = frame.copy()
        close = IndicatorCalculator._column_as_ndarray(result, close_column)
        fast, slow, signal = periods
        macd, macd_signal, macd_hist = talib.MACD(
            close, fastperiod=fast, slowperiod=slow, signalperiod=signal
        )
        result["macd"] = macd
        result["macd_signal"] = macd_signal
        result["macd_hist"] = macd_hist
        return result

    # ==================== 趋势强度 ====================
    @staticmethod
    def compute_adx(
        frame: pd.DataFrame,
        *,
        adx_periods: Sequence[int] | None = None,
        high_column: str = DEFAULT_HIGH_COLUMN,
        low_column: str = DEFAULT_LOW_COLUMN,
        close_column: str = DEFAULT_CLOSE_COLUMN,
    ) -> pd.DataFrame:
        """计算多周期 ADX 指标."""

        periods = tuple(adx_periods or IndicatorCalculator.DEFAULT_ADX_PERIODS)
        IndicatorCalculator._ensure_columns(
            frame, [high_column, low_column, close_column]
        )
        result = frame.copy()
        high = IndicatorCalculator._column_as_ndarray(result, high_column)
        low = IndicatorCalculator._column_as_ndarray(result, low_column)
        close = IndicatorCalculator._column_as_ndarray(result, close_column)
        for period in periods:
            result[f"adx_{period}"] = talib.ADX(high, low, close, timeperiod=period)
        return result

    # ==================== 动量指标 ====================
    @staticmethod
    def compute_rsi(
        frame: pd.DataFrame,
        *,
        rsi_periods: Sequence[int] | None = None,
        close_column: str = DEFAULT_CLOSE_COLUMN,
    ) -> pd.DataFrame:
        """计算多周期 RSI 指标."""

        periods = tuple(rsi_periods or IndicatorCalculator.DEFAULT_RSI_PERIODS)
        IndicatorCalculator._ensure_columns(frame, [close_column])
        result = frame.copy()
        close = IndicatorCalculator._column_as_ndarray(result, close_column)
        for period in periods:
            result[f"rsi_{period}"] = talib.RSI(close, timeperiod=period)
        return result

    @staticmethod
    def compute_cci(
        frame: pd.DataFrame,
        *,
        cci_periods: Sequence[int] | None = None,
        high_column: str = DEFAULT_HIGH_COLUMN,
        low_column: str = DEFAULT_LOW_COLUMN,
        close_column: str = DEFAULT_CLOSE_COLUMN,
    ) -> pd.DataFrame:
        """计算多周期 CCI 指标."""

        periods = tuple(cci_periods or IndicatorCalculator.DEFAULT_CCI_PERIODS)
        IndicatorCalculator._ensure_columns(
            frame, [high_column, low_column, close_column]
        )
        result = frame.copy()
        high = IndicatorCalculator._column_as_ndarray(result, high_column)
        low = IndicatorCalculator._column_as_ndarray(result, low_column)
        close = IndicatorCalculator._column_as_ndarray(result, close_column)
        for period in periods:
            result[f"cci_{period}"] = talib.CCI(high, low, close, timeperiod=period)
        return result

    @staticmethod
    def compute_stoch(
        frame: pd.DataFrame,
        *,
        stoch_periods: Sequence[int] | None = None,
        high_column: str = DEFAULT_HIGH_COLUMN,
        low_column: str = DEFAULT_LOW_COLUMN,
        close_column: str = DEFAULT_CLOSE_COLUMN,
    ) -> pd.DataFrame:
        """计算 Stochastic Oscillator (KDJ) 指标."""

        periods = tuple(stoch_periods or IndicatorCalculator.DEFAULT_STOCH_PERIODS)
        if len(periods) != 3:
            raise ValueError(
                "STOCH 参数必须是 (period, fastk_period, fastd_period) 三个整数"
            )
        IndicatorCalculator._ensure_columns(
            frame, [high_column, low_column, close_column]
        )
        result = frame.copy()
        high = IndicatorCalculator._column_as_ndarray(result, high_column)
        low = IndicatorCalculator._column_as_ndarray(result, low_column)
        close = IndicatorCalculator._column_as_ndarray(result, close_column)
        period, fastk_period, fastd_period = periods
        k_line, d_line = talib.STOCH(
            high,
            low,
            close,
            fastk_period=period,
            slowk_period=fastk_period,
            slowd_period=fastd_period,
        )
        result[f"stoch_k_{period}"] = k_line
        result[f"stoch_d_{period}"] = d_line
        return result

    # ==================== 波动指标 ====================
    @staticmethod
    def compute_atr(
        frame: pd.DataFrame,
        *,
        atr_periods: Sequence[int] | None = None,
        high_column: str = DEFAULT_HIGH_COLUMN,
        low_column: str = DEFAULT_LOW_COLUMN,
        close_column: str = DEFAULT_CLOSE_COLUMN,
    ) -> pd.DataFrame:
        """计算多周期 ATR."""

        periods = tuple(atr_periods or IndicatorCalculator.DEFAULT_ATR_PERIODS)
        IndicatorCalculator._ensure_columns(
            frame, [high_column, low_column, close_column]
        )
        result = frame.copy()
        high = IndicatorCalculator._column_as_ndarray(result, high_column)
        low = IndicatorCalculator._column_as_ndarray(result, low_column)
        close = IndicatorCalculator._column_as_ndarray(result, close_column)
        for period in periods:
            result[f"atr_{period}"] = talib.ATR(high, low, close, timeperiod=period)
        return result

    @staticmethod
    def compute_bbands(
        frame: pd.DataFrame,
        *,
        bbands_params: Sequence[int | float] | None = None,
        close_column: str = DEFAULT_CLOSE_COLUMN,
    ) -> pd.DataFrame:
        """使用 TA-Lib 计算布林带(Bollinger Bands).

        参数为元组 (timeperiod, nbdev_up, nbdev_dn, matype).
        """

        IndicatorCalculator._ensure_columns(frame, [close_column])
        result = frame.copy()
        close = IndicatorCalculator._column_as_ndarray(result, close_column)

        params = tuple(bbands_params or IndicatorCalculator.DEFAULT_BBANDS_PARAMS)
        if len(params) != 4:
            raise ValueError(
                "BBANDS 参数必须是 (timeperiod, nbdev_up, nbdev_dn, matype) 四个值"
            )

        timeperiod_val = int(cast(int | float, params[0]))
        nbdev_up_val = float(cast(int | float, params[1]))
        nbdev_dn_val = float(cast(int | float, params[2]))
        matype_val = cast(talib.MA_Type, params[3])

        upper, middle, lower = talib.BBANDS(
            close,
            timeperiod=timeperiod_val,
            nbdevup=nbdev_up_val,
            nbdevdn=nbdev_dn_val,
            matype=matype_val,
        )

        result[f"bb_upper_{timeperiod_val}"] = upper
        result[f"bb_middle_{timeperiod_val}"] = middle
        result[f"bb_lower_{timeperiod_val}"] = lower

        return result

    # ==================== 成交量 ====================
    @staticmethod
    def compute_obv(
        frame: pd.DataFrame,
        *,
        close_column: str = DEFAULT_CLOSE_COLUMN,
        volume_column: str = "volume",
    ) -> pd.DataFrame:
        """计算 OBV (On-Balance Volume) 指标."""

        IndicatorCalculator._ensure_columns(frame, [close_column, volume_column])
        result = frame.copy()
        close = IndicatorCalculator._column_as_ndarray(result, close_column)
        volume = IndicatorCalculator._column_as_ndarray(result, volume_column)
        result["obv"] = talib.OBV(close, volume)
        return result

    @staticmethod
    def compute_ad(
        frame: pd.DataFrame,
        *,
        high_column: str = DEFAULT_HIGH_COLUMN,
        low_column: str = DEFAULT_LOW_COLUMN,
        close_column: str = DEFAULT_CLOSE_COLUMN,
        volume_column: str = "volume",
    ) -> pd.DataFrame:
        """计算 AD (Accumulation/Distribution) 指标."""

        IndicatorCalculator._ensure_columns(
            frame, [high_column, low_column, close_column, volume_column]
        )
        result = frame.copy()
        high = IndicatorCalculator._column_as_ndarray(result, high_column)
        low = IndicatorCalculator._column_as_ndarray(result, low_column)
        close = IndicatorCalculator._column_as_ndarray(result, close_column)
        volume = IndicatorCalculator._column_as_ndarray(result, volume_column)
        result["ad"] = talib.AD(high, low, close, volume)
        return result

    @staticmethod
    def compute_volume_sma(
        frame: pd.DataFrame,
        *,
        volume_sma_periods: Sequence[int] | None = None,
        volume_column: str = "volume",
    ) -> pd.DataFrame:
        """计算成交量的多周期 SMA(简单移动平均)。"""
        periods = tuple(
            volume_sma_periods or IndicatorCalculator.DEFAULT_VOLUME_SMA_PERIODS
        )
        IndicatorCalculator._ensure_columns(frame, [volume_column])
        result = frame.copy()
        volume = IndicatorCalculator._column_as_ndarray(result, volume_column)
        # 为每个周期计算 SMA
        for period in periods:
            result[f"volume_sma_{period}"] = talib.SMA(volume, timeperiod=period)
        return result

    @staticmethod
    def compute_vwma(
        frame: pd.DataFrame,
        *,
        vwma_periods: Sequence[int] | None = None,
        close_column: str = DEFAULT_CLOSE_COLUMN,
        volume_column: str = "volume",
    ) -> pd.DataFrame:
        """计算成交量加权移动平均线 (VWMA)。

        VWMA 通过成交量加权价格,成交量大的交易日对均线影响更大。
        计算公式: VWMA = SUM(价格 * 成交量) / SUM(成交量)
        """
        periods = tuple(vwma_periods or IndicatorCalculator.DEFAULT_VWMA_PERIODS)
        IndicatorCalculator._ensure_columns(frame, [close_column, volume_column])
        result = frame.copy()
        close = IndicatorCalculator._column_as_ndarray(result, close_column)
        volume = IndicatorCalculator._column_as_ndarray(result, volume_column)

        for period in periods:
            # 计算价格*成交量的移动总和
            pv_sum = talib.SUM(close * volume, timeperiod=period)
            # 计算成交量的移动总和
            v_sum = talib.SUM(volume, timeperiod=period)
            # VWMA = (价格*成交量)之和 / 成交量之和
            result[f"vwma_{period}"] = pv_sum / v_sum

        return result

    # ==================== 辅助函数 ====================
    @staticmethod
    def compute_full_suite(
        frame: pd.DataFrame,
        *,
        ema_periods: Sequence[int] | None = None,
        macd_periods: Sequence[int] | None = None,
        rsi_periods: Sequence[int] | None = None,
        atr_periods: Sequence[int] | None = None,
        bbands_params: Sequence[int | float] | None = None,
        close_column: str = DEFAULT_CLOSE_COLUMN,
        high_column: str = DEFAULT_HIGH_COLUMN,
        low_column: str = DEFAULT_LOW_COLUMN,
        volume_column: str = "volume",
    ) -> pd.DataFrame:
        """一次性计算完整指标套件（EMA+MACD+RSI+ATR+OBV+BBANDS）。

        返回包含所有常用指标的 DataFrame，避免重复遍历数据。
        """
        result = frame.copy()
        result = IndicatorCalculator.compute_ema(
            result, ema_periods=ema_periods, close_column=close_column
        )
        result = IndicatorCalculator.compute_macd(
            result, macd_periods=macd_periods, close_column=close_column
        )
        result = IndicatorCalculator.compute_rsi(
            result, rsi_periods=rsi_periods, close_column=close_column
        )
        result = IndicatorCalculator.compute_atr(
            result,
            atr_periods=atr_periods,
            high_column=high_column,
            low_column=low_column,
            close_column=close_column,
        )
        result = IndicatorCalculator.compute_obv(
            result, close_column=close_column, volume_column=volume_column
        )
        result = IndicatorCalculator.compute_bbands(
            result, bbands_params=bbands_params, close_column=close_column
        )
        return result

    @staticmethod
    def _column_as_ndarray(frame: pd.DataFrame, column: str) -> np.ndarray:
        return frame[column].to_numpy(dtype=float, copy=False)

    @staticmethod
    def _ensure_columns(frame: pd.DataFrame, columns: Sequence[str]) -> None:
        missing = [col for col in columns if col not in frame.columns]
        if missing:
            raise ValueError(f"DataFrame 缺少必需列: {', '.join(missing)}")


__all__ = ["IndicatorCalculator"]
