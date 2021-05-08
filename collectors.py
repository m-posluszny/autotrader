from binance.client import Client
from abc import ABC, abstractmethod
import pandas as pd
import datetime
import yfinance as yahoo

class Collector(ABC):
    
    def __init__(self):
        self.start_date = datetime.datetime.strptime('1 Jan 2016', '%d %b %Y')
        self.end_date = datetime.datetime.today()
        self.client = None
    
    @abstractmethod
    def get_dataframe(symbol):
        ...

        
class BinanceCollector(Collector):
    
    def __init__(self, api_key, api_secret):
        super().__init__()
        
        self.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'CloseTime', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ]
        
        self.client = Client(api_key=api_key, api_secret=api_secret)
        self.api_key = api_key
        self.api_secret = api_secret
        
    def get_dataframe(self, symbol, interval,start_date = None, end_date = None):
        start_date = start_date or self.start_date
        end_date = end_date or self.end_date

        klines = self.client.get_historical_klines(symbol, interval, self.start_date.strftime("%d %b %Y %H:%M:%S"), self.end_date.strftime("%d %b %Y %H:%M:%S"), 1000)
        data = pd.DataFrame(klines, columns = self.columns)
        data['Date'] = pd.to_datetime(data['Date'], unit='ms')
        return data
    
class YahooCollector(Collector):
    
    def __init__(self):
        super().__init__()        
        
    def get_dataframe(self, symbol, interval,start_date = None, end_date = None):
        start_date = start_date or self.start_date
        end_date = end_date or self.end_date
        
        self.client = yahoo.Ticker(symbol)
        data = self.client.history(start = start_date, end = end_date, interval=interval)
        return data