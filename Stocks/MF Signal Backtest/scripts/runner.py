"""Phase 4: month-by-month portfolio runner for a signal strategy and its random-stock control.

run_portfolio(choose, ...)  - every action date: sell what has exited (at the open), pay last year's
                              tax, add this year's monthly amount, buy whole shares of the chosen stock
                              at the open, leftover rupees to cash. At the end, sell everything still
                              held at the last close, pay the final tax, and compute XIRR.
strategy_chooser(signal)    - the month's rank 1 (or next rank if 3 lots are already open / one share
                              is not affordable at the actual open price).
random_chooser(...)         - a random eligible NSE stock from the SAME liquidity quintile as the
                              strategy's pick that month (cash months stay cash); 1,000 runs = the luck baseline.
"""
from __future__ import annotations

import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import engine as E  # noqa: E402
from signals import monthly_amount  # noqa: E402

P = E.P


@dataclass
class Options:
    rules: E.Rules = E.Rules()
    max_lots: int = 3             # user-confirmed: up to 3 open buys per stock
    reinvest: bool = False        # variant: add exit proceeds to the next buy
    taxes: bool = True
    track_value: bool = False     # monthly portfolio value (for drawdown)
    cash_rate: float = 0.0        # yearly after-tax return on idle cash (0 = conservative)
    park: str | None = "NIFTY SMALLCAP 250"   # user decision: idle money goes into a small-cap fund
                                              # (index-fund proxy; None = keep as cash)


class Park:
    """Idle money parked in a fund: buys units on the day money becomes free; redeems oldest units
    first (to pay tax); everything is sold at the end. Gains are taxed like any equity fund."""

    def __init__(self, nav: pd.Series, book: E.Book):
        self.nav, self.book, self.lots = nav, book, []   # lots: [date, units, cost]

    def px(self, d):
        return float(self.nav.loc[:pd.Timestamp(d)].iloc[-1])

    def deposit(self, d, amount):
        if amount > 0.005:
            self.lots.append([pd.Timestamp(d), amount * (1 - MF_STAMP) / self.px(d), amount])

    def value(self, d):
        p = self.px(d)
        return sum(u for _, u, _ in self.lots) * p

    def redeem(self, d, amount):
        """Sell units worth `amount` (oldest first); returns rupees raised."""
        self.lots.sort(key=lambda l: l[0])
        p, raised = self.px(d), 0.0
        while self.lots and raised < amount - 0.005:
            ld, u, c = self.lots[0]
            need_u = (amount - raised) / p
            take = min(u, need_u)
            cost = c * take / u
            r = self.book._fy(d)
            r["lt" if (pd.Timestamp(d) - ld).days > 365 else "st"] += take * p - cost
            raised += take * p
            if take >= u - 1e-12:
                self.lots.pop(0)
            else:
                self.lots[0] = [ld, u - take, c - cost]
        return raised

    def liquidate(self, d):
        return self.redeem(d, self.value(d) + 1.0)


class LotCache:
    def __init__(self, pr: E.Prices):
        self.pr, self.c = pr, {}

    def get(self, iss, date, rules):
        k = (iss, pd.Timestamp(date), rules)
        if k not in self.c:
            self.c[k] = E.simulate_lot(self.pr, iss, date, rules)
        return self.c[k]


def months_table() -> pd.DataFrame:
    s = pd.read_parquet(E.SIGNALS, columns=["ym", "action_date"]).drop_duplicates("ym")
    s = s.dropna().sort_values("ym")
    return s[s["action_date"] <= E.END_DATE].reset_index(drop=True)


