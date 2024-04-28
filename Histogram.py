import sys
import cv2
import numpy as np

def change_brightness(img, alpha, beta):
    img_new = np.asarray(alpha * img + beta, dtype=np.uint8)
    img_new[img_new > 255] = 255
    img_new[img_new < 0] = 0
    return img_new

if __name__ == "__main__":
    alpha = 1.0
    beta = -35
    if len(sys.argv) == 3:
        alpha = float(sys.argv[1])
        beta = int(sys.argv[2])
    
    img = cv2.imread('imghistogram.png', cv2.IMREAD_GRAYSCALE)  # Load image as grayscale
    
    # Change brightness
    img_brightened = change_brightness(img, alpha, beta)
    
    # Resize the images
    new_width = 500
    new_height = 350
    img_resized = cv2.resize(img, (new_width, new_height))
    img_brightened_resized = cv2.resize(img_brightened, (new_width, new_height))
    

    cv2.imshow('Original Image', img_resized)
    cv2.imshow('Brightened Image', img_brightened_resized)

    cv2.imwrite('img_3_new1_original_resized.jpg', img_resized)
    cv2.imwrite('img_3_new1_brightened_resized.jpg', img_brightened_resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
