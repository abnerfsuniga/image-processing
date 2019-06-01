
import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import sqrt
from rgb_cube import RGB_Cube
from utils import euclidian_distance, is_power_two

def median_cut(cube, n_cut, iteration):
    if iteration != n_cut:
        cut_cube(cube, iteration)
    

def cut_cube(cube, iteration):
    iteration += 1
    if cube._bsize == max(cube._bsize, cube._gsize, cube._rsize):
        #corta mediana no canal Blue
        return
    elif cube._gsize == max(cube._bsize, cube._gsize, cube._rsize):
        #corta mediana no canal Green
        return
    else:
        #corta mediana no canal Red       
        return

def main(): 
    cube_list = []
    img = cv2.imread('dog.jpg')
    cube = RGB_Cube(img[:, :, 0], img[:, :, 1], img[:, :, 2])
    cube_list.append(cube)
    exp, is_power_2 = is_power_two(16)
    global iteration
    iteration = 0
    if is_power_2:
        median_cut(cube, exp, iteration)

if (__name__ == '__main__'):
    main()