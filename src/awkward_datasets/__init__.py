from awkward_datasets._version import version
from awkward_datasets.json import (
    line_delimited_records,
    line_delimited_records_text,
    single_record,
    single_record_text,
    muon_files,
)

__version__ = version

__all__ = (
    "line_delimited_records",
    "line_delimited_records_text",
    "single_record",
    "single_record_text",
    "muon_files",
)
