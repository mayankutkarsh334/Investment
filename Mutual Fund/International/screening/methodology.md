# Screening Methodology — International Funds

**Context:** ₹20,000/month SIP, 10+ year horizon. This is the **third co-equal sleeve** alongside the FlexiCap **core** and the SmallCap **satellite** — a geographic / currency diversifier. Same 2-stage screening pipeline as FlexiCap and SmallCap, but with material adjustments for the international equity context.

**Universe:** 53 International **equity** Funds (Direct, Growth plan) — data from Tickertape, May 21, 2026. (Overseas debt/US-Treasury, gold-mining, and REIT FoFs are excluded as separate asset classes.)

**Scope decisions (set with the investor):**
- **Full international** — US, global-developed, emerging markets, China, Europe, Asia, and thematic — not restricted to one geography.
- **All-active study** — see §1. Eliminating SIP-closed funds removes the entire passive index lane, so this is effectively an all-active study; the passive lane is documented as closed-by-regulation, to be revisited if the SEBI cap resets.

---

## Why International Screening Differs from Domestic Equity

### 1. The Defining Hard Filter: Open to SIP (the SEBI Overseas Limit)

This is the international equivalent of SmallCap's AUM ceiling — a **structural investability constraint that no return metric captures.**

- SEBI/RBI cap the **industry-wide overseas investment** at **US $7 billion** (plus $1bn for overseas ETFs). When the industry breaches the cap, AMCs must **stop accepting fresh subscriptions** into funds that buy foreign securities.
- As of the May 2026 data, **43 of the 53** international equity funds show **"SIP: Not allowed"** — they are closed to fresh monthly investment.
- **Critically, this wipes out the entire passive index lane.** Every NASDAQ-100, S&P-500, and MSCI-World *index tracker* (Motilal Oswal Nasdaq 100, Kotak US, Mirae S&P 500 / FANG+, Navi, HDFC Developed World, ICICI Nasdaq) is closed, because passive funds that buy overseas ETFs hit the tighter $1bn ETF sub-limit first.
- **What remains open are mostly active offshore-feeder funds** (the Edelweiss feeder family, Franklin, PGIM) — these invest into an *underlying foreign mutual fund* rather than an ETF, and several AMCs still had headroom.
- **Threshold: SIP "Not allowed" → eliminated in Stage 1.** You cannot run a 10-year monthly SIP into a fund that won't accept it. This is the single most consequential filter in the international study.

> **Consequence — an all-active study.** Because closure is concentrated in the passive lane, eliminating closed funds leaves a survivor set that is **100% actively managed.** The two-lane (passive vs active) comparison is therefore documented but not populated on the passive side; the passive lane's verdict is *"un-investable via SIP today — revisit on cap reset."*

### 2. No AUM Upper Limit (the opposite of SmallCap)

In SmallCap, large AUM was disqualifying because small-cap stocks are illiquid. **International FoFs invest in deep, liquid foreign markets** (US large-cap, MSCI World) or into large underlying funds — there is **no capacity constraint.** A ₹6,000 Cr NASDAQ feeder has no execution problem. So:
- **No AUM maximum filter.**
- AUM *minimum* still applies (operational viability), but at a **lower floor than SmallCap** — international feeders are structurally smaller. **Threshold: AUM ≥ ₹100 Cr** (vs ₹500 Cr for SmallCap).

### 3. Skill is Measured vs the Fund's OWN Benchmark — Never Cross-Geography

The most important Stage-2 adaptation. A US-tech fund's 19% 5Y CAGR and an ASEAN fund's 11% reflect **which market did well, not manager skill.** Filtering the full-international universe on absolute CAGR would simply select "whatever geography ran hottest" (the US) and eliminate every diversifier — defeating the entire purpose of an international sleeve.
- **Stage 2 uses peer-relative and benchmark-relative metrics** (Returns vs sub-category, Alpha), not raw cross-geography CAGR.
- Geography selection (US vs Global vs EM vs Europe) is a **portfolio-construction decision made in the decision tree**, not a screening filter.

### 4. Cost is Structurally Higher — Handled in Module 4, Not as a Hard Gate

International active funds carry a **double layer of fees**: the Indian feeder's ER **plus** the embedded expense of the underlying foreign fund. Active offshore feeders legitimately run 1.3–1.6% Direct ER. A tight ER hard-filter (like SmallCap's 1.0%) would eliminate the entire active offshore-feeder lane — which is the only investable lane. So:
- **No tight ER hard filter.** A loose ceiling (ER ≤ 1.75%) catches only egregious cases.
- **True all-in cost** (feeder ER + underlying fund TER) is analysed in **Module 4**, where it is a primary scoring axis.

