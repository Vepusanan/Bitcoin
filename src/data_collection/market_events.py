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
        {'date': '2020-05-11', 'event': 'Bitcoin Halving', 'type': 'technical', 'severity': 5},
        {'date': '2020-10-08', 'event': 'Square buys $50M Bitcoin', 'type': 'institutional', 'severity': 3},
        {'date': '2020-12-10', 'event': 'Grayscale Bitcoin Trust premium spikes', 'type': 'institutional', 'severity': 2},
        
        # 2021 Events
        {'date': '2021-02-08', 'event': 'Tesla buys $1.5B Bitcoin', 'type': 'institutional', 'severity': 5},
        {'date': '2021-04-14', 'event': 'Coinbase IPO', 'type': 'market', 'severity': 4},
        {'date': '2021-05-12', 'event': 'Elon Musk suspends Tesla Bitcoin payments', 'type': 'regulatory', 'severity': 4},
        {'date': '2021-09-07', 'event': 'El Salvador adopts Bitcoin as legal tender', 'type': 'regulatory', 'severity': 4},
        {'date': '2021-09-24', 'event': 'China bans cryptocurrency transactions', 'type': 'regulatory', 'severity': 5},
        
        # 2022 Events
        {'date': '2022-01-27', 'event': 'Russia considers accepting Bitcoin payments', 'type': 'regulatory', 'severity': 3},
        {'date': '2022-05-12', 'event': 'Terra Luna collapse affects crypto market', 'type': 'market', 'severity': 5},
        {'date': '2022-11-11', 'event': 'FTX exchange collapse', 'type': 'market', 'severity': 5},
        
        # 2023 Events
        {'date': '2023-01-03', 'event': 'SEC approves Bitcoin spot ETF applications for review', 'type': 'regulatory', 'severity': 3},
        {'date': '2023-03-10', 'event': 'Silicon Valley Bank collapse affects crypto', 'type': 'macroeconomic', 'severity': 4},
        {'date': '2023-06-15', 'event': 'BlackRock files for Bitcoin ETF', 'type': 'institutional', 'severity': 4},
        
        # 2024 Events
        {'date': '2024-01-10', 'event': 'SEC approves Bitcoin spot ETFs', 'type': 'regulatory', 'severity': 5},
        {'date': '2024-04-19', 'event': 'Bitcoin Halving', 'type': 'technical', 'severity': 5},
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