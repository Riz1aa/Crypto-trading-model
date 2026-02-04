import ccxt
import pandas as pd

def load_btc_1m(limit=1000):
    exchange = ccxt.binance()
    ohlcv = exchange.fetch_ohlcv("BTC/USDT", timeframe="1m", limit=limit)
    df = pd.DataFrame(ohlcv, columns=["timestamp","open","high","low","close","volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df
