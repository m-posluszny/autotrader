from collectors import BinanceCollector, YahooCollector
from moving_averages import MovingAverage
from oscillators import Oscillators
from plotly.subplots import make_subplots
import json
import plotly.graph_objects as go
import datetime

def generate_candlesticks(data,name="generic_plot"):

    fig_up = go.Figure()
    fig_dwn = go.Figure()
    fig_up.add_trace(go.Candlestick(x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close']))
    no_os = True
    for col in data:
        if "IND" in col and "MA" in col:
            fig_up.add_trace(go.Bar(name=col,x=data["Date"],y=data[col]))
                
        elif "MA" in col:
            fig_up.add_trace(go.Scatter(name=col,x=data['Date'],
                y=data[col],line_shape='spline'))
        
        elif "OS" in col:
            fig_dwn.add_trace(go.Scatter(name=col, x=data['Date'],
                y=data[col], line_shape='spline'))
           

    fig_up.update_layout(barmode='group', bargap=0.00, bargroupgap=0.0)
    fig_up.write_image(f"{name}.pdf")
    fig_dwn.write_image(f"{name}_2.pdf")


def ma_test(df):
    ma = MovingAverage(df)
    ma.add_sma(5)
    ma.add_sma(10)
    ma.add_sma(25)
    ma.add_sma(50)
    ma.add_sma(75)
    ma.add_sma(100)
    # ma.get_indicators("EMA")
    
def oscillator_test(df):
    os = Oscillators(df)
    os.add_stochastic()
    
def main():
    config = json.load(open("./config.json"))
    binance_key = config["binance_key"]  
    binance_secret = config["binance_secret"]
    collector = BinanceCollector(binance_key, binance_secret)
    df = collector.get_dataframe("BTCUSDC","12h",start_date=datetime.datetime.strptime('1 Mar 2021', '%d %b %Y'))
    ma_test(df)
    oscillator_test(df)
    generate_candlesticks(df)
    df.to_csv("binance_test.csv")
    
if __name__ == "__main__":
    main()
