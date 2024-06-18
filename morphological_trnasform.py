import cv2
from matplotlib import pyplot as plt
import numpy as np

smarties = cv2.imread("smarties.png", cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(smarties, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones([3, 3], np.uint8)

dilation = cv2.dilate(mask, kernel, iterations=3)
erosion = cv2.erode(mask, kernel, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
grad = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

plt.subplot(1, 3, 1)
plt.imshow(smarties, "grey")
plt.xticks([]),plt.yticks([])
plt.subplot(1, 3, 2)
plt.imshow(mask, "grey")
plt.xticks([]),plt.yticks([])
plt.subplot(1, 3, 3)
plt.imshow(grad, "grey")
plt.xticks([]),plt.yticks([])
plt.show()