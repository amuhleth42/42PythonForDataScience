import pandas as pd


def load(path: str):
    """
    docstring
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as err:
        print("Error:", err)
