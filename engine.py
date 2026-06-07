# engine.py

def compute_confluence(features):
    results = []

    tech = features["technical"]
    flow = features["flow"]
    macro = features["macro"]

    # simple weighted scoring model
    for key in tech.keys():
        score = (
            tech[key] * 0.4 +
            flow.get("net_flow", 0) * 0.3 +
            macro.get("market_volatility", 0) * 0.3
        )

        results.append({
            "asset": key,
            "score": float(score),
            "state": classify(score)
        })

    return results


def classify(score):
    if score > 0.7:
        return "bullish_bias"
    elif score < 0.3:
        return "bearish_pressure"
    else:
        return "neutral"