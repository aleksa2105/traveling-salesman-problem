from gene import *


class Unit:
    """ One unit represents travel between every city in its list 
        with condition that first city must also be the last """

    def __init__(self, genes: list):
        self.genes = genes
        self.value = self.fitness()

    def fitness(self):
        pass

    def __str__(self):
        genes_str = ""
        for gene in self.genes:
            genes_str += str(gene.city_name) + ', '
        return "[" + genes_str + str(self.genes[0].city_name) + "]"


def read_file(file_name: str) -> Unit:
    with open(file_name) as file:
        genes = list()
        for line in file.readlines():
            line_split = line.split(' ')
            name, x, y = float(line_split[0]), float(line_split[1]), float(line_split[2])
            genes.append(Gene(name, x, y))
            
        unit = Unit(genes)
        return unit


def random_unit(genes: list) -> Unit:
    """ Randomly move every gene except first one"""
    pass