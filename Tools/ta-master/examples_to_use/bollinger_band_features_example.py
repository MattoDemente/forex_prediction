"""This is a example adding bollinger band features.
"""
import pandas as pd
from ta import *

# Load data
df = pd.read_csv('../data/datas.csv', sep=',')

# Clean nan values
df = utils.dropna(df)

print(df.columns)

# Add bollinger band high indicator filling nans values
df['bb_high_indicator'] = bollinger_hband_indicator(df["Close"], n=20, ndev=2,
                                                        fillna=True)

# Add bollinger band low indicator filling nans values
df['bb_low_indicator'] = bollinger_lband_indicator(df["Close"], n=20, ndev=2,
                                                        fillna=True)

print(df.columns)
