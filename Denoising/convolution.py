import numpy as np 
import cv2 as cv

#Creating an averaging kernel
avg_filter = np.ones((3,3),np.float32)/9

img = cv.imread('../Images/noisy.jpg')
cv.imshow('Before denoising',img)
cv.waitKey(0)

new = cv.filter2D(img,-1,avg_filter)
cv.imshow('After denoising',new)
cv.waitKey(0)


