# Market Structure Analysis System (EOD-Based)

A Python framework for decomposing financial markets into structured 
feature layers using end-of-day data. The system applies a confluence 
scoring model to produce interpretable market state classifications for 
research and analysis purposes.

---

## Current Status

**Observation Mode** — Due to the MSCI rebalancing effective June 1, 2026, 
the system is currently in observation mode. Full forward validation 
begins after June 23, 2026.

---

## Related Articles

This project is documented in a multi-part article series on Medium.

- **Part 1:** [Why IHSG Looks Random Until You Structure 
It](https://medium.com/@cynthianoor/part-1-why-ihsg-looks-random-until-you-structure-it-a-python-based-eod-market-signal-system-867e72f6cdba) 
— Architecture and Philosophy
- **Part 2:** [Building the Confluence 
Engine](https://medium.com/@cynthianoor/part-2-building-the-confluence-engine-implementation-architecture-and-data-design) 
— Implementation and Data Design *(forthcoming)*

---

## System Architecture

The system decomposes market behavior into three independent layers:

| Layer | Description |
| :--- | :--- |
| **Technical features** | Momentum, trend, volatility, reversal patterns 
|
| **Broker flow features** | Institutional participation, accumulation, 
distribution |
| **Macro and regime features** | Market context, policy factors, MSCI 
status |

These layers are combined into a weighted confluence score.

---

## Disclaimer

This project is intended for:

- research exploration
- data analysis
- education
- system design practice

It is **not** a trading system. It does **not** provide financial advice, 
buy/sell recommendations, or automated trading execution.

---

## Forward Validation

Empirical results will be published after the MSCI rebalancing period 
concludes (post-June 23, 2026). See Part 4 of the article series.

---

## Author

Cynthia Maulina Noor

Engineering + MBA candidate. Exploring EOD data systems for structured 
market analysis using Python.

---

## License

MIT

---

*The system is designed for structured market observation and research, 
not trading execution.*
