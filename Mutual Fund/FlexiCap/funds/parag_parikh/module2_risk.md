# Module 2: Risk Profile — Parag Parikh Flexi Cap Fund

## Raw Data (Source: Tickertape, May 10 2026)

| Metric | Parag Parikh | Category Avg | Assessment |
|--------|-------------|-------------|------------|
| Volatility | **9.06%** | 14.14% | Lowest in entire FlexiCap universe |
| Max Drawdown | 31.20% | ~36% avg | Better than most peers |
| Sharpe Ratio | 0.089 | — | Low — due to weak 1Y returns |
| Sortino Ratio | 0.0098 | — | Low — same reason |
| Tracking Error | 7.14% | — | High — very active bets vs benchmark |
| Beta vs Nifty 500 | 0.55 | — | Very defensive |
| Downside Capture | 59% | ~94% (peers) | Falls only 59% as much as benchmark |

---

## Volatility vs Shortlisted Peers

```mermaid
xychart-beta
    title "Volatility — Parag Parikh vs Shortlisted Peers (%)"
    x-axis ["PP", "HDFC", "AB SL", "Union", "Edelweiss", "BOI", "JM", "HSBC", "Quant"]
    y-axis "Volatility %" 0 --> 18
    bar [9.06, 12.36, 13.34, 13.93, 13.85, 14.52, 14.49, 15.44, 16.00]
```
> PP = Parag Parikh | BOI = Bank of India | AB SL = Aditya Birla SL

Parag Parikh has the **lowest volatility among all shortlisted funds** — by a wide margin (9.06% vs next best 12.36%).

---

## Max Drawdown vs Shortlisted Peers

```mermaid
xychart-beta
    title "Max Drawdown — Lower is Better (%)"
    x-axis ["BOI", "PP", "JM", "Union", "Edelweiss", "AB SL", "HSBC", "HDFC", "Quant"]
    y-axis "Max Drawdown %" 0 --> 45
    bar [23.73, 31.20, 34.95, 35.36, 36.10, 38.59, 39.79, 41.84, 41.28]
```
> Sorted lowest to highest drawdown | PP = Parag Parikh | BOI = Bank of India

- **Best:** Bank of India (23.73%) — least worst fall
- **Parag Parikh:** 31.20% — 2nd best among shortlisted funds
- **Worst:** HDFC (41.84%) and Quant (41.28%) — nearly halved at worst point

A 31.20% drawdown means: if you had invested ₹1,00,000 at the peak, it would have dropped to ₹68,800 before recovering. For SIP, this is manageable — you're buying more units during the dip.

---

## Sharpe Ratio vs Shortlisted Peers

```mermaid
xychart-beta
    title "Sharpe Ratio — Higher is Better"
    x-axis ["PP", "HDFC", "JM", "Union", "Edelweiss", "AB SL", "HSBC", "Quant", "BOI"]
    y-axis "Sharpe Ratio" 0 --> 1.3
    bar [0.089, 0.130, 0.151, 0.284, 0.502, 0.551, 0.619, 0.656, 1.159]
```
> Sorted lowest to highest | PP = Parag Parikh | BOI = Bank of India

Parag Parikh has the **lowest Sharpe ratio** among peers — but this is largely a consequence of its weak 1Y return (4.21%). Sharpe is calculated over the short-term period. The long-term risk-adjusted return picture is different from what this snapshot shows.

---

## Volatility Decomposed — Why Is PP So Low?

Three structural reasons why Parag Parikh has unusually low volatility:

```mermaid
pie title "What Keeps Volatility Low"
    "Domestic Largecap equity (stable)" : 62.86
    "International equity (low India-correlation)" : 11.81
    "A-rated bonds (non-equity buffer)" : 9.92
    "Cash (zero volatility)" : 4.25
    "Mid + Small equity (higher vol)" : 6.15
    "Other" : 5.01
```

1. **Only 6.15% in mid+small** — these are the volatile segments
2. **9.92% in A-rated bonds** — bonds reduce overall portfolio swings
3. **11.81% in international stocks** — US tech stocks have low correlation with Indian market cycles

---

## Tracking Error — What It Means

Parag Parikh's tracking error is **7.14%** — among the highest in the category.

```mermaid
xychart-beta
    title "Tracking Error vs Shortlisted Peers (%)"
    x-axis ["AB SL", "Edelweiss", "Union", "HDFC", "JM", "HSBC", "Quant", "BOI", "PP"]
    y-axis "Tracking Error %" 0 --> 8
    bar [2.37, 2.19, 2.39, 3.92, 5.80, 3.46, 6.48, 7.38, 7.14]
```

High tracking error = fund bets far from its benchmark (Nifty 500 TRI). For Parag Parikh, this comes from:
- Holding international stocks (not in Nifty 500)
- Holding A-rated bonds (not in an equity benchmark)
- Very low mid/small allocation vs what the benchmark contains

This is a feature, not a bug — but it means in years when the benchmark does well, the fund can significantly lag.

---

## Risk vs Return — Positioning Among Peers

```mermaid
quadrantChart
    title Risk vs 5Y Return (shortlisted funds)
    x-axis "Lower Risk (Volatility)" --> "Higher Risk"
    y-axis "Lower Return (5Y CAGR)" --> "Higher Return"
    quadrant-1 High Risk, High Return
    quadrant-2 Low Risk, High Return
    quadrant-3 Low Risk, Low Return
    quadrant-4 High Risk, Low Return
    Parag Parikh: [0.08, 0.45]
    HDFC: [0.37, 0.85]
    Quant: [0.93, 0.75]
    JM: [0.68, 0.73]
    Edelweiss: [0.55, 0.53]
    HSBC: [0.80, 0.51]
    Bank of India: [0.69, 0.97]
    AB SL: [0.47, 0.22]
    Union: [0.51, 0.01]
```
> Ideal quadrant: Top-left (Low Risk, High Return). Parag Parikh sits in low-risk, mid-return territory.

---

## Module 2 Scorecard

| Sub-dimension | Score (1–5) | Reasoning |
|---------------|------------|-----------|
| Volatility | 5 | Lowest in category — exceptional for SIP investor comfort |
| Max Drawdown | 4 | 31.20% — 2nd best among shortlisted; bad but not worst |
| Sharpe Ratio | 2 | 0.089 — lowest among peers; inflated by 1Y weakness |
| Sortino Ratio | 2 | 0.0098 — same issue as Sharpe |
| Tracking Error | 3 | High (7.14%) but explainable by international + bond holdings |
| Downside Protection | 5 | Beta 0.55, downside capture 59% — best in class |
| **Module 2 Overall** | **4 / 5** | Best-in-class downside protection; Sharpe/Sortino temporarily depressed |
