# Data Analysis with Pandas and Python

<div align="center">

[![Notebooks](https://img.shields.io/badge/CI-notebooks-green)](https://github.com/sivabalanb/Data-Analysis-with-Pandas-and-Python/actions)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2%2B-orange)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

**A practical, hands-on introduction to data analysis with Pandas — every
notebook runs, every notebook explains itself, and every dataset is included.**

[Run instantly on Colab](#run-instantly) · [View notebooks](#notebooks) · [Install](#installation)

</div>

> Like this repo? ⭐ **Star it** so others can find it, and **fork it** to work
> through the exercises yourself. Contributions are welcome — see
> [Contributing](#contributing).

## Why this repository

- **Learn by doing.** Every topic maps to a runnable notebook — execute it
  locally, on [Colab](#run-instantly), or on [Kaggle](https://www.kaggle.com/).
- **Modern Pandas.** Code targets current Pandas (2.x/3.x). Deprecated APIs
  (`squeeze`, `sheetname`, `pandas.Panel`) are deliberately avoided, and
  every notebook is verified by CI on every push.
- **Explained, not just code.** Each notebook contains narrative explanations,
  not bare code cells — the *why* matters as much as the *how*.
- **Reproducible.** Data files ship with the notebooks, `requirements.txt`
  pins the dependencies, and a CI test runner executes every notebook.
- **Real projects.** Includes an end-to-end analysis project on a real public
  dataset, not just toy examples.

## Run instantly

Zero setup. Click a notebook and it opens in your browser:

| | Open in Colab | Open in Binder |
|---|---|---|
| 01 Series | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/01_series.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=01_series.ipynb) |
| 02 DataFrames 1 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/02_dataframes_1.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=02_dataframes_1.ipynb) |
| 03 DataFrames 2 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/03_dataframes_2.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=03_dataframes_2.ipynb) |
| 04 DataFrames 3 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/04_dataframes_3.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=04_dataframes_3.ipynb) |
| 05 Merge & Join | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/05_merge_join_concat.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=05_merge_join_concat.ipynb) |
| 06 GroupBy | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/06_groupby.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=06_groupby.ipynb) |
| 07 MultiIndex | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/07_multindex.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=07_multindex.ipynb) |
| 08 Date & Time | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/08_date_time.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=08_date_time.ipynb) |
| 09 Text Data | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/09_text_data.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=09_text_data.ipynb) |
| 10 Visualization | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/10_visualization.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=10_visualization.ipynb) |
| 11 Input & Output | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/11_input_output.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=11_input_output.ipynb) |
| 12 Read CSV | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/12_read_csv.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=12_read_csv.ipynb) |
| 13 Options | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/13_options_settings.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=13_options_settings.ipynb) |
| 14 Project | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sivabalanb/Data-Analysis-with-Pandas-and-Python/blob/master/14_project_chicago_salaries.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sivabalanb/Data-Analysis-with-Pandas-and-Python/HEAD?labpath=14_project_chicago_salaries.ipynb) |

## Table of contents

1. [Installation](#installation)
2. [Get started](#get-started)
3. [Notebooks](#notebooks)
4. [Contributing](#contributing)
5. [Contributors](#contributors)
6. [License](#license)

## Installation

You need **Python 3.10+**.

We recommend a virtual environment to keep dependencies isolated:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

This installs Pandas, NumPy, Matplotlib, Seaborn, Plotly, and openpyxl.

## Get started

Launch Jupyter from the repository root:

```bash
jupyter lab
```

Then open the notebooks in the order listed below. The
[`00_introduction.ipynb`](./00_introduction.ipynb) notebook explains how to
navigate the repository and how the notebooks are organized.

## Notebooks

Core path (follow in order):

| # | Notebook | Topic |
|---|----------|-------|
| 1 | `01_series.ipynb` | The Series type — creation, attributes, methods |
| 2 | `02_dataframes_1.ipynb` | DataFrames: structure, selection, dtypes |
| 3 | `03_dataframes_2.ipynb` | DataFrames: sorting, ranking, filtering |
| 4 | `04_dataframes_3.ipynb` | `loc`/`iloc` indexing, missing data |
| 5 | `05_merge_join_concat.ipynb` | Combining datasets |
| 6 | `06_groupby.ipynb` | Split-apply-combine, aggregation |
| 7 | `07_multindex.ipynb` | MultiIndex, pivot, unstack |
| 8 | `08_date_time.ipynb` | Working with dates and times |
| 9 | `09_text_data.ipynb` | String methods and cleaning |
| 10 | `10_visualization.ipynb` | Plotting with Matplotlib |
| 11 | `11_input_output.ipynb` | Reading/writing CSV and Excel |
| 12 | `12_read_csv.ipynb` | Reading CSVs in detail |
| 13 | `13_options_settings.ipynb` | Display and global options |
| 14 | `14_project_chicago_salaries.ipynb` | End-to-end analysis project (real public data) |

## Contributing

Improvements, bug fixes, and extra exercises are welcome. Please read
[CONTRIBUTING.md](./CONTRIBUTING.md) first — it covers setup, keeping git diffs
clean (recommended `nbstripout`), and the PR checklist.

Short version:

1. Fork the repository.
2. Make your change and keep code on modern Pandas APIs.
3. Clear notebook outputs before committing.
4. Verify with `python scripts/test_notebooks.py`.
5. Open a pull request using the [PR template](./.github/pull_request_template.md).

Please also read [NOTICE.md](./NOTICE.md) — it explains which material is
covered by the repository license.

## Contributors

Thanks to everyone who has helped improve this repository.

<!--
To add yourself: open a pull request that appends your GitHub handle below,
keeping the list alphabetical. That's it — no scripts, no maintainer approval
beyond a normal review.
-->
- [sivabalanb](https://github.com/sivabalanb) — author & maintainer

## License

Original code in this repository is released under the
[MIT License](./LICENSE). Examples and datasets derived from third-party
sources are not covered by that license — see
[NOTICE.md](./NOTICE.md) for details.