import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('live_recording.avi', fourcc, 20.0, (width, height))

while cap.isOpened():
  ret, frame = cap.read()
  if ret:
    cv2.imshow("live_preview", frame)
    out.write(frame)
    if cv2.waitKey(1) == ord('q'):
      break
  else:
    break

cap.release()
out.release()
cv2.destroyAllWindows()