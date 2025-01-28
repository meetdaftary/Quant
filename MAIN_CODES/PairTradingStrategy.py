import pandas as pd
import numpy as np

class PairTrading:

    def __init__(self):

        return

    def backtest_trade1(self, S1, S2, money, scale_factor, window1, window2):
        
        cash = money
        countS1 = 0
        countS2 = 0
        
        avail_cap = money
        ratios = S1 / S2
        ma1 = ratios.rolling(window=window1).mean()
        ma2 = ratios.rolling(window=window2).mean()
        std = ratios.rolling(window=window2).std()
        zscore = (ma1 - ma2) / std

        valid_indices = zscore.dropna().index

        portfolio_values = [cash]

        for i in valid_indices:
            # print(zscore[i])
            z = zscore[i]
            ratio = ratios[i]
            trade_amount = avail_cap * scale_factor

            if z < -1:
                if trade_amount>0:
                    stk1=trade_amount // S1[i]
                    stk2=trade_amount // S2[i]
                    countS1 -= stk1
                    countS2 += stk2
                    amt1=stk1*S1[i]
                    amt2=stk2*S2[i]
                    avail_cap = avail_cap - amt1 - amt2
                    cash = cash + amt1 - amt2

            elif z > 1:
                if trade_amount>0:
                    stk1=trade_amount // S1[i]
                    stk2=trade_amount // S2[i]
                    countS1 += (trade_amount / S1[i])
                    countS2 -= (trade_amount / S2[i])
                    amt1=stk1*S1[i]
                    amt2=stk2*S2[i]
                    avail_cap = avail_cap - amt1 - amt2
                    cash = cash - amt1 + amt2

            elif abs(z) < 0.75:
                avail_cap = avail_cap + S1[i] * countS1 + S2[i] * countS2
                cash += S1[i] * countS1 + S2[i] * countS2
                countS1 = 0
                countS2 = 0

            portfolio_value = cash + S1[i] * countS1 + S2[i] * countS2
            portfolio_values.append(portfolio_value)

        # portfolio_values = np.array(portfolio_values)
        # portfolio_returns = np.diff(portfolio_values) / portfolio_values[:-1]

        # final_value = portfolio_values[-1]
        # years = (S1.index[-1] - S1.index[0]).days / 365
        # cagr = calculate_cagr(money, final_value, years)

        # benchmark_returns = benchmark.pct_change().dropna()
        # benchmark_cagr = calculate_cagr(benchmark.iloc[0], benchmark.iloc[-1], years)
        # benchmark_sharpe = calculate_sharpe_ratio(benchmark_returns)

        # sharpe_ratio = calculate_sharpe_ratio(portfolio_returns)

        # print("STRATEGY CAGR: ",cagr*100,"%")
        # print("BENCHMARK CAGR: ",benchmark_cagr*100,"%")
        # print("STRATEGY SHARPE: ",sharpe_ratio)
        # print("BENCHMARK SHARPE: ",benchmark_sharpe)
        # print("FINAL AMT.: ",cash)

        return portfolio_values

