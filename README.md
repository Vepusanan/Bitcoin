## Bitcoin Volatility Analysis (Statify)

Analyze Bitcoin price behavior, volatility regimes, and the impact of key market events. This repo includes data collection utilities, exploratory and analytical notebooks, and plotting utilities to reproduce the results.

### Contents
- `src/`: Python modules for data collection, analysis, and visualization
  - `data_collection/bitcoin_prices.py`: Download and process BTC price data
  - `data_collection/market_events.py`: Curated event database and helpers
  - `analysis/`: Descriptive stats, distribution analysis, hypothesis tests
  - `visualization/plots.py`: Reusable plotting helpers
- `data/`: Data directory
  - `raw/`: Raw inputs (e.g., `bitcoin_prices.csv`)
  - `processed/`: Processed/derived datasets (e.g., `market_events.csv`)
- `notebooks/`: Jupyter notebooks for the main analysis
  - `01_data_exploration.ipynb`: Robust loading + EDA + basic visuals
  - `02_event_impact_analysis.ipynb`: Event windows and return impact
  - `03_volatility_measures_comparison.ipynb`: Rolling volatility measures (std, Parkinson, Garman–Klass)
  - `04_key_insights_summary.ipynb`: Synthesis of findings
- `results/`: Saved figures/outputs
- `setup/`: Setup and test utilities
  - `setup.py`: Project bootstrap (creates folders, installs requirements)
  - `requirements.txt`: Python dependencies
  - `test_setup.py`: Quick verification of environment and structure
- `main.py`: Example orchestrator/entry-point for scripted runs

---

### Quickstart
1) Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # on macOS/Linux
# .\.venv\Scripts\activate  # on Windows PowerShell
```

2) Install dependencies:
```bash
python setup/setup.py
# or
pip install -r setup/requirements.txt
```

3) Verify the setup (imports, structure, basic data collection):
```bash
python setup/test_setup.py
```

4) Run the analysis notebooks in `notebooks/` in the order listed above.

---

### Data
- Bitcoin prices: pulled via `yfinance` or loaded from `data/raw/bitcoin_prices.csv`.
- Market events: `data/processed/market_events.csv` (curated set); also reproducible via `src/data_collection/market_events.py`.

Notes on CSV format:
- The provided `bitcoin_prices.csv` uses a 3-line header pattern: first line contains field names, second line tickers, third line a `Date` marker. The notebooks contain loaders that handle this format using `skiprows=3` and custom column names `['Date'] + headers_from_line1`.

---

### How to Run
- From notebooks (recommended for exploration): open each notebook and Run All.
- From script: use `main.py` as an example orchestrator. You can adapt it to your workflow.

Common commands:
```bash
# create data folders and install packages
python setup/setup.py

# verify environment and structure
python setup/test_setup.py
```

---

### Notebooks Overview
- `01_data_exploration.ipynb`
  - Robust data loading for the 3-line header CSV
  - Summary statistics, null checks
  - Close price and 30d volatility visualizations
  - Events preview

- `02_event_impact_analysis.ipynb`
  - Computes daily returns
  - Builds event windows (pre/post days) and aggregates relative-day returns
  - Plots average return around events

- `03_volatility_measures_comparison.ipynb`
  - Computes 30d annualized volatility using:
    - Standard deviation of returns
    - Parkinson estimator
    - Garman–Klass estimator
  - Plots the measures side-by-side

- `04_key_insights_summary.ipynb`
  - Summarizes findings and links/embeds visuals from `results/`

---

### Testing
Run the setup test to validate your environment:
```bash
python setup/test_setup.py
```
What it checks:
- Package imports (pandas, numpy, yfinance, scipy, matplotlib)
- Repo structure and key files (resolved from repo root)
- Data collection: event dataset creation and a small BTC price fetch

---

### Troubleshooting
- Requirements install fails
  - Ensure you are using the project’s virtual environment
  - Use: `pip install -r setup/requirements.txt`
- Notebooks can’t find data files
  - Confirm presence of `data/raw/bitcoin_prices.csv` and `data/processed/market_events.csv`
  - Re-create folders with `python setup/setup.py`
- CSV header parsing errors
  - The notebooks assume a 3-line header format; if your CSV differs, adjust the loader cell accordingly

---

### Environment
- Python 3.10+ recommended (project tested on Python 3.13 in a venv)
- OS: macOS/Linux/Windows

---

### License
This project is for academic/research purposes. If you intend to reuse or distribute, add an explicit license file and update this section accordingly.

