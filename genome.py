from math import sqrt

def get_distance(city1: tuple, city2) -> float:
    """ Get distance between two genes """
    x1, y1 = city1
    x2, y2 = city2
    return sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)) # Euclid's distance