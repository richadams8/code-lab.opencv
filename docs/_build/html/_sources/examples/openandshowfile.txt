Opening and Displaying an Image
================================

Example of how to open and display an image::

  import numpy as np
  import cv2
  from matplotlib import pyplot as plt

  img_bgr = cv2.imread("someimg.jpg")
  # OpenCV reads in image in BGR so we have to convert it to RGB for pyplot
  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  plt.imshow(img_rgb)
  plt.show()
