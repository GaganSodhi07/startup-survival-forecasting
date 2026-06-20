# Startup Survival & Funding Forecasting (Germany)

Supporting analysis notebook for the master's thesis *"Development of an
Integrated Financial Risk, Liquidity, and Survival Forecasting Model for
Early-Stage Startups in Germany: A Sector-Specific Approach Using Monte Carlo
Simulation and Predictive Analytics."*

HTW Berlin, MBA & Engineering — Gagan Deep Sodhi · Supervisor: Prof. Dr.
Thomas Rachfall

## What this is

Reproducible code for the analytical figures used in the thesis proposal,
covering three German startup sectors (SaaS, AI, FinTech):

- **Stage 1 — Kaplan-Meier survival estimation**: sector-specific hazard
  rates and survival curves (tests H1)
- **Stage 2 — Monte Carlo simulation**: 24-month funding requirement
  distributions, parameterised by the Stage 1 hazard rates rather than
  generic distributional assumptions (tests H3)
- **K-Means clustering**: data-driven sector segmentation by seed round
  size and burn rate, validated against manual sector labels
- **OLS regression**: German-calibrated model vs. generic European
  benchmark, R² comparison (tests H2)
- **Random Forest**: permutation feature importance for 24-month survival,
  corroborating sector as the primary driver (H1)

All datasets are **synthetic**, generated with `numpy.random.seed(42)` to
stand in for the Crunchbase/Dealroom-calibrated data used in the full
thesis pipeline — the code structure and statistical approach are real,
the numbers are illustrative.

## Repository structure

```
.
├── StartupSurvival.ipynb       # main notebook — all 4 figures
├── generate_data.py            # regenerates data/*.csv
├── data/
│   ├── survival_curves.csv
│   └── monte_carlo_samples.csv
├── outputs/                    # generated figures (PNG)
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone <this-repo-url>
cd startup-survival-forecasting
pip install -r requirements.txt
python generate_data.py
jupyter notebook StartupSurvival.ipynb
```

Or open directly in Google Colab and run `generate_data.py` as the first
cell if the `data/` folder isn't present.

## Figures

**Fig 3.2 — KM Survival Curves + Monte Carlo Funding Distributions**
![Fig 3.2](outputs/fig_32_outputs.png)

**Fig A.5 — K-Means Cluster Analysis**
![Fig A.5](outputs/fig_a5_kmeans.png)

**Fig A.6 — OLS Regression Validation**
![Fig A.6](outputs/fig_a6_ols.png)

**Fig A.7 — Random Forest Feature Importance**
![Fig A.7](outputs/fig_a7_rf.png)

## Data sources (full thesis pipeline)

Stepstone Gehaltsreport 2026 · JLL Berlin Office Q1 2026 · Crunchbase ·
Dealroom · Destatis · KfW · German Startup Monitor · Bundesministerium der
Finanzen

## Author

Gagan Deep Sodhi — HTW Berlin MBA & Engineering
