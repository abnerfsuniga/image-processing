import cv2
import numpy as np
import math
import sys
import os

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac

def primes_reduction(primes, n):
    factor = 1
    while len(primes) > n-1:
        factor *= primes.pop(0)
    primes.append(factor)
    return primes

def min_distance(pixel, cartesian):
    min = None
    min_array = []
    for c in cartesian:
        dist = np.linalg.norm(pixel-c)
        if min == None or dist < min:
            min = dist
            min_array = c
    return min_array

def quant_uniforme(image, cartesian):
    newimage = image.copy()
    h = image.shape[0]
    w = image.shape[1]
    for y in range(h):
        for x in range(w):
            newimage[y, x] = min_distance(image[y, x], cartesian)
    return newimage

def main():
    image_path = sys.argv[1]
    n_colors = int(sys.argv[2])

    img = cv2.imread(image_path)
    primes_list = primes_reduction(primes(n_colors), 3)
    a = np.linspace(0, 255, primes_list[0], dtype=int)
    b = np.linspace(0, 255, primes_list[1], dtype=int)
    c = np.linspace(0, 255, primes_list[2], dtype=int)

    cartesian = np.array(np.meshgrid(a, b, c)).T.reshape(-1,3)  
    img_uniforme = quant_uniforme(img, cartesian)
    
    pixels = img_uniforme.reshape((img_uniforme.shape[0] * img_uniforme.shape[1], 3))
    cube = np.unique(pixels, axis=0)
    print(len(cube))
    
    cv2.imwrite(f"{os.path.splitext(image_path)[0]}_um_{n_colors}.jpg", img_uniforme)
    cv2.imshow('Uniform Method', img_uniforme)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if (__name__ == '__main__'):
    main()