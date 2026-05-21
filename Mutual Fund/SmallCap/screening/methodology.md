# Screening Methodology — Small Cap Funds

**Context:** ₹20,000/month SIP, 10+ year horizon. Parallel study to FlexiCap research. Same 2-stage screening pipeline but with small-cap-specific adjustments.

**Universe:** 36 Small Cap Funds (Direct, Growth plan) — data from Tickertape, May 21, 2026.

---

## Why Small Cap Screening Differs from FlexiCap

### 1. AUM Has a Hard Upper Limit Here

In FlexiCap, AUM mattered for mid-cap agility but large-AUM funds (HDFC ₹91K Cr) were not eliminated — just penalised in Module 4. For small cap, AUM creates a structural impossibility above a certain threshold:

- SEBI mandates 65%+ in small-cap stocks (251st company onwards)
- Small-cap stocks are illiquid — a ₹1,000 Cr fund can buy/sell quickly; a ₹70,000 Cr fund cannot
- At ₹70,000 Cr (Nippon), putting 65% into small caps = ₹45,500 Cr in illiquid positions
- A typical small-cap stock has ₹500–5,000 Cr market cap; SEBI limits MF stake to <10% of shares
- **Consequence:** Large-AUM funds gravitate toward the 250th–350th ranked companies (largest "small caps") and avoid true 400th–800th ranked companies (genuine small caps). They begin to behave like mid-cap funds masquerading as small cap.
- **Threshold chosen: ₹30,000 Cr** — funds above this are eliminated in Stage 1, not just penalised. This eliminates Nippon (₹72,673 Cr), SBI (₹37,141 Cr), HDFC (₹33,724 Cr), Quant (₹30,374 Cr).

### 2. The ER Ceiling is Tighter

Small cap funds are inherently high-cost businesses (more analyst research, more trading, smaller ticket sizes). But paying more than 1.0% in direct plan ER is unjustifiable:
- The small cap category already has structural higher volatility (16% vs 14% for FlexiCap)
- High ER compounds the risk asymmetry — when a small cap fund falls 40-50%, you're also paying 1%+ of your depleted corpus annually
- **Threshold: ER > 1.0% eliminated.** FlexiCap used 1.5%; this is tightened to 1.0% for small cap given the higher base risk.

### 3. Fund Age is Especially Critical Here

The 2018 small-cap crash (IL&FS crisis + NBFC liquidity freeze, Jul 2018 – Mar 2019) caused the Nifty SmallCap 250 to fall ~45% and not recover for 3 years. Any small cap fund launched after mid-2018 has **no verified track record through this event**, which is the single most important stress test for this category.

- **Threshold: < 60 months (5 years) eliminated** — same as FlexiCap, but the reasoning is stronger for small cap
- Even for funds that pass (launched 2018-2019), the 2018 crash test is analysed in detail in Module 1 and Module 2
- Bandhan Small Cap (launched ~Jan 2020) is a notable survivor with an age caveat: its 5Y CAGR measures from May 2021 onward, missing the 2018 crash and the COVID bottom entirely

### 4. Sharpe Ratio as a Quality Signal

A negative Sharpe ratio means the fund's return did not exceed the risk-free rate over the measurement period. For a small cap fund — which carries 2x the risk of a large-cap fund — generating sub-risk-free returns is disqualifying:
- **Threshold: Sharpe < 0 eliminated** — same as FlexiCap
- This eliminates several large, well-known funds (Kotak, Franklin, ICICI Pru, Tata) that have underperformed recently despite their brand

---

## Stage 1 — Hard Filters (Applied in Order)

| Filter | Threshold | Rationale | Small Cap vs FlexiCap |
|--------|-----------|-----------|----------------------|
| Expense Ratio | ER ≤ 1.0% (Direct) | High ER compounds drawdown pain; small cap already high risk | Tighter (FlexiCap: 1.5%) |
| AUM minimum | AUM ≥ ₹500 Cr | Below this, operational risk and redemption pressure become material | Same as FlexiCap |
| AUM maximum | AUM ≤ ₹30,000 Cr | Above this, genuine small-cap execution is structurally impaired | **New — not in FlexiCap** |
| Fund age | ≥ 60 months (5 years) | Minimum track record; small-cap 2018 crash is the key stress test | Same as FlexiCap |
| Sharpe Ratio | Sharpe ≥ 0 | Generating returns above risk-free rate over recent period | Same as FlexiCap |

---

## Stage 2 — Performance Filters

Both conditions must be met:

| Filter | Threshold | Rationale |
|--------|-----------|-----------|
| 5Y CAGR | > category median (all 36 funds' non-zero 5Y CAGR values) | Fund must outperform median peer over the most relevant SIP horizon |
| Returns vs sub-category (3Y) | > 1.0x | Fund must beat the sub-category average over 3 years — consistent peer outperformance |

**Category median 5Y CAGR:** 19.15% (computed across 22 funds with non-zero 5Y data as of May 21, 2026)

---

## Key Screening Decisions

### Why use the full-category median (all 36 funds) rather than the Stage-1 survivor median?
Using the full 36-fund median anchors the threshold to the actual distribution of the universe, not to a self-selected group. If Stage 1 disproportionately eliminates underperformers, the survivor-median would be inflated, making the 5Y filter less discriminating.

### Why not filter on 3Y CAGR > median?
3Y CAGR reflects the post-COVID bull market (2021-2024) more than skill. 5Y CAGR covers two distinct regimes: the 2021-2022 bull run AND the 2022-2023 correction AND the 2023-2025 recovery. It is more cycle-aware.

### Why not filter on max drawdown?
Max drawdown varies substantially by fund age. A fund launched in 2020 (Bandhan) has a max DD of 24% — not because it protects better, but because it missed the 2018 crash. Using max DD as a screening filter would reward inception bias. Instead, max DD is studied deeply in Module 2 with full context.

### Why no AUM soft filter at Stage 2?
AUM impact (sweet spot, forced deployment, turnover) is a continuous variable that needs detailed modelling in Module 4. A binary Stage 2 cutoff would lose too much information. Bandhan at ₹25,346 Cr is flagged as "approaching the constraint zone" and studied in Module 4 — not eliminated.

---

## What the Filters Cannot Catch

The 2-stage filter produces a quantitative shortlist. The following risks require deep study (Modules 5 & 6) that no screener can surface:

1. **Manager tenure misalignment** — a fund's 5Y returns may have been built by a departed manager. The current manager may have only 6-12 months on the fund.
2. **AMC governance flags** — SEBI investigations, front-running allegations, related-party conflicts. Not in Tickertape data.
3. **Inception bias** — a fund launched just before a major bull market will have inflated CAGR. Module 1 must decompose calendar-year returns and adjust for launch timing.
4. **Portfolio quality within small cap** — SEBI defines small cap as 251st+ company. But there is a vast quality difference between a ₹4,000 Cr company (safe, liquid) and a ₹200 Cr company (illiquid, governance risk). The screener sees "65% small cap" — Module 3 must look at the actual quality of those positions.
5. **Redemption pressure during stress** — small cap funds can face forced selling during crashes if investors panic-redeem. AUM size, exit load structure, and cash holding all matter for this.

---

*Methodology version: 1.0 | Created: May 2026 | Data date: May 21, 2026 | Universe: 36 Small Cap Funds (Direct Growth)*
