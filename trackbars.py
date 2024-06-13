import cv2
import numpy as np

# Use a trackbar to adjust brightness of an image
# Use another to switch between colored and grayscale
original = cv2.imread("graf1.png", cv2.IMREAD_UNCHANGED)
img = original.copy()
offset = -100

def adjustBrightness(x):
  scale = np.zeros([original.shape[0], original.shape[1], 3], np.uint8) + abs(x+offset)
  tmp = original[:]
  # print(scale)
  if offset+x < 0:
    cv2.subtract(tmp, scale, img)
  else:
    cv2.add(tmp, scale, img)
  # print(original)


def adjustColor(x):
  global img
  if x == 1:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  else:
    img = original.copy()


cv2.namedWindow("image")
cv2.createTrackbar("Brightness", "image", 0, 200, adjustBrightness)
cv2.setTrackbarPos("Brightness", "image", 100)
cv2.createTrackbar("ColorScheme", "image", 0, 1, adjustColor)

while True:
  cv2.imshow("image", img)
  k = cv2.waitKey(1)
  if k == 27 & 0xFF:
    break

cv2.destroyAllWindows()