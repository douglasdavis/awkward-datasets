from __future__ import annotations

from pathlib import Path

DIR = Path(__file__).parent.resolve()


def line_delimited_records_text() -> str:
    f = DIR / "data" / "simple" / "line_delim_records.json"
    return f.read_text()


def single_record_text() -> str:
    f = DIR / "data" / "simple" / "single_record.json"
    return f.read_text()


def muon_files(n: int | None = None) -> list[str]:
    d = DIR / "data" / "muons"
    files = sorted(map(str, d.iterdir()))
    if n is not None:
        return files[:n]
    return files
