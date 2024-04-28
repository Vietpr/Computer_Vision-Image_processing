import cv2

image = cv2.imread("2.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply multi-decay median filter
denoised_image = cv2.fastNlMeansDenoising(gray_image, None, h=18, templateWindowSize=7, searchWindowSize=21)

cv2.imshow('Original Image', gray_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
