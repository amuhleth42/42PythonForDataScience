import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    docstring
    """
    try:
        pairs = np.stack((height, weight), axis=1)
        res = [x[1] / (x[0] ** 2) for x in pairs]
        return res
    except Exception as err:
        print("Error:", err)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    docstring
    """
    try:
        arr = np.array(bmi)
        res = [x > limit for x in arr]
        return res
    except Exception as err:
        print("Error:", err)
