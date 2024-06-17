import cv2
from matplotlib import pyplot as plt

gradient = cv2.imread("gradient.png", 0)
sudoku = cv2.imread("sudoku.png", 0)

if gradient is not None:
  # cv2.imshow("gradient", gradient)

# Check documentation for other threshing type
  _, thresh1 = cv2.threshold(gradient, 127, 255, cv2.THRESH_BINARY)
  _, thresh2 = cv2.threshold(gradient, 127, 255, cv2.THRESH_BINARY_INV)

  # cv2.imshow("thresh1", thresh1)
  # cv2.imshow("thresh2", thresh2)

  # Adaptive thresholding
  threshA = cv2.adaptiveThreshold(sudoku, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
  threshB = cv2.adaptiveThreshold(sudoku, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)

  cv2.imshow("Adaptive", threshA)
  cv2.imshow("AdaptiveB", threshB)
  cv2.imshow("AdaptiveC", sudoku)

  cv2.waitKey(0)

cv2.destroyAllWindows()