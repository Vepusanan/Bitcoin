import pandas as pd
import numpy as np
from scipy import stats
from datetime import datetime, timedelta

def event_impact_analysis(btc_data, events_data, window_days=10):
    """
    Analyze the impact of events on Bitcoin volatility using t-tests
    """
    
    results = []
    
    for idx, event in events_data.iterrows():
        event_date = event['date']
        
        # Define before and after periods
        before_start = event_date - timedelta(days=window_days)
        before_end = event_date - timedelta(days=1)
        after_start = event_date + timedelta(days=1)
        after_end = event_date + timedelta(days=window_days)
        
        # Get volatility data for before and after periods
        before_data = btc_data[(btc_data.index >= before_start) & 
                              (btc_data.index <= before_end)]['Abs_Return'].dropna()
        after_data = btc_data[(btc_data.index >= after_start) & 
                             (btc_data.index <= after_end)]['Abs_Return'].dropna()
        
        if len(before_data) > 3 and len(after_data) > 3:
            # Perform two-sample t-test
            t_stat, p_value = stats.ttest_ind(before_data, after_data)
            
            results.append({
                'event_id': event['event_id'],
                'event': event['event'],
                'event_type': event['type'],
                'severity': event['severity'],
                'before_volatility_mean': before_data.mean(),
                'after_volatility_mean': after_data.mean(),
                'volatility_change': after_data.mean() - before_data.mean(),
                't_statistic': t_stat,
                'p_value': p_value,
                'significant': p_value < 0.05
            })
    
    return pd.DataFrame(results)

def correlation_analysis(btc_data, events_data):
    """
    Analyze correlation between event severity and volatility changes
    """
    
    # This is a simplified version - you'll expand based on your event impact analysis
    event_impacts = event_impact_analysis(btc_data, events_data)
    
    # Calculate correlation between severity and volatility change
    correlation = stats.pearsonr(event_impacts['severity'], 
                               event_impacts['volatility_change'])
    
    return {
        'correlation_coefficient': correlation[0],
        'p_value': correlation[1],
        'significant': correlation[1] < 0.05
    }

# Example usage
if __name__ == "__main__":
    # Load data (you'll need to run previous members' code first)
    btc_data = pd.read_csv('data/raw/bitcoin_prices.csv', index_col=0, parse_dates=True)
    events_data = pd.read_csv('data/processed/market_events.csv', parse_dates=['date'])
    
    # Perform event impact analysis
    impact_results = event_impact_analysis(btc_data, events_data)
    
    # Perform correlation analysis
    correlation_results = correlation_analysis(btc_data, events_data)
    
    print("Hypothesis testing completed!")