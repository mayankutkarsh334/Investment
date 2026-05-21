# HSBC Flexi Cap Fund — Module Research Plan

**Context:** ₹20,000/month SIP, 10-year horizon. This is fund #7 of 9 shortlisted FlexiCap funds.
**Key hypothesis to test:** HSBC has the highest ER (1.22%) in the shortlist but strong returns. Does the return quality justify the cost premium? Does the foreign AMC structure create governance risks or advantages?
**Framework:** Same 6-module weighted scoring used for PP, JM, Edelweiss, HDFC, Quant, BOI.
**Data date:** Use Tickertape CSV (May 10, 2026) as primary source. Cross-verify all key metrics independently.

---

## Known Facts from Screener CSVs (pre-research baseline)

| Metric | HSBC Value | Source | Notes |
|--------|-----------|--------|-------|
| Volatility | 15.44% | Tickertape risk CSV | 2nd highest in shortlist after Quant (16%) |
| Max Drawdown | 39.79% | Tickertape risk CSV | 2nd worst after HDFC (41.84%) |
| Sharpe | 0.619 | Tickertape ratio CSV | 5th of 9 |
| Sortino | 0.066 | Tickertape ratio CSV | 5th of 9 |
| Tracking Error | 3.46% | Tickertape risk CSV | 4th lowest — moderate active share |
| Beta | ~1.0 | Inferred from vol profile | Near-market tracker |
| ER (Direct) | **1.22%** | Tickertape schema CSV | **Highest in shortlist — the critical red flag** |
| AUM | ~₹5,400 Cr | Tickertape schema CSV | Sweet-spot range (like JM, Edelweiss) |
| Mid + Small | **46.29%** | Tickertape composition CSV | **Highest in shortlist — strongest FlexiCap DNA** |
| Largecap | 53.1% | Tickertape composition CSV | Lowest in shortlist |
| Top 10 Concentration | 26.2% | Tickertape composition CSV | Most diversified (tied with JM) |
| Portfolio PE | 26.30 | Tickertape ratio CSV | Above category avg (25.30) |
| % Away from ATH | 0.93% | Tickertape ratio CSV | Near ATH — portfolio very healthy |

---

## Module 1: Returns Consistency

### Raw Data Table (Tickertape, May 10 2026)
Collect and populate all of:
- CAGR 3Y, CAGR 5Y, CAGR 10Y
- Rolling 3Y Average
- Alpha (3Y)
- Absolute 1Y, 6M, 3M
- 3Y benchmark beat (vs NIFTY 500 TRI)

