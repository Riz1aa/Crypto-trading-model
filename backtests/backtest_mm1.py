import pandas as pd
from utils.indicators import *
from strategies.mm1_cvd_oi import generate_signals
from utils.data_loader import load_btc_1m

df = load_btc_1m(1000)
df["open_interest"] = 100000 + df.index * 5  # TEMP MOCK

df = calculate_cvd(df)
df["cvd_trend"] = cvd_trend(df, 5)
df["oi_change"] = oi_change_pct(df, 5)
df["price_stagnant"] = price_stagnation(df, 5)

df = generate_signals(df)

capital = 10000
position = None
entry_price = 0

for i in range(len(df)):
    if position is None:
        if df.loc[i, "long_signal"]:
            position = "long"
            entry_price = df.loc[i, "close"]
        elif df.loc[i, "short_signal"]:
            position = "short"
            entry_price = df.loc[i, "close"]

    else:
        price = df.loc[i, "close"]
        pnl = (price - entry_price) / entry_price if position == "long" else (entry_price - price) / entry_price

        if pnl >= 0.003 or pnl <= -0.002:
            capital *= (1 + pnl)
            position = None

print("Final capital:", capital)
