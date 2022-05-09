from __future__ import annotations

from pathlib import Path

DIR = Path(__file__).parent.resolve()


def muons(n: int | None = None) -> list[str]:
    d = DIR / "data" / "parquet"
    files = sorted(map(str, d.iterdir()))
    if n is not None:
        return files[:n]
    return files
