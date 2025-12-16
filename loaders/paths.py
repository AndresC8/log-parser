import os
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"

if __name__ == "__main__":
    # print("BASE_DIR:    ", BASE_DIR)
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("DATA_DIR:    ", DATA_DIR)
    print("RAW_DIR:     ", RAW_DIR)