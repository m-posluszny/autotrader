import pandas as pd

class MovingAverage:
    
    def __init__(self) -> None:
        pass
    
    def get_ma(self, dataframe, period):
        dates = dataframe["Date"]
        prices = dataframe["Close"]
        ma_dates = []
        ma_prices = []
        ma_dataframe = pd.DataFrame()
        ma_sum = 0
        period_counter = 0
        for date, price in zip(dates,prices):
            ma_sum+=price
            if period_counter == int(period/2):
                ma_dates.append(date)
            if period_counter == period-1:
                ma_prices.append(ma_sum/period)
                ma_sum = 0
                period_counter = 0
            else:
                period_counter +=1
        ma_dataframe["Date"] = ma_dates
        ma_dataframe["Close"] = ma_prices
        return ma_dataframe