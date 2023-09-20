import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    docstring
    """
    try:
        arr = np.array(family, dtype='f')
        print(f"My shape is : {arr.shape}")
        res = arr[start:end]
        print(f"My new shape is : {res.shape}")
        return res

    except Exception as err:
        print("Error:", err)
