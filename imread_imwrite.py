import cv2

lena = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)

cv2.imshow("image", lena)
key = cv2.waitKey(0)

if key == 27:
  cv2.destroyAllWindows()
elif key == ord('s'):
  cv2.imwrite("lena_copy.png", lena)
  cv2.destroyAllWindows()