### Cross-Source Verification Table
Verify every key return metric across: Tickertape | ValueResearch | Groww | IndMoney | Advisorkhoj
- Flag any anomalies (like BOI's 1Y Tickertape anomaly)
- Document the "canonical" figure used and why

### CAGR vs Benchmark Chart (Mermaid xychart-beta)
Bar = HSBC returns | Line = NIFTY 500 TRI
Periods: 1Y, 3Y, 5Y, 10Y

### Benchmark Outperformance Table
| Period | Fund | Benchmark | Outperformance |

### Rolling Average vs Point-to-Point Chart
Compare trailing 3Y CAGR vs Rolling 3Y average — explain the gap (good or bad)

### Returns vs Peers (Sub-category Multiples)
| Period | vs Sub-category multiple | Interpretation |
Periods: 10Y, 5Y, 3Y, 1Y — values above 1.0 = outperforming category

### Returns vs All 9 Shortlisted Peers Chart
Bar chart showing HSBC's 3Y CAGR and 5Y CAGR position relative to all 9 shortlisted funds

### Absolute Returns Short-Term Trend Chart
3M, 6M, 1Y bar chart — is momentum accelerating or decelerating?

### "Why Is the 1Y Return What It Is?" Section
- Attribute the 1Y return to: market conditions, mid/small allocation (HSBC has 46%), sector bets, manager decisions
- Is it above/below expectations given 46% mid+small allocation?

### Additional Metrics (Web Research)
| Metric | Value | Source |
- Beta vs Nifty 500
- Upside Capture Ratio
- Downside Capture Ratio
- Portfolio Turnover
- Info Ratio

### Upside vs Downside Capture Asymmetry Chart + Table
The key question: HSBC has highest mid+small (46%) — does this translate to good capture asymmetry or just higher risk both ways?

### Calendar Year Returns Chart (2016 or inception–2026 YTD)
Bar chart for each calendar year
**Key years to find and document:**
- 2018 (mid/small crash — critical since HSBC has 46% mid+small)
- 2019 (polarized large-cap year)
- 2020 (COVID full year)
- 2021 (post-COVID bull)
- 2022 (rate hike year)
- 2023 (mid/small rally — HSBC should have done well here)
- 2024 (bull continuation)
- 2025 (correction — how did 46% mid+small hold up?)
- 2026 YTD

Table: Year | Return | Notes | Winner vs peers

### COVID Crash Analysis (Feb–Mar 2020)
- Pre-crash peak NAV, trough NAV, % fall, recovery date
- Compare to: BOI's -23.73% (non-comparable — not launched), PP's -31.2%, peers' -35 to -42%
- **Important:** HSBC with 46% mid+small likely fell harder — quantify this

### SIP XIRR vs Lumpsum CAGR
| Period | Lumpsum CAGR | SIP XIRR | SIP Advantage / Disadvantage |
3Y and 5Y comparison
Higher volatility (15.44%) means more rupee cost averaging benefit — verify this

### Fund History / Inception Context
- When was HSBC Flexi Cap launched?
- Is there a 10Y CAGR? If not, document the gap clearly
- Manager attribution: how many managers over the fund's history?

### Module 1 Scorecard
| Sub-dimension | Score (1–5) | Reasoning |
- Long-term returns (5Y+)
- Consistency across periods
- Alpha generation
- Peer outperformance
- Capture ratio asymmetry
- SIP XIRR premium
- Recent momentum
- **Module 1 Overall**

---

## Module 2: Risk Profile

### Raw Data Table (Tickertape, May 10 2026)
| Metric | HSBC | Category Avg | Assessment |
Pre-filled from screener: Volatility 15.44%, Max DD 39.79%, Sharpe 0.619, Sortino 0.066, TE 3.46%
Also collect: Beta, Upside Capture, Downside Capture, Portfolio PE, % Away from ATH

### Volatility Chart (all 9 peers, sorted low to high)
Bar = each fund's volatility | Line = category average (14.14%)
HSBC at 15.44% is 2nd highest — position it correctly

### Why Is HSBC's Volatility High? (Structural Analysis)
Break down by portfolio composition — what's driving 15.44% volatility:
- 46% mid+small (the primary driver — these are inherently more volatile)
- Near-zero bonds (no dampening)
- Near-100% equity (99.4%)
- Portfolio PE 26.3 (above avg — growth tilt means more sentiment-driven swings)
Use a pie or composition chart to show the structural reasons

### Max Drawdown Chart (all 9 peers, sorted lowest to highest)
What ₹1L became at worst point table (for all 9 funds)
HSBC at 39.79% — 2nd worst. Interrogate this:
- When did this drawdown occur? (Year, market context)
- How long to recover?
- How does it compare to BOI's 23.73% and PP's 31.2%?

### Sharpe Ratio Analysis
Chart (all 9 peers sorted lowest to highest)
- HSBC at 0.619 — where does it rank?
- Break down Sharpe formula: (return − risk-free) / volatility
- Is 0.619 respectable given 15.44% volatility? (numerator analysis)
- Scenario: what does Sharpe look like if 1Y returns recover to historical average?

### Sortino Ratio Analysis
Chart (all 9 peers)
- HSBC at 0.066 — rank and context
- Does Sortino tell a different story from Sharpe? (downside-only volatility)

### Upside vs Downside Capture — Critical Section for HSBC
This is the most important risk metric for HSBC because of its 46% mid+small.
Hypothesis: High mid+small usually means high upside capture AND high downside capture — a symmetric risk profile, not an asymmetric one like PP's 90/59.
| | Upside Capture | Downside Capture | Asymmetry Ratio |
| HSBC | ? | ? | ? |
| Parag Parikh | 90% | 59% | 1.52x |
| Typical Peer | ~100% | ~94% | ~1.06x |

Chart: HSBC upside vs downside side by side vs PP vs peer average

### Tracking Error Analysis
HSBC at 3.46% — relatively low (only Edelweiss 2.19% and AB SL 2.37% are lower).
But HSBC has 46% mid+small — high active mid+small exposure should produce higher TE.
Why is TE moderate? Possible explanation: HSBC's stock selection within mid+small tracks the category average, not a highly differentiated approach. Verify.

### PE Ratio Risk Analysis
Portfolio PE 26.30 — above category average (25.30).
- What does a PE above category avg mean for crash exposure?
- Safety margin vs value trap argument (in reverse vs PP)
- Which sectors drive HSBC's above-avg PE?

### ATH Distance Analysis
HSBC is only 0.93% below ATH — near the top.
Compare to peers in ATH distance chart.
Is being near ATH a positive signal (portfolio momentum) or a risk signal (limited upside, vulnerable to mean reversion)?

### Risk vs Return Quadrant Chart (all 9 peers)
x-axis: volatility (risk) | y-axis: 5Y CAGR (return)
Where does HSBC sit? High-risk + high-return or high-risk + mediocre-return?

### Points For and Against — Risk Summary

### Module 2 Scorecard
| Sub-dimension | Score (1–5) | Reasoning |
- Volatility
- Max Drawdown
- Sharpe Ratio
- Sortino Ratio
- Tracking Error
- Downside Protection (capture ratio)
- PE Valuation Buffer
- **Module 2 Overall**

---

## Module 3: Portfolio DNA

### Raw Data Table (Tickertape, May 10 2026 + cross-verify with INDMoney/Groww/official)
Pre-filled from screener: Mid+Small 46.29%, Largecap 53.1%, Top 10 Conc 26.2%, PE 26.30, % ATH 0.93%
Also collect: Total Equity%, Midcap% separately, Smallcap% separately, International%, Debt%, Cash%, Top 3%, Top 5%, Portfolio Turnover

### "Is HSBC a True FlexiCap?" Section
HSBC at 46% mid+small is the highest in the shortlist — it is the most FlexiCap-pure fund.
- Total equity comparison chart (HSBC vs all 9 peers)
- Mid+Small allocation chart — HSBC at the top
- Verdict: HSBC is what the FlexiCap label actually promises

### Asset Allocation Pie Chart
Largecap | Midcap | Smallcap | Debt | Cash | Other
Document what HSBC does NOT have: international equity (0%), bonds (0% or near 0%)

### Mid vs Small Cap Split
Of the 46% mid+small: how much is midcap and how much is smallcap?
This matters: smallcap is more volatile, less liquid, and harder to exit
Chart + analysis of what the split means for crash protection and liquidity

### Sector Concentration Analysis
What are the top 3–5 sectors? What % of portfolio?
Is there a single dominant sector bet (like HDFC's 40% in FinServ)?
Identify any concentration risk comparable to Quant's 24.56% Adani exposure
FinServ | Technology | Consumer | Healthcare | Others breakdown

### Top Holdings Analysis
Who are the top 5–10 holdings?
- Are they quality businesses with moats?
- Any governance or regulatory concerns on individual holdings?
- How does holding quality compare to PP's conservative largecaps?

### Concentration Chart (Top 3 / Top 5 / Top 10)
HSBC Top 10 = 26.2% (tied with JM as most diversified in shortlist)
Compare to PP (52.4%) and Quant (71.4%) for context
Is low concentration in top 10 consistent with 46% mid+small? (it should be — small-caps mean more stocks needed)

### PE Ratio vs Peers Chart
HSBC at 26.30 — slightly above category avg (25.30), but not extreme like Quant (31.10)
What does this PE level say about the portfolio's growth vs value tilt?

### Portfolio Turnover Analysis
Collect actual turnover %
High turnover + 46% mid+small = high transaction costs in the most illiquid segment
Compare to PP's 20% and BOI's equivalent

### Debt and Cash Analysis
HSBC likely holds near-zero debt (like JM)
What is the cash %, and is it strategic or just operational float?
Compare to PP's structural 10% bond buffer

### ATH Distance Chart (all 9 peers sorted)
HSBC at 0.93% — near top. BOI at 0.02%.
What does this signal about current portfolio health?

### The AUM Sweet Spot Analysis
HSBC at ~₹5,400 Cr — similar to JM (₹5,041 Cr)
How does this AUM enable the 46% mid+small allocation?
Compare to PP's AUM constraint (₹1.4L Cr → only 6.15% mid+small)
Projected AUM where mid+small allocation would start shrinking

### Points For and Against — Portfolio DNA

### Module 3 Scorecard
| Sub-dimension | Score (1–5) | Reasoning |
- Cap allocation fit for FlexiCap
- International diversification
- Bond quality / cash management
- Valuation discipline (PE)
- Concentration risk
- Portfolio turnover
- Sector diversification
- ATH proximity
- **Module 3 Overall**

---

## Module 4: Cost & AUM Impact

### Raw Data Table
| Metric | Value |
- ER Direct: 1.22% (**highest in shortlist — the primary concern**)
- ER Regular: collect from official source
- Direct-Regular gap (₹)
- Exit Load: collect exact terms
- AUM: ~₹5,400 Cr (verify exact figure)
- Monthly SIP inflow estimate
- Portfolio Turnover (feeds into hidden cost analysis)
- Min SIP amount

### ER Comparison Chart (all 9 peers, sorted lowest to highest)
HSBC at 1.22% should be visually isolated at the expensive end
Line = PP's ER (0.53%) as reference

### 10Y ER Impact on ₹20K SIP — The Central Calculation
Assume identical gross returns for all funds. Show net corpus after fees:
| Fund | ER | 10Y Net Corpus | Gap vs cheapest |
Work through the math: at what return does HSBC's higher ER become too expensive to justify?
**The break-even question:** If HSBC generates X% gross returns, what net return does the investor get? How many percentage points of alpha does HSBC need just to break even with Edelweiss (0.52%)?

### Break-Even Alpha Calculation
HSBC charges 0.70% more than Edelweiss (1.22% vs 0.52%).
For HSBC to deliver the same net return to investors, it must generate 0.70% more alpha every year.
Chart: "HSBC needs to outperform Edelweiss by 0.70%/year just to break even on cost"
How often does any active fund consistently outperform by 0.70%/year? Historical data.

### Direct vs Regular Plan
| Plan | ER | 10Y Corpus | Difference |
- Direct: 1.22%
- Regular: collect (likely ~2.0–2.2%)
- ₹4L+ difference over 10Y on ₹20K SIP

### Exit Load Structure
Compare to all peers. Note exact redemption terms.
For a 10Y SIP investor — does the exit load structure matter practically?

### AUM Analysis: Sweet Spot or Danger Zone?
HSBC at ~₹5,400 Cr — same range as JM
This AUM enables genuine mid+small execution (46% is proof)
Projected AUM trajectory (if SIP inflows continue at current pace)
At what AUM does HSBC face the same constraints as PP?

### Monthly Forced Deployment Problem
How much arrives in monthly SIP inflows?
With 46% mid+small — are there enough quality opportunities being deployed into?
Compare to PP's forced-deployment problem at ₹1,000 Cr/month

### Portfolio Turnover × Mid+Small = Hidden Transaction Cost
High turnover + illiquid mid+small = expensive to execute
Calculate illustrative annual market impact cost vs a low-turnover peer
Even if ER says 1.22%, the "true all-in cost" is higher if turnover is high

### The Core Dilemma Section
Write the explicit dilemma clearly:
- HSBC offers the best FlexiCap DNA (46% mid+small, 26% top-10 diversity)
- HSBC has the highest ER (1.22%)
- These two things are in tension: the best product at the highest price
- Is the price justified? Frame the answer in terms of:
  a) How much extra alpha HSBC historically generated vs cheaper peers
  b) Whether that alpha has been consistent or cyclical

