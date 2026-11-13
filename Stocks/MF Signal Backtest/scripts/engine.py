"""Phase 4: backtest engine.

Three layers
  1. simulate_lot()  - one monthly buy from entry to exit, day by day, in split-adjusted prices:
                       stop-loss ladder, 'funds selling' exit, 24-month cap, suspension/delisting.
                       Returns ratios (exit / entry, dividends / entry), so results are reused for any
                       rupee amount and cached.
  2. Book            - the investor's money: stepped-up monthly contributions, whole shares, leftover
                       cash, Indian trading charges in rupees, capital-gains tax per financial year
                       (set-off and carry-forward), dividend tax, final liquidation, XIRR.
  3. run_strategy() / run_random() / sip_benchmark() - who picks what each month.

Conventions (all from study_plan.md; user-confirmed rules marked *)
  * buy at the OPEN of the action date (first trading day on/after the 11th of the next month)
  * stop ladder (on the highest price since entry):  start -10%; +15%->+5%, +20%->+10%, +25%->+15%,
    +30%->+20%, +40%->+30%, then 10-point steps (variant: 5-point steps all the way)
  * stop check uses the day's LOW against the stop set by earlier days' highs; a gap below the stop
    fills at the OPEN; the day's HIGH updates the peak only after the check (conservative)
  * 'funds selling' (sell_default flag of a newer portfolio month) -> sell at that action date's open
  * 24 months after each buy -> sell at the open
  * each monthly buy is its own lot; up to 3 open lots per stock; tax by each lot's own holding period
  - a stock that stops trading is closed at its last close (delisted / suspended > 180 days)
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "data/processed"
END_DATE = pd.Timestamp("2026-11-11")
SIGNALS = P / "signals.parquet"   # set to signals_NEW / signals_ALL before building Prices for Phase 6

# ---------------- charges (delivery, discount broker; 2026 rates) ----------------
STT = 0.001            # 0.1% on buy and on sell
STAMP_BUY = 0.00015    # 0.015% on buy
EXCH = 0.0000297       # NSE transaction charge
SEBI = 0.000001        # Rs 10 per crore
GST = 0.18             # on brokerage + exchange + SEBI charges
DP_SELL = 15.93        # depository charge per stock sold (Rs 13.5 + GST)
BROKERAGE = 0.0        # Rs per order (variant: 20)

# ---------------- tax (today's rules applied to every year) ----------------
CESS = 1.04
STCG_RATE = 0.20 * CESS        # held <= 12 months
LTCG_RATE = 0.125 * CESS       # held > 12 months, above the yearly exemption
LTCG_EXEMPT = 125000.0
DIV_TAX = 0.30 * CESS          # dividends taxed at slab; 30% slab assumed (conservative)


def buy_cost(value: float) -> float:
    return value * (STT + STAMP_BUY + EXCH + SEBI) + (BROKERAGE + value * (EXCH + SEBI)) * GST + BROKERAGE


def sell_cost(value: float) -> float:
    return value * (STT + EXCH + SEBI) + (BROKERAGE + value * (EXCH + SEBI)) * GST + BROKERAGE + DP_SELL


# ---------------- stop ladder ----------------
def stop_gain(peak_gain: np.ndarray, five_point: bool = False) -> np.ndarray:
    """Stop level (as gain over entry) given the highest gain reached so far."""
    pg = np.asarray(peak_gain, dtype=float)
    out = np.full(pg.shape, -0.10)
    if five_point:
        step = np.floor(np.round(pg * 20, 9)) / 20 - 0.10
        return np.where(pg >= 0.15, step, out)
    out = np.where(pg >= 0.15, 0.05, out)
    out = np.where(pg >= 0.20, 0.10, out)
    out = np.where(pg >= 0.25, 0.15, out)
    out = np.where(pg >= 0.30, 0.20, out)
    tens = np.floor(np.round(pg * 10, 9)) / 10 - 0.10
    return np.where(pg >= 0.40, tens, out)


# ---------------- price arrays ----------------
class Prices:
    """Per-issuer numpy arrays of split-adjusted prices, loaded once."""

    def __init__(self):
        px = pd.read_parquet(P / "prices_adj.parquet", columns=[
            "date", "issuer", "open", "adj_open", "adj_high", "adj_low", "adj_close", "adj_div", "gap_days"])
        px = px.sort_values(["issuer", "date"])
        self.a = {}
        for iss, g in px.groupby("issuer", sort=False):
            self.a[iss] = {
                "date": g["date"].values.astype("datetime64[D]"),
                "open_raw": g["open"].values.astype(float),
                "o": g["adj_open"].values.astype(float), "h": g["adj_high"].values.astype(float),
                "l": g["adj_low"].values.astype(float), "c": g["adj_close"].values.astype(float),
                "div": g["adj_div"].values.astype(float), "gap": g["gap_days"].fillna(0).values,
            }
        sig = pd.read_parquet(SIGNALS, columns=["issuer", "action_date", "sell_default", "sell_3h",
                                                               "sell_10pct"])
        self.sell = {}
        for col in ("sell_default", "sell_3h", "sell_10pct"):
            d = sig[sig[col]].groupby("issuer")["action_date"].apply(lambda s: np.sort(s.values.astype("datetime64[D]")))
            self.sell[col] = d.to_dict()

    def idx(self, iss, date):
        d = self.a[iss]["date"]
        i = np.searchsorted(d, np.datetime64(pd.Timestamp(date).date()))
        return i if i < len(d) and d[i] == np.datetime64(pd.Timestamp(date).date()) else None

    def close_on_or_before(self, iss, date):
        a = self.a[iss]
        i = np.searchsorted(a["date"], np.datetime64(pd.Timestamp(date).date()), side="right") - 1
        return (a["c"][i], a["date"][i]) if i >= 0 else (np.nan, None)


@dataclass(frozen=True)
class Rules:
    five_point: bool = False          # 5-point steps above +30%
    sell_flag: str | None = "sell_default"   # None = ignore 'funds selling' exit
    cap_months: int = 24
    initial_stop: float = -0.10
    use_stops: bool = True
    atr_mult: float | None = None     # variant: initial stop = -mult x ATR(14)% (bounded 5%..35%)


@dataclass
class LotResult:
    exit_date: pd.Timestamp
    reason: str          # stop | funds_selling | time_cap | delisted | open
    ret: float           # exit price / entry price (split-adjusted)
    div: float           # dividends received / entry price
    peak: float          # highest gain reached


def simulate_lot(pr: Prices, iss: str, entry_date, rules: Rules = Rules()) -> LotResult | None:
    """Follow one buy (at the open of entry_date) to its exit."""
    a = pr.a.get(iss)
    if a is None:
        return None
    i0 = pr.idx(iss, entry_date)
    if i0 is None or not np.isfinite(a["o"][i0]) or a["o"][i0] <= 0:
        return None
    entry = a["o"][i0]
    d0 = a["date"][i0]
    n = len(a["date"])
    # window ends at the earlier of: last trading day, the day before a >180-day trading gap
    last = n - 1
    gaps = np.nonzero(a["gap"][i0 + 1:] > 180)[0]
    if len(gaps):
        last = i0 + gaps[0]  # last row before the gap
    cap_date = np.datetime64((pd.Timestamp(d0) + pd.DateOffset(months=rules.cap_months)).date())
    i_cap = int(np.searchsorted(a["date"], cap_date))
    end_d = np.datetime64(END_DATE.date())
    i_end = int(np.searchsorted(a["date"], end_d, side="right")) - 1
    hi = min(last, i_end)
    if hi < i0:
        return None
    o, h, l, c = a["o"][i0:hi + 1], a["h"][i0:hi + 1], a["l"][i0:hi + 1], a["c"][i0:hi + 1]
    # earliest-exit candidates (offsets from i0)
    cand = []
    init = rules.initial_stop
    if rules.atr_mult and i0 >= 15:
        hh, ll, cc = a["h"][i0 - 14:i0], a["l"][i0 - 14:i0], a["c"][i0 - 15:i0 - 1]
        tr = np.maximum(hh - ll, np.maximum(np.abs(hh - cc), np.abs(ll - cc)))
        init = -min(0.35, max(0.05, rules.atr_mult * np.nanmean(tr) / entry))
    if rules.use_stops:
        peak_prev = np.maximum.accumulate(np.concatenate([[entry], h[:-1]]))
        peak_prev[0] = entry
        stop_px = entry * (1 + np.where(peak_prev / entry - 1 < 0.15, init,
                                        stop_gain(peak_prev / entry - 1, rules.five_point)))
        hit = np.nonzero(l <= stop_px)[0]
        if len(hit):
            k = int(hit[0])
            fill = o[k] if (k > 0 and o[k] <= stop_px[k]) else stop_px[k]
            cand.append((k, 1, fill, "stop"))
    if rules.sell_flag:
        flags = pr.sell[rules.sell_flag].get(iss)
        if flags is not None:
            nxt = flags[flags > d0]
            if len(nxt):
                j = int(np.searchsorted(a["date"], nxt[0]))
                if j < len(a["date"]) and a["date"][j] == nxt[0] and j <= hi:
                    cand.append((j - i0, 0, o[j - i0], "funds_selling"))
    if i_cap <= hi:
        cand.append((i_cap - i0, 0, o[i_cap - i0], "time_cap"))
    if cand:
        k, _, fill, reason = min(cand, key=lambda t: (t[0], t[1]))
    else:
        k, fill = hi - i0, c[hi - i0]
        reason = "open" if hi == i_end and a["date"][hi] >= end_d - np.timedelta64(7, "D") else "delisted"
    divs = a["div"][i0 + 1:i0 + k + 1].sum()
    peak = (np.max(h[:k + 1]) / entry - 1) if k >= 0 else 0.0
    return LotResult(pd.Timestamp(a["date"][i0 + k]), reason, float(fill / entry), float(divs / entry), float(peak))


# ---------------- the investor's book ----------------
def fy_end(d: pd.Timestamp) -> pd.Timestamp:
    return pd.Timestamp(year=d.year + (1 if d.month > 3 else 0), month=3, day=31)


@dataclass
class Book:
    cash: float = 0.0
    flows: list = field(default_factory=list)          # (date, amount) investor's view: -in, +out
    realized: dict = field(default_factory=dict)       # fy_end -> {"st": x, "lt": y, "div": z}
    stcl_cf: float = 0.0
    ltcl_cf: float = 0.0
    taxes_paid: float = 0.0
    charges: float = 0.0
    trades: list = field(default_factory=list)

    def contribute(self, date, amount):
        self.cash += amount
        self.flows.append((pd.Timestamp(date), -amount))

    def _fy(self, d):
        return self.realized.setdefault(fy_end(pd.Timestamp(d)), {"st": 0.0, "lt": 0.0, "div": 0.0})

    def realize(self, entry_date, exit_date, cost_basis, proceeds_gross, dividends):
        sc = sell_cost(proceeds_gross)
        net = proceeds_gross - sc
        self.charges += sc
        self.cash += net + dividends
        gain = net - cost_basis
        long_term = (pd.Timestamp(exit_date) - pd.Timestamp(entry_date)).days > 365
        r = self._fy(exit_date)
        r["lt" if long_term else "st"] += gain
        if dividends:
            r["div"] += dividends
        return gain, long_term

    def settle_taxes(self, upto: pd.Timestamp):
        """Pay tax for every financial year that ended on or before `upto`."""
        for fy in sorted(k for k in self.realized if k <= upto and not self.realized[k].get("paid")):
            r = self.realized[fy]
            st, lt = r["st"], r["lt"]
            if st < 0 and lt > 0:                      # short-term loss can absorb long-term gain
                use = min(-st, lt); st += use; lt -= use
            new_ltcl = -lt if lt < 0 else 0.0
            lt = max(lt, 0.0)
            use = min(self.stcl_cf, max(st, 0.0)); st -= use; self.stcl_cf -= use        # brought-forward ST loss
            use = min(self.stcl_cf, lt); lt -= use; self.stcl_cf -= use
            use = min(self.ltcl_cf, lt); lt -= use; self.ltcl_cf -= use               # brought-forward LT loss
            if st < 0:
                self.stcl_cf += -st; st = 0.0
            self.ltcl_cf += new_ltcl
            tax = st * STCG_RATE + max(lt - LTCG_EXEMPT, 0.0) * LTCG_RATE + r["div"] * DIV_TAX
            r["tax"], r["paid"] = tax, True
            self.taxes_paid += tax
            if tax > 0:
                from_cash = min(self.cash, tax)
                self.cash -= from_cash
                if tax > from_cash:                      # shortfall paid from the investor's pocket
                    self.flows.append((fy, -(tax - from_cash)))


def xirr(flows) -> float:
    if not flows:
        return float("nan")
    d0 = min(d for d, _ in flows)
    t = np.array([(d - d0).days / 365.25 for d, _ in flows])
    v = np.array([a for _, a in flows])
    f = lambda r: np.sum(v / (1 + r) ** t)  # noqa: E731
    lo, hi = -0.99, 5.0
    if f(lo) * f(hi) > 0:
        return float("nan")
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def monthly_amount(year: int) -> float:
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from signals import monthly_amount as m
    return m(year)
