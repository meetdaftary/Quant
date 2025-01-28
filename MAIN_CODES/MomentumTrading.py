import pandas as pd
import numpy as np

class Momentum:

    def __init__(self):

        return

    def backtest_trade(self, stock, x, y, z):

        data4 = stock[[x, y]]
        percentage_change = data4.pct_change(periods=z) * 100
        percentage_change.columns = [f"{col}_pct_change" for col in data4.columns]
        data4 = pd.concat([data4, percentage_change], axis=1)
        data4 = data4.iloc[z:].reset_index(drop=True)

        initial_capital = 100000
        capital = initial_capital
        money = initial_capital
        allocated_asset = None
        data4['Capital'] = 0.0

        for i in range(len(data4)):
            if i == 0:
                if data4.loc[i, f'{x}_pct_change'] >= data4.loc[i, f'{y}_pct_change']:
                    no_of_stk = (money // data4.loc[i, x])
                    money = money - no_of_stk * data4.loc[i, x]
                    allocated_asset = x
                else:
                    no_of_stk = (money // data4.loc[i, y])
                    money = money - no_of_stk * data4.loc[i, y]
                    allocated_asset = y
            else:
                if data4.loc[i, f'{x}_pct_change'] >= data4.loc[i, f'{y}_pct_change']:
                    new_asset = x
                else:
                    new_asset = y

                if new_asset != allocated_asset:
                    money = money + no_of_stk * data4.loc[i, allocated_asset]
                    allocated_asset = new_asset
                    no_of_stk = (money // data4.loc[i, allocated_asset])
                    money = money - no_of_stk * data4.loc[i, allocated_asset]

            data4.loc[i, 'Capital'] = money + no_of_stk * data4.loc[i, allocated_asset]

        portfolio_values = data4['Capital'].tolist()
        return portfolio_values