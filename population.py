
from unit import *
from roulette_table import RouletteTable

class Population:

    def __init__(self, units: list):
        self.units = units

    def get_next_population(self) -> list[Unit]:
        """ Choose units for next generation with rank based roulette selection """
        roulette = RouletteTable(self.units)
        parents = roulette.get_parents()

        children = self._crossover(parents)
        self._mutate_children(children)

        return self._select_population(parents, children)
    
    def get_best_unit(self):
        return min(self.units, key=lambda unit: unit.calc_fitness())

    def _crossover(self, parents:list[Unit]) -> list:
        """ Crossover parent units to get children """
        children = list()
        for i in range(len(parents) - 1):
            p1, p2 = parents[i], parents[i+1] # pick parents in pairs
            c1_genes, c2_genes = list(), list()
            pcg1, pcg2 = set(), set() # parent crossover genes

            crossover_size = (len(p1.genes) // CROSSOVER_SIZE) # we will take 1/3th of genes from each parent to crossover
            for i in range(crossover_size):
                c1_genes.append(copy.deepcopy(p1.genes[i]))
                c2_genes.append(copy.deepcopy(p2.genes[i]))
                pcg1.add(p1.genes[i])
                pcg2.add(p2.genes[i])

            for i in range(len(p1.genes)): # fill rest of genes in child1 and child2
                if p1.genes[i] not in pcg2:
                    c2_genes.append(p1.genes[i])
                if p2.genes[i] not in pcg1:
                    c1_genes.append(p2.genes[i])
            
            children.append(Unit(c1_genes))
            children.append(Unit(c2_genes))

        return children
            
    def _mutate_children(self, children:list[Unit]):
        for child in children:
            child.mutate()

    def _select_population(self, parents:list[Unit], children:list[Unit]) -> list[Unit]:
        parents.extend(children)
        total_population = parents
        total_population_sorted = sorted(total_population, key=lambda unit: unit.calc_fitness())
        rest_index = 0 # pick elite_count of elites and then continue from rest_index to pick children
        new_population = []
        elite_count = ELITISM_SIZE
        while elite_count > 0:
            unit = total_population_sorted[rest_index]
            if unit.age < UNIT_MAX_AGE:
                unit.age += 1
                new_population.append(unit)
                elite_count -= 1
            rest_index += 1
        for i in range(rest_index, len(total_population)):
            unit = total_population_sorted[i]
            if unit.is_child() and len(new_population) < POPULATION_SIZE:
                unit.age += 1
                new_population.append(unit)

        assert(len(new_population) == POPULATION_SIZE)
        return new_population


def get_starting_population() -> Population:
    """ Read file with genes and return random starting population """
    genes = list()
    with open(FILE_NAME) as file: # read genes from file
        for line in file.readlines():
            line_split = line.split(' ')
            id, x, y = int(line_split[0]), float(line_split[1]), float(line_split[2])
            genes.append(Gene(id, x, y))
        
    units = [get_random_unit(genes) for _ in range(POPULATION_SIZE)]
    return Population(units)
