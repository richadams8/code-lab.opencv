__author__ = 'Rich Adams'

import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

class phoneReaderLab:

  def __init__(self, imageLocation):
    # Blur Parameters
    self.smoothSize = 10
    self.sigmaColor = 30
    self.sigmaSpace = 10

    # Canny Parameters
    self.cannyMin = 50
    self.cannyMax = 100

    # Images
    self.img_bgr = None
    self.img_rgb = None
    self.img_gray = None
    self.img_smoothed = None
    self.img_edge = None
    self.img_contour = None

    # Features
    self.contours = None
    self.screenContour = None

    # Plots
    self.f = None
    self.ax1 = None
    self.ax2 = None
    self.ax3 = None
    self.ax4 = None

    # Controls
    self.slideSmoothSize = None
    self.slideSigmaColor = None
    self.slideSigmaSpace = None
    self.slideCannyMin = None
    self.slideCannyMax = None


    self.initDisplay()
    self.readImage(imageLocation)
    self.processImage()
    self.show()

  def readImage(self, imageFile):
    self.img_bgr = cv2.imread(imageFile)
    self.img_rgb = cv2.cvtColor(self.img_bgr, cv2.COLOR_BGR2RGB)
    self.ax1.imshow(self.img_rgb, aspect='auto')
    self.processImage()


  def processImage(self):
    self.img_gray = cv2.cvtColor(self.img_bgr, cv2.COLOR_BGR2GRAY)
    # self.img_smoothed = cv2.GaussianBlur(img_gray, 11, 20)
    self.img_smoothed = \
      cv2.bilateralFilter(self.img_gray, self.smoothSize, self.sigmaColor, self.sigmaColor)
    self.img_edge = cv2.Canny(self.img_smoothed, self.cannyMin, self.cannyMax)
    (self.contours, _) = cv2.findContours(self.img_edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    self.contours = sorted(self.contours, key=cv2.contourArea, reverse=True)[:20]
    self.img_contour = self.img_rgb.copy()
    cv2.drawContours(self.img_contour, self.contours, -1, (0, 255, 0), 3)

    # Set the images to their displays
    self.ax2.imshow(self.img_gray, cmap='gray', aspect='auto')
    self.ax3.imshow(self.img_smoothed, cmap='gray', aspect='auto')
    self.ax4.imshow(self.img_edge, cmap='gray', aspect='auto')
    self.ax1.imshow(self.img_contour, aspect='auto')

  def initDisplay(self):
    # Display images
    self.f, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = \
      plt.subplots(2, 2, subplot_kw=dict(xticks=[], yticks=[]))
    axSliderCannyMin = plt.axes([0.25, 0.1, 0.65, 0.03])
    self.slideCannyMin = Slider(axSliderCannyMin, 'Canny Min', 0, 300, self.cannyMin)
    self.slideCannyMin.on_changed(self.__updateCannyMin)
    plt.tight_layout()

  def show(self):
    plt.show()

  def draw(self):
    plt.draw()

  def __updateCannyMin(self, val):
    self.cannyMin = val
    self.processImage()
    self.draw()

if __name__ == "__main__":
  lab = phoneReaderLab("../samples/polycom_simple.jpg")
