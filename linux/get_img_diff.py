import numpy as np
import cv2

# reads image 'opencv-logo.png' as grayscale
img     = cv2.imread('djap.png.cropped', 0) 
img_old = cv2.imread('djap.png.cropped.old', 0) 

img_sub = img-img_old

the_diff = np.sum(img_sub)

if (the_diff > 1000):
    print(1)
    exit(1)
else:
    print(0)
    exit(0)
