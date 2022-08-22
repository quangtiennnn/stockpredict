import requests
import pandas as pd

API_KEY = "92TJMSJYSE7VYVKU"
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
class StockData:
    def __init__(self,symbol):
        self.symbol = symbol
        self.df = self.get_stockdata()

    def get_stockdata(self):
        parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.symbol,
            "apikey": API_KEY,
            "datatype": 'json'
        }
        response = requests.get(url=STOCK_API_ENDPOINT, params=parameters)
        data = response.json()
        df_raw = pd.DataFrame.from_dict(data["Time Series (Daily)"]).T
        df = df_raw.rename(columns={
            '1. open': 'open',
            '2. high': 'high',
            '3. low': 'low',
            '4. close': 'close',
            '5. volume': 'volume',
        })
        df.index = pd.to_datetime(df.index)
        df.index.name = 'date'
        for col in df.columns:
            df[col] = pd.to_numeric(df[col])
        return df
