import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_descriptive_stats(btc_data):
    """
    Calculate comprehensive descriptive statistics for Bitcoin data
    """
    
    stats_dict = {}
    
    # Basic statistics for returns
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
    
    # Basic statistics for volatility
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
    
    # Basic statistics for prices
    prices = btc_data['Close']
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
    
    # Shapiro-Wilk test (for smaller samples)
    if len(data_series) <= 5000:
        shapiro_stat, shapiro_p = stats.shapiro(data_series)
        results['shapiro'] = {
            'statistic': shapiro_stat,
            'p_value': shapiro_p,
            'is_normal': shapiro_p > alpha
        }
    
    # Kolmogorov-Smirnov test
    ks_stat, ks_p = stats.kstest(data_series, 'norm', args=(data_series.mean(), data_series.std()))
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

# Example usage
if __name__ == "__main__":
    # Load Bitcoin data (you'll need to run Member 1's code first)
    btc_data = pd.read_csv('data/raw/bitcoin_prices.csv', index_col=0, parse_dates=True)
    
    # Calculate descriptive statistics
    desc_stats = calculate_descriptive_stats(btc_data)
    
    # Test normality of returns
    normality_results = test_normality(btc_data['Daily_Return'].dropna())
    
    print("Descriptive Statistics calculated successfully!")