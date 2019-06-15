import cv2
import numpy as np
import sys

def correlation(img, mask):
    y, x = img.shape
    new_image = np.zeros((y - 1, x - 1))
    new_y, new_x = new_image.shape
 
    for i in range(0, new_y):
        for j in range(0, new_x):
            new_image[i][j] = calculate_each_pixel(img, mask, i, j)

    new_image = (new_image / np.amax(new_image)) * 255
    return new_image.astype(np.uint8)

def calculate_each_pixel(img, mask, line, col):
    result = 0
    mask_y, mask_x = mask.shape

    for i in range(0, mask_y):
        for j in range(0, mask_x):
            result += img[line + (i - 1)][col + (j - 1)] * mask[i][j]

    return result

def main():
    image_path = sys.argv[1]
    mask = np.ones((3, 3)) * (1 / 9)
    #mask = np.array([[1, 2, 1], [2, 4, 1], [1, 2, 1]])
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