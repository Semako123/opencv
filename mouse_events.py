import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]

print(events)

def click_event(event, x, y, flags, param ):
  if event == cv2.EVENT_LBUTTONDOWN:
    text = f"{x},{y}"
    cv2.putText(image, text, (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
    cv2.imshow("image", image)

image = np.zeros([512, 512, 3], np.uint8)
cv2.imshow("image", image)

cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
