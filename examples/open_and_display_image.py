__author__ = 'Rich Adams'

import numpy as np
import cv2
from matplotlib import pyplot as plt

img_bgr = cv2.imread("../samples/polycom_simple.jpg")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis('off')
plt.show()
