import cv2
import numpy as np


drawing = False  # True if mouse is pressed
p1, p2 = (-1, -1), (-1, -1)  # Initial and final points for the rectangle``

def draw_rectangle(event, x, y, flags, param):
    global drawing, p1, p2

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        p1 = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        p2 = (x, y)
        cv2.rectangle(img, p1, p2, (0, 0, 0), 2)  # Draw the rectangle on the image


width, height = 800, 600
img = np.ones((height, width, 3), dtype=np.uint8) * 255


cv2.namedWindow('Draw Rectangle')
cv2.setMouseCallback('Draw Rectangle', draw_rectangle)

while True:
    cv2.imshow('Draw Rectangle', img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
