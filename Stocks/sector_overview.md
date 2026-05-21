# Sector Overview & Ranking

## Purpose
Rank all 13 macro-sectors by current momentum to decide which sector to study first — same logic as choosing "FlexiCap" as the first mutual fund category.

---

## Sector Selection Methodology

Four signals, all derived from Tickertape CSV data:

| Signal | Weight | Source | Calculation |
|--------|--------|--------|-------------|
| **Relative Return** | 40% | File (6) | Avg 1Y return of stocks in sector minus Nifty 1Y return |
| **Breadth** | 25% | File (10) | % of stocks in sector with Close Price > 200D SMA |
| **Institutional Flow** | 20% | File (4) | Avg (FII 3M change + DII 3M change) across sector |
| **Momentum Rank** | 15% | File (7) | Median Price Momentum Rank (percentile 0–100) of sector |

**Composite Score** = (0.40 x Normalized Relative Return) + (0.25 x Breadth %) + (0.20 x Normalized Inst. Flow) + (0.15 x Median Momentum Rank / 100)

Scores normalized to 0–100 for comparison. Highest composite = study first.

---

## Sector Ranking

> **Status: Pending computation.** Will be populated by running sector-level analysis on the 17 Tickertape CSVs.

| Rank | Sector | Rel. Return | Breadth | Inst. Flow | Mom. Rank | Composite | Status |
|------|--------|-------------|---------|------------|-----------|-----------|--------|
| 1 | — | — | — | — | — | — | Pending |
| 2 | — | — | — | — | — | — | Pending |
| 3 | — | — | — | — | — | — | Pending |
| 4 | — | — | — | — | — | — | Pending |
| 5 | — | — | — | — | — | — | Pending |
| 6 | — | — | — | — | — | — | Pending |
| 7 | — | — | — | — | — | — | Pending |
| 8 | — | — | — | — | — | — | Pending |
| 9 | — | — | — | — | — | — | Pending |
| 10 | — | — | — | — | — | — | Pending |
| 11 | — | — | — | — | — | — | Pending |
| 12 | — | — | — | — | — | — | Pending |
| 13 | — | — | — | — | — | — | Pending |

---

## Sub-Sector to Macro-Sector Mapping

### 1. Banking & Financial Services (692 stocks)

| Sub-Sector | Count |
|------------|-------|
| Investment Banking & Brokerage | 189 |
| Diversified Financials | 166 |
| Specialized Finance | 110 |
| Consumer Finance | 99 |
| Asset Management | 36 |
| Private Banks | 27 |
| Insurance | 15 |
| Home Financing | 13 |
| Public Banks | 12 |
| Stock Exchanges & Ratings | 8 |
| Payment Infrastructure | 6 |

### 2. Information Technology (296 stocks)

| Sub-Sector | Count |
|------------|-------|
| IT Services & Consulting | 175 |
| Software Services | 97 |
| Technology Hardware | 23 |
| Communication & Networking | 17 |
| Data Processing & Outsourced Services | 2 |
| Application Software | 1 |
| IT Services | 1 |

### 3. Pharma & Healthcare (329 stocks)

| Sub-Sector | Count |
|------------|-------|
| Pharmaceuticals | 218 |
| Hospitals & Diagnostic Centres | 61 |
| Health Care Equipment & Supplies | 33 |
| Biotechnology | 17 |
| Labs & Life Sciences Services | 14 |

### 4. Energy (153 stocks)

| Sub-Sector | Count |
|------------|-------|
| Renewable Energy | 36 |
| Renewable Energy Equipment & Services | 25 |
| Oil & Gas — Equipment & Services | 16 |
| Power Generation | 15 |
| Oil & Gas — Storage & Transportation | 14 |
| Gas Distribution | 13 |
| Oil & Gas — Refining & Marketing | 12 |
| Power Infrastructure | 12 |
| Power Transmission & Distribution | 11 |
| Oil & Gas — Exploration & Production | 6 |
| Power Trading & Consultancy | 5 |
| Mining — Coal | 2 |

### 5. Metals & Mining (233 stocks)

| Sub-Sector | Count |
|------------|-------|
| Iron & Steel | 140 |
| Precious Metals, Jewellery & Watches | 88 |
| Metals — Diversified | 33 |
| Gold | 26 |
| Silver | 18 |
| Metals — Aluminium | 18 |
| Mining — Diversified | 16 |
| Metals — Copper | 7 |
| Mining — Manganese | 4 |
| Metals — Coke | 3 |
| Metals — Iron | 3 |
| Metals — Lead | 2 |
| Mining — Iron Ore | 2 |
| Mining — Copper | 1 |
| Steel | 1 |

### 6. FMCG & Consumer Staples (271 stocks)

