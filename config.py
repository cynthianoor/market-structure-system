# config.py

CONFIG = {
    "MARKET_DATA_PATH": "data/market_data.csv",
    "BROKERFLOW_PATH": "data/brokerflow.csv",
    "OUTPUT_DIR": "outputs/",
    
    # Thresholds (kept minimal, no trading framing)
    "TECHNICAL_WEIGHT": 1.0,
    "FLOW_WEIGHT": 1.0,
    "MACRO_WEIGHT": 1.0,

    "CONFLUENCE_THRESHOLD": 50,
}