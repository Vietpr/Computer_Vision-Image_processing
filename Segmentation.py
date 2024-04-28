import cv2
import numpy as np

image = cv2.imread("iamge3.png")

if image is None:
    print("Error: Unable to read the image.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (1, 1), 0) 
    canny = cv2.Canny(blur, 120, 250, 5)
    dilated = cv2.dilate(canny, (1, 1), iterations=1)

    (cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


    min_width, min_height = 35, 35

  
    box_count = 0
    segmentation_count = len(cnt)

    for contour in cnt:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
  
        if w > min_width and h > min_height:
           
            radius = int((w + h) / 4)
            center = (int(x + w / 2), int(y + h / 2))
            cv2.circle(rgb, center, radius, (0, 255, 0), 2)
            box_count += 1


    cv2.putText(rgb, f"Number of eggs is: {box_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # show number segmentations
    cv2.imshow("Image with Circular Segmentation", rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    print("Number of bounding boxes:", box_count)
    print("Number of segmentations:", segmentation_count)