### Counter-Arguments — Why The ER May Be Justifiable
- Foreign AMC infrastructure premium (global research, risk systems, compliance)
- If HSBC generates sustained 1%+ annual alpha over Edelweiss — the cost is paid
- Smaller AUM means less market impact — the "true cost" gap may be narrower than ER suggests
- The 46% mid+small access is unique — what's the right price for true FlexiCap execution?

### Points For and Against — Cost & AUM

### Module 4 Scorecard
| Sub-dimension | Score (1–5) | Reasoning |
- Expense ratio
- Direct vs Regular gap
- Exit load structure
- AUM manageability
- Turnover-adjusted impact cost
- Alpha sustainability (ER justification)
- **Module 4 Overall**

---

## Module 5: Fund Manager Quality

### Raw Data Table (cross-source verified)
| Metric | Value | Source |
Collect all of:
- Primary Manager name
- Role / title
- Managing HSBC Flexi Cap since (date)
- Fund tenure (years)
- Total industry experience (years)
- Career history (firm by firm, years each)
- Education / certifications
- Investment philosophy (exact terms used)
- Co-managers (names, roles, tenure)
- Total schemes managed across the AMC
- AUM managed (total across all funds)
- Investor letters: Yes / No
- Skin-in-game disclosure: Yes / No
- Personal SEBI issues: any penalties, show-cause notices?
- Key-man risk assessment

