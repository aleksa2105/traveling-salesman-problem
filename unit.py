from gene import *
from params import *
import random
import copy


class Unit:
    """ One unit represents travel between every city in its list,
        with condition that first city must also be the last one. """

    def __init__(self, genes: list):
        self.genes = genes
        self.age = 1

    def calc_fitness(self) -> float:
        total = 0.0
        for i in range(len(self.genes)-1):
            total += get_distance(self.genes[i], self.genes[i+1])

        total += get_distance(self.genes[len(self.genes)-1], self.genes[0]) # add distance between last and first 
        return total
    
    def is_child(self):
        return self.age <= 1
    
    def mutate(self):
        for i in range(len(self.genes)):
            chance = random.random()
            if chance <= MUTATION_CHANCE:
                rand = self._get_random_index(len(self.genes), i)
                self.genes[i], self.genes[rand] = self.genes[rand], self.genes[i]
    
    def __str__(self):
        ids = [str(gene.id) for gene in self.genes]
        ids.append(str(self.genes[0].id))
        genes_str = ', '.join(ids)
        return genes_str
    
    @staticmethod
    def _get_random_index(list_size: int, current_index: int):
        """ Return random list index that is not current_index """
        rand = random.randint(0, list_size - 2)
        return rand if rand < current_index else rand + 1


def get_random_unit(genes: list[Gene]) -> Unit:
    """ Randomly shuffle genes """
    shuffled_genes = copy.deepcopy(genes)
    random.shuffle(shuffled_genes)
    unit = Unit(shuffled_genes)
    return unit
