#!/usr/bin/env python3
"""
Bitcoin Volatility Analysis - Main Execution Script

This script runs the complete Bitcoin volatility analysis pipeline:
1. Data collection (Bitcoin prices and market events)
2. Descriptive statistics analysis
3. Distribution analysis
4. Hypothesis testing (event impact analysis)
5. Visualization generation

Author: Bitcoin Analysis Project
Date: 2024
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
project_root = Path(__file__).resolve().parent
src_path = project_root / 'src'
sys.path.insert(0, str(src_path))

# Import modules
from data_collection.bitcoin_prices import collect_bitcoin_data, save_bitcoin_data
from data_collection.market_events import create_events_database, save_events_data
from analysis.descriptive_stats import calculate_descriptive_stats, test_normality
from analysis.distribution_analysis import test_normality_comprehensive, fit_alternative_distributions
from analysis.hypothesis_tests import event_impact_analysis, correlation_analysis
from visualization.plots import plot_bitcoin_timeseries, plot_distribution_analysis

def main():
    """
    Main execution function for Bitcoin volatility analysis
    """
    print("=" * 60)
    print("BITCOIN VOLATILITY ANALYSIS")
    print("=" * 60)
    
    # Step 1: Data Collection
    print("\n1. COLLECTING DATA...")
    print("-" * 30)
    
    # Collect Bitcoin price data
    print("Collecting Bitcoin price data...")
    btc_data = collect_bitcoin_data()
    if btc_data is None:
        print("ERROR: Failed to collect Bitcoin data. Exiting.")
        return 1
    
    # Save Bitcoin data
    save_bitcoin_data(btc_data)
    
    # Create and save market events data
    print("Creating market events database...")
    events_data = create_events_database()
    save_events_data(events_data)
    
    print(f"✓ Data collection complete: {len(btc_data)} Bitcoin records, {len(events_data)} events")
    
    # Step 2: Descriptive Statistics
    print("\n2. CALCULATING DESCRIPTIVE STATISTICS...")
    print("-" * 40)
    
    desc_stats = calculate_descriptive_stats(btc_data)
    normality_results = test_normality(btc_data['Daily_Return'].dropna())
    
    # Save descriptive statistics
    results_dir = project_root / 'results'
    results_dir.mkdir(exist_ok=True)
    
    with open(results_dir / 'descriptive_stats.txt', 'w') as f:
        f.write("BITCOIN VOLATILITY ANALYSIS - DESCRIPTIVE STATISTICS\n")
        f.write("=" * 50 + "\n\n")
        f.write("DESCRIPTIVE STATISTICS:\n")
        f.write(str(desc_stats))
        f.write("\n\nNORMALITY TEST RESULTS:\n")
        f.write(str(normality_results))
    
    print("✓ Descriptive statistics calculated and saved")
    
    # Step 3: Distribution Analysis
    print("\n3. ANALYZING DISTRIBUTIONS...")
    print("-" * 30)
    
    returns = btc_data['Daily_Return'].dropna()
    dist_tests = test_normality_comprehensive(returns)
    alt_distributions = fit_alternative_distributions(returns)
    
    print("✓ Distribution analysis complete")
    
    # Step 4: Event Impact Analysis
    print("\n4. ANALYZING EVENT IMPACTS...")
    print("-" * 30)
    
    impact_results = event_impact_analysis(btc_data, events_data)
    correlation_results = correlation_analysis(btc_data, events_data)
    
    print(f"✓ Event impact analysis complete: {len(impact_results)} events analyzed")
    
    # Step 5: Generate Visualizations
    print("\n5. GENERATING VISUALIZATIONS...")
    print("-" * 35)
    
    try:
        plot_bitcoin_timeseries(btc_data)
        plot_distribution_analysis(btc_data)
        print("✓ Visualizations generated and saved")
    except Exception as e:
        print(f"Warning: Error generating visualizations: {e}")
    
    # Step 6: Summary Report
    print("\n6. GENERATING SUMMARY REPORT...")
    print("-" * 35)
    
    # Create summary report
    summary_file = results_dir / 'analysis_summary.txt'
    with open(summary_file, 'w') as f:
        f.write("BITCOIN VOLATILITY ANALYSIS - SUMMARY REPORT\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Data Period: {btc_data.index.min().strftime('%Y-%m-%d')} to {btc_data.index.max().strftime('%Y-%m-%d')}\n")
        f.write(f"Total Records: {len(btc_data)}\n")
        f.write(f"Total Events: {len(events_data)}\n\n")
        
        f.write("KEY FINDINGS:\n")
        f.write("-" * 15 + "\n")
        f.write(f"Mean Daily Return: {desc_stats['returns']['mean']:.4f}\n")
        f.write(f"Daily Return Std Dev: {desc_stats['returns']['std']:.4f}\n")
        f.write(f"Mean Volatility (30d): {desc_stats['volatility']['mean']:.4f}\n")
        f.write(f"Returns Skewness: {desc_stats['returns']['skewness']:.4f}\n")
        f.write(f"Returns Kurtosis: {desc_stats['returns']['kurtosis']:.4f}\n\n")
        
        f.write("NORMALITY TESTS:\n")
        f.write("-" * 15 + "\n")
        for test_name, test_result in normality_results.items():
            f.write(f"{test_name}: {'Normal' if test_result['is_normal'] else 'Not Normal'} (p={test_result['p_value']:.4f})\n")
        
        f.write(f"\nEVENT IMPACT ANALYSIS:\n")
        f.write("-" * 20 + "\n")
        f.write(f"Events with significant impact: {impact_results['significant'].sum()}\n")
        f.write(f"Correlation between severity and volatility change: {correlation_results['correlation_coefficient']:.4f}\n")
        f.write(f"Correlation significant: {correlation_results['significant']}\n")
    
    print("✓ Summary report generated")
    
    # Final success message
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("=" * 60)
    print(f"Results saved to: {results_dir}")
    print("Generated files:")
    print("  - descriptive_stats.txt")
    print("  - analysis_summary.txt")
    print("  - bitcoin_timeseries.png")
    print("  - distribution_analysis.png")
    print("  - event_*_impact.png (for each event)")
    
    return 0

if __name__ == "__main__":
    try:
        import pandas as pd
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\nAnalysis interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
