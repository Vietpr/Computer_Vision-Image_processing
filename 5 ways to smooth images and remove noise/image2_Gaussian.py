import cv2

image = cv2.imread("2.png")

blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  

cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Filter', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

