from collectors import BinanceCollector
import json


def main():
    config = json.load("./config.json")
    binance_key = config["binance_key"]  
    binance_secret = config["binance_secret"]
    collector = BinanceCollector(binance_key, binance_secret)
    df = collector.get_dataframe("BTCUSDC","3d")
    df.to_csv("binance_test.csv")
    
if __name__ == "__main__":
    main()