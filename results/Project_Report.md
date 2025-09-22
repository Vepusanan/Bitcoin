## Bitcoin Volatility Analysis – Detailed Report

### 1. Introduction – Background, motivation, objectives
Bitcoin (BTC) exhibits exceptional volatility relative to traditional assets. Such variability affects trading strategies, risk management, and valuation. This project studies BTC volatility and event-driven return dynamics using daily data and a curated list of impactful market events.

Motivation:
- Inform portfolio risk controls with realistic return/volatility behavior.
- Compare volatility estimators that use different intraday information content.
- Assess short-horizon return behavior around major news.

Objectives:
- Build a reproducible analysis pipeline (data, notebooks, modules).
- Characterize BTC returns and volatility (descriptive and distributional properties).
- Compare realized volatility to range-based estimators (Parkinson, Garman–Klass).
- Quantify average returns around events and test volatility changes.

### 2. Literature Review – Summary of related works
1) Baur & Dimpfl (2018): Cryptocurrencies display asymmetric and elevated volatility, supporting non-Gaussian modeling approaches.
2) Katsiampa (2017): GARCH-family models fit BTC well; volatility persistence is high, motivating robust estimators.
3) Parkinson (1980) and Garman–Klass (1980): Range-based variance estimators can be more efficient than close-to-close volatility by leveraging intraday high–low (and open–close) information.
4) Corbet et al. (2019): Event sensitivity and regime behavior are salient in crypto markets; narrative context matters.

These works justify our focus on range-based volatility, distribution tests, and event-window analysis.

### 3. Methodology – Data source, sampling, statistical tests used
Data sources:
- Prices: BTC-USD from Yahoo Finance via `yfinance` or pre-saved `data/raw/bitcoin_prices.csv`. The CSV uses a 3-line header layout; loaders in `01_data_exploration.ipynb` parse and standardize columns.
- Events: `data/processed/market_events.csv` with 62 dated events (2020–2021), each annotated by severity and direction.

Sampling and features:
- Frequency: daily close-to-close returns `ret_t = (Close_t / Close_{t-1}) − 1`.
- Derived metrics: `Daily_Return`, `Abs_Return = |Daily_Return|`, rolling 30d volatility.

Statistical procedures:
- Descriptive stats: mean, std, min/max, quantiles, skewness, kurtosis (`descriptive_stats.py`).
- Normality tests: Shapiro–Wilk, Kolmogorov–Smirnov, D’Agostino; Anderson–Darling in `distribution_analysis.py`.
- Volatility measures (30d window, annualized):
  - Realized volatility: rolling std of returns × √365.
  - Parkinson: based on ln(High/Low) range; efficient under certain assumptions.
  - Garman–Klass: combines range and open–close to further improve efficiency.
- Event analysis: Windowed aggregation of returns around event dates; t-tests on pre/post-event absolute returns to test volatility shifts (`hypothesis_tests.py`).

Reproducibility:
- `setup/requirements.txt`, `setup/setup.py`, `setup/test_setup.py`; notebooks `01–04` and `src/*` modules.

### 4. Results – Tables, plots, descriptive and inferential outcomes
Descriptive statistics (high level):
- Returns are heavy-tailed (positive skewness, excess kurtosis). Dispersion is high, typical of BTC.
- Volatility clusters: 30d rolling volatility shows sustained regimes of high/low variance.

Distributional tests:
- Normality is rejected by multiple tests (p < 0.05) for most sample windows, supporting fat-tailed modeling assumptions.

Volatility estimators:
- In turbulent periods, Parkinson and Garman–Klass tend to produce higher and more responsive readings than close-to-close realized volatility, reflecting wider intraday ranges.
- In calmer periods, all measures converge; GK typically remains slightly higher due to its use of open–close and range.

Event-window outcomes:
- Average returns by relative day around events indicate asymmetry: negative events show sharper immediate impacts, while positive events may diffuse over a few days.
- Pre/post t-tests on `Abs_Return` frequently indicate higher volatility post-event for severe events; significance is event-dependent.

Figures and tables (see notebooks/results):
- Price and 30d volatility time series: `01_data_exploration.ipynb`.
- Annualized volatility comparison (std vs Parkinson vs GK): `03_volatility_measures_comparison.ipynb`.
- Average relative-day returns around events: `02_event_impact_analysis.ipynb`.
- Per-event volatility-impact figures saved to `results/` by `hypothesis_tests.py`.

Note: Concrete numeric tables depend on the current dataset version; re-run notebooks to regenerate.

### 5. Discussion – Interpretation of findings
Interpretation:
- BTC’s non-Gaussian returns and volatility clustering challenge simple normal-based risk models.
- Range-based estimators provide complementary insight by incorporating intraday variation; they are particularly informative during shocks.
- Events materially affect return dispersion; incorporating an event calendar can enhance timing and risk controls.

Implications:
- Risk systems should use multiple volatility measures and monitor regime shifts.
- Strategy evaluation should stress-test around historical event windows.

Limitations and sensitivity:
- Daily data miss intraday microstructure (gaps, jumps). Results may vary across sample windows.
- Event list is curated; classification and severity scoring introduce subjectivity.

### 6. Conclusion – Summary, implications, and limitations
We built a reproducible pipeline to analyze BTC volatility and event impacts. Results confirm heavy tails, regime-dependent volatility, and meaningful event-driven effects. Range-based measures (Parkinson, GK) add value to realized volatility, especially during turbulent phases. Future work: intraday analysis, formal regime-switching or GARCH-family models, and expanded event taxonomies.

### 7. References – APA
Baur, D. G., & Dimpfl, T. (2018). Asymmetric volatility in cryptocurrencies. Economics Letters, 173, 148–151.

Corbet, S., Lucey, B., Urquhart, A., & Yarovaya, L. (2019). Cryptocurrencies as a financial asset: A systematic analysis. International Review of Financial Analysis, 62, 182–199.

Garman, M. B., & Klass, M. J. (1980). On the estimation of security price volatilities from historical data. Journal of Business, 53(1), 67–78.

Katsiampa, P. (2017). Volatility estimation for Bitcoin: A comparison of GARCH models. Economics Letters, 158, 3–6.

Parkinson, M. (1980). The extreme value method for estimating the variance of the stock price. Journal of Business, 53(1), 61–65.

### 8. Appendix (if necessary)
Reproduction steps:
- Create environment and install dependencies: `python setup/setup.py` (or `pip install -r setup/requirements.txt`).
- Execute notebooks in order: 01 → 02 → 03 → 04.
- Figures are written to `results/` when running `hypothesis_tests.py` or the notebooks.


