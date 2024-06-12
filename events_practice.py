import cv2
import numpy as np

image = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)

def click_event(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN:
    # print("clicked")
    print(image[x, y])
    color = np.zeros([512, 512, 3], np.uint8) 
    color += image[x,y]
    print(color)
    cv2.imshow("color", color)
    cv2.imshow("image", image)

cv2.imshow("image", image)
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()