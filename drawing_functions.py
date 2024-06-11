import cv2

image = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)

if image is not None:
  #draw line
  img_line = cv2.line(image, (0,0), (255, 255), (255, 0, 0), 5)
  img_aline = cv2.arrowedLine(image, (0,0), (255, 255), (255, 0, 0), 5)

  #check documentation for other image annotation methods  

  #display_result
  cv2.imshow("image_draw", img_aline)
  if cv2.waitKey(0):
    cv2.destroyAllWindows()