**Primary sources to use:**
- HSBC AMC website (hsbcmf.com)
- SEBI MF disclosure: www.sebi.gov.in or the fund's SID/SAI
- ValueResearch fund manager profile
- Morningstar India fund manager page
- Business Standard / Mint / Economic Times interviews
- AdvisorKhoj fund manager profile
- PrimeInvestor (if available)

### Management Team Table
| Manager | Role | Tenure at HSBC AMC | Tenure on this fund | Background |

### Fund Manager Tenure Chart (all 9 peers)
Bar chart: years each lead manager has been on their current fund
Where does HSBC rank? (PP = 13Y, AB SL = 15Y are the benchmarks)

### Manager Continuity Story
Has HSBC Flexi Cap had manager changes?
If yes: when, how many in the last 4 years? (HDFC had 3 changes — a red flag)
If no: how long has the current manager been in place?
Critically: how much of the 3Y/5Y/10Y track record was built by the current manager vs predecessors?

### Investment Philosophy — What Framework Does HSBC Use?
Is it articulated clearly? Is it documented anywhere public?
Evaluate: GARP / Growth / Value / Blend / Momentum / Quantitative?
Compare to documented philosophies: PP (Graham/Buffett), JM (GEEQ), Edelweiss (FAIR), Quant (VLRT black-box)
The question: can you describe the philosophy in one sentence? If not, it may be undocumented.

