from numpy.lib.function_base import append
import pandas as pd
import numpy as np
import math
from pandas.core import api

class MovingAverage:
    
    def __init__(self, dataframe):
        self.df = dataframe
    
    def set_df(self, dataframe):
        self.df = dataframe
    
    def add_sma(self, period):
        self.df[f"SMA{period}"] = self.df["Close"].rolling(window = period, min_periods = 1).mean()
        return self.df[f"SMA{period}"]

    def add_ema(self, period):
        self.df[f"EMA{period}"] = self.df["Close"].ewm(span = period, adjust = False).mean()
        return  self.df[f"EMA{period}"]
    
    def add_wma(self, period):
        weights = lambda x: [(2*y)/(len(x)*(len(x)+1)) for y in range(len(x), 0, -1)]
        self.df[f"WMA{period}"] = (self.df['Close']
            .rolling(window=period,min_periods=1)
            .apply(lambda x: np.sum(x*weights(x)), raw=False))

    def get_indicators(self, ma_type):
        ma = {}
        name = ""
        for col in self.df:
            if ma_type in col:
                val = int(col[3:])
                name = col[:3]
                ma[val] = self.df[col]
        if len(ma) < 2:
            return False
        vals = list(ma.keys())
        vals.sort()
        signals = []
        scale = math.floor(math.log10(self.df["Close"].mean()))
        scale = pow(10,scale-0.5)
        for i in range(len(list(ma.values())[0])-1,-1,-1):
            signal = []
            for j in range(0,len(vals)-1):
                val_a = ma[vals[j]][i]
                val_b = ma[vals[j+1]][i]
                w =(j+1) * scale
                if val_a < val_b:
                    signal.append(1*w)
                elif val_a > val_b:
                    signal.append(-1*w)
                else:
                    signal.append(0)
            signals.append(sum(signal))
        self.df[f"IND_{name}"] = signals
        