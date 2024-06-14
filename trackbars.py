import cv2
import numpy as np

# NOTE: The code is just a rough and basic implementation
# It can still be better improved or implemented
# For practice you can try to fix the problem with the use of callbacks for this feature implementation
# CLUE: Can you access the other trackbar's position in another's callback
# Or Create an update display function that runs after each callback

# Use a trackbar to adjust brightness of an image
# Use another to switch between colored and grayscale
original = cv2.imread("graf1.png", cv2.IMREAD_UNCHANGED)
img = original.copy()
offset = -100

def adjustBrightness(x):
  pass
  # scale = np.zeros([original.shape[0], original.shape[1], 3], np.uint8) + abs(x+offset)
  # tmp = original[:]
  # # print(scale)
  # if offset+x < 0:
  #   cv2.subtract(tmp, scale, img)
  # else:
  #   cv2.add(tmp, scale, img)
  # cv2.imshow("image", img)


def adjustColor(x):
  pass
  # global img
  # if x == 1:
  #   img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # else:
  #   img = original.copy()


cv2.namedWindow("image")
cv2.createTrackbar("Brightness", "image", 0, 200, adjustBrightness)
cv2.setTrackbarPos("Brightness", "image", 100)
cv2.createTrackbar("ColorScheme", "image", 0, 1, adjustColor)

while True:
  cv2.imshow("image", img)
  k = cv2.waitKey(1)
  if k == 27 & 0xFF:
    break

  shade = cv2.getTrackbarPos("ColorScheme", "image")
  x = cv2.getTrackbarPos("Brightness", "image")
  scale = np.zeros([original.shape[0], original.shape[1], 3], np.uint8) + abs(x+offset)
  tmp = original[:]

  # print(scale)
  # print(offset+x)
  if offset+x < 0:
    cv2.subtract(tmp, scale, img)
  else:
    cv2.add(tmp, scale, img)

  if shade == 1:
    tmp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(tmp, cv2.COLOR_GRAY2BGR)
  else:
    if offset+x < 0:
      cv2.subtract(tmp, scale, img)
    else:
      cv2.add(tmp, scale, img)

cv2.destroyAllWindows()