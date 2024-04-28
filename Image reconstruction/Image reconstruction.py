import cv2
import matplotlib.pyplot as plt
import os

# Create a list of image file names from A to F
alphabet = ['A', 'B', 'C', 'D', 'E', 'F']

imgs = []

for alp in alphabet:
    filename = f"{alp}.jpg"  
    img = cv2.imread(filename)
    imgs.append(img)

# Create a stitcher object
stitcher = cv2.Stitcher_create()

# Stitch the photos together
status, stitched_image = stitcher.stitch(imgs)

# Check whether the image stitching was successful or not
if status == cv2.Stitcher_OK:
    stitched_image = cv2.cvtColor(stitched_image, cv2.COLOR_BGR2RGB)
    plt.imshow(stitched_image)
    plt.axis('off')
    plt.show()
else:
    print("Stitching failed.")