### Philosophy Tested Under Market Pressure
Key market events and how HSBC's manager responded:
| Year | Market Environment | HSBC Response | Outcome |
- 2018: mid/small crash (HSBC has 46% mid+small — were they tested hard?)
- 2020: COVID crash
- 2022: rate hike correction
- 2024: momentum rally — did HSBC catch it?
- 2025: correction — how did 46% mid+small hold up?

### Foreign AMC Manager Context
HSBC is a foreign bank subsidiary. What does this mean for the fund manager?
- Are investment decisions made in India or partially guided by global HSBC investment teams?
- Is there a "global investment committee" override on India decisions?
- How does HSBC India AMC's investment process compare to domestic AMCs?
- Risk: foreign parent could exit India market (Fidelity, Goldman, JP Morgan have exited Indian AMC JVs in the past). What happens to the fund manager and unitholders if HSBC decides to sell its India AMC business?

### Key-Man Risk Analysis
If the primary manager leaves tomorrow:
- Is there a bench of trained co-managers?
- Does the investment philosophy survive the person, or is it person-dependent?
- HSBC as a large institution likely has deeper bench than a boutique like PPFAS — verify

### SEBI / Regulatory Issues
Check the fund's SAI/SID "Penalties" page for any SEBI actions against:
- The fund manager personally
- HSBC AMC India
- Parent HSBC Group (any relevant global compliance issues affecting India operations)

### Skin in the Game
Does the manager invest personally in the fund?
HSBC, as a corporate, may have restrictions on this — clarify.

### Investor Communication Quality
Quarterly / annual letters? Fact sheet quality? Portfolio commentary depth?
Compare to PP's benchmark (quarterly letters, explicit decision explanations) and JM's (none)

### Module 5 Scorecard
| Sub-dimension | Score (1–5) | Reasoning |
- Manager tenure on fund
- Philosophy clarity & documentation
- Philosophy discipline under pressure
- Track record attribution clarity
- Skin in the game
- Investor communication
- Key-man risk
- Foreign AMC structure risk
- SEBI / regulatory record
- **Module 5 Overall**

---

## Module 6: AMC Trustworthiness

