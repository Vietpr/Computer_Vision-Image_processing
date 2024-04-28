import cv2
import numpy as np

MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 0.15

img_need_aligned = cv2.imread("image1.jpg")
img_template = cv2.imread("image2.jpg")


im1Gray = cv2.cvtColor(img_need_aligned, cv2.COLOR_BGR2GRAY)
im2Gray = cv2.cvtColor(img_template, cv2.COLOR_BGR2GRAY)

# Using ORB detector to find keypoint and descriptor
orb = cv2.ORB_create(MAX_FEATURES)
keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

# Match features.
matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
matches = matcher.match(descriptors1, descriptors2, None)

# Sort matches by score
matches = sorted(matches, key=lambda x: x.distance, reverse=False)

# Choose the best matches
numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
matches = matches[:numGoodMatches]

# Draw the best matches
imMatches = cv2.drawMatches(img_need_aligned, keypoints1, img_template, keypoints2, matches, None)
#cv2.imwrite("matches.jpg", imMatches)

# Get the location of the common points
points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)

for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt

# Find homography
h, _ = cv2.findHomography(points1, points2, cv2.RANSAC)

# Use homography to align photos
height, width, channels = img_template.shape
im1Reg = cv2.warpPerspective(img_need_aligned, h, (width, height))

cv2.imshow('Original Image', img_need_aligned)
cv2.imshow('Aligned Image', im1Reg)
cv2.imshow('matches', imMatches)
cv2.waitKey(0)
cv2.destroyAllWindows()





