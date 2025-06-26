from genome import *
from params import *
from utils import *
import random
import copy


class Chromosome:
    """ One Chromosome represents travel between every city in its list,
        with condition that first city must also be the last one. """

    def __init__(self, genes: list):
        self.genes = genes
        self.age = 1

    def calc_fitness(self) -> float:
        total = 0.0
        for i in range(len(self.genes)-1):
            total += get_distance(CITIES[self.genes[i]], CITIES[self.genes[i+1]])

        total += get_distance(CITIES[self.genes[len(self.genes)-1]], CITIES[self.genes[0]]) # add distance between last and first 
        return total
    
    def is_child(self):
        return self.age <= 1
    
    def mutate(self):
        for i in range(len(self.genes)):
            chance = random.random()
            if chance <= MUTATION_CHANCE:
                rand = random_list_index(len(self.genes), i)
                self.genes[i], self.genes[rand] = self.genes[rand], self.genes[i]
    
    def __str__(self):
        ids = [str(gene) for gene in self.genes]
        ids.append(str(self.genes[0]))
        genes_str = ', '.join(ids)
        return genes_str
    

def get_random_chromosome(genes: list[int]) -> list[Chromosome]:
    """ Randomly shuffle genes """
    shuffled_genes = copy.deepcopy(genes)
    random.shuffle(shuffled_genes)
    chromosome = Chromosome(shuffled_genes)
    return chromosome
