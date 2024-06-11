import cv2

# Read video from live cam
# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#   ret, frame = cap.read()

#   if ret:
#     cv2.imshow("live_capture", frame)
#   else:
#      break
  
#   if cv2.waitKey(1) == 27:
#       break

# cap.release()
# cv2.destroyAllWindows()


# Read video from file
cap = cv2.VideoCapture("Megamind.avi")
fps = cap.get(cv2.CAP_PROP_FPS)

while cap.isOpened():
  ret, frame  = cap.read()

  if ret:
    cv2.imshow('megamind', frame)
  else:
    break

  if cv2.waitKey(int(fps)) == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()