📊 Market Structure Analysis System (EOD-Based)
Overview

This project is a simplified market structure analysis framework built on end-of-day (EOD) financial data.

It decomposes market behavior into three interpretable layers:

Technical features
Institutional flow features
Macro/regime features

These layers are then combined into a single confluence scoring model to produce structured market state interpretations.

⚠️ Disclaimer

This project is intended for:

research exploration
data analysis education
system design practice

It is not a trading tool and does not provide financial advice, buy/sell recommendations, or automated trading execution.

🧠 System Philosophy

Financial markets often appear noisy when analyzed through isolated indicators.

This system assumes:

Market behavior becomes more interpretable when decomposed into structured feature layers.

Instead of predicting price direction directly, the system focuses on:

feature aggregation
structural interpretation
relative scoring of conditions
🏗️ System Architecture

The system is intentionally minimal and modular:

market_structure_system/

├── main.py        → pipeline execution
├── config.py      → system configuration
├── data.py        → data loading and preprocessing
├── features.py    → feature engineering layer
├── engine.py      → confluence scoring model
🔧 Feature Layers
1. Technical Features

Captures short-to-medium term market behavior.

Includes simplified representations of:

momentum
volatility
trend structure
2. Flow Features

Represents institutional activity signals derived from:

net buying/selling pressure
imbalance in flow activity
3. Macro / Regime Features

Captures broader market environment characteristics:

trend context
volatility regime approximation
⚙️ Confluence Engine

All feature layers are combined into a unified scoring model:

Each feature group contributes to a weighted score
The final score is mapped into a market state:
Score Range	State
> 0.7	bullish_bias
0.3 – 0.7	neutral
< 0.3	bearish_pressure
📤 Output Format

The system produces structured outputs such as:

BBCA:
  score: 0.82
  state: bullish_bias
  drivers: technical + flow + macro

AMMN:
  score: 0.34
  state: bearish_pressure
  drivers: flow + volatility
🎯 Design Goals

This system was designed with three priorities:

Simplicity over complexity
Interpretability over prediction
Modularity over monolithic design
🧪 Intended Use Cases
Market structure research
Feature engineering experimentation
System design for financial data
Educational demonstration of multi-layer analysis
📌 Limitations
Uses simplified feature representations
Does not model order book or real-time execution
Not optimized for trading performance
EOD-only data structure
🚀 Future Extensions (Optional)

Potential extensions include:

higher-resolution intraday data integration
machine learning-based scoring models
regime clustering models
visualization dashboard layer
👤 Author Context (Optional)

This project is part of a broader exploration into:

data-driven market structure analysis
operations + analytics systems design
financial system decomposition using Python
