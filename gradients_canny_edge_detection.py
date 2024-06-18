import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sudoku.png", cv2.IMREAD_GRAYSCALE)

# Laplacian transformation
lap = cv2.Laplacian(img, cv2.CV_64F)
lap_res = np.uint8(np.absolute(lap))

# SobelX
sobelX = np.uint8(np.absolute(cv2.Sobel(img, cv2.CV_64F, 1, 0)))

# SobelY
sobelY = np.uint8(np.absolute(cv2.Sobel(img, cv2.CV_64F, 0, 1)))

# Sobel Combined Bitwise
sobelCombinedB = cv2.bitwise_or(sobelX, sobelY)

# Canny edge detection
canny = cv2.Canny(img, 100, 200)

titles = ["Image", "Laplacian", "SobelX", "SobelY", "Sobel Combined Bitwise", "Canny Edge Detection"]
res = [img, lap_res, sobelX, sobelY, sobelCombinedB, canny]

for i in range(len(titles)):
  plt.subplot(2, 3, i+1)
  plt.imshow(res[i], "grey")
  plt.axis("off")


plt.show()
