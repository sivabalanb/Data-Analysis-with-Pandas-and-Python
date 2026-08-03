---
name: Notebook changes
about: Changes or additions to notebooks
title: ""
labels: ""
assignees: ""
---

## What does this PR do?

<!-- One or two sentences. If fixing a bug, link the issue. -->

## Checklist

- [ ] I ran **Kernel → Restart & Run All** on every notebook I changed and they
      complete without errors.
- [ ] I cleared notebook outputs before committing
      (`Edit → Clear All Outputs`, or `nbstripout` if configured).
- [ ] I only used modern Pandas APIs (no `squeeze`, `sheetname`,
      `DataFrame.append`, `pandas.Panel`).
- [ ] My code avoids chained assignment; I used `df.loc[mask, "col"] = ...`.
- [ ] I added or updated a markdown cell explaining *why* the code does what it
      does.
- [ ] `python scripts/test_notebooks.py` passes for all notebooks.
- [ ] If I added/renamed a notebook, I updated the README notebook table.
- [ ] I read [NOTICE.md](./NOTICE.md) and the material I added is not
      third-party course content.

## Related issues

<!-- Closes #123, addresses #456, or N/A. -->
