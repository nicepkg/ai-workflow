"""
Segmented Funnel Analysis Example

This example demonstrates advanced funnel analysis with segmentation,
showing how different user groups behave differently in the conversion funnel.
"""

import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts.funnel_analyzer import FunnelAnalyzer
from scripts.visualizer import FunnelVisualizer

def create_segmented_data():
    """
    Create sample e-commerce funnel data with segmentation.
    """
    np.random.seed(42)
    n_users = 15000

    # Generate user segments with different behaviors
    segments = []
    devices = []
    genders = []

    for i in range(n_users):
        # Create segments with different characteristics
        segment_prob = np.random.random()
        if segment_prob < 0.3:
            segments.append('New User')
        elif segment_prob < 0.7:
            segments.append('Returning User')
        else:
            segments.append('VIP User')

        devices.append(np.random.choice(['Mobile', 'Desktop'], p=[0.6, 0.4]))
        genders.append(np.random.choice(['Male', 'Female'], p=[0.55, 0.45]))

    # Generate funnel behavior based on segments
    data = {
        'user_id': range(1, n_users + 1),
        'segment': segments,
        'device': devices,
        'gender': genders,
        'homepage': True
    }

    df = pd.DataFrame(data)

    # Generate step completion probabilities based on segment
    for i, row in df.iterrows():
        segment = row['segment']

        if segment == 'New User':
            # Lower conversion rates for new users
            search_prob = 0.4
            product_view_prob = 0.2
            add_to_cart_prob = 0.08
            purchase_prob = 0.02
        elif segment == 'Returning User':
            # Medium conversion rates
            search_prob = 0.6
            product_view_prob = 0.35
            add_to_cart_prob = 0.18
            purchase_prob = 0.06
        else:  # VIP User
            # Higher conversion rates for VIP users
            search_prob = 0.8
            product_view_prob = 0.6
            add_to_cart_prob = 0.4
            purchase_prob = 0.25

        # Apply segment-specific probabilities
        df.loc[i, 'search'] = np.random.random() < search_prob
        if df.loc[i, 'search']:
            df.loc[i, 'product_view'] = np.random.random() < product_view_prob
            if df.loc[i, 'product_view']:
                df.loc[i, 'add_to_cart'] = np.random.random() < add_to_cart_prob
                if df.loc[i, 'add_to_cart']:
                    df.loc[i, 'purchase'] = np.random.random() < purchase_prob
                else:
                    df.loc[i, 'purchase'] = False
            else:
                df.loc[i, 'add_to_cart'] = False
                df.loc[i, 'purchase'] = False
        else:
            df.loc[i, 'product_view'] = False
            df.loc[i, 'add_to_cart'] = False
            df.loc[i, 'purchase'] = False

    return df

def analyze_segments(analyzer, df, segment_col):
    """
    Perform detailed segment analysis.
    """
    print(f"\n=== Analysis by {segment_col} ===")

    # Get segmented funnels
    segment_funnels = analyzer.segment_analysis(segment_col)

    # Calculate metrics for each segment
    segment_metrics = {}
    for segment, funnel_df in segment_funnels.items():
        metrics = analyzer.calculate_metrics(funnel_df)
        segment_metrics[segment] = metrics

        print(f"\n{segment} Segment:")
        print(f"  Users: {funnel_df.iloc[0]['users']:,}")
        print(f"  Conversion Rate: {metrics['total_conversion_rate']:.1%}")
        if metrics['biggest_drop_off_step']:
            print(f"  Biggest Drop-off: {metrics['biggest_drop_off_step']} ({metrics['biggest_drop_off_rate']:.1%})")

    return segment_funnels, segment_metrics

def create_segment_comparison_chart(segment_funnels, segment_metrics, segment_type):
    """
    Create a detailed segment comparison visualization.
    """
    visualizer = FunnelVisualizer()

    # Create comparison chart
    comparison_fig = visualizer.create_segment_comparison(
        segment_funnels,
        metric="total_conversion_rate",
        title=f"Conversion Rate by {segment_type}"
    )
    visualizer.save_figure(comparison_fig, f'segment_comparison_{segment_type.lower()}.html', 'html')

    # Create segmented funnel chart
    segmented_funnel_fig = visualizer.create_segmented_funnel(
        segment_funnels,
        title=f"Funnel Comparison by {segment_type}"
    )
    visualizer.save_figure(segmented_funnel_fig, f'segmented_funnel_{segment_type.lower()}.html', 'html')

