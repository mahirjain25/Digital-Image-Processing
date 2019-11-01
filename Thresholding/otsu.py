import cv2 as cv 
import numpy as np 

img = cv.imread('../Images/thresholding.png',0)
cv.imshow('Before binarization',img)
cv.waitKey(0)

thresh, binarized = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

#Threshold value as found by Otsu's Algorithm
print("Threshold value: ",thresh)

cv.imshow('Binarized Image',binarized)
cv.waitKey(0)
