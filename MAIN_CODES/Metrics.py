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

    def sortino_ratio(self, returns, risk_free_rate=0.06822):  
        avg_return = np.mean(returns) - (risk_free_rate / 252)    
        downside_returns = returns[returns < risk_free_rate / 252]
        downside_deviation = np.std(downside_returns, ddof=1) if len(downside_returns) > 0 else 0
        annualized_return = avg_return * 252
        annualized_downside_deviation = downside_deviation * np.sqrt(252)
        sortino_ratio = annualized_return / annualized_downside_deviation if annualized_downside_deviation > 0 else np.nan
        return sortino_ratio

    def calmar_ratio(self, returns):
        annualized_return = np.mean(returns) * 252  
        cumulative_returns = np.cumprod(1 + returns)
        peak = np.maximum.accumulate(cumulative_returns)
        drawdowns = (cumulative_returns - peak) / peak
        max_drawdown = np.min(drawdowns)  
        calmar_ratio = annualized_return / abs(max_drawdown) if max_drawdown < 0 else np.nan  
        return calmar_ratio