### Raw Data Table (cross-source verified)
| Metric | Value | Source |
Collect all of:
- AMC full name (HSBC Asset Management (India) Private Limited)
- Parent / Ownership (HSBC Group — %)
- SEBI Registration date
- Founded / operations commenced
- CEO name, tenure, background
- CIO name, tenure, background
- Total schemes
- Total AMC AUM
- Flexi Cap as % of AMC AUM
- Regulatory actions (SEBI penalties page in SID/SAI)
- Annual revenue estimate (ER × AUM)
- Profitability (if public)
- App rating (Google Play / App Store)
- Investor letters: Yes / No
- Bank distribution conflict: HSBC Bank India pushes HSBC MF?
- Global parent stability / India commitment

**Primary sources:**
- hsbcmf.com (About Us)
- HSBC AMC SID/SAI penalties disclosure page
- SEBI AMFI website for AMC registration details
- HSBC Group annual report (global parent financials)
- Business Standard / Mint for any news on HSBC AMC India exits or restructuring
- Morningstar AMC page

### AMC Overview Narrative
Who is HSBC Asset Management India? Foreign bank subsidiary vs domestic AMC.
When did HSBC enter India's mutual fund space?
Any ownership structure changes over time?

### Regulatory Record
SEBI actions chart (all 9 AMCs — pre-existing data from other modules + new HSBC data)
For HSBC specifically:
- Any SEBI show-cause notices?
- Any penalties on the AMC or individuals?
- Any front-running or governance investigations?
- **Global parent issues:** Any HSBC Group compliance failures globally that affected India operations?

### Foreign AMC Exit Risk — The Unique HSBC Risk
This is a risk no other shortlisted fund carries. Historical precedent:
| AMC | Foreign Parent | Exit Year | What Happened |
| Goldman Sachs MF | Goldman Sachs | 2017 | Sold to Reliance Capital |
| JP Morgan AMC India | JP Morgan | 2016 | Sold to Edelweiss |
| Fidelity India | Fidelity | 2012 | Sold to L&T Finance |
| Deutsche AMC India | Deutsche Bank | 2017 | Sold to DHFL Pramerica |
| Pinebridge Investments | AIG | 2012 | Sold to Kotak |

Pattern: when global economic conditions tighten or parent strategy shifts, foreign AMCs exit India.
**The question:** Is HSBC Asset Management India committed to the India market for the next 10 years?
Evidence to examine:
- HSBC Group's India strategic statements (recent annual reports, investor days)
- HSBC India AMC AUM growth trajectory (growing = commitment signal; shrinking = exit watch)
- Any news of HSBC Global reviewing India AMC business
- What happens to unitholders if HSBC sells: SEBI requires acquiring AMC to honor existing scheme terms — not a financial risk, but manager continuity and brand change risk

### Ownership Structure Analysis
Who owns HSBC AMC India? (HSBC Group %)
Is there an Indian partner or is it 100% foreign-owned?
Compare to domestic AMCs: PPFAS (independent), HDFC (HDFC Bank 52.4%), BOI (govt bank 100%)

### AMC Size and Scheme Focus
Total AUM vs. number of schemes: is HSBC focused or bloated?
What % of HSBC AMC's AUM is in FlexiCap specifically?
Does the AMC have strong equity DNA or is it primarily a debt/liquid fund house?

### Bank Distribution Conflict
HSBC Bank India has branches and wealth management services.
Do HSBC Bank RMs push HSBC MF products to clients?
If yes: captive distribution = fee income secured regardless of performance = reduced performance incentive
Compare to HDFC AMC's conflict with HDFC Bank

### AMC Financial Health
Is HSBC AMC India profitable?
Fee revenue estimate: 1.22% × ₹5,400 Cr = ~₹66 Cr/year
Is this enough to sustain quality operations? Or does the business require parent subsidy?
Compare to PPFAS (₹747 Cr/year) and JM (loss-making, parent subsidizes)

### Investor Communication Quality
Fact sheet quality? Monthly commentary? Annual reports?
Does HSBC communicate like a serious long-term partner or a transactional product house?

### Points For and Against — AMC Trustworthiness

### Module 6 Scorecard
| Sub-dimension | Score (1–5) | Reasoning |
- Regulatory record
- Ownership / independence
- AMC financial stability
- Exit risk (foreign parent)
- Investor communication
- Distribution conflict
- Scheme focus
- Parent stability
- **Module 6 Overall**

---

## README.md (Fund Summary File)

After all 6 modules are complete, the README should contain:

