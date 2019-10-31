# For salt and pepper noise, we can use the median filter

import cv2 as cv 
import numpy as np 

img = cv.imread('../Images/salt_pepper.jpeg')
cv.imshow('Original',img)
cv.waitKey(0)

new = cv.medianBlur(img,3)

cv.imshow('After denoising',new)
cv.waitKey(0)

