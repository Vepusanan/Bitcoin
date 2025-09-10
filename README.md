# Bitcoin Volatility Analysis

A comprehensive analysis of Bitcoin price volatility and its relationship with major market events from 2020-2024.

## Project Overview

This project analyzes Bitcoin's price volatility patterns and investigates the impact of significant market events on Bitcoin's price movements. The analysis includes:

- **Data Collection**: Bitcoin price data from Yahoo Finance and curated market events
- **Descriptive Statistics**: Comprehensive statistical analysis of Bitcoin returns and volatility
- **Distribution Analysis**: Testing for normality and fitting alternative distributions
- **Event Impact Analysis**: Statistical testing of how market events affect Bitcoin volatility
- **Visualization**: Time series plots, distribution plots, and event impact charts

## Project Structure

```
Bitcoin/
├── data/
│   ├── raw/                    # Raw Bitcoin price data
│   └── processed/              # Processed market events data
├── src/
│   ├── data_collection/        # Data collection modules
│   │   ├── bitcoin_prices.py   # Bitcoin price data collection
│   │   └── market_events.py    # Market events database
│   ├── analysis/               # Analysis modules
│   │   ├── descriptive_stats.py    # Descriptive statistics
│   │   ├── distribution_analysis.py # Distribution testing
│   │   └── hypothesis_tests.py     # Event impact analysis
│   └── visualization/          # Visualization modules
│       └── plots.py            # Plotting functions
├── results/                    # Analysis results and plots
├── main.py                     # Main execution script
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Installation

1. **Clone or download the project**
   ```bash
   cd /path/to/Bitcoin
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Quick Start

Run the complete analysis pipeline:

```bash
python main.py
```

This will:
1. Collect Bitcoin price data (2020-2024)
2. Create market events database
3. Perform descriptive statistics analysis
4. Test distribution assumptions
5. Analyze event impacts on volatility
6. Generate visualizations
7. Create summary report

### Individual Modules

You can also run individual analysis modules:

```bash
# Data collection
python src/data_collection/bitcoin_prices.py
python src/data_collection/market_events.py

# Analysis
python src/analysis/descriptive_stats.py
python src/analysis/distribution_analysis.py
python src/analysis/hypothesis_tests.py

# Visualization
python src/visualization/plots.py
```

## Dependencies

- **pandas** (≥1.5.0): Data manipulation and analysis
- **numpy** (≥1.21.0): Numerical computing
- **yfinance** (≥0.2.0): Yahoo Finance data collection
- **scipy** (≥1.9.0): Statistical functions
- **matplotlib** (≥3.5.0): Plotting and visualization

## Data Sources

- **Bitcoin Prices**: Yahoo Finance (BTC-USD)
- **Market Events**: Curated database of 62 major Bitcoin market events (2020-2024)

## Analysis Methods

### Descriptive Statistics
- Mean, standard deviation, skewness, kurtosis
- Quantile analysis
- Volatility measures (30-day rolling standard deviation)

### Distribution Analysis
- Normality tests (Shapiro-Wilk, Kolmogorov-Smirnov, Anderson-Darling)
- Alternative distribution fitting (t-distribution, skew-normal, Laplace, generalized extreme value)

### Event Impact Analysis
- Paired t-tests comparing pre/post event volatility
- Correlation analysis between event severity and volatility changes
- Statistical significance testing

## Results

The analysis generates several output files in the `results/` directory:

- `descriptive_stats.txt`: Detailed statistical summary
- `analysis_summary.txt`: Executive summary of findings
- `bitcoin_timeseries.png`: Price and volatility time series
- `distribution_analysis.png`: Return distribution plots
- `event_*_impact.png`: Individual event impact charts

## Key Findings

The analysis reveals several important patterns in Bitcoin volatility:

1. **Non-normal Distribution**: Bitcoin returns exhibit significant skewness and excess kurtosis
2. **Event Sensitivity**: Major market events significantly impact Bitcoin volatility
3. **Volatility Clustering**: High volatility periods tend to cluster together
4. **Severity Correlation**: Event severity correlates with volatility changes

## Technical Notes

- **Data Period**: January 2020 - December 2024
- **Frequency**: Daily data
- **Missing Data**: Handled by forward-filling and dropping incomplete records
- **Statistical Tests**: 5% significance level used throughout

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed and virtual environment is activated
2. **Data Loading**: The script will automatically download fresh data if needed
3. **Path Issues**: All scripts use relative paths from the project root
4. **Memory Issues**: For large datasets, consider reducing the date range

### Getting Help

If you encounter issues:
1. Check that all dependencies are installed correctly
2. Ensure you're running from the project root directory
3. Verify that the virtual environment is activated
4. Check the console output for specific error messages

## License

This project is for educational and research purposes. Please cite appropriately if used in academic work.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests for improvements.

---

**Note**: This analysis is for educational purposes only and should not be considered as financial advice.