def main():
    """
    Run segmented funnel analysis example.
    """
    print("=== Segmented Funnel Analysis Example ===\n")

    # Create segmented sample data
    print("1. Creating segmented sample data...")
    df = create_segmented_data()
    print(f"   Generated data for {len(df)} users")
    print(f"   Segments: {df['segment'].value_counts().to_dict()}")

    # Initialize analyzer
    analyzer = FunnelAnalyzer()
    analyzer.load_data(df, user_id_col='user_id')

    # Define funnel steps
    steps = ['Homepage', 'Search', 'Product View', 'Add to Cart', 'Purchase']
    step_columns = ['homepage', 'search', 'product_view', 'add_to_cart', 'purchase']
    analyzer.define_steps(steps, step_columns)

    # Overall analysis
    print("\n2. Overall funnel analysis...")
    overall_funnel = analyzer.build_funnel()
    print("\nOverall Funnel Results:")
    print(overall_funnel[['step', 'users', 'conversion_rate']].to_string(
        index=False,
        formatters={'conversion_rate': '{:.1%}'.format}
    ))

    # Segment analysis
    print("\n3. Segment analysis...")

    # Analysis by user segment
    segment_funnels, segment_metrics = analyze_segments(analyzer, df, 'segment')
    create_segment_comparison_chart(segment_funnels, segment_metrics, 'User Segment')

    # Analysis by device
    device_funnels, device_metrics = analyze_segments(analyzer, df, 'device')
    create_segment_comparison_chart(device_funnels, device_metrics, 'Device')

    # Analysis by gender
    gender_funnels, gender_metrics = analyze_segments(analyzer, df, 'gender')
    create_segment_comparison_chart(gender_funnels, gender_metrics, 'Gender')

    # Generate insights with segmentation
    print("\n4. Generating segmented insights...")
    insights = analyzer.generate_insights(overall_funnel, segment_funnels)
    print("Key Insights:")
    for insight in insights:
        print(f"  {insight}")

    # Create comprehensive dashboard with segmentation
    print("\n5. Creating comprehensive dashboard...")
    visualizer = FunnelVisualizer()
    dashboard_fig = visualizer.create_comprehensive_dashboard(
        overall_funnel,
        segment_funnels,
        title="Segmented Funnel Analysis Dashboard"
    )
    visualizer.save_figure(dashboard_fig, 'segmented_dashboard.html', 'html')

    # Export segmented report
    print("\n6. Exporting segmented report...")
    report_path = analyzer.export_report(
        overall_funnel,
        segment_funnels,
        filename='segmented_funnel_report.html'
    )

    # Performance summary
    print("\n=== Performance Summary ===")
    best_segment = max(segment_metrics.items(), key=lambda x: x[1]['total_conversion_rate'])
    worst_segment = min(segment_metrics.items(), key=lambda x: x[1]['total_conversion_rate'])

    print(f"Best Performing Segment: {best_segment[0]} ({best_segment[1]['total_conversion_rate']:.1%})")
    print(f"Worst Performing Segment: {worst_segment[0]} ({worst_segment[1]['total_conversion_rate']:.1%})")
    print(f"Performance Gap: {(best_segment[1]['total_conversion_rate'] / worst_segment[1]['total_conversion_rate'] - 1):.1f}x")

    print(f"\n=== Analysis Complete ===")
    print(f"Generated files:")
    print(f"  - segment_comparison_user segment.html")
    print(f"  - segmented_funnel_user segment.html")
    print(f"  - segment_comparison_device.html")
    print(f"  - segmented_funnel_device.html")
    print(f"  - segment_comparison_gender.html")
    print(f"  - segmented_funnel_gender.html")
    print(f"  - segmented_dashboard.html")
    print(f"  - segmented_funnel_report.html")

if __name__ == "__main__":
    main()