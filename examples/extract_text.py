__author__ = 'Rich Adams'

import numpy as np
import cv2
from matplotlib import pyplot as plt

img_bgr = cv2.imread("../samples/polycom_simple.jpg")
plt.imshow(img_bgr)
plt.show()

print "hello world"