### 5. Currency (₹/$) Is a Return Driver, Not Just a Risk

A meaningful slice of an Indian investor's international return is **rupee depreciation** (historically ~3–4%/year vs USD). This is a *tailwind* unique to the category and must be decomposed in Module 1 (how much of the CAGR is the foreign market vs INR weakening) and assessed in Module 2 (currency volatility, and the tail risk of a rupee *appreciation* phase).

### 6. Taxation Changes the Net Outcome

International FoFs are taxed differently from domestic equity funds, and the rules shifted across the April-2023 / April-2025 / April-2026 Finance Acts. The post-tax outcome is **materially different** from a domestic equity fund at the same gross CAGR, and varies by holding structure (FoF vs feeder, equity-orientation of the underlying). Taxation is documented per fund in **Module 4**.

---

## Stage 1 — Hard Filters (Applied in Order)

| Filter | Threshold | Rationale | International vs Domestic |
|--------|-----------|-----------|--------------------------|
| **Open to SIP** | SIP "Allowed" | Cannot run a monthly SIP into a closed fund; SEBI $7bn overseas cap | **New — the defining international filter** |
| Fund age | ≥ 60 months (5 years) | Minimum through-cycle track record | Same as domestic |
| AUM minimum | AUM ≥ ₹100 Cr | Operational viability; redemption resilience | **Lower floor** (SmallCap: ₹500 Cr) |
| AUM maximum | **None** | Foreign markets are liquid — no capacity constraint | **Removed** (SmallCap: ₹30,000 Cr cap) |
| Sharpe Ratio | Sharpe ≥ 0 | Returns must exceed risk-free over the recent period | Same as domestic |
| Expense Ratio | ER ≤ 1.75% (loose) | Catches egregious cost only; true cost handled in Module 4 | **Looser** (SmallCap: 1.0%) — double-fee reality |

**Result:** 53 → **10 survivors** (all active). See [stage1_hard_filters.md](stage1_hard_filters.md).

---

## Stage 2 — Performance Filters (peer-relative, never cross-geography)

| Filter | Threshold | Rationale |
|--------|-----------|-----------|
| Manager adds value | Alpha > 0 (vs own benchmark) | The fund must beat the index it actually tracks — the only fair skill test across geographies |
| Not a persistent peer-laggard | Returns vs sub-category (3Y) ≥ ~0.85x **OR** a unique diversification role | Eliminate funds that lag their *own* peer group without offering distinct geographic/style coverage |

**Result:** 10 → **8 shortlisted**. See [stage2_performance.md](stage2_performance.md).

---

## Key Screening Decisions

### Why eliminate closed funds rather than score them?
A 10-year monthly SIP is the investment vehicle. A fund that does not accept SIPs is not investable *as a SIP*, no matter how good. Scoring it would produce a recommendation the investor cannot act on. Closed funds are catalogued in `all_funds_data.md` so the study can re-open them instantly if the SEBI cap resets.

### Why no absolute-CAGR filter in Stage 2?
Cross-geography CAGR measures market beta, not skill. Over the 5Y window the US (NASDAQ/tech) crushed EM and Europe — an absolute filter would deterministically select US funds and reject every diversifier, defeating the sleeve's purpose. Skill is isolated only by comparing each fund to *its own* benchmark/peers.

### Why keep multiple funds in the same geography (3 US, 2 EM)?
Like running several small-cap funds, holding two managers in one geography lets the deep study compare **AMC execution and style** (US growth vs US value vs US tech; PGIM EM vs Edelweiss EM) rather than just market exposure.

---

## What the Filters Cannot Catch (requires deep study)

1. **Underlying-fund risk** — most survivors are *feeders* into a foreign mutual fund (e.g. a JPMorgan, BlackRock, or Edelweiss-affiliated underlying). The underlying's manager, mandate, and fee are the *real* engine; the Indian AMC is a wrapper. Module 5 must look through to the underlying.
2. **Currency decomposition** — how much of the record is the foreign market vs rupee depreciation (Module 1).
3. **True all-in cost** — feeder ER + embedded underlying TER (Module 4).
4. **Taxation drift** — the post-2023/2025/2026 tax treatment of FoFs (Module 4).
5. **Reopening risk / closure history** — whether the fund has repeatedly closed and reopened with the SEBI cap, disrupting SIPs (Modules 4 & 6).
6. **Benchmark-label errors** — Tickertape mislabels some (e.g. Franklin Asian Equity shows "NIFTY 500"); the real mandate must be verified per fund.

---

*Methodology version: 1.0 | Created: June 2026 | Data date: May 21, 2026 | Universe: 53 International Equity Funds (Direct Growth)*
