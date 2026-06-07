# features.py

import numpy as np

# ---------------------------
# 1. TECHNICAL FEATURES (merged)
# ---------------------------
def compute_technical_features(market_df):
    """
    Combines:
    - RSI
    - MACD-like momentum
    - Moving average deviation
    - Mean reversion signals
    """

    features = {}

    features["momentum_score"] = market_df["close"].pct_change().rolling(5).mean()
    features["volatility_score"] = market_df["close"].rolling(10).std()
    features["trend_score"] = market_df["close"].rolling(20).mean()

    return features


# ---------------------------
# 2. FLOW FEATURES (broker + whale merged)
# ---------------------------
def compute_flow_features(flow_df):
    """
    Combines:
    - broker accumulation
    - broker distribution
    - whale detection
    """

    features = {}

    features["net_flow"] = flow_df["buy_value"] - flow_df["sell_value"]
    features["flow_imbalance"] = flow_df["buy_value"] / (flow_df["sell_value"] + 1)

    return features


# ---------------------------
# 3. MACRO / REGIME FEATURES (simplified)
# ---------------------------
def compute_macro_features(market_df):
    """
    Simplified regime proxy:
    - volatility regime
    - market trend direction
    """

    features = {}

    features["market_trend"] = market_df["close"].rolling(30).mean()
    features["market_volatility"] = market_df["close"].rolling(30).std()

    return features


# ---------------------------
# MAIN WRAPPER
# ---------------------------
def compute_features(market_df, flow_df):
    return {
        "technical": compute_technical_features(market_df),
        "flow": compute_flow_features(flow_df),
        "macro": compute_macro_features(market_df)
    }