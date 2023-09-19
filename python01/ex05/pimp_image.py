import numpy as np


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of image received
    """
    return 255 - array


def ft_red(array) -> np.ndarray:
    """
    Isolate the red values of image received
    """
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    return red


def ft_green(array) -> np.ndarray:
    """
    Isolate the green values of image received
    """
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    return green


def ft_blue(array) -> np.ndarray:
    """
    Isolate the blue values of image received
    """
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    return blue


def ft_grey(array) -> np.ndarray:
    """
    Get a grayscale version of the image received, using the Luminance method
    """
    tmp = np.dot(array[..., :3], [0.299, 0.587, 0.114])
    tmp = tmp.astype(np.uint8)
    gray = np.stack((tmp, tmp, tmp), axis=-1)
    return gray
