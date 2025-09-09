import pandas as pd
import numpy as np
from datetime import datetime
import os

def create_events_database():
    """
    Create a database of major Bitcoin market events (2020-2024)
    """
    
    # Major Bitcoin events with dates, types, and severity scores (1-5)
    events_data = [
        # 2020 Events
        {'date': '2020-03-12', 'event': 'Bitcoin crashes 50% in COVID Black Thursday', 'severity': 5, 'price_impact': 'negative'},
        {'date': '2020-07-26', 'event': 'Bitcoin breaks above $10K resistance', 'severity': 3, 'price_impact': 'positive'},
        {'date': '2020-10-21', 'event': 'Bitcoin rally begins on institutional demand', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2020-11-30', 'event': 'Bitcoin breaks $19K approaching ATH', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2020-12-17', 'event': 'Bitcoin breaks $20K all-time high', 'severity': 5, 'price_impact': 'positive'},
        {'date': '2020-12-30', 'event': 'Bitcoin ends year up 300%', 'severity': 4, 'price_impact': 'positive'},
        
        {'date': '2021-01-08', 'event': 'Bitcoin breaks $40K milestone', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2021-01-11', 'event': 'Bitcoin correction from $42K to $30K', 'severity': 3, 'price_impact': 'negative'},
        {'date': '2021-02-09', 'event': 'Bitcoin surges to $48K on Tesla news', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2021-02-20', 'event': 'Bitcoin breaks $50K for first time', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2021-03-13', 'event': 'Bitcoin reaches $60K milestone', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2021-04-14', 'event': 'Bitcoin peaks at $64.8K before Coinbase IPO', 'severity': 5, 'price_impact': 'positive'},
        {'date': '2021-04-18', 'event': 'Bitcoin drops 15% amid leveraged liquidations', 'severity': 4, 'price_impact': 'negative'},
        {'date': '2021-05-19', 'event': 'Bitcoin crashes 30% to $30K on China ban', 'severity': 5, 'price_impact': 'negative'},
        {'date': '2021-07-21', 'event': 'Bitcoin bounces above $30K support', 'severity': 3, 'price_impact': 'positive'},
        {'date': '2021-07-26', 'event': 'Bitcoin Amazon rumor spike to $40K', 'severity': 3, 'price_impact': 'positive'},
        {'date': '2021-09-07', 'event': 'Bitcoin dips below $43K on El Salvador launch day', 'severity': 3, 'price_impact': 'negative'},
        {'date': '2021-09-21', 'event': 'Bitcoin falls to $40K on Evergrande fears', 'severity': 3, 'price_impact': 'negative'},
        {'date': '2021-10-01', 'event': 'Bitcoin Q4 rally begins, breaks $48K', 'severity': 3, 'price_impact': 'positive'},
        {'date': '2021-10-20', 'event': 'Bitcoin surges past $65K on ETF hopes', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2021-11-10', 'event': 'Bitcoin reaches new ATH at $69K', 'severity': 5, 'price_impact': 'positive'},
        {'date': '2021-12-04', 'event': 'Bitcoin crashes from $59K to $42K', 'severity': 4, 'price_impact': 'negative'},
        
        # 2022 Market Events
        {'date': '2022-01-24', 'event': 'Bitcoin falls below $33K amid market sell-off', 'severity': 4, 'price_impact': 'negative'},
        {'date': '2022-03-28', 'event': 'Bitcoin recovers to $47K in March rally', 'severity': 3, 'price_impact': 'positive'},
        {'date': '2022-04-05', 'event': 'Bitcoin rejected at $47K resistance', 'severity': 2, 'price_impact': 'negative'},
        {'date': '2022-05-09', 'event': 'Bitcoin crashes below $30K as LUNA collapses', 'severity': 5, 'price_impact': 'negative'},
        {'date': '2022-06-13', 'event': 'Bitcoin breaks below $25K support', 'severity': 4, 'price_impact': 'negative'},
        {'date': '2022-06-18', 'event': 'Bitcoin hits cycle low at $17.6K', 'severity': 5, 'price_impact': 'negative'},
        {'date': '2022-07-21', 'event': 'Bitcoin bounces to $24K in dead cat bounce', 'severity': 2, 'price_impact': 'positive'},
        {'date': '2022-08-15', 'event': 'Bitcoin rallies to $25K on inflation data', 'severity': 3, 'price_impact': 'positive'},
        {'date': '2022-11-09', 'event': 'Bitcoin crashes to $15.5K on FTX collapse', 'severity': 5, 'price_impact': 'negative'},
        {'date': '2022-11-21', 'event': 'Bitcoin finds support around $15.5K', 'severity': 3, 'price_impact': 'positive'},
        
        # 2023 Market Events
        {'date': '2023-01-01', 'event': 'Bitcoin starts year at $16.5K', 'severity': 2, 'price_impact': 'neutral'},
        {'date': '2023-01-14', 'event': 'Bitcoin breaks above $21K resistance', 'severity': 3, 'price_impact': 'positive'},
        {'date': '2023-02-02', 'event': 'Bitcoin surges above $23K on risk-on sentiment', 'severity': 3, 'price_impact': 'positive'},
        {'date': '2023-03-10', 'event': 'Bitcoin spikes to $28K on banking crisis fears', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2023-04-11', 'event': 'Bitcoin breaks above $30K for first time since June', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2023-06-10', 'event': 'Bitcoin drops to $25K on SEC exchange lawsuits', 'severity': 3, 'price_impact': 'negative'},
        {'date': '2023-07-13', 'event': 'Bitcoin rallies to $31K on Ripple court victory', 'severity': 3, 'price_impact': 'positive'},
        {'date': '2023-10-16', 'event': 'Bitcoin surges to $35K on ETF optimism', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2023-10-24', 'event': 'Bitcoin briefly touches $35K then corrects', 'severity': 2, 'price_impact': 'negative'},
        {'date': '2023-12-04', 'event': 'Bitcoin breaks $42K on ETF approval hopes', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2023-12-11', 'event': 'Bitcoin corrects to $40K on profit-taking', 'severity': 2, 'price_impact': 'negative'},
        
        # 2024 Market Events
        {'date': '2024-01-11', 'event': 'Bitcoin spikes to $49K on ETF approval day', 'severity': 5, 'price_impact': 'positive'},
        {'date': '2024-01-24', 'event': 'Bitcoin corrects to $39K after ETF sell-off', 'severity': 3, 'price_impact': 'negative'},
        {'date': '2024-02-12', 'event': 'Bitcoin breaks $50K post-ETF accumulation', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2024-02-28', 'event': 'Bitcoin surges to $57K in February rally', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2024-03-05', 'event': 'Bitcoin breaks 2021 ATH, reaches $69K', 'severity': 5, 'price_impact': 'positive'},
        {'date': '2024-03-14', 'event': 'Bitcoin sets new ATH at $73.8K', 'severity': 5, 'price_impact': 'positive'},
        {'date': '2024-04-02', 'event': 'Bitcoin corrects to $66K pre-halving', 'severity': 3, 'price_impact': 'negative'},
        {'date': '2024-04-13', 'event': 'Bitcoin drops to $60K on Iran-Israel tensions', 'severity': 3, 'price_impact': 'negative'},
        {'date': '2024-05-01', 'event': 'Bitcoin struggles around $57K post-halving', 'severity': 2, 'price_impact': 'negative'},
        {'date': '2024-06-07', 'event': 'Bitcoin falls to $66K range-bound trading', 'severity': 2, 'price_impact': 'negative'},
        {'date': '2024-07-05', 'event': 'Bitcoin drops to $53K on Mt. Gox fears', 'severity': 4, 'price_impact': 'negative'},
        {'date': '2024-08-05', 'event': 'Bitcoin crashes to $49K on yen carry trade unwind', 'severity': 5, 'price_impact': 'negative'},
        {'date': '2024-09-06', 'event': 'Bitcoin falls below $53K on macro weakness', 'severity': 3, 'price_impact': 'negative'},
        {'date': '2024-10-14', 'event': 'Bitcoin breaks above $67K on Trump odds', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2024-10-29', 'event': 'Bitcoin surges to $73K pre-election', 'severity': 4, 'price_impact': 'positive'},
        {'date': '2024-11-06', 'event': 'Bitcoin explodes to $75K on Trump victory', 'severity': 5, 'price_impact': 'positive'},
        {'date': '2024-11-12', 'event': 'Bitcoin reaches new ATH at $89K', 'severity': 5, 'price_impact': 'positive'},
        {'date': '2024-11-22', 'event': 'Bitcoin briefly touches $99K approaching $100K', 'severity': 5, 'price_impact': 'positive'},
        {'date': '2024-12-05', 'event': 'Bitcoin consolidates in $95K-$100K range', 'severity': 3, 'price_impact': 'positive'}
    ]
    
    # Create DataFrame
    events_df = pd.DataFrame(events_data)
    events_df['date'] = pd.to_datetime(events_df['date'])
    
    # Add additional columns for analysis
    events_df['year'] = events_df['date'].dt.year
    events_df['month'] = events_df['date'].dt.month
    events_df['event_id'] = range(1, len(events_df) + 1)
    
    print(f"Events database created with {len(events_df)} events")
    return events_df

def save_events_data(events_df, filename='market_events.csv'):
    """
    Save events data to CSV file
    """
    if not os.path.exists('data/processed'):
        os.makedirs('data/processed')
    
    filepath = f'data/processed/{filename}'
    events_df.to_csv(filepath, index=False)
    print(f"Events data saved to {filepath}")

# Example usage
if __name__ == "__main__":
    events = create_events_database()
    save_events_data(events)
    print(events.head())