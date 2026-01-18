"""LongPort K 线数据获取工具，支持多周期行情查询与导出。

Main Functions:
  - fetch_candlesticks: 获取标的 K 线数据并返回 pandas.DataFrame（前复权）
  - _parse_period: 解析 K 线周期字符串
  - _candlesticks_to_df: 将响应转换为 DataFrame
  - main: 命令行入口

Usage:
  python scripdatetime/longport_candlesticks.py --symbol 700.HK --period day --count 200 --output /tmp/700_day.csv
  python scripdatetime/longport_candlesticks.py --symbol AAPL.US --period 1m --count 500
"""

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Iterator

import pandas as pd
from longport.openapi import AdjustType, Config, Period, QuoteContext


@contextmanager
def open_quote_ctx() -> Iterator[QuoteContext]:
    """从 .env 初始化 QuoteContext，并在结束时尝试关闭。"""

    ctx = QuoteContext(Config.from_env())
    try:
        yield ctx
    finally:
        close_fn = getattr(ctx, "close", None)
        if callable(close_fn):
            close_fn()


def fetch_candlesticks(
    symbol: str,
    period: type[Period] = Period.Day,
    count: int = 100,
    adjust_type: type[AdjustType] = AdjustType.ForwardAdjust,
) -> pd.DataFrame:
    """获取标的 K 线并返回 DataFrame（index 为 UTC datetime）。"""

    with open_quote_ctx() as ctx:
        resp = ctx.candlesticks(symbol, period, count, adjust_type)

    return _candlesticks_to_df(resp)


def _candlesticks_to_df(resp) -> pd.DataFrame:
    c_list = getattr(resp, "candlesticks", None) or []
    records = []
    for c in c_list:
        records.append({
            "symbol": c.symbol,
            "datetime": datetime.fromtimestamp(c.timestamp, tz=timezone.utc),
            "open": float(c.open),
            "high": float(c.high),
            "low": float(c.low),
            "close": float(c.close),
            "volume": int(c.volume),
            "turnover": float(c.turnover),
        })

    df = pd.DataFrame(records)
    if df.empty:
        return df
    df = df.set_index("datetime").sort_index()
    return df


def _parse_period(value: str) -> type[Period]:
    mapping = {
        "1m": Period.Min_1,
        "2m": Period.Min_2,
        "3m": Period.Min_3,
        "5m": Period.Min_5,
        "10m": Period.Min_10,
        "15m": Period.Min_15,
        "20m": Period.Min_20,
        "30m": Period.Min_30,
        "45m": Period.Min_45,
        "60m": Period.Min_60,
        "120m": Period.Min_120,
        "180m": Period.Min_180,
        "240m": Period.Min_240,
        "1h": Period.Min_60,
        "4h": Period.Min_240,
        "day": Period.Day,
        "d": Period.Day,
        "week": Period.Week,
        "w": Period.Week,
        "month": Period.Month,
        "m": Period.Month,
        "quarter": Period.Quarter,
        "q": Period.Quarter,
        "year": Period.Year,
        "y": Period.Year,
    }
    try:
        return mapping[value.lower()]
    except KeyError as exc:
        msg = f"不支持的 period: {value}"
        raise argparse.ArgumentTypeError(msg) from exc


def main() -> None:
    parser = argparse.ArgumentParser(
        description="获取 LongPort K 线并输出 CSV 或 stdout"
    )
    parser.add_argument("--symbol", required=True, help="标的代码，如 700.HK / AAPL.US")
    parser.add_argument(
        "--period",
        default="day",
        type=_parse_period,
        help="K线周期，支持 1m/5m/15m/30m/60m/1h/day/week/month",
    )
    parser.add_argument("--count", type=int, default=100, help="返回条数，默认 100")

    parser.add_argument(
        "--output",
        help="输出 CSV 路径。不填则打印前几行与汇总。",
    )

    args = parser.parse_args()

    df = fetch_candlesticks(
        args.symbol,
        period=args.period,
        count=args.count,
    )

    if df.empty:
        print("空数据（可能无权限或代码/周期不匹配）")
        return

    if args.output:
        df.to_csv(args.output)
        print(f"已写入: {args.output}, 行数={len(df)}")
    else:
        print(df.head())
        print("----")
        print(df.tail())
        print(f"总行数: {len(df)}")


if __name__ == "__main__":
    main()
