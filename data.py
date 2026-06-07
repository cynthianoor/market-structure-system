# data.py

import pandas as pd
from config import CONFIG

def load_market_data():
    return pd.read_csv(CONFIG["MARKET_DATA_PATH"])

def load_brokerflow_data():
    return pd.read_csv(CONFIG["BROKERFLOW_PATH"])

def prepare_data():
    market = load_market_data()
    flow = load_brokerflow_data()

    # minimal cleaning only
    market = market.dropna()
    flow = flow.dropna()

    return market, flow