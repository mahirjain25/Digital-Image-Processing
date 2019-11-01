import cv2 as cv  
import numpy as np 

img = cv.imread('../Images/mri.jpeg',0)
cv.imshow('MRI Scan',img)
cv.waitKey(0)

thresh, binarized = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print("Threshold value: ",thresh)

cv.imshow('Binarized scan',binarized)
cv.waitKey(0)

strel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
opening = cv.morphologyEx(binarized,cv.MORPH_OPEN,strel)

cv.imshow('After opening',opening)
cv.waitKey(0)

nb_components, output, stats, centroids = cv.connectedComponentsWithStats(opening, connectivity=4)
sizes = stats[:, -1]

max_label = 1
max_size = sizes[1]
for i in range(2, nb_components):
    if sizes[i] > max_size:
        max_label = i
        max_size = sizes[i]

img2 = np.zeros(output.shape)
img2[output == max_label] = 255
cv.imshow("Biggest component", img2)
cv.waitKey(0)