
from chromosome import *
from selection import *
from crossover import *

class Population:

    def __init__(self, chromosomes: list):
        self.chromosomes = chromosomes

    def get_next_population(self) -> list[Chromosome]:
        """ Get chromosomes for next generation """
        # select parents
        parents = TournamentSelection.select(self.chromosomes)
        # crossover operator
        children = OX1_crossover(parents)
        # mutate children
        self._mutate_children(children)
        # select next population and return it
        return self._select_population(parents, children)
    
    def get_best_chromosome(self):
        """ Return chromosome with lowest fitness value """
        return min(self.chromosomes, key=lambda chromosome: chromosome.calc_fitness())
    
    def _mutate_children(self, children:list[Chromosome]):
        for child in children:
            chance = random.random()
            if chance <= MUTATION_CHANCE:
                child.displacement_mutate()

    def _select_population(self, parents:list[Chromosome], children:list[Chromosome]) -> list[Chromosome]:
        parents.extend(children)
        total_population = parents
        total_population_sorted = sorted(total_population, key=lambda c: c.calc_fitness())
        rest_index = 0 # pick elite_count of elites and then continue from rest_index to pick children
        new_population = []
        elite_count = int(ELITISM_RATE * POPULATION_SIZE)
        while elite_count > 0:
            c = total_population_sorted[rest_index]
            if c.age < CHROMOSOME_MAX_AGE:
                c.age += 1
                new_population.append(c)
                elite_count -= 1
            rest_index += 1
        for i in range(rest_index, len(total_population)):
            c = total_population_sorted[i]
            if c.is_child() and len(new_population) < POPULATION_SIZE:
                c.age += 1
                new_population.append(c)

        # assert(len(new_population) == POPULATION_SIZE)
        return new_population


def get_starting_population() -> Population:
    """ Read file with genes and return random starting population """
    genes = list()
    with open(FILE_NAME) as file: # read genes from file
        for line in file.readlines():
            line_split = line.split(' ')
            id, x, y = int(line_split[0]), float(line_split[1]), float(line_split[2])
            CITIES[id] = (x, y)
            genes.append(id)
        
    chromosomes = [get_random_chromosome(genes) for _ in range(POPULATION_SIZE)]
    return Population(chromosomes)
