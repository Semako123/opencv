import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]

print(events)

def click_event(event, x, y, flags, param ):
  global points
  if event == cv2.EVENT_LBUTTONDOWN:
    text = f"{x},{y}"
    cv2.putText(image, text, (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
    cv2.imshow("image", image)
  if event == cv2.EVENT_RBUTTONDOWN:
    cv2.circle(image, (x,y), 3, (255,255,255), -1)
    points.append((x, y))
    if len(points) >= 2:
      cv2.line(image, points[-1], points[-2], (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("image", image)


# image = np.zeros([512, 512, 3], np.uint8)
image = cv2.imread("lena.jpg", -1)
points = []
cv2.imshow("image", image)

cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
