import pandas as pd

def detect_fvg(data):
    """
    Detects Fair Value Gaps (FVG) in price data.
    A bullish FVG occurs when:
    candle1 high < candle3 low
    A bearish FVG occurs when:
    candle1 low > candle3 high
    """

    signals = []

    for i in range(2, len(data)):
        c1 = data.iloc[i-2]
        c2 = data.iloc[i-1]
        c3 = data.iloc[i]

        # Bullish FVG
        if c1['high'] < c3['low']:
            signals.append({
                "type": "BUY",
                "entry": c3['low'],
                "index": i
            })

        # Bearish FVG
        elif c1['low'] > c3['high']:
            signals.append({
                "type": "SELL",
                "entry": c3['high'],
                "index": i
            })

    return signals