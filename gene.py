import math

class Gene:
    """ One gene represents city's coordinates """

    def __init__(self, city_name:int, x:float, y:float):
        self.city_name = city_name
        self.x = x
        self.y = y


def get_distance(g1: Gene, g2: Gene) -> float:
    """ Get distance between two genes """
    return math.sqrt((g1.x - g2.x)*(g1.x - g2.x) + (g1.y - g2.y)*(g1.y - g2.y)) # Euclid's distance