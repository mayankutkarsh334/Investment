# Phase 6 Plan: Confirm or Rule Out with More Fund Houses

> **Status:** Done Nov-13-2026 — results in [phase6_results.md](phase6_results.md): H1 inconclusive (edge replicated, fails G4), H2 rejected.
> **Why:** Phase 5 was borderline:
> - **B (biggest bets)** beat luck on stock picking (98.7th percentile) but tied the small-cap SIP on money and leaned on one stock (TVS Motor);
> - **C (your small-new-bets idea)** looked best *without* stop-losses (15.6% XIRR, +0.9 points a year over the small-cap SIP) but only reached the 90th percentile.
>
> The study plan says a borderline result must be tested on more fund houses before it's believed.

---

## 1. The key design idea: a replication on independent fund houses

Simply adding fund houses to the same six and re-running would mostly re-measure the same thing. And the Phase 5 rules were partly chosen after seeing Phase 5 results. So Phase 6 runs **two separate datasets**:

| Dataset | Fund houses | Role |
|---|---|---|
| **NEW** | Only the newly added houses (ICICI, Axis, UTI + any others that pass the audit) | **Replication.** Their buying decisions were never used to design anything. If the effect is real, it should appear here too |
| **ALL** | The 6 pilot houses + the new ones | **Strength.** More votes, closer to "the industry" |

A hypothesis is **confirmed only if it passes on both**.

---

## 2. Pre-registered hypotheses (fixed now, before any Phase 6 data is seen)

Only these two are tests. Anything else run in Phase 6 is labelled a **diagnostic** and can't confirm anything.

### H1: B (biggest bets) with your original rules
- **Buy:** each month, the eligible stock that some **diversified** fund (sector/thematic excluded, same list as Phase 3) holds furthest above the average weight across all funds **in that dataset**. Qualifies at ≥ 3 percentage points above the average.
- **Exits (unchanged):** −10% stop ladder (+15% → +5% … then 10-point steps), funds-selling flag, 24-month cap.
- **Unchanged:** ₹2,000 → ₹5,000 a month, price ≤ that amount, ≥ ₹1 crore daily turnover, skip stocks flagged "funds selling", up to 3 buys per stock, idle money in the small-cap fund.

### H2: C (small new bets) without price stop-losses
- **Buy:** each month, the eligible stock where the most fund houses opened a **new position below 2% weight** (ties broken by rupees bought). Unchanged from Phase 3.
- **Exits:**
  - **no price stop**;
  - sell when the funds-selling flag fires (2+ houses cut or exit, or total fund holdings −20%);
  - otherwise sell at **24 months**.
- **Everything else as H1.**

### Pass rule (same four gates; G1's bar raised for two tests)

| Gate | Test |
|---|---|
| **G1** | Average return per buy beats **≥ 97.5%** of 1,000 random portfolios, run with the *same* exit rule, same months, same liquidity band. The bar is 97.5% (not 95%) because two hypotheses are tested |
| **G2** | Above the random median in both halves (2014–19, 2020–26) |
| **G3** | Above the random median without its 10 best buys |
| **G4** | Post-tax XIRR beats SIPs into the Nifty 500, the flagship funds and the small-cap fund |
| **G5 (new)** | Still passes G1 at 95% **after removing its most-bought stock**, to catch a TVS-Motor-style single-stock result |

**Confirmed** = passes G1–G5 on **both NEW and ALL**.
**Rejected** = fails G1 on NEW.
**Still inconclusive** = anything in between.

---

## 3. Data to add

| Fund house | Archive (from Phase 0 audit) | Download method | Status |
|---|---|---|---|
| **ICICI Prudential** | Jan-2013 → today (FY12-13: Jan–Mar only) | Site download API (needs a browser session); Phase 0 found the call | Must have |
| **Axis** | 2012 → today (Nov-2012 confirmed) | Year/month picker on the statutory-disclosures page; find the underlying request | Must have |
| **UTI** | 2014 → today (month not checked) | Form-based picker; find the underlying request | Must have |
| Tata, Canara Robeco, Motilal Oswal, Bandhan (ex-IDFC), Sundaram, Invesco, HSBC (ex-L&T), quant, Edelweiss | **Not yet checked** | AMFI's portfolio-disclosure page links each house's archive | Add any with **monthly ISIN files from ≤ 2014** |
| Kotak, Mirae, Franklin | Only recent months online | — | Excluded (as Phase 0) |

**Window:** each dataset starts at the month from which **at least 3 of its houses** have files (NEW probably ~2014). Its signals start the month after.

---

## 4. Steps

| # | Step | Output | Rough effort |
|---|---|---|---|
| **6.0** | **Audit** the 9 unchecked fund houses: archive start, ISINs present, format. Fix the NEW set | `phase6_audit.md` | Short |
| **6.1** | **Downloaders** for ICICI, Axis, UTI (browser session → API calls) and any extra houses | `links_<amc>.csv`, files in `data/raw/files/` | Biggest step: each site differs |
| **6.2** | **Parse, classify, validate** with the Phase 1 pipeline. New layouts may need parser tweaks. Same checks: coverage, launches vs renames, double-counting, size realism, spot checks | holdings tables with the new houses | Medium |
| **6.3** | **Signals** for both datasets (`--houses NEW` / `--houses ALL`); B's average weight and the selling flag computed within each dataset | `signals_NEW.parquet`, `signals_ALL.parquet` | Small (code exists) |
| **6.4** | **Run H1 and H2** on both datasets against 1,000 random portfolios each, and apply G1–G5 | `phase6_results.md` | Small (engine exists) |
| **6.5** | **Diagnostics only** (can't confirm anything): A/D on the new data, other exit rules, liquid-fund parking | appendix | Optional |

---

## 5. What each outcome would mean for you

| Outcome | Meaning | Sensible next step |
|---|---|---|
| H1 or H2 **confirmed** | The effect repeats on fund houses never used to design it | **Phase 7: paper-trade it live for 6–12 months** (run each month after the 10th, record picks, no money). Only then consider small real amounts |
| **Inconclusive** | Some signal, not enough to rely on | Paper-trade at most; don't put money in |
| Both **rejected** | Copying fund buying adds nothing for a small monthly investor | Stop. A plain SIP in a good small-cap or flexi-cap fund did as well with no effort |

---

## 6. Limits Phase 6 can't fix

1. **Same 2014–2026 market.** New fund houses are independent decision-makers, but the same rising market. A bull-market bias toward "no stop-loss" (H2) remains. Only live paper trading after 2026 tests a new period.
2. **Fund houses copy each other.** Big houses often own the same stocks, so NEW isn't fully independent of the pilot six. It's still the best replication available.
3. **The tested rules are fixed here.** If they fail, Phase 6 doesn't go looking for new rules on the same data. That would repeat the over-fitting risk.

---

*This is a historical test, not investment advice.*
