import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def collect_bitcoin_data(start_date='2020-01-01', end_date='2024-12-31'):
    """
    Collect Bitcoin price data from Yahoo Finance
    """
    print("Downloading Bitcoin data...")
    try:
        # Download Bitcoin data
        btc = yf.download('BTC-USD', start=start_date, end=end_date)
        
        # Calculate daily returns
        btc['Daily_Return'] = btc['Close'].pct_change()
        
        # Calculate volatility (30-day rolling standard deviation)
        btc['Volatility_30d'] = btc['Daily_Return'].rolling(window=30).std()
        
        # Calculate absolute returns for volatility analysis
        btc['Abs_Return'] = abs(btc['Daily_Return'])
        
        # Remove NaN values
        btc = btc.dropna()
        
        print(f"Data collected successfully: {len(btc)} records")
        return btc
        
    except Exception as e:
        print(f"Error collecting data: {e}")
        return None

def save_bitcoin_data(data, filename='bitcoin_prices.csv'):
    """
    Save Bitcoin data to CSV file
    """
    if not os.path.exists('data/raw'):
        os.makedirs('data/raw')
    
    filepath = f'data/raw/{filename}'
    data.to_csv(filepath)
    print(f"Data saved to {filepath}")

# Example usage
if __name__ == "__main__":
    btc_data = collect_bitcoin_data()
    if btc_data is not None:
        save_bitcoin_data(btc_data)
        print(btc_data.head())