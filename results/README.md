# Result files

## `raw/`
- `seed_level_results.csv` — aggregate test metrics for each scenario × seed × algorithm.
- `daily_results.csv` — per-test-date evaluation metrics used for paired daily analysis.
- `training_results.csv` — requested/completed timesteps and wall-clock training time.
- `rule_based_baseline_results.csv` — deterministic fixed-threshold reference summary.
- `rule_based_baseline_daily.csv` — daily rule-based reference metrics.
- `daily_coverage_audit.csv` — retained interval counts by calendar date.

## `statistics/`
- `multiseed_summary_mean_sd_ci95.csv` — mean, sample SD, and 95% CI across five seeds.
- `paired_daily_wilcoxon.csv` — raw two-sided paired Wilcoxon results across 18 test dates.
- `paired_daily_wilcoxon_holm.csv` — Holm-adjusted p-values used in the manuscript.
- `training_time_summary.csv` — multi-seed training-time summary.
- `statistical_interpretation_for_manuscript.txt` — compact statistical interpretation notes.

## `tables/`
Manuscript-ready baseline, reward-sensitivity, environment-sensitivity, and training-time tables, plus the final post-processing workbook.

## `metadata/`
- `scaler_metadata.json` — metadata from train-only normalization.
