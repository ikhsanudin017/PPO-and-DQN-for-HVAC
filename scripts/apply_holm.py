from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INFILE = ROOT / "results" / "statistics" / "paired_daily_wilcoxon.csv"
OUTFILE = ROOT / "results" / "statistics" / "paired_daily_wilcoxon_holm_recomputed.csv"


def holm_adjust(p_values):
    """Holm step-down adjusted p-values, preserving NaNs."""
    p = np.asarray(p_values, dtype=float)
    out = np.full(p.shape, np.nan, dtype=float)
    valid = np.where(~np.isnan(p))[0]
    if len(valid) == 0:
        return out

    ordered = valid[np.argsort(p[valid])]
    m = len(ordered)
    running = 0.0
    for rank, idx in enumerate(ordered):
        candidate = (m - rank) * p[idx]
        running = max(running, candidate)
        out[idx] = min(running, 1.0)
    return out


df = pd.read_csv(INFILE)
df = df.rename(columns={"p_value_two_sided": "p_value_raw"})
df["p_value_holm_within_scenario"] = np.nan

for scenario, idx in df.groupby("scenario", sort=False).groups.items():
    idx = list(idx)
    df.loc[idx, "p_value_holm_within_scenario"] = holm_adjust(df.loc[idx, "p_value_raw"].to_numpy())

# Optional global correction across all valid tests, included for transparency.
df["p_value_holm_global_valid_tests"] = holm_adjust(df["p_value_raw"].to_numpy())
df["significant_holm_0_05"] = df["p_value_holm_within_scenario"] < 0.05

df.to_csv(OUTFILE, index=False)
print(f"Wrote: {OUTFILE}")
