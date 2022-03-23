from __future__ import annotations

from pathlib import Path

DIR = Path(__file__).resolve()


def line_delimited_records() -> str:
    f = DIR / "data" / "line_delim_records.json"
    return f.read_text()


def single_record() -> str:
    f = DIR / "data" / "single_record.json"
    return f.read_text()


def muons() -> Path:
    pass
