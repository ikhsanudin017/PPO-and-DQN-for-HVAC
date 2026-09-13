# Push to GitHub

After creating an empty GitHub repository, open a terminal in this folder and run:

```bash
git init
git add .
git commit -m "Initial reproducibility release for the JOSCEX study"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the repository URL with your own GitHub repository URL.

## Before pushing

Recommended quick check:

```bash
python scripts/verify_repository.py
```

The raw `sensor_data.csv` is intentionally excluded by `.gitignore`.

If you later add many model checkpoint `.zip` files and the repository becomes large, use Git LFS or attach the checkpoints to a GitHub Release.
