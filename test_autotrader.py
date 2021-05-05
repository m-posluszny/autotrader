from collectors import BinanceCollector, YahooCollector
import json


def main():
    config = json.load(open("./config.json"))
    binance_key = config["binance_key"]  
    binance_secret = config["binance_secret"]
    collector = BinanceCollector(binance_key, binance_secret)
    df = collector.get_dataframe("BTCUSDC","3d")
    df.to_csv("binance_test.csv")
    
    collector = YahooCollector()
    df = collector.get_dataframe("TSLA","5d")
    df.to_csv("yahoo_test.csv")
    
    
if __name__ == "__main__":
    main()