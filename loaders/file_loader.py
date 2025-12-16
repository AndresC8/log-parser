import os
import pandas as pd
from loaders.paths import RAW_DIR

def load_logs(filename: str):
    path = os.path.join(RAW_DIR, filename)
    
    print(f"Loading: {path}")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Doesnt exists: {path}")
    
    df = pd.read_csv(path)

    return df
