from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
import matplotlib.pyplot as plt


array = ft_load("landscape.jpg")
invert = ft_invert(array)
red = ft_red(array)
green = ft_green(array)
blue = ft_blue(array)
grey = ft_grey(array)
print(ft_invert.__doc__)

fig, axes = plt.subplots(3, 2)

axes[0, 0].imshow(array)
axes[0, 1].imshow(invert)
axes[1, 0].imshow(red)
axes[1, 1].imshow(green)
axes[2, 0].imshow(blue)
axes[2, 1].imshow(grey)

axes[0, 0].set_title('Original')
axes[0, 1].set_title('Invert')
axes[1, 0].set_title('Red')
axes[1, 1].set_title('Green')
axes[2, 0].set_title('Blue')
axes[2, 1].set_title('Gray')
plt.show()
