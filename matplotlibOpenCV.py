import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()

""" Matplotlib graph using the pixel locations as coordinates, 
here. Should you wish to draw on your images, however, Matplotlib is not required. 
OpenCV provides great methods for this. When you are done making modifications, 
you can save, like so:"""