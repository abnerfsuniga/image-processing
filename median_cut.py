
import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import sqrt
import cython
from rgb_cube import RGB_Cube

def main(): 
    img = cv2.imread('dog.jpg')
    cube = RGB_Cube(img)
    cube.print()


if (__name__ == '__main__'):
    main()