import pandas as pd
import numpy as np
from scipy import stats
from datetime import timedelta
import matplotlib.pyplot as plt
from pathlib import Path

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

        # Even if some data exists, continue
        if len(before_data) == 0 and len(after_data) == 0:
            continue

        # Fill missing data with empty Series to avoid errors
        before_mean = before_data.mean() if len(before_data) > 0 else np.nan
        after_mean = after_data.mean() if len(after_data) > 0 else np.nan

        # Perform t-test only if both have enough data
        if len(before_data) > 3 and len(after_data) > 3:
            t_stat, p_value = stats.ttest_ind(before_data, after_data)
            significant = p_value < 0.05
        else:
            t_stat, p_value, significant = np.nan, np.nan, False

        # Handle both "type" and "event_type" column names
        if 'type' in event.index:
            event_type = event['type']
        elif 'event_type' in event.index:
            event_type = event['event_type']
        else:
            event_type = "unknown"

        results.append({
            'event_id': event['event_id'],
            'event': event['event'],
            'event_type': event_type,
            'severity': event['severity'],
            'before_volatility_mean': before_mean,
            'after_volatility_mean': after_mean,
            'volatility_change': after_mean - before_mean if not np.isnan(before_mean) and not np.isnan(after_mean) else np.nan,
            't_statistic': t_stat,
            'p_value': p_value,
            'significant': significant
        })

        # Plot the event impact
        window_data = btc_data[(btc_data.index >= before_start) & (btc_data.index <= after_end)]['Abs_Return']
        if len(window_data) > 0:
            plt.figure(figsize=(10, 5))
            plt.plot(window_data.index, window_data.values, label='Abs_Return', color='blue', alpha=0.7)
            plt.axvline(event_date, color='red', linestyle='--', label='Event Date')
            plt.title(f"Volatility around Event: {event['event']}")
            plt.xlabel('Date')
            plt.ylabel('Absolute Return')
            plt.legend()
            plt.grid(True, alpha=0.3)

            results_dir = Path(__file__).resolve().parents[2] / 'results'
            results_dir.mkdir(parents=True, exist_ok=True)
            plt.savefig(results_dir / f"event_{event['event_id']}_impact.png", dpi=300, bbox_inches='tight')
            plt.close()

    return pd.DataFrame(results)


def correlation_analysis(btc_data, events_data, window_days=10):
    """
    Analyze correlation between event severity and volatility changes
    """
    event_impacts = event_impact_analysis(btc_data, events_data, window_days)

    # Drop NaN changes to avoid correlation issues
    valid_impacts = event_impacts.dropna(subset=['volatility_change'])

    if len(valid_impacts) > 0:
        correlation = stats.pearsonr(valid_impacts['severity'], valid_impacts['volatility_change'])
        return {
            'correlation_coefficient': correlation[0],
            'p_value': correlation[1],
            'significant': correlation[1] < 0.05
        }
    else:
        return {
            'correlation_coefficient': np.nan,
            'p_value': np.nan,
            'significant': False
        }


if __name__ == "__main__":
    # Load Bitcoin data
    btc_data = pd.read_csv(
        'data/raw/bitcoin_prices.csv',
        index_col=0,
        parse_dates=True,
        date_parser=lambda x: pd.to_datetime(x, format="%Y-%m-%d", errors="coerce")
    )
    btc_data.index = pd.to_datetime(btc_data.index, errors='coerce')  # ensure datetime index

    # Load events data
    events_data = pd.read_csv('data/processed/market_events.csv', parse_dates=['date'])

    # Debug: show column names to confirm structure
    print("Events Data Columns:", events_data.columns.tolist())
    print(events_data.head())

    # Perform event impact analysis
    impact_results = event_impact_analysis(btc_data, events_data)
    print("\nEvent Impact Results:")
    print(impact_results.head())

    # Perform correlation analysis
    correlation_results = correlation_analysis(btc_data, events_data)
    print("\nCorrelation Results:")
    print(correlation_results)
