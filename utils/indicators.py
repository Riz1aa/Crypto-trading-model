import pandas as pd

def calculate_cvd(df):
    df["delta"] = df["volume"] * (df["close"] - df["open"]).apply(lambda x: 1 if x > 0 else -1)
    df["cvd"] = df["delta"].cumsum()
    return df

def cvd_trend(df, lookback):
    return df["cvd"].diff(lookback)

def oi_change_pct(df, lookback):
    return (df["open_interest"] - df["open_interest"].shift(lookback)) / df["open_interest"].shift(lookback)

def price_stagnation(df, lookback, threshold=0.001):
    high = df["high"].rolling(lookback).max()
    low = df["low"].rolling(lookback).min()
    mid = (high + low) / 2
    return abs(df["close"] - mid) / mid < threshold
