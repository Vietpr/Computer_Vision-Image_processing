import cv2

image = cv2.imread("2.png")

kernel_size = 5

blurred_image = cv2.medianBlur(image, kernel_size)


cv2.imshow('Original Image', image)
cv2.imshow('Median Filter', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

