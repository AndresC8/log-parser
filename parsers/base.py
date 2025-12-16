from pathlib import Path
from typing import Iterable, List

def read_lines(path: str):
    p = Path(path)
    with p.open("r", encoding="utf-8", errors="ignore") as f:
        return [line.rstrip("\n") for line in f]
    
def iter_lines(path: str):
    p = Path(path)

    with p.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            yield line.rstrip("\n")