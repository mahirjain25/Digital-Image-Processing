import numpy as np 
import cv2 as cv 

img = cv.imread('../Images/hitman.png')
cv.imshow('image',img)
cv.waitKey(0)

# Image dimensions and datatype
print(img.shape, img.dtype)

#Removing the red channel
red_removed = img
red_removed[:,:,2] = 0

cv.imshow('Red channel removed',red_removed)
cv.waitKey(0)

#Adding two images
added_img = cv.add(img,red_removed)
cv.imshow('Addition',added_img)
cv.waitKey(0)

