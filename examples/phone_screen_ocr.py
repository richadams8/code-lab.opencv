import os
import numpy as np
import scipy
import cv2
from matplotlib import pyplot as plt

#Set up a figure to display stuff
f, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, subplot_kw=dict(xticks=[], yticks=[]))
plt.tight_layout()

# Read in image
imageFile = "../samples/polycom_simple.jpg"
img_bgr = cv2.imread(imageFile)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
ax1.imshow(img_rgb, aspect='auto')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
ax2.imshow(img_gray, cmap='gray', aspect='auto')

# Smooth image
img_smoothed = cv2.bilateralFilter(img_gray, 10, 30, 10)
ax3.imshow(img_smoothed, cmap='gray', aspect='auto')

# Threshold image
img_thresh = np.empty_like(img_smoothed)
cv2.inRange(img_smoothed, 70, 200, img_thresh)
ax4.imshow(img_thresh, cmap='gray', aspect='auto')

# Extract bounding box for screen
(contours, _) = cv2.findContours(img_thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
screenContour = sorted(contours, key=cv2.contourArea, reverse=True)[0]
img_contour = img_rgb.copy()
x, y, w, h = cv2.boundingRect(screenContour)
screenRect = ((x, y), (x+w, y+h))
cv2.drawContours(img_contour, screenContour, 0, (0, 0, 255), thickness=1)
ax5.imshow(img_contour, aspect='auto')
cv2.rectangle(img_contour, (x, y), (x+w, y+h), (0, 255, 0), thickness=3)
ax5.imshow(img_contour, aspect='auto')

# Write out screen image
img_screen = img_thresh[y:y+h, x:x+w]
img_small = cv2.resize(img_screen, (0,0), fx=0.5, fy=0.5)
ax6.imshow(img_small, cmap='gray')
splitpath = os.path.splitext(imageFile)
writeto = splitpath[0] + "_screen" + splitpath[1]
cv2.imwrite(writeto, img_small)

# Use Tesseract to read the screen image
textoutput = splitpath[0]
command = " ".join(["tesseract", writeto, textoutput])
os.system(command)


plt.show()
