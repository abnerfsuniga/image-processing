#Máscaras para teste
#https://docs.gimp.org/2.8/pt_BR/plug-in-convmatrix.html


import cv2
import numpy as np
import math
import statistics
import sys

def correlation(img, mask):
    y, x = img.shape
    new_image = np.zeros((y-1, x-1))
    new_y, new_x = new_image.shape
 
    for i in range(0, new_y):
        for j in range(0, new_x):
            new_image[i][j] = calculate_pixel(img, mask, i, j)

    new_image = (new_image / np.amax(new_image)) * 255
    return new_image.astype(np.uint8)

def calculate_pixel(img, mask, line, col):
    result = 0
    result += img[line][col] * mask[1][1]
    result += img[line-1][col-1] * mask[0][0]
    result += img[line-1][col] * mask[0][1]
    result += img[line-1][col+1] * mask[0][2]
    result += img[line][col-1] * mask[1][0]
    result += img[line][col+1] * mask[1][2]
    result += img[line+1][col-1] * mask[2][0]
    result += img[line+1][col] * mask[2][1]
    result += img[line+1][col+1] * mask[2][2]
    
    return result

def main():
    image_path = sys.argv[1]
    #Máscara para destacar bordas
    mask = [[1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9]]

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