### Fund Identity Table
| Field | Value |
- Scheme name, ISIN, Scheme code (MFAPI)
- Inception date
- AUM (as of May 2026)
- ER Direct / Regular
- Exit Load
- Benchmark
- Primary fund manager (name, since)
- AMC
- Min SIP

### One-Line Identity
"HSBC Flexi Cap — [one line capturing the fund's defining trade-off]"
Expected: something about "highest mid+small exposure + highest ER + foreign AMC exit risk"

### Module Scores Summary Table
| Module (Weight) | Score | Key Reason |
| M1 Returns (25%) | | |
| M2 Risk (20%) | | |
| M3 Portfolio (15%) | | |
| M4 Cost (20%) | | |
| M5 Manager (15%) | | |
| M6 AMC (5%) | | |
| **Weighted Total** | | |

### Hard Filter Checklist
| Filter | HSBC | Note |
- Active regulator probe on key person?
- Data destruction alleged?
- Max drawdown > 50%?
- Manager < 12 months tenure on fund?
- Single-group exposure > 20%?
- Top-10 concentration > 65%?
- Black-box undocumented model?
- **Foreign parent exit risk?** ← unique additional filter for HSBC

### One-Line Verdict
Written after scoring is complete.

---

## Research Sources Checklist (Required Before Writing)

| Source | URL | What to Pull |
|--------|-----|-------------|
| HSBC MF Official | hsbcmf.com | Fund page, fact sheet, manager bio, SID |
| HSBC AMC About Us | hsbcmf.com/about-us | AMC history, team, ownership |
| HSBC AMC SID/SAI | AMFI website | Penalties page, trustee details |
| Tickertape | Already downloaded | All CSV files in FlexiCap/ folder |
| ValueResearch Online | valueresearchonline.com | Fund page, manager page, cross-verify returns |
| Morningstar India | morningstar.in | Independent risk metrics, manager profile |
| AdvisorKhoj | advisorkhoj.com | Rolling returns, SIP XIRR, capture ratios |
| PrimeInvestor | primeinvestor.in | If accessible — risk analysis |
| MoneyWorks4Me | moneyworks4me.com | Business quality of holdings |
| Groww | groww.in | Returns cross-verify, portfolio holdings |
| IndMoney | indmoney.com | Returns cross-verify |
| SEBI AMFI DB | amfiindia.com | Official registration, compliance |
| HSBC Group Annual Report | hsbc.com | India commitment, global financials |
| News Search | Business Standard, Mint, ET | Any controversies, exit rumors, manager changes |
| MFAPI | mfapi.in | NAV history for own calculations (scheme code needed) |

---

## Module Writing Order (Recommended)

1. **Module 3** first — get the portfolio composition right; informs all other modules
2. **Module 1** second — return data is the foundation; cross-source verify carefully
3. **Module 2** third — risk profile; many data points already gathered from M1+M3
4. **Module 4** fourth — cost analysis; use AUM from M3, turnover from M3
5. **Module 5** fifth — manager; deepest web research needed
6. **Module 6** last — AMC; builds on manager context; foreign exit risk is the key new analysis

---

## Key Open Questions (Answer in the Respective Modules)

1. **M1:** Does HSBC's 46% mid+small actually translate to strong returns in mid+small-heavy years (2023, 2024)? Verify year-by-year.
2. **M1:** What is HSBC's 10Y CAGR? If the fund is young, document the inception date and note the gap.
3. **M2:** What is HSBC's actual Upside/Downside Capture ratio? Does 46% mid+small create symmetric (not asymmetric) capture?
4. **M3:** What is the mid vs small split within the 46%? High small-cap = higher risk + harder to exit.
5. **M3:** What is HSBC's actual portfolio turnover? High turnover + 46% mid+small = expensive execution.
6. **M4:** Does HSBC's historical alpha consistently exceed its 0.70% ER premium over Edelweiss? Year-by-year.
7. **M5:** Who is the current manager? How long have they been on HSBC Flexi Cap specifically? Any recent manager changes?
8. **M5:** How is the investment philosophy documented? Is there a public investment framework?
9. **M6:** Any history of HSBC Group selling or restructuring its India AMC business?
10. **M6:** Is HSBC AMC profitable as a standalone India entity or does it rely on parent subsidy?

---

*Plan created: 2026-05-21 | Based on: full read of PP, BOI module files (30+ module files) | Framework: 6-module weighted scoring | To study: HSBC Flexi Cap*
