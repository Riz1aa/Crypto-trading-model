def generate_signals(df):
    df["long_signal"] = (
        (df["cvd_trend"] > 0) &
        (df["oi_change"] > 0.002) &
        (df["price_stagnant"])
    )

    df["short_signal"] = (
        (df["cvd_trend"] < 0) &
        (df["oi_change"] > 0.002) &
        (df["price_stagnant"])
    )

    return df
      
