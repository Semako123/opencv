import cv2
import numpy as np

image = cv2.imread("lena.jpg", 1)
print(image.shape)
print(image.size)
print(image.dtype)

b,g,r = cv2.split(image)
img = cv2.merge((r,g,b))

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()