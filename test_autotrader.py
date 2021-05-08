from collectors import BinanceCollector, YahooCollector
from moving_average import MovingAverage
import json
import plotly.graph_objects as go
import datetime

def generate_candlesticks(data,name="generic_plot"):
    
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close']))
    for col in data:
        if "IND" in col:
            fig.add_trace(go.Bar(name=col,x=data["Date"],y=data[col]))
        
        elif "MA" in col:
            fig.add_trace(go.Scatter(name=col,x=data['Date'],
                y=data[col],line_shape='spline'))

    fig.update_layout(barmode='group', bargap=0.00,bargroupgap=0.0)
    fig.write_image(f"{name}.pdf")

def main():
    config = json.load(open("./config.json"))
    binance_key = config["binance_key"]  
    binance_secret = config["binance_secret"]
    collector = BinanceCollector(binance_key, binance_secret)
    df = collector.get_dataframe("BTCUSDC","1d",start_date=datetime.datetime.strptime('1 Mar 2020', '%d %b %Y'))
    ma = MovingAverage(df)
    ma.add_ema(5)
    ma.add_ema(10)
    ma.add_ema(25)
    ma.add_ema(50)
    ma.add_ema(75) 
    ma.add_ema(100)
    ma.get_indicators("EMA")
    generate_candlesticks(df)
    # collector = YahooCollector()
    # df = collector.get_dataframe("TSLA","5d")
    # ma.set_df(df)    
    # generate_candlesticks(df)
    
if __name__ == "__main__":
    main()
