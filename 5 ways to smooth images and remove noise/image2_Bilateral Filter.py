import cv2

image = cv2.imread("2.png")

bilateral_filtered_image = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

cv2.imshow('Original Image', image)
cv2.imshow('Bilateral Filtered Image', bilateral_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
