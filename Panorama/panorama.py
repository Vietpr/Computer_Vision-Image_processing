import cv2
import numpy as np

image_paths = ["1.jpg", "2.jpg", "3.jpg"]
images = []
for image_path in image_paths:
    img = cv2.imread(image_path)
    if img is None:
        print("cant not read image:", image_path)
        continue
    images.append(img)

# Create ORB object
orb = cv2.ORB_create()

# Find keypoints and calculate descriptor for each image
keypoints_list = []
descriptors_list = []
for image in images:
    keypoints, descriptors = orb.detectAndCompute(image, None)
    keypoints_list.append(keypoints)
    descriptors_list.append(descriptors)

# Create matcher
matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)

# stitching images 
status, stitched_image = cv2.Stitcher_create().stitch(images)


if status == cv2.Stitcher_OK:

    cv2.imshow("Panorama", stitched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("stitching fail!")
