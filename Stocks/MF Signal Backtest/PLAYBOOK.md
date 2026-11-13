# Strategy Lab Playbook: Testing Any Investment Idea on 2013–2026 Data

> **Purpose:** a reusable, honest way to simulate an investment idea on Indian market history and decide whether it's worth real money.
> **Built in:** the MF-signal study (Phases 0–6, Nov-2026). **Findings so far:** [FINDINGS.md](FINDINGS.md).

---

## 1. The workflow (every idea, every time)

```
 1. Write an IDEA CARD   ->  2. Code the ranking rule   ->  3. Run vs 1,000 random portfolios
        (before data)          (no look-ahead)              (same months, size band, exits)
                                                                      |
 6. Paper-trade live  <-  5. Replicate on unseen data  <-  4. Apply the gates (G1–G5)
    (if it survives)         (if it passes)                  record result, don't tweak
```

**Rules that keep it honest:**
1. **The idea card comes first.** Rule, exits, money rules and pass/fail are written down before any result is seen.
2. **One run per idea card.** If you change the rule after seeing the result, it's a **new** idea, so log it as one and test it on data it wasn't tuned on.
3. **Count your tries.** For *k* ideas tested together, raise G1's bar (2 → 97.5%, 4 → 98.75%, 10 → 99.5%).
4. **Passing needs replication** on independent data (other fund houses, a held-out period, or live paper trading) before real money.

---

## 2. Idea card template (copy into `ideas/<name>.md`)

```markdown
# Idea: <name>            Date: <yyyy-mm-dd>      Test # in this batch: <k>

## Hypothesis (one sentence)
<e.g. "Stocks with the strongest 12-month return keep beating random stocks over the next months.">

## Buy rule (monthly, on the action date = first trading day >= 11th)
- Universe: affordable (price <= monthly amount), >= Rs 1 cr/day traded, EQ/BE series
- Rank by: <exact formula, using only data before the action date>
- Pick: rank 1 (next if 3 lots already held or unaffordable)

## Exit rule
- Stops: <ladder / ATR k / none>    Time cap: <months>    Funds-selling exit: <on/off>

## Money rules
- Monthly amount: Rs 2,000 (2014) -> Rs 5,000 (2026), +7.94% each Jan   (or: <other>)
- Idle money: small-cap index fund   (or: cash / liquid fund / Nifty 500)

## Pass / fail (fixed now)
- G1 >= <95% / stricter if several ideas> of random portfolios on avg return per buy
- G2 both halves, G3 without top-10 buys, G4 post-tax XIRR beats SIPs (Nifty 500, 6 funds, small-cap),
  G5 without most-bought stock

## Result (filled after the single run)
<numbers, gates, verdict, date>
```

---

## 3. How to run an idea (code)

1. `cp scripts/strategy_template.py scripts/idea_<name>.py`
2. Edit four things at the top:
   - `IDEA`: the name.
   - `RULES = E.Rules(...)`: `use_stops`, `five_point`, `atr_mult`, `cap_months`, `sell_flag`, `initial_stop`.
   - `OPTIONS = R.Options(...)`: `max_lots`, `park` (idle-money fund: `"NIFTY SMALLCAP 250"`, `"NIFTY 500"`, `"NIFTY MIDCAP 150"`, a fund code like `"hdfc"`, or `None` for cash), `reinvest`, `cash_rate`, `taxes`.
   - `build_rankings(pr, uni)`: return `{ym: [issuer, …]}` best first. **Use only data dated before each action date.** `uni` holds every buyable stock per month (`ym, date, issuer, adv20_cr, liq_q`).
3. Run: `.venv/bin/python -I scripts/idea_<name>.py` (1,000 random portfolios ≈ 2 minutes; pass `100` for a quick check).
4. The script prints:
   - average, median, win rate and holding days per buy;
   - the random distribution and percentile;
   - t-stat;
   - both halves;
   - without the top 10 buys;
   - XIRR vs the three SIPs;
   - G1–G4.

   For G5 (without the most-bought stock), see `scripts/run_phase6.py`.

**Example already in the template:** 12-month momentum (price only). Smoke run with 100 random portfolios:
- +5.7% per buy, 98th percentile, but t 0.8;
- **fails G3** (−1.3% without its 10 best buys) → driven by a few winners, not a consistent edge.

**For mutual-fund-based ideas,** start from `scripts/signals.py` (votes per fund house, conviction weights, streaks) and add a new `q_X` / `rank_X` pair. `runner.strategy_chooser("X", pr)` then works directly, as in `run_phase5.py`.

---

## 4. What the lab already provides

### 4.1 Data (in `data/processed/`, rebuilt from scripts; git-ignored)

