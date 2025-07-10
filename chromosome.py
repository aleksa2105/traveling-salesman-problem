from genome import *
from params import *
from utils import *
import random
import copy
from math import inf


class Chromosome:
    """ One Chromosome represents travel between every city in its list,
        with condition that first city must also be the last one. """

    def __init__(self, genes: list, calc_fitness: bool):
        self.genes = genes
        self.age = 1
        self.fitness = inf
        if calc_fitness:
            self.calc_fitness()

    def calc_fitness(self):
        total = 0.0
        for i in range(len(self.genes)-1):
            total += get_distance(CITIES[self.genes[i]], CITIES[self.genes[i+1]])

        total += get_distance(CITIES[self.genes[len(self.genes)-1]], CITIES[self.genes[0]]) # add distance between last and first 
        self.fitness = total
    
    def is_child(self):
        return self.age <= 1
    
    def mutate(self):
        """ mutation based on displacement method """
        n = len(self.genes)
        i, j = sorted(random.sample(range(n), 2))  # i < j
        segment = self.genes[i:j+1]
        rest = self.genes[:i] + self.genes[j+1:]
        if len(rest) == 0: # no changes, return
            return

        possible_positions = list(range(0, i+1)) + list(range(i, len(rest)+1))
        insert_pos = random.choice(possible_positions)

        self.genes = rest[:insert_pos] + segment + rest[insert_pos:]
    
    def __str__(self):
        ids = [str(gene) for gene in self.genes]
        ids.append(str(self.genes[0]))
        genes_str = ', '.join(ids)
        return genes_str
    

def get_random_chromosome(genes: list[int]) -> list[Chromosome]:
    """ Randomly shuffle genes """
    shuffled_genes = list(genes)
    random.shuffle(shuffled_genes)
    chromosome = Chromosome(shuffled_genes, calc_fitness=True)
    return chromosome
