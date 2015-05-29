import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read in image
img_bgr = cv2.imread("../samples/polycom_simple.jpg")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Smooth image
img_smoothed = cv2.bilateralFilter(img_gray, 10, 30, 10)

# Threshold image
img_thresh = np.empty_like(img_smoothed)
cv2.inRange(img_smoothed, 90, 200, img_thresh)

# Extract bounding box for screen
(contours, _) = cv2.findContours(img_thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
screenContour = sorted(contours, key=cv2.contourArea, reverse=True)[0]
img_contour = img_rgb.copy()
x, y, w, h = cv2.boundingRect(screenContour)
screenRect = ((x, y), (x+w, y+h))
cv2.rectangle(img_contour, screenRect[0], screenRect[1], (0, 0, 255), thickness=3)
