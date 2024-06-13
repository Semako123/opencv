import cv2
import numpy as np

img1 = cv2.imread("image_1.png", 0)
img2 = np.zeros([183, 275], np.uint8)
cv2.circle(img2, (138, 92), 20, (255,255,255), -1)

bitAnd = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1, img2)
bitXor = cv2.bitwise_xor(img1, img2)

cv2.imshow("bitAnd", bitAnd)
cv2.imshow("bitOr", bitOr)
cv2.imshow("bitXor", bitXor)

cv2.waitKey(0)
cv2.destroyAllWindows()