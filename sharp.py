import cv2
import numpy as np

imagedata_original = cv2.imread('image.png')

cv2.imshow('original image' , imagedata_original)
cv2.waitKey(0)

sharpening_filter = np.array([[-1,-1,-1],
                                [-1,9,-1],
                                [-1,-1,-1]])

sharpened_image = cv2.filter2D(imagedata_original, -1, sharpening_filter)

cv2.imshow('sharpened image', sharpened_image)
cv2.imwrite('neweye.png',sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
