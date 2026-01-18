#!/usr/bin/env python3
"""
Stock Screener - Filter and analyze stocks by financial metrics.
"""

import argparse
import json
from typing import Dict, List, Optional, Tuple, Union

import pandas as pd
import numpy as np


class StockScreener:
    """Filter and screen stocks by financial metrics."""

    # Standard column mappings
    COLUMN_ALIASES = {
        'symbol': ['symbol', 'ticker', 'stock'],
        'name': ['name', 'company', 'company_name'],
        'sector': ['sector', 'industry', 'category'],
        'price': ['price', 'close', 'last_price', 'current_price'],
        'pe_ratio': ['pe_ratio', 'pe', 'p/e', 'price_earnings'],
        'pb_ratio': ['pb_ratio', 'pb', 'p/b', 'price_book'],
        'ps_ratio': ['ps_ratio', 'ps', 'p/s', 'price_sales'],
        'peg_ratio': ['peg_ratio', 'peg'],
        'market_cap': ['market_cap', 'marketcap', 'mkt_cap', 'capitalization'],
        'dividend_yield': ['dividend_yield', 'div_yield', 'yield', 'dividend'],
        'eps': ['eps', 'earnings_per_share'],
        'revenue': ['revenue', 'sales', 'total_revenue'],
        'revenue_growth': ['revenue_growth', 'rev_growth', 'sales_growth'],
        'earnings_growth': ['earnings_growth', 'earn_growth', 'eps_growth'],
        'profit_margin': ['profit_margin', 'net_margin', 'margin'],
        'roe': ['roe', 'return_on_equity'],
        'roa': ['roa', 'return_on_assets'],
        'debt_to_equity': ['debt_to_equity', 'de_ratio', 'd/e'],
        'current_ratio': ['current_ratio'],
        'payout_ratio': ['payout_ratio', 'dividend_payout'],
        'beta': ['beta'],
        '52w_high': ['52w_high', 'high_52w', 'year_high'],
        '52w_low': ['52w_low', 'low_52w', 'year_low'],
    }

    def __init__(self):
        """Initialize the screener."""
        self.df = None
        self.original_df = None
        self._column_map = {}

    def _normalize_columns(self):
        """Normalize column names to standard format."""
        if self.df is None:
            return

        lower_cols = {c.lower(): c for c in self.df.columns}

        for standard_name, aliases in self.COLUMN_ALIASES.items():
            for alias in aliases:
                if alias.lower() in lower_cols:
                    original_col = lower_cols[alias.lower()]
                    if original_col != standard_name:
                        self._column_map[standard_name] = original_col
                    break

    def _get_col(self, standard_name: str) -> str:
        """Get actual column name from standard name."""
        return self._column_map.get(standard_name, standard_name)

    def _has_col(self, standard_name: str) -> bool:
        """Check if a column exists."""
        col = self._get_col(standard_name)
        return col in self.df.columns if self.df is not None else False

    def load_csv(self, filepath: str) -> 'StockScreener':
        """Load stock data from CSV."""
        self.df = pd.read_csv(filepath)
        self.original_df = self.df.copy()
        self._normalize_columns()

        # Convert market cap shorthand (1B, 500M)
        if self._has_col('market_cap'):
            col = self._get_col('market_cap')
            self.df[col] = self.df[col].apply(self._parse_market_cap)

        return self

    def load_dataframe(self, df: pd.DataFrame) -> 'StockScreener':
        """Load from existing DataFrame."""
        self.df = df.copy()
        self.original_df = self.df.copy()
        self._normalize_columns()
        return self

    def _parse_market_cap(self, value) -> float:
        """Parse market cap values like '1.5B', '500M'."""
        if pd.isna(value):
            return np.nan
        if isinstance(value, (int, float)):
            return float(value)

        value = str(value).upper().strip()
        multipliers = {'T': 1e12, 'B': 1e9, 'M': 1e6, 'K': 1e3}

        for suffix, mult in multipliers.items():
            if value.endswith(suffix):
                try:
                    return float(value[:-1]) * mult
                except ValueError:
                    return np.nan

        try:
            return float(value)
        except ValueError:
            return np.nan

    def reset(self) -> 'StockScreener':
        """Reset to original unfiltered data."""
        if self.original_df is not None:
            self.df = self.original_df.copy()
        return self

    def filter(self, **criteria) -> pd.DataFrame:
        """
        Filter stocks by multiple criteria.

        Supported criteria:
        - metric=(min, max) - range filter
        - metric_min=value - minimum filter
        - metric_max=value - maximum filter
        """
        if self.df is None:
            return pd.DataFrame()

        mask = pd.Series([True] * len(self.df), index=self.df.index)

        for key, value in criteria.items():
            # Parse key
            if key.endswith('_min'):
                metric = key[:-4]
                min_val = value
                max_val = None
            elif key.endswith('_max'):
                metric = key[:-4]
                min_val = None
                max_val = value
            else:
                metric = key
                if isinstance(value, tuple) and len(value) == 2:
                    min_val, max_val = value
                else:
                    continue

            # Get actual column name
            col = self._get_col(metric)
            if col not in self.df.columns:
                continue

            # Apply filters
            if min_val is not None:
                mask &= self.df[col] >= min_val
            if max_val is not None:
                mask &= self.df[col] <= max_val

        self.df = self.df[mask]
        return self.df

    def filter_by_sector(self, sectors: List[str]) -> 'StockScreener':
        """Filter to specific sectors."""
        if self.df is None or not self._has_col('sector'):
            return self

        col = self._get_col('sector')
        sectors_lower = [s.lower() for s in sectors]
        mask = self.df[col].str.lower().isin(sectors_lower)
        self.df = self.df[mask]
        return self

    def filter_by_metric(self, metric: str, min_val: float = None,
                        max_val: float = None) -> 'StockScreener':
        """Filter by a single metric."""
        if self.df is None:
            return self

        col = self._get_col(metric)
        if col not in self.df.columns:
            return self

        if min_val is not None:
            self.df = self.df[self.df[col] >= min_val]
        if max_val is not None:
            self.df = self.df[self.df[col] <= max_val]

        return self

    def value_screen(self) -> pd.DataFrame:
        """Apply value investing screen."""
        self.reset()
        return self.filter(
            pe_ratio=(0, 15),
            pb_ratio_max=2.0,
            dividend_yield_min=2.0,
            profit_margin_min=10
        )

    def growth_screen(self) -> pd.DataFrame:
        """Apply growth investing screen."""
        self.reset()
        criteria = {}

        if self._has_col('revenue_growth'):
            criteria['revenue_growth_min'] = 15
        if self._has_col('earnings_growth'):
            criteria['earnings_growth_min'] = 20
        if self._has_col('peg_ratio'):
            criteria['peg_ratio_max'] = 2.0

        return self.filter(**criteria) if criteria else self.df

    def dividend_screen(self) -> pd.DataFrame:
        """Apply dividend investing screen."""
        self.reset()
        criteria = {'dividend_yield': (2.0, 8.0)}

        if self._has_col('payout_ratio'):
            criteria['payout_ratio_max'] = 75

        return self.filter(**criteria)

    def quality_screen(self) -> pd.DataFrame:
        """Apply quality investing screen."""
        self.reset()
        criteria = {}

        if self._has_col('roe'):
            criteria['roe_min'] = 15
        if self._has_col('profit_margin'):
            criteria['profit_margin_min'] = 15
        if self._has_col('debt_to_equity'):
            criteria['debt_to_equity_max'] = 0.5
        if self._has_col('current_ratio'):
            criteria['current_ratio_min'] = 2.0

        return self.filter(**criteria) if criteria else self.df

    def custom_screen(self, criteria: Dict) -> pd.DataFrame:
        """Apply custom screening criteria."""
        self.reset()
        return self.filter(**criteria)

    def compare(self, symbols: List[str]) -> pd.DataFrame:
        """Compare specific stocks side by side."""
        if self.original_df is None:
            return pd.DataFrame()

        symbol_col = self._get_col('symbol')
        if symbol_col not in self.original_df.columns:
            return pd.DataFrame()

        # Filter to requested symbols
        mask = self.original_df[symbol_col].str.upper().isin([s.upper() for s in symbols])
        subset = self.original_df[mask].copy()

        if len(subset) == 0:
            return pd.DataFrame()

        # Transpose for side-by-side comparison
        subset = subset.set_index(symbol_col)
        return subset.T

    def rank_by(self, metric: str, ascending: bool = True, top_n: int = None) -> pd.DataFrame:
        """Rank stocks by a single metric."""
        if self.df is None:
            return pd.DataFrame()

        col = self._get_col(metric)
        if col not in self.df.columns:
            return self.df

        result = self.df.sort_values(col, ascending=ascending)

        if top_n:
            result = result.head(top_n)

        return result

    def sector_summary(self) -> pd.DataFrame:
        """Get summary statistics by sector."""
        if self.original_df is None or not self._has_col('sector'):
            return pd.DataFrame()

        sector_col = self._get_col('sector')

        # Build aggregation dict
        agg_dict = {}
        agg_dict[sector_col] = 'count'

        for metric in ['pe_ratio', 'dividend_yield', 'profit_margin', 'market_cap']:
            col = self._get_col(metric)
            if col in self.original_df.columns:
                agg_dict[col] = 'mean'

        result = self.original_df.groupby(sector_col).agg(agg_dict).reset_index()

        # Rename columns
        rename_map = {sector_col + '_count': 'count'} if sector_col + '_count' in result.columns else {}
        if 'count' not in result.columns and sector_col in result.columns:
            # First column after groupby is count
            pass

        result.columns = ['sector'] + [f'avg_{c}' if c != sector_col else 'count'
                                       for c in result.columns[1:]]

        return result.sort_values('count', ascending=False)

    def metric_distribution(self, metric: str) -> Dict:
        """Get distribution statistics for a metric."""
        if self.df is None:
            return {}

        col = self._get_col(metric)
        if col not in self.df.columns:
            return {}

        data = self.df[col].dropna()

        return {
            "count": len(data),
            "mean": round(data.mean(), 2),
            "median": round(data.median(), 2),
            "std": round(data.std(), 2),
            "min": round(data.min(), 2),
            "max": round(data.max(), 2),
            "percentiles": {
                "25%": round(data.quantile(0.25), 2),
                "50%": round(data.quantile(0.50), 2),
                "75%": round(data.quantile(0.75), 2),
                "90%": round(data.quantile(0.90), 2)
            }
        }

    def score_stocks(self, weights: Dict[str, float] = None) -> pd.DataFrame:
        """
        Score stocks using weighted metrics.

        Args:
            weights: Dict of metric -> weight. Positive = higher is better,
                    negative = lower is better.
        """
        if self.df is None or len(self.df) == 0:
            return pd.DataFrame()

        if weights is None:
            weights = {
                'pe_ratio': -0.2,
                'dividend_yield': 0.3,
                'profit_margin': 0.3,
                'revenue_growth': 0.2
            }

        result = self.df.copy()
        scores = pd.Series(0.0, index=result.index)

        for metric, weight in weights.items():
            col = self._get_col(metric)
            if col not in result.columns:
                continue

            # Normalize to 0-1 scale
            data = result[col].fillna(result[col].median())
            min_val = data.min()
            max_val = data.max()

            if max_val > min_val:
                normalized = (data - min_val) / (max_val - min_val)
            else:
                normalized = pd.Series(0.5, index=data.index)

            # Apply weight (negative weight inverts the score)
            if weight < 0:
                normalized = 1 - normalized
                weight = abs(weight)

            scores += normalized * weight

        # Normalize final score to 0-100
        if scores.max() > scores.min():
            scores = (scores - scores.min()) / (scores.max() - scores.min()) * 100

        result['score'] = scores.round(1)
        result = result.sort_values('score', ascending=False)

        return result

    def percentile_rank(self, metrics: List[str]) -> pd.DataFrame:
        """Calculate percentile rank for each metric."""
        if self.df is None:
            return pd.DataFrame()

        result = self.df.copy()

        for metric in metrics:
            col = self._get_col(metric)
            if col not in result.columns:
                continue

            result[f'{metric}_percentile'] = result[col].rank(pct=True) * 100

        return result

    def to_csv(self, filepath: str) -> str:
        """Export filtered results to CSV."""
        if self.df is not None:
            self.df.to_csv(filepath, index=False)
        return filepath

    def to_json(self, filepath: str) -> str:
        """Export filtered results to JSON."""
        if self.df is not None:
            self.df.to_json(filepath, orient='records', indent=2)
        return filepath

    def summary_report(self) -> str:
        """Generate text summary of current results."""
        if self.df is None or len(self.df) == 0:
            return "No stocks in current filter."

        lines = ["=" * 50, "STOCK SCREENING RESULTS", "=" * 50, ""]

        lines.append(f"Total stocks: {len(self.df)}")

        # Sector breakdown
        if self._has_col('sector'):
            sector_col = self._get_col('sector')
            sector_counts = self.df[sector_col].value_counts()
            lines.append(f"\nSector breakdown:")
            for sector, count in sector_counts.head(5).items():
                lines.append(f"  {sector}: {count}")

        # Metric summaries
        lines.append(f"\nMetric summaries:")
        for metric in ['pe_ratio', 'dividend_yield', 'profit_margin', 'market_cap']:
            col = self._get_col(metric)
            if col in self.df.columns:
                data = self.df[col].dropna()
                if len(data) > 0:
                    lines.append(f"  {metric}: avg={data.mean():.2f}, median={data.median():.2f}")

        # Top stocks by market cap
        if self._has_col('market_cap') and self._has_col('symbol'):
            lines.append(f"\nTop 5 by market cap:")
            mc_col = self._get_col('market_cap')
            sym_col = self._get_col('symbol')
            top = self.df.nlargest(5, mc_col)
            for _, row in top.iterrows():
                cap = row[mc_col]
                cap_str = f"${cap/1e12:.2f}T" if cap >= 1e12 else f"${cap/1e9:.2f}B" if cap >= 1e9 else f"${cap/1e6:.2f}M"
                lines.append(f"  {row[sym_col]}: {cap_str}")

        return "\n".join(lines)


