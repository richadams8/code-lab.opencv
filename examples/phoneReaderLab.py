__author__ = 'Rich Adams'

import numpy as np
import cv2
from matplotlib import pyplot as plt

class phoneReaderLab:

  def __init__(self, imageLocation):
    # Blur Parameters
    self.smoothSize = 10
    self.sigmaColor = 30
    self.sigmaSpace = 10

    # Canny Parameters
    self.cannyMin = 100
    self.cannyMax = 150

    # Images
    self.img_bgr = None
    self.img_rgb = None
    self.img_gray = None
    self.img_smoothed = None
    self.img_edge = None

    # Plots
    self.f = None
    self.ax1 = None
    self.ax2 = None
    self.ax3 = None
    self.ax4 = None

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

    # Set the images to their displays
    self.ax2.imshow(self.img_gray, cmap='gray', aspect='auto')
    self.ax3.imshow(self.img_smoothed, cmap='gray', aspect='auto')
    self.ax4.imshow(self.img_edge, cmap='gray', aspect='auto')

  def initDisplay(self):
    # Display images
    self.f, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = \
      plt.subplots(2, 2, subplot_kw=dict(xticks=[], yticks=[]))
    plt.tight_layout()

  def show(self):
    plt.show()

  def draw(self):
    plt.draw()

if __name__ == "__main__":
  lab = phoneReaderLab("../samples/polycom_simple.jpg")
