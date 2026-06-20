"""
generate_data.py
Regenerates the synthetic datasets used by StartupSurvival.ipynb.

Run this once before opening the notebook:
    python generate_data.py

Produces:
    data/survival_curves.csv       — Kaplan-Meier hazard/survival data by sector
    data/monte_carlo_samples.csv   — Monte Carlo funding-requirement samples by sector

Both are illustrative synthetic datasets (seed=42) standing in for the
Crunchbase-calibrated data used in the full thesis pipeline.
"""

import numpy as np
import pandas as pd
import os

np.random.seed(42)

os.makedirs("data", exist_ok=True)

# ── Dataset 1: survival_curves.csv ──────────────────────────────
# Sector hazard rates (monthly), Kaplan-Meier style exponential survival
t = np.arange(0, 37)
hazard_rates = {"SaaS": 0.026, "AI": 0.042, "FinTech": 0.034}

km_rows = []
for sector, lam in hazard_rates.items():
    for month in t:
        km_rows.append({
            "sector": sector,
            "month": month,
            "hazard_rate": round(lam, 4),
            "survival_probability": round(np.exp(-lam * month) * 100, 2),
        })

df_km = pd.DataFrame(km_rows)
df_km.to_csv("data/survival_curves.csv", index=False)
print(f"survival_curves.csv: {len(df_km)} rows")

# ── Dataset 2: monte_carlo_samples.csv ──────────────────────────
# 24-month funding requirement, log-normal by sector, 3,000 draws each
mc_params = {"SaaS": (12.0, 0.22), "AI": (12.7, 0.25), "FinTech": (12.3, 0.23)}

mc_rows = []
for sector, (mu, sig) in mc_params.items():
    samples = np.exp(np.random.normal(mu, sig, 3000)) / 1000  # EUR thousands
    for s in samples:
        mc_rows.append({"sector": sector, "funding_required_eur_k": round(s, 1)})

df_mc = pd.DataFrame(mc_rows)
df_mc.to_csv("data/monte_carlo_samples.csv", index=False)
print(f"monte_carlo_samples.csv: {len(df_mc)} rows")

print("\nDone. Both CSVs written to data/")
