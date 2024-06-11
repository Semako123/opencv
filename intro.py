import cv2

print(cv2.__version__)
#print opencv version

#Reading images using opencv
#Flags
#0 - GREYSCALE
#1:COLOR
#-1: UNCHANGED

lena_img = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)

#Display image
cv2.imshow("image", lena_img)
cv2.waitKey(0) 
cv2.destroyAllWindows()

#Write to image/ create new image
cv2.imwrite("lena_copy.png", lena_img)

