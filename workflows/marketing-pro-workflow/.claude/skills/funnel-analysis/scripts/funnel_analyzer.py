"""
Funnel Analysis Core Functions

This module provides the main functionality for analyzing user conversion funnels,
including data processing, conversion rate calculations, and segmentation analysis.
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Optional, Tuple
import warnings

class FunnelAnalyzer:
    """
    Main class for funnel analysis.

    Provides methods for building funnels from user journey data,
    calculating conversion rates, and performing segmentation analysis.
    """

    def __init__(self):
        self.data = None
        self.funnel_steps = []
        self.user_id_col = 'user_id'

    def load_data(self, data: pd.DataFrame, user_id_col: str = 'user_id') -> None:
        """
        Load user journey data for funnel analysis.

        Args:
            data: DataFrame containing user journey information
            user_id_col: Name of the user identifier column
        """
        self.data = data.copy()
        self.user_id_col = user_id_col
        print(f"Loaded data with {len(data)} users and {len(data.columns)} columns")

    def define_steps(self, steps: List[str], step_columns: List[str] = None) -> None:
        """
        Define funnel steps for analysis.

        Args:
            steps: List of step names in order
            step_columns: List of corresponding column names (optional)
        """
        self.funnel_steps = steps
        if step_columns:
            self.step_columns = step_columns
        else:
            # Default: assume columns have same names as steps
            self.step_columns = steps
        print(f"Defined funnel with {len(steps)} steps: {steps}")

    def build_funnel(self) -> pd.DataFrame:
        """
        Build funnel data frame with user counts at each step.

        Returns:
            DataFrame with step names and user counts
        """
        if self.data is None:
            raise ValueError("No data loaded. Use load_data() first.")

        if not self.funnel_steps:
            raise ValueError("No steps defined. Use define_steps() first.")

        funnel_data = []

        for i, (step_name, step_col) in enumerate(zip(self.funnel_steps, self.step_columns)):
            if step_col in self.data.columns:
                # Count users who reached this step
                if self.data[step_col].dtype == 'bool':
                    count = self.data[step_col].sum()
                elif pd.api.types.is_datetime64_any_dtype(self.data[step_col]):
                    count = self.data[step_col].notna().sum()
                else:
                    # Assume non-null means reached step
                    count = self.data[step_col].notna().sum()

                funnel_data.append({
                    'step': step_name,
                    'step_order': i + 1,
                    'users': count,
                    'conversion_rate': None  # Will calculate later
                })
            else:
                warnings.warn(f"Column '{step_col}' not found in data")

        funnel_df = pd.DataFrame(funnel_data)

        # Calculate conversion rates
        for i in range(len(funnel_df)):
            if i == 0:
                funnel_df.loc[i, 'conversion_rate'] = 1.0
            else:
                prev_users = funnel_df.loc[i-1, 'users']
                curr_users = funnel_df.loc[i, 'users']
                if prev_users > 0:
                    funnel_df.loc[i, 'conversion_rate'] = curr_users / prev_users
                else:
                    funnel_df.loc[i, 'conversion_rate'] = 0

        return funnel_df

    def segment_analysis(self, segment_col: str) -> Dict[str, pd.DataFrame]:
        """
        Perform funnel analysis segmented by a categorical variable.

        Args:
            segment_col: Column name for segmentation

        Returns:
            Dictionary with segment names as keys and funnel DataFrames as values
        """
        if segment_col not in self.data.columns:
            raise ValueError(f"Segment column '{segment_col}' not found")

        segments = self.data[segment_col].unique()
        segment_funnels = {}

        for segment in segments:
            segment_data = self.data[self.data[segment_col] == segment].copy()

            # Temporarily replace data for segment
            original_data = self.data
            self.data = segment_data

            try:
                segment_funnel = self.build_funnel()
                segment_funnels[str(segment)] = segment_funnel
            finally:
                # Restore original data
                self.data = original_data

        return segment_funnels

    def calculate_metrics(self, funnel_df: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate key funnel metrics.

        Args:
            funnel_df: Funnel DataFrame from build_funnel()

        Returns:
            Dictionary with calculated metrics
        """
        if len(funnel_df) == 0:
            return {}

        total_users_start = funnel_df.iloc[0]['users']
        total_users_end = funnel_df.iloc[-1]['users']

        metrics = {
            'total_conversion_rate': total_users_end / total_users_start if total_users_start > 0 else 0,
            'total_drop_off_rate': 1 - (total_users_end / total_users_start) if total_users_start > 0 else 0,
            'biggest_drop_off_step': None,
            'biggest_drop_off_rate': 0
        }

        # Find biggest drop-off
        for i in range(1, len(funnel_df)):
            prev_users = funnel_df.iloc[i-1]['users']
            curr_users = funnel_df.iloc[i]['users']

            if prev_users > 0:
                drop_off_rate = 1 - (curr_users / prev_users)
                if drop_off_rate > metrics['biggest_drop_off_rate']:
                    metrics['biggest_drop_off_rate'] = drop_off_rate
                    metrics['biggest_drop_off_step'] = funnel_df.iloc[i]['step']

        return metrics

    def generate_insights(self, funnel_df: pd.DataFrame,
                         segment_funnels: Dict[str, pd.DataFrame] = None) -> List[str]:
        """
        Generate actionable insights from funnel analysis.

        Args:
            funnel_df: Main funnel DataFrame
            segment_funnels: Optional segmented funnels for comparison

        Returns:
            List of insight strings
        """
        insights = []
        metrics = self.calculate_metrics(funnel_df)

        # Overall conversion insights
        if metrics['total_conversion_rate'] < 0.01:
            insights.append("❗ Critical: Overall conversion rate is below 1%, requires immediate attention")
        elif metrics['total_conversion_rate'] < 0.05:
            insights.append("⚠️ Warning: Overall conversion rate is below 5%, optimization needed")
        else:
            insights.append(f"✓ Overall conversion rate is {metrics['total_conversion_rate']:.1%}")

        # Drop-off insights
        if metrics['biggest_drop_off_step']:
            drop_off_pct = metrics['biggest_drop_off_rate'] * 100
            insights.append(f"🎯 Biggest drop-off: {metrics['biggest_drop_off_step']} ({drop_off_pct:.1f}% loss)")

        # Step-by-step insights
        for i, row in funnel_df.iterrows():
            if i > 0:  # Skip first step
                conv_rate = row['conversion_rate']
                if conv_rate < 0.3:
                    insights.append(f"📉 {row['step']} has very low conversion ({conv_rate:.1%})")
                elif conv_rate < 0.6:
                    insights.append(f"📊 {row['step']} has moderate conversion ({conv_rate:.1%})")

        # Segment comparison insights
        if segment_funnels:
            best_segment = None
            worst_segment = None
            best_rate = 0
            worst_rate = 1

            for segment, seg_funnel in segment_funnels.items():
                seg_metrics = self.calculate_metrics(seg_funnel)
                if seg_metrics.get('total_conversion_rate', 0) > best_rate:
                    best_rate = seg_metrics['total_conversion_rate']
                    best_segment = segment
                if seg_metrics.get('total_conversion_rate', 1) < worst_rate:
                    worst_rate = seg_metrics['total_conversion_rate']
                    worst_segment = segment

            if best_segment and worst_segment:
                insights.append(f"🏆 Best performing segment: {best_segment} ({best_rate:.1%})")
                insights.append(f"🔻 Worst performing segment: {worst_segment} ({worst_rate:.1%})")

        return insights

    def export_report(self, funnel_df: pd.DataFrame,
                     segment_funnels: Dict[str, pd.DataFrame] = None,
                     filename: str = 'funnel_analysis_report.html') -> str:
        """
        Export comprehensive funnel analysis report.

        Args:
            funnel_df: Main funnel DataFrame
            segment_funnels: Optional segmented funnels
            filename: Output filename

        Returns:
            Path to generated report file
        """
        # Generate insights
        insights = self.generate_insights(funnel_df, segment_funnels)
        metrics = self.calculate_metrics(funnel_df)

        # Create HTML report
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Funnel Analysis Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
                .metrics {{ margin: 20px 0; }}
                .insights {{ background-color: #f9f9f9; padding: 20px; border-radius: 5px; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Funnel Analysis Report</h1>
                <p>Generated on {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>

            <div class="metrics">
                <h2>Key Metrics</h2>
                <ul>
                    <li><strong>Total Conversion Rate:</strong> {metrics.get('total_conversion_rate', 0):.1%}</li>
                    <li><strong>Total Drop-off Rate:</strong> {metrics.get('total_drop_off_rate', 0):.1%}</li>
                    <li><strong>Biggest Drop-off:</strong> {metrics.get('biggest_drop_off_step', 'N/A')}</li>
                </ul>
            </div>

            <div class="insights">
                <h2>Key Insights</h2>
                <ul>
                    {''.join([f'<li>{insight}</li>' for insight in insights])}
                </ul>
            </div>

            <div>
                <h2>Funnel Details</h2>
                <table>
                    <tr>
                        <th>Step</th>
                        <th>Users</th>
                        <th>Conversion Rate</th>
                        <th>Drop-off Rate</th>
                    </tr>
        """

        # Add funnel table rows
        for i, row in funnel_df.iterrows():
            if i == 0:
                drop_off_rate = 0
            else:
                prev_users = funnel_df.iloc[i-1]['users']
                drop_off_rate = 1 - (row['users'] / prev_users) if prev_users > 0 else 0

            html_content += f"""
                    <tr>
                        <td>{row['step']}</td>
                        <td>{row['users']:,}</td>
                        <td>{row['conversion_rate']:.1%}</td>
                        <td>{drop_off_rate:.1%}</td>
                    </tr>
            """

        html_content += """
                </table>
            </div>
        </body>
        </html>
        """

        # Write to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"Report saved to {filename}")
        return filename