import cv2 as cv 
import numpy as np 

img = cv.imread('../Images/noisy.jpg')
cv.imshow('Noisy image',img)
cv.waitKey(0)

# h=12, hcolor=12, search_space_dim = 21, neighbourhood_dim = 7
denoised_image = cv.fastNlMeansDenoisingColored(img,None,12,12,7,21)
cv.imshow('After denoising',denoised_image)
cv.waitKey(0)

