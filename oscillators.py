import numpy as np


class Oscillators:

    def __init__(self, dataframe):
        self.df = dataframe

    def set_df(self, dataframe):
        self.df = dataframe

    def add_stochastic(self):
        df = self.df
        df.sort_values("Date",ascending=True)
        high_14 = df["High"].rolling(14).max()
        low_14 = df["Low"].rolling(14).min()
        print(((df["Close"] - low_14)/(high_14 - low_14)))
        df['OS_%K'] = ((df["Close"] - low_14)/(high_14 - low_14))*100
        df['OS_%D'] = df['OS_%K'].rolling(3).mean()
        return df[['OS_%K', 'OS_%D']]

    def get_indicators(self, ma_type):
        pass
