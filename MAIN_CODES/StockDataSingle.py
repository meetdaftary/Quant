# import pandas as pd
# import yfinance as yf

# class StockDataFetcher:
#     def __init__(self, symbols, start_date, end_date):
#         """
#         Initialize the StockDataFetcher class.

#         Parameters:
#         symbols (list): List of stock symbols to fetch.
#         start_date (str): Start date for fetching stock data in YYYY-MM-DD format.
#         end_date (str): End date for fetching stock data in YYYY-MM-DD format.
#         """
#         self.symbols = symbols
#         self.start_date = start_date
#         self.end_date = end_date

#     def fetch_data(self):
#         """
#         Fetch adjusted close stock data for the given symbols and date range.

#         Returns:
#         pd.DataFrame: DataFrame containing adjusted close prices for each symbol.
#         """
#         data = pd.DataFrame()
#         for symbol in self.symbols:
#             print(f"Fetching data for {symbol}...")  # Debug statement
#             stock_data = yf.download(symbol, start=self.start_date, end=self.end_date)
#             data[symbol] = stock_data['Close']
#         return data



import pandas as pd
import yfinance as yf

class StockDataImporter:
    
    def __init__(self, symbol, start_date, end_date):

        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date

    def fetch_data(self):

        data = pd.DataFrame()
        print(f"Fetching data for {self.symbol}...")  # Debug statement
        stock_data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        return stock_data