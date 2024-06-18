import cv2
from matplotlib import pyplot as plt

lena = cv2.imread("lena.jpg")

cv2.imshow("lena", lena)
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()