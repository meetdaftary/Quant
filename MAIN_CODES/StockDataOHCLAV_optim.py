import pandas as pd
import yfinance as yf

class StockDataFetcher:
    def __init__(self, symbols, start_date, end_date):

        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date

    # def fetch_data(self):

    #     data = pd.DataFrame()
    #     for symbol in self.symbols:
    #         print(f"Fetching data for {symbol}...")  # Debug statement
    #         stock_data = yf.download(symbol, start=self.start_date, end=self.end_date)
    #         data[f"{symbol}_Open"] = stock_data['Open']
    #         data[f"{symbol}_High"] = stock_data['High']
    #         data[f"{symbol}_Low"] = stock_data['Low']  
    #         data[f"{symbol}_Close"] = stock_data['Close']         
    #         data[f"{symbol}_Adj Close"] = stock_data['Adj Close']
    #         data[f"{symbol}_Volume"] = stock_data['Volume']
    #     return data

    def fetch_data(self):
        all_data = []  # Collect individual DataFrames for each symbol
        for symbol in self.symbols:
            print(f"Fetching data for {symbol}...")  # Debug statement
            stock_data = yf.download(symbol, start=self.start_date, end=self.end_date)
            stock_data = stock_data[['Open', 'High','Low', 'Close', 'Adj Close', 'Volume']]  # Select necessary columns
            stock_data.columns = [f"{symbol}_{col}" for col in stock_data.columns]  # Rename columns
            all_data.append(stock_data)

        # Concatenate all individual DataFrames along the columns (axis=1)
        combined_data = pd.concat(all_data, axis=1)
        return combined_data
