
import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import sqrt
from rgb_cube import RGB_Cube
from utils import euclidian_distance, is_power_two

def median_cut(cube, n_cut, iteration):
    if iteration != n_cut:
        cut_cube(cube, n_cut, iteration)
    else:
        cube_list.append(cube)
        for each_cube in cube_list:
            each_cube.select_representative()
    

def cut_cube(cube, n_cut, iteration):
    color_aux_list = []
    half = 0

    iteration += 1
    if cube._bsize == max(cube._bsize, cube._gsize, cube._rsize):
        color_aux_list = cube.b_list
        half = len(color_aux_list) // 2
        new_cube1 = RGB_Cube(color_aux_list[:half], cube.g_list, cube.r_list)
        new_cube2 = RGB_Cube(color_aux_list[half:], cube.g_list, cube.r_list)

    elif cube._gsize == max(cube._bsize, cube._gsize, cube._rsize):
        color_aux_list = cube.g_list
        half = len(color_aux_list) // 2
        new_cube1 = RGB_Cube(cube.b_list, color_aux_list[:half], cube.r_list)
        new_cube2 = RGB_Cube(cube.b_list, color_aux_list[half:], cube.r_list)

    else:
        color_aux_list = np.sort(cube.r_list)
        half = len(color_aux_list) // 2
        new_cube1 = RGB_Cube(cube.b_list, cube.g_list, color_aux_list[:half])
        new_cube2 = RGB_Cube(cube.b_list, cube.g_list, color_aux_list[half:])

    median_cut(new_cube1, n_cut, iteration)
    median_cut(new_cube2, n_cut, iteration)

def nearst_color(pixel, cube_list):
    distance = euclidian_distance(pixel, cube_list[0].rep_color, 3)
    nearst_rgb_color = cube_list[0].rep_color

    for cube in cube_list:
        if euclidian_distance(pixel, cube.rep_color, 3) < distance:
            nearst_rgb_color = cube.rep_color

    return nearst_rgb_color            

def convert(img, cube_list):
    newimage = img.copy()
    h = img.shape[0]
    w = img.shape[1]
    for y in range(h):
        for x in range(w):
            newimage[y, x] = nearst_color(img[y, x], cube_list)

    return newimage

def main(): 
    img = cv2.imread('dog.jpg')
    cube = RGB_Cube(img[:, :, 0], img[:, :, 1], img[:, :, 2])
    exp, is_power_2 = is_power_two(64)
    global iteration
    global cube_list

    cube_list = []
    iteration = 0
    if is_power_2:
        median_cut(cube, exp, iteration)

    new_image = convert(img, cube_list)
    cv2.imshow('image', img)
    cv2.imshow('new_image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if (__name__ == '__main__'):
    main()