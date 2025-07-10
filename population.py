
from chromosome import *
from selection import *
from crossover import *

class Population:

    def __init__(self, chromosomes: list, generation: int):
        self.chromosomes = chromosomes
        self.generation = generation

    def get_next_population(self, reset:bool) -> list[Chromosome]:
        """ Get chromosomes for next generation """
        parents = TournamentSelection.select(self.chromosomes)
        children = OX1_crossover(parents)
        self._mutate_children(children)
        return self._select_population(parents, children, reset)
    
    def get_best_chromosome(self):
        """ Return chromosome with lowest fitness value """
        return min(self.chromosomes, key=lambda c: c.fitness)
    
    def _mutate_children(self, children:list[Chromosome]):
        """ Mutate given children and calculate their fitness afterwards """
        for child in children:
            chance = random.random()
            if chance <= MUTATION_CHANCE:
                child.displacement_mutate()
            child.calc_fitness()

    def _select_population(self, parents:list[Chromosome], children:list[Chromosome], reset) -> list[Chromosome]:
        total_population = parents + children
        total_population.sort(key=lambda c: c.fitness)

        new_population = list()

        elite_count = int(ELITISM_RATE * POPULATION_SIZE)
        i = 0 
        while elite_count > 0: # pick elite_count of elites and then continue from i to pick children
            c = total_population[i]
            if c.age < CHROMOSOME_MAX_AGE:
                c.age += 1
                new_population.append(c)
                elite_count -= 1
            i += 1
        for i in range(i, len(total_population)):
            c = total_population[i]
            if c.is_child() and len(new_population) < POPULATION_SIZE:
                c.age += 1
                new_population.append(c)

        if reset:
            self._reset_population(new_population)

        return new_population
    
    @staticmethod
    def _reset_population(sortedPopulation):
        n = len(sortedPopulation)
        k = int(n * RESET_RATE) # number of chromosomes to be reset
        for i in range(n-1, n-k, -1):
            sortedPopulation[i] = get_random_chromosome(sortedPopulation[i].genes)


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
    return Population(chromosomes, 0)
