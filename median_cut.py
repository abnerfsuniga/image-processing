import cv2
import numpy as np
import math
import statistics
import matplotlib.pyplot as plt

def find_diff_component(cube):
    b = abs(cube[:,0].max() - cube[:,0].min())
    g = abs(cube[:,1].max() - cube[:,1].min())
    r = abs(cube[:,2].max() - cube[:,2].min())
    maxdiff = max(b, g, r)
    if maxdiff == b:
        return 0
    elif maxdiff == g:
        return 1
    else:
        return 2

def median_cut(cube, n):
    
    if n == 1 or len(cube) == 0:
        return cuts.append(cube)
    
    # Achando a banda com maior diferença
    idx_maxdiff = find_diff_component(cube)

    # Ordenando pela banda
    cube = np.array(sorted(cube, key=lambda x: x[idx_maxdiff]))

    # Achando mediana
    median = statistics.median(cube[::,idx_maxdiff])

    # Dividindo cubo
    first_half = cube[cube[::,idx_maxdiff] <= median]
    second_half = cube[cube[::,idx_maxdiff] > median]
    
    n_iteration = n / 2
    first_bins = median_cut(first_half, n_iteration)
    second_bins = median_cut(second_half, n_iteration)

def quant_median_cut(image, LUT):
    newimage = image.copy()
    h = image.shape[0]
    w = image.shape[1]
    for y in range(h):
        for x in range(w):
            newimage[y, x] = LUT[tuple(image[y, x])]
    return newimage

def main():
    img = cv2.imread('dog.jpg')

    # Construindo o cubo RGB
    pixels = img.reshape((img.shape[0]*img.shape[1], 3))
    cube = np.unique(pixels, axis=0)

    n = 16
    log2n = math.log2(n)

    # Verificando se é potência de 2
    assert(int(log2n) - log2n == 0)

    global cuts
    cuts = [] 
    median_cut(cube, n)

    # Filtra cortes vazios (sem cores)
    cuts = list(filter(lambda cut: len(cut) > 0, cuts))

    # Criando LUT
    LUT = {}
    for cut in cuts:
        mean = np.mean(cut, axis=0, dtype=int)
        for color in cut:
            LUT[tuple(color)] = mean
    
    img_median_cut = quant_median_cut(img, LUT)

    pixels = img_median_cut.reshape((img_median_cut.shape[0] * img_median_cut.shape[1], 3))
    cube = np.unique(pixels, axis=0)
    print(len(cube))

    cv2.imshow('New Image', img_median_cut)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if (__name__ == '__main__'):
    main()