| File | Contents | Coverage |
|---|---|---|
| `prices_adj.parquet` | Every NSE equity stock, daily: raw OHLC, volume, value; split/bonus/demerger-adjusted OHLC; dividends; total-return index; `gap_days` | Nov-2013 → Nov-2026, 3,706 companies (incl. delisted) |
| `prices_raw.parquet` | Same, unadjusted | same |
| `corp_actions.parquet` | Splits, bonuses, consolidations, demergers, rights at zero premium, dividends (parsed from NSE) | Oct-2013 → Nov-2026 |
| `index_tri.parquet` | Nifty 500 / 50 / Midcap 150 / Smallcap 250 **total-return** indices | Jan-2013 → Nov-2026 |
| `fund_nav.parquet` | Daily NAV of 6 flagship flexi/multi-cap direct plans (HDFC, SBI, Nippon, ABSL, DSP, PPFAS) | 2013 → Nov-2026 |
| `holdings_scheme.parquet` | Every active-equity scheme's monthly holdings: shares, split-adjusted shares, ₹ value, % of NAV | 9 fund houses, 2013 → Oct-2026 |
| `holdings_amc.parquet` | The same rolled up to fund house × company × month | same |
| `fund_actions.parquet` | Each fund house's monthly vote per company: new / increase / cut / exit / hold (launch- and flow-adjusted) | same |
| `signals.parquet` (pilot 6 houses), `signals_NEW.parquet` (ICICI/Axis/UTI), `signals_ALL.parquet` (9) | Monthly votes, signal scores A–D, sell flags, action date, reference price, liquidity, eligibility, ranks | Dec-2013 / May-2014 → Oct-2026 |

**Keys:**
- `issuer` = first 7 characters of the ISIN; it survives splits and ticker renames.
- `ym` = portfolio month (`YYYY-MM`).
- `action_date` = when you could act on that month's data.

### 4.2 Engine (`scripts/engine.py`, `runner.py`, `evaluate.py`)

| Feature | Detail |
|---|---|
| Fills | Buy at the open of the action date; whole shares; leftover rupees to the parking fund |
| Exits | Stop ladder (−10%, +15%→+5% … 10-point steps; 5-point variant; ATR-based initial stop), time cap, "funds selling" flag, delisting/suspension (last close) |
| Conservative intraday logic | The low is checked against the stop from *earlier* days' highs; a gap below the stop fills at the open |
| Costs | STT, stamp duty, NSE and SEBI fees + GST, ₹15.93 depository fee per sale; brokerage configurable |
| Tax | Today's rules every year: STCG 20%, LTCG 12.5% above ₹1.25 L, 4% cess, loss set-off and carry-forward, per-buy holding period; dividends at 31.2% |
| Idle money | Parked in a chosen fund/index from the day it's free; tax paid by redeeming the oldest units |
| Money rules | Stepped-up monthly amount (`signals.monthly_amount`); up to N buys per stock; optional reinvestment |
| Luck baseline | `runner.random_chooser`: random buyable stock, same month, same liquidity quintile, same rules, ×1,000 |
| Benchmarks | `runner.sip_benchmark`: same monthly amounts into any index/fund series, taxed at exit |
| Verified by | 19 hand-built tests (`scripts/test_engine.py`), hand-checked real trades, placebo signal fails |

---

## 5. Refreshing the data (run in this order; each step is resumable)

```bash
cd "Stocks/MF Signal Backtest"
# fund portfolios
.venv/bin/python -I scripts/harvest_links.py            # Nippon, DSP, PPFAS pages (save pages first, see script)
.venv/bin/python -I scripts/hdfc_links.py               # HDFC API (save API JSON first, see script)
.venv/bin/python -I scripts/icici_links.py              # ICICI API
.venv/bin/python -I scripts/download.py <amc> ...       # download files listed in links_<amc>.csv
.venv/bin/python -I scripts/uti_schemewise.py           # UTI from Oct-2023
.venv/bin/python -I scripts/parse_holdings.py           # -> holdings_raw / sheets_raw
.venv/bin/python -I scripts/classify_schemes.py         # active-equity schemes
.venv/bin/python -I scripts/build_holdings.py           # clean tables + checks.csv
# prices
.venv/bin/python -I scripts/download_prices.py [start] [end]
.venv/bin/python -I scripts/corp_actions.py             # needs data/raw/nse/corpact/*.json (NSE API via curl + cookie)
.venv/bin/python -I scripts/build_prices.py
.venv/bin/python -I scripts/adjust_holdings.py
# signals
.venv/bin/python -I scripts/fund_flows.py
.venv/bin/python -I scripts/signals.py PILOT|NEW|ALL
```

**Links that need a browser session:** SBI, ABSL and Axis lists were taken through Chrome (each fund house's portfolio page). See `phase1_holdings.md` and `phase6_results.md` for the exact endpoints.

**After any refresh:** check `data/processed/checks.csv` (missing months, jumps) and re-run `scripts/test_engine.py`.

---

## 6. Checklist before trusting any result

- [ ] Idea card written and dated before the run.
- [ ] The ranking uses only data before the action date.
- [ ] The rule was compared with 1,000 random portfolios under the **same** exits and money rules.
- [ ] G1 bar adjusted for how many ideas were tried.
- [ ] Both halves positive vs random.
- [ ] Survives removing the top 10 buys and the most-bought stock.
- [ ] Post-tax XIRR beats the simple SIPs (otherwise: just buy the fund).
- [ ] Replicated on data not used to design it.
- [ ] Paper-traded live for 6–12 months before real money.
- [ ] Remembered that 2014–2026 was mostly a bull market.

---

## 7. Known limits of the lab

1. **One market period**, 2014–2026, mostly rising.
2. **NSE only**: BSE-only stocks are absent.
3. **No fundamentals** (earnings, P/E, balance sheets) yet. Only prices, volumes, corporate actions and fund holdings.
4. **Tax rules are today's** for all years; surcharge ignored.
5. **The small-cap fund is an index proxy** (Nifty Smallcap 250 TRI − 0.3%).
6. **Dividends** are credited at exit; demergers are treated as value-neutral.
