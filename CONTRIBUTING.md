# Contributing to Data Analysis with Pandas and Python

Thanks for considering a contribution! This project is a learning resource, so
the best contributions are ones that help other learners.

## Types of contributions that help most

- **Fixing a bug** in a notebook (a cell that errors, a deprecation warning).
- **Clarifying an explanation** — a markdown cell that confuses you will
  confuse others.
- **New exercises** — short "try it yourself" challenges with solutions.
- **New datasets** with clear provenance (public/open data only).
- **New notebooks** — please open an issue first to discuss scope.

## Quick start

1. Fork the repository.
2. Create a feature branch: `git checkout -b fix/your-change`.
3. Make your change. Keep code on **modern Pandas APIs** — avoid deprecated
   methods (`squeeze`, `sheetname`, `DataFrame.append`, `pandas.Panel`).
4. Verify every notebook still runs:
   ```bash
   pip install -r requirements.txt nbclient nbformat ipykernel
   python scripts/test_notebooks.py
   ```
   All notebooks must show `OK` before you open a PR.
5. Clear notebook outputs before committing (see below).
6. Commit with a clear message and open a pull request using the
   [PR template](./.github/pull_request_template.md).

## Keeping git diffs clean (recommended: `nbstripout`)

Notebooks store their rendered outputs in JSON, which makes diffs noisy. This
repository deliberately does **not** force a git filter via `.gitattributes` —
doing so would break `git commit` for contributors who don't have the filter
installed. Instead, we recommend that *you* install `nbstripout` locally:

```bash
pip install nbstripout
nbstripout --install
```

`nbstripout --install` sets up a per-repo git filter that automatically clears
notebook outputs when you commit. If you'd rather not install it, just run
**Kernel → Restart & Run All** to confirm your changes work, then
**Edit → Clear All Outputs** before committing.

> Without this step your notebook changes will still be accepted, but please
> keep the diff readable by not committing large rendered outputs.

## Code style

- Add a markdown cell explaining *why* a code cell does what it does.
- Prefer `df["col"]` over `df.col`.
- Use `df.loc[mask, "col"] = ...` to modify filtered rows (never chained
  assignment).
- Update the README notebook table if you add or rename a notebook.

## Licensing note

Before contributing, please read [NOTICE.md](./NOTICE.md). Original code is
MIT-licensed; material derived from third-party courses or datasets is **not**
covered by that license, so don't add it without the rights to do so.

## Reporting issues

- Include the notebook name and the exact cell that fails.
- Paste the full error traceback and your `pandas.__version__`.
- Check existing issues first to avoid duplicates.

## Recognition

Every accepted contributor is added to the Contributors section in the README
(follow the instructions in that section).