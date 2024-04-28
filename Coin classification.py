import cv2
import numpy as np


img = cv2.imread("image1.jpg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


blurred = cv2.GaussianBlur(gray, (15, 15), 0)


circles = cv2.HoughCircles(
    blurred,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=50,
    param1=50,
    param2=30,
    minRadius=10,
    maxRadius=100,
)


if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    coin_types = {"L_1": 0, "L_2": 0} 

    for (x, y, r) in circles:
       
        if 20 <= r <= 25:
            coin_type = "L_1"
        elif 26 <= r <= 30:
            coin_type = "L_2"
        else:
            coin_type = "Unknown"

   
        if coin_type != "Unknown":
            coin_types[coin_type] += 1

        # Draw the circle with type label
        cv2.circle(img, (x, y), r, (0, 255, 0), 4)
        cv2.putText(img, coin_type, (x - 20, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    cv2.imshow("Coins", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    for coin_type, count in coin_types.items():
        print(f"{coin_type}: {count} coins")
else:
    print("No circles/coins found in the image.")