from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "notebooks" / "HVAC_PPO_DQN_JOSCEX_Reproducibility.ipynb",
    ROOT / "results" / "raw" / "seed_level_results.csv",
    ROOT / "results" / "raw" / "daily_results.csv",
    ROOT / "results" / "raw" / "training_results.csv",
    ROOT / "results" / "statistics" / "paired_daily_wilcoxon_holm.csv",
    ROOT / "results" / "tables" / "table_baseline_final_for_manuscript.csv",
]

missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing:
    raise SystemExit("Missing required files:\n- " + "\n- ".join(missing))

with open(required[0], "r", encoding="utf-8") as f:
    nb = json.load(f)
assert nb.get("nbformat") == 4, "Notebook is not a valid nbformat 4 JSON document."

seed = pd.read_csv(ROOT / "results" / "raw" / "seed_level_results.csv")
train = pd.read_csv(ROOT / "results" / "raw" / "training_results.csv")
holm = pd.read_csv(ROOT / "results" / "statistics" / "paired_daily_wilcoxon_holm.csv")

assert len(seed) == 60, f"Expected 60 seed-level results, found {len(seed)}"
assert len(train) == 60, f"Expected 60 training records, found {len(train)}"
assert set(seed["seed"]) == {42, 43, 44, 45, 46}, "Unexpected seed set"
assert seed["scenario"].nunique() == 6, "Expected 6 experimental scenarios"
assert set(seed["algorithm"]) == {"PPO", "DQN"}, "Expected PPO and DQN"
assert (seed["n_test_dates"] == 18).all(), "Expected 18 test dates for every learned policy"
assert (seed["n_test_steps"] == 4893).all(), "Expected 4,893 test steps for every learned policy"

baseline_energy = holm[(holm["scenario"] == "baseline") & (holm["metric"] == "daily_energy_kwh")]
assert len(baseline_energy) == 1
p = float(baseline_energy.iloc[0]["p_value_holm_within_scenario"])
assert abs(p - 3.0517578125e-05) < 1e-12, f"Unexpected baseline Holm p-value: {p}"

print("Repository verification passed.")
print(f"Seed-level runs: {len(seed)}")
print(f"Training records: {len(train)}")
print(f"Scenarios: {seed['scenario'].nunique()}")
print("Seeds:", sorted(seed["seed"].unique().tolist()))
