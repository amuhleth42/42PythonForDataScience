import numpy as np
import os
from PIL import Image


def ft_load(path: str):
    """
    docstring
    """
    try:
        s = path.lower()
        assert (
            s.endswith("jpg") or s.endswith("jpeg")
        ), "File format not supported"
        assert os.path.exists(path), "Path not found"
        print(path)
        img = Image.open(path)
        arr = np.array(img)
        print(f"The shape of image is: {arr.shape}")
        return arr

    except Exception as err:
        print("Error:", err)
