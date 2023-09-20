from load_image import ft_load
from PIL import Image
import numpy as np


def zoom(img):
    """
    docstring
    """
    (x, y, z) = img.shape
    xoff = int((x - 400) / 2)
    yoff = int((y - 400) / 2)
    new_img = img[xoff:(x - xoff), yoff:(y - yoff), 0:3]

    gray_img = np.dot(new_img[..., :3], [0.299, 0.587, 0.114])
    gray_img = gray_img.astype(np.uint8)
    return gray_img


def rotate(img):
    res = np.transpose(img)
    print(f"New shape after Transpose: {res.shape}")
    print(res)
    Image.fromarray(res).save("transposed_animal.jpeg")


def main():
    img = ft_load("animal.jpeg")
    print(img)
    (x, y, z) = img.shape
    if x < 400 or y < 400 or z != 3:
        print("Error: img too small or corrupted")
        return

    zoomed_img = zoom(img)
    rotate(zoomed_img)


if __name__ == "__main__":
    main()