| Sub-Sector | Count |
|------------|-------|
| Agro Products | 109 |
| Packaged Foods & Meats | 73 |
| FMCG — Foods | 69 |
| Sugar | 35 |
| FMCG — Personal Products | 29 |
| Alcoholic Beverages | 25 |
| Tea & Coffee | 22 |
| Seeds | 12 |
| FMCG — Household Products | 11 |
| FMCG — Tobacco | 7 |
| Soft Drinks | 2 |
| Packaged Foods | 1 |
| Food Distributors | 1 |

### 7. Automobiles (179 stocks)

| Sub-Sector | Count |
|------------|-------|
| Auto Parts | 126 |
| Agricultural & Farm Machinery | 20 |
| Two Wheelers | 12 |
| Four Wheelers | 9 |
| Trucks & Buses | 5 |
| Tractors | 3 |
| Three Wheelers | 3 |
| Cycles | 3 |

### 8. Capital Goods & Defense (400 stocks)

| Sub-Sector | Count |
|------------|-------|
| Industrial Machinery | 195 |
| Electrical Components & Equipments | 82 |
| Electronic Equipments | 52 |
| Cables | 31 |
| Heavy Electrical Equipments | 29 |
| Aerospace & Defense Equipments | 17 |
| Batteries | 11 |
| Heavy Machinery | 9 |

### 9. Chemicals (354 stocks)

| Sub-Sector | Count |
|------------|-------|
| Specialty Chemicals | 143 |
| Commodity Chemicals | 131 |
| Plastic Products | 63 |
| Fertilizers & Agro Chemicals | 58 |
| Diversified Chemicals | 22 |

### 10. Infrastructure & Real Estate (574 stocks)

| Sub-Sector | Count |
|------------|-------|
| Real Estate | 228 |
| Construction & Engineering | 209 |
| Logistics | 107 |
| Roads | 21 |
| Rail | 10 |
| Shipbuilding | 9 |
| Ports | 4 |
| Dredging | 3 |
| Airports | 2 |

### 11. Consumer Discretionary (373 stocks)

| Sub-Sector | Count |
|------------|-------|
| Apparel & Accessories | 77 |
| Hotels, Resorts & Cruise Lines | 69 |
| Home Electronics & Appliances | 33 |
| Retail — Speciality | 24 |
| Tour & Travel Services | 20 |
| Home Furnishing | 16 |
| Restaurants & Cafes | 16 |
| Retail — Apparel | 15 |
| Footwear | 14 |
| Retail — Online | 12 |
| Housewares | 11 |
| Retail — Department Stores | 9 |
| Stationery | 9 |
| Wellness Services | 8 |
| Theme Parks & Gaming | 6 |
| Theatres | 2 |

### 12. Cement & Building Materials (197 stocks)

| Sub-Sector | Count |
|------------|-------|
| Cement | 44 |
| Building Products — Others | 43 |
| Building Products — Pipes | 40 |
| Building Products — Ceramics | 18 |
| Building Products — Granite | 17 |
| Wood Products | 17 |
| Building Products — Laminates | 10 |
| Building Products — Glass | 10 |
| Building Products — Prefab Structures | 6 |
| Paints | 6 |

### 13. Telecom & Media (128 stocks)

| Sub-Sector | Count |
|------------|-------|
| Movies & TV Serials | 44 |
| Advertising | 39 |
| Online Services | 27 |
| Publishing | 17 |
| Telecom Services | 14 |
| Animation | 12 |
| Telecom Equipments | 11 |
| TV Channels & Broadcasters | 10 |
| Cable & D2H | 8 |
| Telecom Infrastructure | 6 |
| Radio | 4 |

---

## Unmapped Sub-Sectors

Stocks in these sub-sectors are **not assigned to any macro-sector** and are excluded from sector-level study. They may be reviewed individually if they appear in broad market screens.

| Sub-Sector | Count | Reason |
|------------|-------|--------|
| Textiles | 312 | Cross-cutting (spans FMCG, discretionary, industrial) — review separately |
| Packaging | 81 | Cross-cutting (serves multiple sectors) |
| Business Support Services | 79 | Too generic — review individually |
| Commodities Trading | 99 | Trading firms, not operating businesses |
| Paper Products | 57 | Niche / declining sector |
| Education Services | 47 | Niche |
| Conglomerates | 26 | Multi-sector by definition |
| Environmental Services | 12 |Niche |
| Employment Services | 13 | Niche |
| Tires & Rubber | 22 | Small — could merge into Automobiles later |
| Water Management | 10 | Niche |
| Outsourced Services | 15 | Overlaps with IT/BPO |
| Academic & Educational Services | 3 | Too small |
| Debt / Equity (fund types) | 287 | Not operating companies |
| Commodity | 2 | Ambiguous |

**Total unmapped:** ~1,125 stocks. Remaining **~4,573 stocks** are mapped to the 13 sectors.

---

*Sector counts based on Tickertape export of May 21, 2026 (5,698 stocks, 153 sub-sectors)*
