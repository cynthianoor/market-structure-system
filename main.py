# main.py

from data import prepare_data
from features import compute_features
from engine import compute_confluence

def run():
    market, flow = prepare_data()

    features = compute_features(market, flow)
    results = compute_confluence(features)

    for r in results:
        print(r)


if __name__ == "__main__":
    run()