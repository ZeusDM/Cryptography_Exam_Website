# Cryptography Exam Website Engine

The static site generator and web frontend for the **UW Cryptography Comprehensive Exam Archive**.

This engine is decoupled from the content vault: it pulls raw LaTeX problems and solutions from [ZeusDM/Cryptography_Exam](https://github.com/ZeusDM/Cryptography_Exam), parses them with Pandoc and MathJax 3, and builds a publication-grade static site using Hugo.

## Local Development

To run the live dev server with hot-reloading:

```bash
# Point to your local Cryptography_Exam directory (or problems/ folder):
python3 scripts/dev.py --math-dir ../Cryptography_Exam
```

Open `http://localhost:1313` in your browser. Any edits made to `.tex` files in `Cryptography_Exam` will trigger an instant rebuild and live-reload the browser.

## Deployment

The site is built and published to **GitHub Pages** via the GitHub Actions workflow in `.github/workflows/deploy.yml`.

It deploys automatically:
- When changes are pushed to `main` on this repository.
- Daily via cron at 04:00 UTC to sync with updates in `Cryptography_Exam`.
- On demand via the **Run workflow** button in the GitHub Actions tab.
