# Trained model checkpoints

The final notebook is configured to save Stable-Baselines3 model checkpoints under:

```text
outputs/models/
```

This Git-ready bundle does not include model checkpoint files because they were not present in the local export used to assemble the bundle.

If checkpoint `.zip` files are available, they can be copied into this directory before publication. For a large collection, GitHub Releases or Git LFS is preferable to normal Git history.

The repository remains reproducible without checkpoints because the full training pipeline, random seeds, hyperparameters, and machine-readable outputs are included.
