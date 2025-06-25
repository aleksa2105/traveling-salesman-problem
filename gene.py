import math

class Gene:
    """ One gene represents city's coordinates """

    def __init__(self, id:int, x:float, y:float):
        self.id = id
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return isinstance(other, Gene) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Gene({self.id})"


def get_distance(g1: Gene, g2: Gene) -> float:
    """ Get distance between two genes """
    return math.sqrt((g1.x - g2.x)*(g1.x - g2.x) + (g1.y - g2.y)*(g1.y - g2.y)) # Euclid's distance