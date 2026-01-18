"""
Funnel Visualization Functions

This module provides visualization utilities for funnel analysis,
including interactive funnel charts, comparison charts, and detailed metrics.
"""

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from typing import Dict, List, Optional


class FunnelVisualizer:
    """
    Class for creating funnel visualizations.

    Provides methods for creating various types of funnel charts
    and comparison visualizations.
    """

    def __init__(self):
        self.color_palette = px.colors.qualitative.Set3

    def create_basic_funnel(self, funnel_df: pd.DataFrame,
                           title: str = "Conversion Funnel",
                           show_values: bool = True) -> go.Figure:
        """
        Create a basic funnel chart.

        Args:
            funnel_df: DataFrame with funnel data
            title: Chart title
            show_values: Whether to show user counts

        Returns:
            Plotly figure object
        """
        fig = go.Figure(go.Funnel(
            y=funnel_df['step'],
            x=funnel_df['users'],
            textposition="inside",
            textinfo="value+percent initial" if show_values else "percent initial",
            marker=dict(color=self.color_palette[:len(funnel_df)])
        ))

        fig.update_layout(
            title={
                'text': title,
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20}
            },
            font=dict(size=14),
            height=600
        )

        return fig

    def create_segmented_funnel(self, segment_funnels: Dict[str, pd.DataFrame],
                               title: str = "Segmented Funnel Comparison") -> go.Figure:
        """
        Create a side-by-side comparison of segmented funnels.

        Args:
            segment_funnels: Dictionary of segment names to funnel DataFrames
            title: Chart title

        Returns:
            Plotly figure object
        """
        segments = list(segment_funnels.keys())
        colors = self.color_palette[:len(segments)]

        fig = go.Figure()

        for i, (segment, funnel_df) in enumerate(segment_funnels.items()):
            fig.add_trace(go.Funnel(
                name=segment,
                y=funnel_df['step'],
                x=funnel_df['users'],
                textinfo="percent initial",
                marker=dict(color=colors[i]),
                opacity=0.8
            ))

        fig.update_layout(
            title={
                'text': title,
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20}
            },
            font=dict(size=12),
            height=700
        )

        return fig

    def create_conversion_rate_chart(self, funnel_df: pd.DataFrame,
                                   title: str = "Step-by-Step Conversion Rates") -> go.Figure:
        """
        Create a bar chart showing conversion rates between steps.

        Args:
            funnel_df: DataFrame with funnel data
            title: Chart title

        Returns:
            Plotly figure object
        """
        # Calculate step-to-step conversion rates
        conv_rates = []
        step_labels = []

        for i in range(len(funnel_df)):
            if i == 0:
                conv_rates.append(1.0)
                step_labels.append(f"{funnel_df.iloc[i]['step']}\n(100%)")
            else:
                prev_users = funnel_df.iloc[i-1]['users']
                curr_users = funnel_df.iloc[i]['users']
                rate = curr_users / prev_users if prev_users > 0 else 0
                conv_rates.append(rate)
                step_labels.append(f"{funnel_df.iloc[i]['step']}\n({rate:.1%})")

        fig = go.Figure(data=[
            go.Bar(
                x=step_labels,
                y=conv_rates,
                marker=dict(color=self.color_palette[2]),
                text=[f"{rate:.1%}" for rate in conv_rates],
                textposition='auto',
            )
        ])

        fig.update_layout(
            title={
                'text': title,
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20}
            },
            xaxis_title="Funnel Step",
            yaxis_title="Conversion Rate",
            yaxis=dict(tickformat='.0%'),
            height=500
        )

        # Add reference line at 100%
        fig.add_hline(y=1.0, line_dash="dash", line_color="red", opacity=0.5)

        return fig

    def create_drop_off_analysis(self, funnel_df: pd.DataFrame,
                               title: str = "Drop-off Analysis") -> go.Figure:
        """
        Create a chart showing user drop-off at each step.

        Args:
            funnel_df: DataFrame with funnel data
            title: Chart title

        Returns:
            Plotly figure object
        """
        # Calculate drop-offs
        drop_offs = []
        drop_off_rates = []
        step_names = []

        for i, row in funnel_df.iterrows():
            if i == 0:
                drop_offs.append(0)
                drop_off_rates.append(0.0)
                step_names.append(row['step'])
            else:
                prev_users = funnel_df.iloc[i-1]['users']
                curr_users = row['users']
                drop_off = prev_users - curr_users
                drop_off_rate = drop_off / prev_users if prev_users > 0 else 0

                drop_offs.append(drop_off)
                drop_off_rates.append(drop_off_rate)
                step_names.append(row['step'])

        # Create subplot
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=("Number of Users Dropped Off", "Drop-off Rate"),
            vertical_spacing=0.1
        )

        # Add bar chart for absolute drop-offs
        fig.add_trace(
            go.Bar(
                x=step_names,
                y=drop_offs,
                marker=dict(color=self.color_palette[4]),
                name="Users Lost"
            ),
            row=1, col=1
        )

        # Add bar chart for drop-off rates
        fig.add_trace(
            go.Bar(
                x=step_names,
                y=drop_off_rates,
                marker=dict(color=self.color_palette[5]),
                name="Drop-off Rate",
                text=[f"{rate:.1%}" for rate in drop_off_rates],
                textposition='auto'
            ),
            row=2, col=1
        )

        fig.update_layout(
            title={
                'text': title,
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20}
            },
            height=700,
            showlegend=False
        )

        fig.update_yaxes(tickformat='.0%', row=2, col=1)

        return fig

    def create_segment_comparison(self, segment_funnels: Dict[str, pd.DataFrame],
                                metric: str = "total_conversion_rate",
                                title: str = "Segment Performance Comparison") -> go.Figure:
        """
        Create a comparison chart of segments by a specific metric.

        Args:
            segment_funnels: Dictionary of segment names to funnel DataFrames
            metric: Metric to compare ('total_conversion_rate' or 'biggest_drop_off')
            title: Chart title

        Returns:
            Plotly figure object
        """
        segments = []
        values = []

        for segment, funnel_df in segment_funnels.items():
            segments.append(segment)

            if metric == "total_conversion_rate":
                if len(funnel_df) > 1:
                    start_users = funnel_df.iloc[0]['users']
                    end_users = funnel_df.iloc[-1]['users']
                    value = end_users / start_users if start_users > 0 else 0
                else:
                    value = 0
            elif metric == "biggest_drop_off":
                max_drop_off = 0
                for i in range(1, len(funnel_df)):
                    prev_users = funnel_df.iloc[i-1]['users']
                    curr_users = funnel_df.iloc[i]['users']
                    drop_off = 1 - (curr_users / prev_users) if prev_users > 0 else 0
                    max_drop_off = max(max_drop_off, drop_off)
                value = max_drop_off
            else:
                value = 0

            values.append(value)

        fig = go.Figure(data=[
            go.Bar(
                x=segments,
                y=values,
                marker=dict(color=self.color_palette[:len(segments)]),
                text=[f"{val:.1%}" for val in values],
                textposition='auto',
            )
        ])

        y_axis_title = "Total Conversion Rate" if metric == "total_conversion_rate" else "Biggest Drop-off Rate"

        fig.update_layout(
            title={
                'text': title,
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20}
            },
            xaxis_title="Segment",
            yaxis_title=y_axis_title,
            yaxis=dict(tickformat='.0%'),
            height=500
        )

        return fig

    def create_comprehensive_dashboard(self, funnel_df: pd.DataFrame,
                                     segment_funnels: Dict[str, pd.DataFrame] = None,
                                     title: str = "Funnel Analysis Dashboard") -> go.Figure:
        """
        Create a comprehensive dashboard with multiple visualizations.

        Args:
            funnel_df: Main funnel DataFrame
            segment_funnels: Optional segmented funnels
            title: Dashboard title

        Returns:
            Plotly figure object
        """
        # Create subplots
        if segment_funnels and len(segment_funnels) > 0:
            fig = make_subplots(
                rows=2, cols=2,
                subplot_titles=(
                    "Conversion Funnel",
                    "Step Conversion Rates",
                    "Drop-off Analysis",
                    "Segment Comparison"
                ),
                specs=[
                    [{"type": "funnel"}, {"type": "bar"}],
                    [{"type": "bar"}, {"type": "bar"}]
                ],
                vertical_spacing=0.1,
                horizontal_spacing=0.1
            )
        else:
            fig = make_subplots(
                rows=2, cols=2,
                subplot_titles=(
                    "Conversion Funnel",
                    "Step Conversion Rates",
                    "Drop-off Analysis",
                    "User Counts per Step"
                ),
                specs=[
                    [{"type": "funnel"}, {"type": "bar"}],
                    [{"type": "bar"}, {"type": "bar"}]
                ],
                vertical_spacing=0.1,
                horizontal_spacing=0.1
            )

        # Add main funnel (top left)
        fig.add_trace(
            go.Funnel(
                y=funnel_df['step'],
                x=funnel_df['users'],
                name="Funnel",
                marker=dict(color=self.color_palette[0])
            ),
            row=1, col=1
        )

        # Add conversion rates (top right)
        conv_rates = [1.0]  # First step is always 100%
        for i in range(1, len(funnel_df)):
            prev_users = funnel_df.iloc[i-1]['users']
            curr_users = funnel_df.iloc[i]['users']
            rate = curr_users / prev_users if prev_users > 0 else 0
            conv_rates.append(rate)

        fig.add_trace(
            go.Bar(
                x=funnel_df['step'],
                y=conv_rates,
                name="Conv. Rates",
                marker=dict(color=self.color_palette[1]),
                text=[f"{rate:.1%}" for rate in conv_rates],
                textposition='auto'
            ),
            row=1, col=2
        )

        # Add drop-off analysis (bottom left)
        drop_offs = [0]  # First step has no drop-off
        for i in range(1, len(funnel_df)):
            prev_users = funnel_df.iloc[i-1]['users']
            curr_users = funnel_df.iloc[i]['users']
            drop_off = prev_users - curr_users
            drop_offs.append(drop_off)

        fig.add_trace(
            go.Bar(
                x=funnel_df['step'],
                y=drop_offs,
                name="Drop-offs",
                marker=dict(color=self.color_palette[2])
            ),
            row=2, col=1
        )

        # Add segment comparison or user counts (bottom right)
        if segment_funnels and len(segment_funnels) > 0:
            segments = list(segment_funnels.keys())
            conv_rates_by_segment = []
            for segment in segments:
                seg_funnel = segment_funnels[segment]
                if len(seg_funnel) > 1:
                    start_users = seg_funnel.iloc[0]['users']
                    end_users = seg_funnel.iloc[-1]['users']
                    rate = end_users / start_users if start_users > 0 else 0
                else:
                    rate = 0
                conv_rates_by_segment.append(rate)

            fig.add_trace(
                go.Bar(
                    x=segments,
                    y=conv_rates_by_segment,
                    name="Segment Rates",
                    marker=dict(color=self.color_palette[3]),
                    text=[f"{rate:.1%}" for rate in conv_rates_by_segment],
                    textposition='auto'
                ),
                row=2, col=2
            )
        else:
            fig.add_trace(
                go.Bar(
                    x=funnel_df['step'],
                    y=funnel_df['users'],
                    name="User Counts",
                    marker=dict(color=self.color_palette[3])
                ),
                row=2, col=2
            )

        fig.update_layout(
            title={
                'text': title,
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 24}
            },
            height=800,
            showlegend=False
        )

        # Update y-axis format for conversion rates
        fig.update_yaxes(tickformat='.0%', row=1, col=2)
        if segment_funnels and len(segment_funnels) > 0:
            fig.update_yaxes(tickformat='.0%', row=2, col=2)

        return fig

    def save_figure(self, fig: go.Figure, filename: str, format: str = 'html') -> str:
        """
        Save figure to file.

        Args:
            fig: Plotly figure object
            filename: Output filename
            format: Output format ('html', 'png', 'pdf', 'svg')

        Returns:
            Path to saved file
        """
        if format.lower() == 'html':
            fig.write_html(filename)
        elif format.lower() == 'png':
            fig.write_image(filename)
        elif format.lower() == 'pdf':
            fig.write_image(filename)
        elif format.lower() == 'svg':
            fig.write_image(filename)
        else:
            raise ValueError(f"Unsupported format: {format}")

        print(f"Figure saved to {filename}")
        return filename