import cv2 as cv
import numpy as np 

#Load colour image but ignore transparency
colour_img = cv.imread('../Images/918.jpg')

#Load image in grayscale
grayscale_img = cv.imread('../Images/918.jpg',0)

#Load image with alpha value
alpha_image = cv.imread('../Images/918.jpg',-1)

#Displaying images one by one

cv.imshow('Colour Image',colour_img)
cv.waitKey(0)

cv.imshow('Grayscale Image',grayscale_img)
cv.waitKey(0)

cv.imshow('Alpha Channel Image',alpha_image)
cv.waitKey(0)

cv.destroyAllWindows()

#Saving an image
cv.imwrite('../Images/918_grayscale.jpg',grayscale_img)