def run_portfolio(choose, pr: E.Prices, cache: LotCache, opt: Options = Options(), label: str = ""):
    """choose(ym, action_date, budget, open_count: dict) -> issuer or None."""
    book = E.Book()
    park = Park(_park_nav(opt.park), book) if opt.park else None
    if park is not None:
        _orig = book.settle_taxes

        def settle(upto, _orig=_orig):
            # raise the year's tax by redeeming fund units the day after the year ends
            for fy in sorted(k for k in book.realized if k <= upto and not book.realized[k].get("paid")):
                need = _tax_preview(book, fy)
                if need > book.cash:
                    book.cash += park.redeem(fy + pd.Timedelta(days=1), need - book.cash)
                _orig(fy)
        book.settle_taxes = settle  # type: ignore
    if not opt.taxes:
        book.settle_taxes = lambda upto: None  # type: ignore
    open_lots = []          # dicts: iss, entry, shares, cost, res, entry_adj
    open_count = defaultdict(int)
    values = []
    last_d = None
    for _, m in months_table().iterrows():
        d = pd.Timestamp(m["action_date"])
        if opt.cash_rate and last_d is not None and book.cash > 0:
            book.cash *= (1 + opt.cash_rate) ** ((d - last_d).days / 365.25)
        last_d = d
        # 1. exits on or before today (sell at the open, before buying)
        still = []
        for lot in open_lots:
            if lot["res"].exit_date <= d and lot["res"].reason != "open":
                _close(book, lot)
                open_count[lot["iss"]] -= 1
                if park is not None:   # sale money and dividends go into the fund on the exit day
                    park.deposit(lot["res"].exit_date, book.cash)
                    book.cash = 0.0
            else:
                still.append(lot)
        open_lots = still
        book.settle_taxes(d - pd.Timedelta(days=1))
        # 2. this month's money
        amt = monthly_amount(d.year)
        book.contribute(d, amt)
        budget = book.cash if opt.reinvest else amt
        # 3. pick and buy
        iss = choose(m["ym"], d, budget, open_count)
        if iss is not None:
            i = pr.idx(iss, d)
            px = pr.a[iss]["open_raw"][i]
            sh = int(budget // px)
            while sh > 0 and sh * px + E.buy_cost(sh * px) > budget:
                sh -= 1
            res = cache.get(iss, d, opt.rules)
            if sh > 0 and res is not None:
                cost = sh * px + E.buy_cost(sh * px)
                book.cash -= cost
                book.charges += E.buy_cost(sh * px)
                open_lots.append({"iss": iss, "entry": d, "shares": sh, "px": px, "cost": cost, "res": res,
                                  "entry_adj": pr.a[iss]["o"][i]})
                open_count[iss] += 1
        if park is not None:           # leftover rupees (or the whole amount in a no-pick month)
            park.deposit(d, book.cash)
            book.cash = 0.0
        if opt.track_value:
            v = book.cash + (park.value(d) if park is not None else 0.0) + sum(l["shares"] * l["px"] * (pr.close_on_or_before(l["iss"], d)[0] / l["entry_adj"])
                                for l in open_lots)
            values.append((d, v, sum(-a for dd, a in book.flows if a < 0)))
    # 4. the end: close everything (exits that already happened, and open lots at the last close)
    if opt.cash_rate and last_d is not None and book.cash > 0:
        book.cash *= (1 + opt.cash_rate) ** ((E.END_DATE - last_d).days / 365.25)
    for lot in open_lots:
        _close(book, lot)
    if park is not None:
        book.cash += park.liquidate(E.END_DATE)
    book.settle_taxes(pd.Timestamp("2100-01-01"))
    final = book.cash
    flows = book.flows + [(E.END_DATE, final)]
    invested = -sum(a for _, a in book.flows if a < 0)
    out = {"label": label, "xirr": E.xirr(flows), "final_value": final, "invested": invested,
           "taxes": book.taxes_paid, "charges": book.charges, "trades": book.trades}
    if opt.track_value:
        out["values"] = values
    return out


def _close(book: E.Book, lot):
    r = lot["res"]
    gross = lot["shares"] * lot["px"] * r.ret
    divs = lot["shares"] * lot["px"] * r.div
    gain, lt = book.realize(lot["entry"], r.exit_date, lot["cost"], gross, divs)
    book.trades.append({"issuer": lot["iss"], "entry": lot["entry"], "exit": r.exit_date, "reason": r.reason,
                        "shares": lot["shares"], "buy_px": lot["px"], "cost": lot["cost"], "gross": gross,
                        "dividends": divs, "gain": gain, "long_term": lt, "ret": r.ret, "peak": r.peak})


_NAV_CACHE = {}


def _park_nav(name):
    if name not in _NAV_CACHE:
        idx, funds = benchmark_series()
        _NAV_CACHE[name] = idx[name] if name in idx else funds[name]
    return _NAV_CACHE[name]


def _tax_preview(book: E.Book, fy) -> float:
    """Tax that settle_taxes() will charge for year `fy` (without changing the book)."""
    import copy
    b = copy.deepcopy(book)
    b.cash = 1e18
    E.Book.settle_taxes(b, fy)
    return b.taxes_paid - book.taxes_paid


# ---------------- choosers ----------------
def strategy_chooser(signal: str, pr: E.Prices, max_lots: int = 3):
    s = pd.read_parquet(E.SIGNALS, columns=["ym", "issuer", f"rank_{signal}"])
    s = s.dropna(subset=[f"rank_{signal}"]).sort_values(["ym", f"rank_{signal}"])
    ranked = s.groupby("ym")["issuer"].apply(list).to_dict()

    def choose(ym, d, budget, open_count):
        for iss in ranked.get(ym, []):
            if open_count[iss] >= max_lots:
                continue
            i = pr.idx(iss, d)
            if i is None:
                continue
            px = pr.a[iss]["open_raw"][i]
            if px + E.buy_cost(px) > budget:
                continue
            return iss
        return None
    return choose


def universe(pr: E.Prices) -> pd.DataFrame:
    """Every NSE stock buyable on each action date (same filters as the signals), with its liquidity quintile."""
    px = pd.read_parquet(P / "prices_adj.parquet", columns=["date", "issuer", "series", "open", "close", "value"])
    px = px.sort_values(["issuer", "date"])
    px["adv20_cr"] = px.groupby("issuer")["value"].transform(lambda v: v.rolling(20, min_periods=15).mean().shift(1)) / 1e7
    px["ref_close"] = px.groupby("issuer")["close"].shift(1)
    mt = months_table()
    u = px[px["date"].isin(set(mt["action_date"]))].merge(mt, left_on="date", right_on="action_date")
    u["amt"] = u["date"].dt.year.map(monthly_amount)
    u = u[u["series"].isin(["EQ", "BE"]) & (u["ref_close"] <= u["amt"]) & (u["adv20_cr"] >= 1.0) & u["open"].notna()]
    sig = pd.read_parquet(E.SIGNALS, columns=["ym", "issuer", "sell_default"])
    u = u.merge(sig, on=["ym", "issuer"], how="left")
    u = u[~u["sell_default"].fillna(False).astype(bool)]   # same skip rule as the strategy
    u["liq_q"] = u.groupby("ym")["adv20_cr"].transform(lambda v: pd.qcut(v.rank(method="first"), 5, labels=False))
    return u[["ym", "date", "issuer", "adv20_cr", "liq_q"]]


def random_chooser(strategy_picks: dict, uni: pd.DataFrame, rng: np.random.Generator, pr: E.Prices, max_lots=3):
    """strategy_picks: ym -> issuer picked by the strategy (None = cash month)."""
    pools = {(ym, q): g["issuer"].values for (ym, q), g in uni.groupby(["ym", "liq_q"])}
    q_of = dict(zip(zip(uni["ym"], uni["issuer"]), uni["liq_q"]))

    def choose(ym, d, budget, open_count):
        sp = strategy_picks.get(ym)
        if sp is None:
            return None
        q = q_of.get((ym, sp))
        pool = pools.get((ym, q)) if q is not None else None
        if pool is None or len(pool) == 0:
            pool = uni.loc[uni["ym"] == ym, "issuer"].values
        for _ in range(50):
            iss = pool[rng.integers(len(pool))]
            if open_count[iss] >= max_lots:
                continue
            i = pr.idx(iss, d)
            if i is None:
                continue
            if pr.a[iss]["open_raw"][i] + E.buy_cost(pr.a[iss]["open_raw"][i]) > budget:
                continue
            return iss
        return None
    return choose


# ---------------- SIP benchmarks ----------------
MF_STAMP = 0.00005          # 0.005% stamp duty on mutual-fund purchases
INDEX_FUND_ER = 0.0020      # index fund expense ratio deducted from the TRI (direct plan, ~0.2%/yr)
PARK_SMALLCAP_ER = 0.0030   # small-cap index fund (direct) ~0.3%/yr


def sip_benchmark(series: dict, label: str, taxes: bool = True):
    """Invest each month's stepped-up amount on the same action dates, split equally across the
    given NAV series {name: pd.Series(nav, index=date)}; sell everything at END_DATE.
    Tax at the end: per instalment, short-term (<= 12 months) at 20.8%, long-term at 13% above Rs 1.25 lakh."""
    lots, flows = [], []
    for _, m in months_table().iterrows():
        d = pd.Timestamp(m["action_date"])
        amt = monthly_amount(d.year)
        flows.append((d, -amt))
        share = amt / len(series)
        for name, s in series.items():
            nav = s.loc[:d].iloc[-1]
            lots.append((d, name, share * (1 - MF_STAMP) / nav, share))
    st = lt = 0.0
    final = 0.0
    for d, name, units, cost in lots:
        v = units * series[name].loc[:E.END_DATE].iloc[-1]
        final += v
        if (E.END_DATE - d).days > 365:
            lt += v - cost
        else:
            st += v - cost
    tax = 0.0
    if taxes:
        if st < 0 and lt > 0:
            use = min(-st, lt); st += use; lt -= use
        tax = max(st, 0) * E.STCG_RATE + max(lt - E.LTCG_EXEMPT, 0) * E.LTCG_RATE
    flows.append((E.END_DATE, final - tax))
    return {"label": label, "xirr": E.xirr(flows), "final_value": final - tax, "invested": -sum(a for _, a in flows[:-1]),
            "taxes": tax}


def benchmark_series():
    tri = pd.read_parquet(P / "index_tri.parquet")
    out = {}
    for idx in ["NIFTY 500", "NIFTY 50", "NIFTY MIDCAP 150", "NIFTY SMALLCAP 250"]:
        s = tri[tri["index"] == idx].set_index("date")["tri"].sort_index()
        yrs = (s.index - s.index[0]).days / 365.25
        er = PARK_SMALLCAP_ER if "SMALLCAP" in idx else INDEX_FUND_ER
        out[idx] = s * np.exp(-er * yrs)
    nav = pd.read_parquet(P / "fund_nav.parquet")
    funds = {a: g.set_index("date")["nav"].sort_index() for a, g in nav.groupby("amc")}
    return out, funds
