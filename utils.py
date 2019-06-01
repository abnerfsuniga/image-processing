from math import sqrt

def is_power_two(number): 
    exp = 0
    while number % 2 == 0:
        number /= 2
        exp += 1

    return exp, True if number == 1 else False
    

def euclidian_distance(coord_a, coord_b, coord_size):
    result = 0
    for i in range(0, coord_size):
        result += (coord_a[i] - coord_b[i]) * (coord_a[i] - coord_b[i])
    
    return sqrt(result)