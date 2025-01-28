import pandas as pd
import numpy as np

class BacktestMetrics:

    def __init__(self):
        return

    def calculate_cagr(self, start_value, end_value, years):
        return (((end_value / start_value) ** (1 / years) - 1) * 100)

    def calculate_sharpe_ratio(self, returns):
        mean_return = np.mean(returns)
        std_return = np.std(returns)
        sharpe_ratio = (mean_return) / std_return
        return (sharpe_ratio)