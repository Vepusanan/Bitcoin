import pandas as pd
import numpy as np
from scipy import stats
import sys
from pathlib import Path

def calculate_descriptive_stats(btc_data):
    """
    Calculate comprehensive descriptive statistics for Bitcoin data
    """
    # Ensure only numeric columns are converted
    numeric_cols = ['Close', 'High', 'Low', 'Open', 'Volume',
                    'Daily_Return', 'Volatility_30d', 'Abs_Return']

    # Flatten MultiIndex if any (from yf.download)
    if isinstance(btc_data.columns, pd.MultiIndex):
        btc_data.columns = ['_'.join(filter(None, col)) for col in btc_data.columns]

    for col in numeric_cols:
        if col in btc_data.columns:
            btc_data[col] = pd.to_numeric(btc_data[col], errors='coerce')

    stats_dict = {}

    # Returns
    if 'Daily_Return' in btc_data.columns:
        returns = btc_data['Daily_Return'].dropna()
        stats_dict['returns'] = {
            'count': len(returns),
            'mean': returns.mean(),
            'std': returns.std(),
            'min': returns.min(),
            'max': returns.max(),
            'median': returns.median(),
            'skewness': stats.skew(returns),
            'kurtosis': stats.kurtosis(returns),
            'q25': returns.quantile(0.25),
            'q75': returns.quantile(0.75)
        }

    # Volatility
    if 'Volatility_30d' in btc_data.columns:
        volatility = btc_data['Volatility_30d'].dropna()
        stats_dict['volatility'] = {
            'count': len(volatility),
            'mean': volatility.mean(),
            'std': volatility.std(),
            'min': volatility.min(),
            'max': volatility.max(),
            'median': volatility.median(),
            'skewness': stats.skew(volatility),
            'kurtosis': stats.kurtosis(volatility)
        }

    # Prices
    if 'Close' in btc_data.columns:
        prices = btc_data['Close'].dropna()
        stats_dict['prices'] = {
            'count': len(prices),
            'mean': prices.mean(),
            'std': prices.std(),
            'min': prices.min(),
            'max': prices.max(),
            'median': prices.median()
        }

    return stats_dict


def test_normality(data_series, alpha=0.05):
    """
    Test if data follows normal distribution using multiple tests
    """
    results = {}

    # Shapiro-Wilk test
    if len(data_series) <= 5000:
        shapiro_stat, shapiro_p = stats.shapiro(data_series)
        results['shapiro'] = {
            'statistic': shapiro_stat,
            'p_value': shapiro_p,
            'is_normal': shapiro_p > alpha
        }

    # Kolmogorov-Smirnov test
    ks_stat, ks_p = stats.kstest(
        data_series,
        'norm',
        args=(data_series.mean(), data_series.std())
    )
    results['kolmogorov_smirnov'] = {
        'statistic': ks_stat,
        'p_value': ks_p,
        'is_normal': ks_p > alpha
    }

    # D'Agostino's normality test
    dagostino_stat, dagostino_p = stats.normaltest(data_series)
    results['dagostino'] = {
        'statistic': dagostino_stat,
        'p_value': dagostino_p,
        'is_normal': dagostino_p > alpha
    }

    return results


if __name__ == "__main__":
    # Project paths
    project_root = Path(__file__).resolve().parents[2]
    data_path = project_root / 'data' / 'raw' / 'bitcoin_prices.csv'
    results_path = project_root / "results"
    results_path.mkdir(parents=True, exist_ok=True)

    if not data_path.exists():
        print(f"Error: CSV file not found at {data_path}")
        sys.exit(1)

    # Load CSV safely
    btc_data = pd.read_csv(data_path)
    
    # Ensure 'Date' column is datetime and set as index
    if 'Date' in btc_data.columns:
        btc_data['Date'] = pd.to_datetime(btc_data['Date'], errors='coerce')
        btc_data = btc_data.set_index('Date')
        btc_data = btc_data[btc_data.index.notna()]

    # Calculate stats
    desc_stats = calculate_descriptive_stats(btc_data)
    normality_results = test_normality(btc_data['Daily_Return'].dropna() if 'Daily_Return' in btc_data.columns else pd.Series(dtype=float))

    # Print and save results
    print("Descriptive Statistics:")
    print(desc_stats)
    print("\nNormality Test Results:")
    print(normality_results)

    output_file = results_path / "descriptive_stats.txt"
    with open(output_file, "w") as f:
        f.write("Descriptive Statistics:\n")
        f.write(str(desc_stats))
        f.write("\n\nNormality Test Results:\n")
        f.write(str(normality_results))

    print(f"\nResults saved to {output_file}")