def parse_number(value: str) -> float:
    """Parse number with K/M/B suffix."""
    if value is None:
        return None

    value = str(value).upper().strip()
    multipliers = {'T': 1e12, 'B': 1e9, 'M': 1e6, 'K': 1e3}

    for suffix, mult in multipliers.items():
        if value.endswith(suffix):
            return float(value[:-1]) * mult

    return float(value)


def main():
    parser = argparse.ArgumentParser(description="Stock Screener - Filter stocks by metrics")

    parser.add_argument("--input", "-i", required=True, help="Input CSV file")

    # Valuation filters
    parser.add_argument("--pe", nargs=2, type=float, metavar=('MIN', 'MAX'),
                       help="P/E ratio range")
    parser.add_argument("--pe-max", type=float, help="Maximum P/E ratio")
    parser.add_argument("--pb-max", type=float, help="Maximum P/B ratio")
    parser.add_argument("--peg-max", type=float, help="Maximum PEG ratio")

    # Size filters
    parser.add_argument("--cap-min", help="Minimum market cap (e.g., 1B, 500M)")
    parser.add_argument("--cap-max", help="Maximum market cap")

    # Income filters
    parser.add_argument("--div-min", type=float, help="Minimum dividend yield")
    parser.add_argument("--div-max", type=float, help="Maximum dividend yield")
    parser.add_argument("--payout-max", type=float, help="Maximum payout ratio")

    # Growth filters
    parser.add_argument("--rev-growth-min", type=float, help="Minimum revenue growth %")
    parser.add_argument("--earn-growth-min", type=float, help="Minimum earnings growth %")

    # Quality filters
    parser.add_argument("--margin-min", type=float, help="Minimum profit margin")
    parser.add_argument("--roe-min", type=float, help="Minimum ROE")
    parser.add_argument("--de-max", type=float, help="Maximum debt/equity")

    # Sector filter
    parser.add_argument("--sector", nargs='+', help="Filter by sector(s)")

    # Presets
    parser.add_argument("--preset", choices=['value', 'growth', 'dividend', 'quality'],
                       help="Use preset screen")

    # Analysis
    parser.add_argument("--compare", nargs='+', metavar='SYMBOL',
                       help="Compare specific stocks")
    parser.add_argument("--rank-by", help="Rank by metric")
    parser.add_argument("--top", type=int, default=20, help="Number of results to show")
    parser.add_argument("--ascending", action="store_true",
                       help="Sort ascending (default: descending)")

    # Output
    parser.add_argument("--output", "-o", help="Output CSV file")
    parser.add_argument("--json", help="Output JSON file")

    args = parser.parse_args()

    screener = StockScreener()
    screener.load_csv(args.input)

    # Apply preset
    if args.preset:
        if args.preset == 'value':
            screener.value_screen()
        elif args.preset == 'growth':
            screener.growth_screen()
        elif args.preset == 'dividend':
            screener.dividend_screen()
        elif args.preset == 'quality':
            screener.quality_screen()
    else:
        # Build filter criteria
        criteria = {}

        if args.pe:
            criteria['pe_ratio'] = tuple(args.pe)
        if args.pe_max:
            criteria['pe_ratio_max'] = args.pe_max
        if args.pb_max:
            criteria['pb_ratio_max'] = args.pb_max
        if args.peg_max:
            criteria['peg_ratio_max'] = args.peg_max

        if args.cap_min:
            criteria['market_cap_min'] = parse_number(args.cap_min)
        if args.cap_max:
            criteria['market_cap_max'] = parse_number(args.cap_max)

        if args.div_min:
            criteria['dividend_yield_min'] = args.div_min
        if args.div_max:
            criteria['dividend_yield_max'] = args.div_max
        if args.payout_max:
            criteria['payout_ratio_max'] = args.payout_max

        if args.rev_growth_min:
            criteria['revenue_growth_min'] = args.rev_growth_min
        if args.earn_growth_min:
            criteria['earnings_growth_min'] = args.earn_growth_min

        if args.margin_min:
            criteria['profit_margin_min'] = args.margin_min
        if args.roe_min:
            criteria['roe_min'] = args.roe_min
        if args.de_max:
            criteria['debt_to_equity_max'] = args.de_max

        if criteria:
            screener.filter(**criteria)

        # Sector filter
        if args.sector:
            screener.filter_by_sector(args.sector)

    # Compare mode
    if args.compare:
        comparison = screener.compare(args.compare)
        print("\n=== Stock Comparison ===")
        print(comparison.to_string())
    else:
        # Rank if requested
        if args.rank_by:
            result = screener.rank_by(args.rank_by, ascending=args.ascending, top_n=args.top)
        else:
            result = screener.df.head(args.top) if screener.df is not None else pd.DataFrame()

        # Display results
        print(screener.summary_report())

        if not result.empty:
            print(f"\n=== Top {min(args.top, len(result))} Results ===")

            # Select columns to display
            display_cols = []
            for col in ['symbol', 'name', 'sector', 'price', 'pe_ratio', 'dividend_yield',
                       'market_cap', 'profit_margin']:
                actual_col = screener._get_col(col)
                if actual_col in result.columns:
                    display_cols.append(actual_col)

            if display_cols:
                print(result[display_cols].to_string(index=False))

    # Export
    if args.output:
        screener.to_csv(args.output)
        print(f"\nExported to: {args.output}")

    if args.json:
        screener.to_json(args.json)
        print(f"Exported to: {args.json}")


if __name__ == "__main__":
    main()
