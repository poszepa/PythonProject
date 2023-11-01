import math
def calculate_area_square(a):
    return a * a

def calculate_area_rectangle(a, b):
    return a * b

def calculate_area_triangle(a, h):
    return a * h / 2

def calculate_area_trapeze(a, b, h):
    return ( (a + b) * h )/ 2

def calculate_area_circle(r):
    return math.pi * math.pow(r, 2)

