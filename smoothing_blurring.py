import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.cvtColor(cv2.imread("lena.jpg", cv2.IMREAD_UNCHANGED), cv2.COLOR_BGR2RGB)
salt_pepper = cv2.imread("salt-pepper.png")

# if image.shape[2] == 4:
#     # Split the image into BGR and Alpha channels
#     b, g, r, alpha = cv2.split(image)
    
#     # Create a white background image
#     white_background = np.ones_like(image[..., :3], dtype=np.uint8) * 255
    
#     # Composite the image with the white background using the alpha channel
#     alpha = alpha / 255.0
#     composite_image = white_background * (1 - alpha[:, :, np.newaxis]) + image[..., :3] * alpha[:, :, np.newaxis]
#     composite_image = composite_image.astype(np.uint8)

#     # Convert from BGR to RGB
#     composite_image = cv2.cvtColor(composite_image, cv2.COLOR_BGR2RGB)
#     image = composite_image

kernel = np.ones([5, 5], np.float32) / 25

# Homogenous filters

filter1 = cv2.filter2D(image, -1, kernel)
filter2 = cv2.blur(image, (5,5))
filter3 = cv2.GaussianBlur(image, (5,5), 0)
filter4 = cv2.medianBlur(image, 5)
filter5 = cv2.bilateralFilter(image, 7, 75, 75)

titles = ["image", "2D convolution", "Blur", "Gaussian", "Median", "Bilateral"]
images = [image, filter1, filter2, filter3, filter4, filter5]

for i in range(len(titles)):
  plt.subplot(2,3,i+1)
  plt.imshow(images[i], "gray")
  plt.xticks([]), plt.yticks([])
  plt.title(titles[i])

plt.show()