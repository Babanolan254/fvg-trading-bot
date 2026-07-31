import pandas as pd
from strategy.fvg_logic import detect_fvg

# Load sample data
data = pd.read_csv("data/sample_data.csv")

# Run FVG detection
signals = detect_fvg(data)

# Print results
for signal in signals:
    print(f"{signal['type']} at {signal['entry']} (index {signal['index']})")