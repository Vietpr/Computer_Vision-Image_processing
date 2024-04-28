import cv2
import numpy as np

image = cv2.imread('image1.jpg')  

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and help with edge detection
blurred = cv2.GaussianBlur(gray, (15, 15), 0)

# Use HoughCircles to detect circles (coins) in the image
circles = cv2.HoughCircles(
    blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=30, minRadius=10, maxRadius=50
)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, f'Number of coins: {len(circles)}', (80, 50), font, 0.4, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Detected Coins", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Number of coins:", len(circles))
else:
    print("No circles (coins) detected.")
