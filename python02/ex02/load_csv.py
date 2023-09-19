import pandas as pd
import os


def load(path: str) -> pd.core.frame.DataFrame:
    """
    docstring
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as err:
        print("Error:", err)
