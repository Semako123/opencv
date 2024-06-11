import cv2
import datetime

cap = cv2.VideoCapture(0)

while cap.isOpened():
  ret, frame = cap.read()
  width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
  height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

  if ret:
    frame = cv2.flip(frame, 1)
    time = datetime.datetime.now()
    text = f"Width: {width} | Height: {height}"
    text1 = f"Time: {time}"
    cv2.putText(frame, text, (10,50), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(frame, text1, (10,80), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1, cv2.LINE_AA)
    cv2.imshow("live_camera", frame)

    if cv2.waitKey(1) == ord('q'):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()