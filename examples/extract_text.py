__author__ = 'Rich Adams'

import numpy as np
import cv2
from matplotlib import pyplot as plt

img_bgr = cv2.imread("../samples/polycom_simple.jpg")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

f, (top, bottom) = plt.subplots(2, 1, True)

top.imshow(img_bgr, aspect='auto')
bottom.imshow(img_rgb, aspect='auto')

plt.tight_layout()

plt.show()
