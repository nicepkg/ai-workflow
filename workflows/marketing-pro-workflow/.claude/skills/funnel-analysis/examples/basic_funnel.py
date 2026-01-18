"""
Basic Funnel Analysis Example

This example demonstrates how to use the Funnel Analysis skill
to analyze a simple e-commerce conversion funnel.
"""

import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts.funnel_analyzer import FunnelAnalyzer
from scripts.visualizer import FunnelVisualizer

def create_sample_data():
    """
    Create sample e-commerce funnel data.
    """
    np.random.seed(42)
    n_users = 10000

    # Generate user data
    data = {
        'user_id': range(1, n_users + 1),
        'device': np.random.choice(['Mobile', 'Desktop'], n_users, p=[0.6, 0.4]),
        'gender': np.random.choice(['Male', 'Female'], n_users, p=[0.55, 0.45]),
        'homepage': True,  # All users visit homepage
        'search': np.random.choice([True, False], n_users, p=[0.5, 0.5]),
        'product_view': np.random.choice([True, False], n_users, p=[0.3, 0.7]),
        'add_to_cart': np.random.choice([True, False], n_users, p=[0.15, 0.85]),
        'purchase': np.random.choice([True, False], n_users, p=[0.05, 0.95])
    }

    # Create dependencies: users must complete previous steps to reach later steps
    df = pd.DataFrame(data)

    # Apply logical dependencies
    for i in range(len(df)):
        if not df.loc[i, 'search']:
            df.loc[i, 'product_view'] = False
            df.loc[i, 'add_to_cart'] = False
            df.loc[i, 'purchase'] = False
        elif not df.loc[i, 'product_view']:
            df.loc[i, 'add_to_cart'] = False
            df.loc[i, 'purchase'] = False
        elif not df.loc[i, 'add_to_cart']:
            df.loc[i, 'purchase'] = False

    return df

def main():
    """
    Run basic funnel analysis example.
    """
    print("=== Basic Funnel Analysis Example ===\n")

    # Create sample data
    print("1. Creating sample e-commerce data...")
    df = create_sample_data()
    print(f"   Generated data for {len(df)} users")

    # Initialize analyzer
    analyzer = FunnelAnalyzer()

    # Load data
    analyzer.load_data(df, user_id_col='user_id')

    # Define funnel steps
    steps = ['Homepage', 'Search', 'Product View', 'Add to Cart', 'Purchase']
    step_columns = ['homepage', 'search', 'product_view', 'add_to_cart', 'purchase']
    analyzer.define_steps(steps, step_columns)

    # Build funnel
    print("\n2. Building conversion funnel...")
    funnel_df = analyzer.build_funnel()
    print("\nFunnel Results:")
    print(funnel_df[['step', 'users', 'conversion_rate']].to_string(index=False,
                                                                   formatters={'conversion_rate': '{:.1%}'.format}))

    # Calculate metrics
    print("\n3. Calculating key metrics...")
    metrics = analyzer.calculate_metrics(funnel_df)
    print(f"Overall Conversion Rate: {metrics['total_conversion_rate']:.1%}")
    print(f"Total Drop-off Rate: {metrics['total_drop_off_rate']:.1%}")
    if metrics['biggest_drop_off_step']:
        print(f"Biggest Drop-off: {metrics['biggest_drop_off_step']} ({metrics['biggest_drop_off_rate']:.1%})")

    # Generate insights
    print("\n4. Generating insights...")
    insights = analyzer.generate_insights(funnel_df)
    print("Key Insights:")
    for insight in insights:
        print(f"  {insight}")

    # Create visualizations
    print("\n5. Creating visualizations...")
    visualizer = FunnelVisualizer()

    # Basic funnel chart
    funnel_fig = visualizer.create_basic_funnel(
        funnel_df,
        title="E-commerce Conversion Funnel"
    )
    visualizer.save_figure(funnel_fig, 'basic_funnel_chart.html', 'html')

    # Conversion rate chart
    conv_rate_fig = visualizer.create_conversion_rate_chart(
        funnel_df,
        title="Step-by-Step Conversion Rates"
    )
    visualizer.save_figure(conv_rate_fig, 'conversion_rates.html', 'html')

    # Drop-off analysis
    drop_off_fig = visualizer.create_drop_off_analysis(
        funnel_df,
        title="User Drop-off Analysis"
    )
    visualizer.save_figure(drop_off_fig, 'drop_off_analysis.html', 'html')

    # Comprehensive dashboard
    dashboard_fig = visualizer.create_comprehensive_dashboard(
        funnel_df,
        title="E-commerce Funnel Dashboard"
    )
    visualizer.save_figure(dashboard_fig, 'funnel_dashboard.html', 'html')

    # Export detailed report
    print("\n6. Exporting detailed report...")
    report_path = analyzer.export_report(funnel_df, filename='basic_funnel_report.html')

    print(f"\n=== Analysis Complete ===")
    print(f"Generated files:")
    print(f"  - basic_funnel_chart.html")
    print(f"  - conversion_rates.html")
    print(f"  - drop_off_analysis.html")
    print(f"  - funnel_dashboard.html")
    print(f"  - basic_funnel_report.html")

if __name__ == "__main__":
    main()