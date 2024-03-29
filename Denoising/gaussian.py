import numpy as np 
import cv2 as cv

img = cv.imread('../Images/noisy.jpg')
cv.imshow('Before denoising',img)
cv.waitKey(0)

#Applying Gaussian Blurring, with stddev = 0 along x and y
new = cv.GaussianBlur(img,(3,3),0)
cv.imshow('After denoising',new)
cv.waitKey(0)


