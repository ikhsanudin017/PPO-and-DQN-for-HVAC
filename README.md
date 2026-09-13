# HVAC PPO vs DQN — JOSCEX Reproducibility Repository

Reproducibility materials for the manuscript:

**Comparative Analysis of Proximal Policy Optimization and Deep Q-Network for HVAC Energy–Comfort Control Using IoT Data**

Authors: **Ikhsanudin, Kusnawi**  
Affiliation: Informatics, Universitas Amikom Yogyakarta, Indonesia

## Scope

This repository contains the final revised Stable-Baselines3/Gymnasium experiment used to compare PPO and DQN under a common HVAC energy–comfort simulation informed by IoT sensor data.

The study is a **simulation comparison**, not a field measurement of HVAC energy savings. The electrical current and power sensors were installed on the household electrical supply rather than a dedicated HVAC circuit. The environment therefore uses an action-dependent simulated-power proxy for controller comparison.

## Final experiment design

- Algorithms: PPO and DQN (Stable-Baselines3)
- Environment: custom Gymnasium environment
- State: 6 normalized components
- Actions: 5 discrete HVAC operating levels
- Target temperature: 24 °C
- Comfort band: 22–26 °C
- Nominal training budget: 500,000 timesteps per run
- Seeds: `42, 43, 44, 45, 46`
- Scenarios: 6
  - baseline
  - reward sensitivity: `alpha = 0.5`
  - reward sensitivity: `beta = 1.0`
  - reward sensitivity: `comfort bonus = 0.0`
  - environment response ×0.8
  - environment response ×1.2
- Total learned models: 60
- Test set: 18 chronological test dates, 4,893 five-minute intervals

## Repository structure

```text
HVAC-PPO-DQN-JOSCEX/
├── README.md
├── requirements.txt
├── .gitignore
├── .gitattributes
├── CITATION.cff
├── notebooks/
│   └── HVAC_PPO_DQN_JOSCEX_Reproducibility.ipynb
├── data/
│   └── README.md
├── models/
│   └── README.md
├── figures/
│   └── Figure3_baseline_energy_comfort_multiseed.png
├── results/
│   ├── README.md
│   ├── raw/
│   ├── statistics/
│   ├── tables/
│   └── metadata/
└── scripts/
    ├── apply_holm.py
    └── verify_repository.py
```

## Installation

Create a Python environment and install the dependencies:

```bash
pip install -r requirements.txt
```

The final notebook also contains its original dependency-installation cell.

## Dataset

The raw `sensor_data.csv` is not committed to Git. Place it at the repository root before running the notebook:

```text
HVAC-PPO-DQN-JOSCEX/
├── sensor_data.csv
└── notebooks/
```

When running the notebook from the `notebooks/` directory, either set the working directory to the repository root or update `DATA_PATH` to point to `../sensor_data.csv`.

Dataset details are documented in [`data/README.md`](data/README.md).

## Running the final experiment

Open:

```text
notebooks/HVAC_PPO_DQN_JOSCEX_Reproducibility.ipynb
```

For the full experiment, the executed notebook uses:

```python
RUN_SMOKE_TEST = False
RUN_FULL_EXPERIMENTS = True
RESUME_IF_AVAILABLE = True
```

The notebook is resumable and stores completed run summaries so interrupted runs do not need to restart from zero.

> Important: the final reported results already exist under `results/`. Re-running all 60 learned models can take many hours depending on hardware.

## Statistical analysis

For each algorithm and scenario, aggregate metrics were summarized across five seeds using mean, sample standard deviation, and a two-sided 95% confidence interval.

For the primary paired comparison, daily metrics were first averaged across the five seeds for each algorithm and each of the 18 test dates. PPO and DQN were then compared using two-sided Wilcoxon signed-rank tests. Four daily outcomes were tested within each scenario:

1. simulated energy,
2. mean comfort deviation,
3. comfort rate,
4. daily episode return.

Holm's step-down correction was applied across these four tests within each scenario. The final adjusted values are stored in:

```text
results/statistics/paired_daily_wilcoxon_holm.csv
```

The correction can be regenerated from the raw Wilcoxon output with:

```bash
python scripts/apply_holm.py
```

## Baseline result summary

Across five baseline training seeds:

| Metric | PPO | DQN |
|---|---:|---:|
| Simulated energy (kWh) | 18.995 ± 0.320 | 19.505 ± 0.116 |
| Comfort deviation (°C) | 0.239 ± 0.072 | 0.246 ± 0.069 |
| Comfort rate (%) | 98.655 ± 0.905 | 99.060 ± 0.000 |
| Mean daily episode return | −109.556 ± 20.231 | −113.746 ± 18.996 |

After Holm correction, the baseline PPO–DQN difference was statistically significant only for simulated energy (`adjusted p = 3.05e-05`).

## Reproducibility notes

- The chronological split is retained.
- The MinMax scaler is fitted on training dates only and then reused for testing.
- PPO completes 501,760 environment steps because Stable-Baselines3 completes the final 2,048-step rollout; DQN completes the requested 500,000 timesteps.
- The rule-based thermostat is treated as a deterministic fixed-threshold operational reference, not as an objective-aligned RL competitor.
- Reward values should not be compared numerically across different reward formulations because changing reward coefficients changes the reward scale.
- Environment ±20% sensitivity is a local simulator robustness probe, not physical calibration.

## Check repository contents

Run:

```bash
python scripts/verify_repository.py
```

## Model checkpoints

The final notebook saves checkpoints to `outputs/models/`. Checkpoint files are not duplicated in this bundle. If they are available and you want to publish them, place them under `models/` or attach them to a GitHub Release.

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). No DOI is claimed because the manuscript is still under revision/publication processing.
