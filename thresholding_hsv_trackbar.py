import cv2

cv2.namedWindow("livestream")
cv2.namedWindow("trackbars")
cap = cv2.VideoCapture(0)

def nothing(x):
  pass

cv2.createTrackbar("h_low", "trackbars", 0, 255, nothing)
cv2.createTrackbar("h_high", "trackbars", 0, 255, nothing)
cv2.createTrackbar("s_low", "trackbars", 0, 255, nothing)
cv2.createTrackbar("s_high", "trackbars", 0, 255, nothing)
cv2.createTrackbar("v_low", "trackbars", 0, 255, nothing)
cv2.createTrackbar("v_high", "trackbars", 0, 255, nothing)

while cap.isOpened():
  ret, frame = cap.read()
  
  key = cv2.waitKey(1)

  h_low = cv2.getTrackbarPos("h_low", "trackbars")
  s_low = cv2.getTrackbarPos("s_low", "trackbars")
  v_low = cv2.getTrackbarPos("v_low", "trackbars")
  h_high = cv2.getTrackbarPos("h_high", "trackbars")
  s_high = cv2.getTrackbarPos("s_high", "trackbars")
  v_high = cv2.getTrackbarPos("v_high", "trackbars")

  if ret:
    mask = cv2.inRange(frame, (h_low, s_low, v_low), (h_high, s_high, v_high))
    output = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("livestream", cv2.flip(output, 1))

  if key == 27 & 0xFF:
    break

cap.release()
cv2.destroyAllWindows()