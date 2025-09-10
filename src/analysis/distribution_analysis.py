# File: src/analysis/distribution_analysis.py

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def test_normality_comprehensive(bitcoin_returns):
    """
    Test if Bitcoin returns follow normal distribution
    Your proposal says: "Tests for determining normalcy"
    """
    
    results = {}
    
    # 1. Shapiro-Wilk Test
    shapiro_stat, shapiro_p = stats.shapiro(bitcoin_returns)
    results['shapiro_wilk'] = {
        'test_statistic': shapiro_stat,
        'p_value': shapiro_p,
        'is_normal': shapiro_p > 0.05,
        'interpretation': 'Normal' if shapiro_p > 0.05 else 'Not Normal'
    }
    
    # 2. Kolmogorov-Smirnov Test
    ks_stat, ks_p = stats.kstest(bitcoin_returns, 'norm')
    results['kolmogorov_smirnov'] = {
        'test_statistic': ks_stat,
        'p_value': ks_p,
        'is_normal': ks_p > 0.05
    }
    
    # 3. Anderson-Darling Test
    ad_result = stats.anderson(bitcoin_returns, dist='norm')
    results['anderson_darling'] = {
        'test_statistic': ad_result.statistic,
        'critical_values': ad_result.critical_values,
        'significance_levels': ad_result.significance_level
    }
    
    return results

def fit_alternative_distributions(bitcoin_returns):
    """
    Your proposal says: "Alternate distributions fitted to Bitcoin return data"
    """
    
    distributions = ['t', 'skewnorm', 'laplace', 'genextreme']
    results = {}
    
    for dist_name in distributions:
        dist = getattr(stats, dist_name)
        
        # Fit the distribution
        params = dist.fit(bitcoin_returns)
        
        # Calculate AIC and BIC for model comparison
        log_likelihood = np.sum(dist.logpdf(bitcoin_returns, *params))
        k = len(params)  # number of parameters
        n = len(bitcoin_returns)  # sample size
        
        aic = 2 * k - 2 * log_likelihood
        bic = k * np.log(n) - 2 * log_likelihood
        
        results[dist_name] = {
            'parameters': params,
            'log_likelihood': log_likelihood,
            'aic': aic,
            'bic': bic
        }
    
    return results