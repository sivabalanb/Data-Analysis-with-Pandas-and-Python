"""Execute every notebook in the repository to verify it runs.

Exits non-zero if any notebook fails, so it can be used as a CI gate.
Run locally with:  python scripts/test_notebooks.py
"""

from __future__ import annotations

import glob
import sys

import nbformat
from nbclient import NotebookClient

REQUIRED_CELL_TYPES = ("code", "markdown")


def main() -> int:
    notebooks = sorted(glob.glob("*.ipynb"))
    if not notebooks:
        print("No notebooks found.")
        return 1

    failures: list[str] = []
    for path in notebooks:
        nb = nbformat.read(path, as_version=4)
        for cell in nb["cells"]:
            if cell["cell_type"] not in REQUIRED_CELL_TYPES:
                failures.append(f"{path}: unexpected cell type {cell['cell_type']!r}")

        try:
            client = NotebookClient(
                nb, timeout=120, kernel_name="python3",
                resources={"metadata": {"path": "."}},
            )
            client.execute()
        except Exception as exc:  # noqa: BLE001 - surface any failure to CI
            failures.append(f"{path}: {str(exc).splitlines()[0]}")
        else:
            print(f"OK   {path}")

    print(f"\nPASS: {len(notebooks) - len(failures)}/{len(notebooks)}")
    for failure in failures:
        print("FAIL", failure)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())