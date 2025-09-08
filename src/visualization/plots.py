import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from pathlib import Path
import sys

def plot_bitcoin_timeseries(btc_data):
    """
    Create time series plots for Bitcoin price and volatility
    """
    fig, axes = plt.subplots(3, 1, figsize=(15, 12))
    
    # Bitcoin price over time
    axes[0].plot(btc_data.index, btc_data['Close'], color='orange', linewidth=1)
    axes[0].set_title('Bitcoin Price Over Time (2020-2024)', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('Price (USD)')
    axes[0].grid(True, alpha=0.3)
    
    # Daily returns
    axes[1].plot(btc_data.index, btc_data['Daily_Return'], color='blue', alpha=0.7)
    axes[1].set_title('Bitcoin Daily Returns', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('Daily Return (%)')
    axes[1].grid(True, alpha=0.3)
    axes[1].axhline(y=0, color='red', linestyle='--', alpha=0.5)
    
    # 30-day volatility
    axes[2].plot(btc_data.index, btc_data['Volatility_30d'], color='red', linewidth=1)
    axes[2].set_title('Bitcoin 30-Day Rolling Volatility', fontsize=14, fontweight='bold')
    axes[2].set_ylabel('Volatility (Std Dev)')
    axes[2].set_xlabel('Date')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Ensure results directory exists and save figure
    results_dir = Path(__file__).resolve().parents[2] / 'results'
    results_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(results_dir / 'bitcoin_timeseries.png', dpi=300, bbox_inches='tight')
    plt.show()


def plot_distribution_analysis(btc_data):
    """
    Create distribution plots for Bitcoin returns
    """
    returns = btc_data['Daily_Return'].dropna()
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Histogram
    axes[0,0].hist(returns, bins=50, density=True, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0,0].set_title('Distribution of Bitcoin Daily Returns')
    axes[0,0].set_xlabel('Daily Return')
    axes[0,0].set_ylabel('Density')
    
    # Q-Q plot
    stats.probplot(returns, dist="norm", plot=axes[0,1])
    axes[0,1].set_title('Q-Q Plot (Normal Distribution)')
    
    # Box plot
    axes[1,0].boxplot(returns)
    axes[1,0].set_title('Box Plot of Daily Returns')
    axes[1,0].set_ylabel('Daily Return')
    
    # Time series of returns
    axes[1,1].plot(btc_data.index, returns, alpha=0.7, color='green')
    axes[1,1].set_title('Daily Returns Over Time')
    axes[1,1].set_xlabel('Date')
    axes[1,1].set_ylabel('Daily Return')
    
    plt.tight_layout()
    
    # Ensure results directory exists and save figure
    results_dir = Path(__file__).resolve().parents[2] / 'results'
    results_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(results_dir / 'distribution_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    # Define paths
    project_root = Path(__file__).resolve().parents[2]
    data_path = project_root / 'data' / 'raw' / 'bitcoin_prices.csv'

    # Check if CSV exists
    if not data_path.exists():
        print(f"Error: CSV file not found at {data_path}")
        sys.exit(1)

    # Load Bitcoin data with robust date parsing
    btc_data = pd.read_csv(
        data_path,
        index_col=0,
        parse_dates=True,
        date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d', errors='coerce')
    )

    # Drop rows where index could not be parsed
    btc_data = btc_data[btc_data.index.notna()]

    print("Index type:", btc_data.index.dtype)
    print("First 5 rows:\n", btc_data.head())

    # Create plots
    plot_bitcoin_timeseries(btc_data)
    plot_distribution_analysis(btc_data)

    print("Visualizations created successfully!")
