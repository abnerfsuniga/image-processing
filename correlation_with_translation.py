#Máscaras para teste
#https://docs.gimp.org/2.8/pt_BR/plug-in-convimgrix.html

import cv2
import numpy as np
import sys

def correlation(img, mask):
    y, x = img.shape
    mask_y, mask_x = mask.shape
    result = np.zeros((y-2, x-2), dtype='float')
    for i in range(0, mask_y):
	    aux_y = y + (i - 2)
	    for j in range(0, mask_x):
		    aux_x = x + (j - 2)
		    result += img[i:aux_y, j:aux_x] * mask[i][j]

    result = (result / np.amax(result)) * 255
    return result.astype(np.uint8)

def main():
    image_path = sys.argv[1]
    mask = np.ones((3, 3))

    img = cv2.imread(image_path, 0)
    #Colocando borda de zeros
    img = np.pad(img, pad_width=1, mode='constant', constant_values=0)
    
    new_image = correlation(img, mask)
    print(new_image)
    cv2.imshow('Image', img)
    cv2.imshow('New_Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if (__name__ == '__main__'):
    main()