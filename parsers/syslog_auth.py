from __future__ import annotations

from pathlib import Path
from typing import Dict, List
import pandas as pd
from .base import iter_lines

def parse_syslog_auth(path: str):
    rows: list[dict[str, object]] = []

    for line in iter_lines(path):
        if not line.strip():
            continue
        rows.append(
            {
                "raw_message": line,
                "timestamp": None,
                "host": None,
                "source_ip": None,
                "dest_ip": None,
                "username": None,
                "event_type": None,
            }
        )

        df = pd.DataFrame(rows)

        return df
