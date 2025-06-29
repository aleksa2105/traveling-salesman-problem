
from chromosome import *
from roulette_table import RouletteTable


class Population:

    def __init__(self, chromosomes: list):
        self.chromosomes = chromosomes

    def get_next_population(self) -> list[Chromosome]:
        """ Get chromosomes for next generation """

        # select parents
        roulette = RouletteTable(self.chromosomes)
        parents = roulette.get_parents()

        # crossover operator
        children = self._OX1_crossover(parents)

        # mutate children
        self._mutate_children(children)

        # select next population and return it
        return self._select_population(parents, children)
    
    def get_best_chromosome(self):
        """ Return chromosome with lowest fitness value """
        return min(self.chromosomes, key=lambda chromosome: chromosome.calc_fitness())
    
    def _PMX_crossover(self, parents:list[Chromosome]):
        x_point = random_list_index(len(parents[0].genes), 0) # crossover point
        children = list()
        for i in range(len(parents) - 1):
            p1, p2 = parents[i], parents[i + 1]
            p1_map, p2_map = {}, {}
            for j in range(len(p1.genes)): # map genome value to its index
                p1_map[p1.genes[j]] = j
                p2_map[p2.genes[j]] = j

            c1 = copy.deepcopy(p1.genes)
            c2 = copy.deepcopy(p2.genes)

            for k in range(x_point):
                # create first offspring
                if p2.genes[k] != c1[k]:
                    c1[k], c1[p1_map[p2.genes[k]]] = c1[p1_map[p2.genes[k]]], c1[k]
                # create second offspring
                if p1.genes[k] != c2[k]:
                    c2[k], c2[p2_map[p1.genes[k]]] = c2[p2_map[p1.genes[k]]], c2[k]

            children.append(Chromosome(c1))
            children.append(Chromosome(c2))

        return children
    
    def _OX1_crossover(self, parents:list[Chromosome]) -> list:
        children = list()
        num_genes = len(parents[0].genes)
        for i in range(len(parents) - 1):
            p1, p2 = parents[i], parents[i+1] # take parents in pairs
            off1, off2 = [0] * num_genes, [0] * num_genes
            pcg1, pcg2 = set(), set() # parent crossover genes

            point1, point2 = sorted(random.sample(range(num_genes), 2)) # crossover points for subtour

            for i in range(point1, point2): # fill subtour in offsprings
                off1[i] = p1.genes[i]
                off2[i] = p2.genes[i]
                pcg1.add(p1.genes[i])
                pcg2.add(p2.genes[i])

            cur_off_pos1 = point2
            cur_off_pos2 = point2
            for i in range(num_genes): # start from second point and traverse in circular order until offsprings are created
                cur_idx = (point2 + i) % num_genes 
                if p2.genes[cur_idx] not in pcg1:
                    off1[cur_off_pos1] = p2.genes[cur_idx]
                    cur_off_pos1 = (cur_off_pos1 + 1) % num_genes
                if p1.genes[cur_idx] not in pcg2:
                    off2[cur_off_pos2] = p1.genes[cur_idx]
                    cur_off_pos2 = (cur_off_pos2 + 1) % num_genes

            children.append(Chromosome(off1))
            children.append(Chromosome(off2))

        return children

    # my version of crossover (it sucks)
    # def _crossover(self, parents:list[Chromosome]) -> list:
    #     """ Crossover parent Chromosomes to get children """
    #     children = list()
    #     for i in range(len(parents) - 1):
    #         p1, p2 = parents[i], parents[i+1] # pick parents in pairs
    #         c1_genes, c2_genes = list(), list()
    #         pcg1, pcg2 = set(), set() # parent crossover genes

    #         crossover_size = (len(p1.genes) // CROSSOVER_SIZE) # we will take 1/3th of genes from each parent to crossover
    #         for i in range(crossover_size):
    #             c1_genes.append(copy.deepcopy(p1.genes[i]))
    #             c2_genes.append(copy.deepcopy(p2.genes[i]))
    #             pcg1.add(p1.genes[i])
    #             pcg2.add(p2.genes[i])

    #         for i in range(len(p1.genes)): # fill rest of genes in child1 and child2
    #             if p1.genes[i] not in pcg2:
    #                 c2_genes.append(p1.genes[i])
    #             if p2.genes[i] not in pcg1:
    #                 c1_genes.append(p2.genes[i])
            
    #         children.append(Chromosome(c1_genes))
    #         children.append(Chromosome(c2_genes))

    #     return children
            
    def _mutate_children(self, children:list[Chromosome]):
        for child in children:
            chance = random.random()
            if chance <= MUTATION_CHANCE:
                child.displacement_mutate()

    def _select_population(self, parents:list[Chromosome], children:list[Chromosome]) -> list[Chromosome]:
        parents.extend(children)
        total_population = parents
        total_population_sorted = sorted(total_population, key=lambda Chromosome: Chromosome.calc_fitness())
        rest_index = 0 # pick elite_count of elites and then continue from rest_index to pick children
        new_population = []
        elite_count = int(ELITISM_RATE * POPULATION_SIZE)
        while elite_count > 0:
            Chromosome = total_population_sorted[rest_index]
            if Chromosome.age < CHROMOSOME_MAX_AGE:
                Chromosome.age += 1
                new_population.append(Chromosome)
                elite_count -= 1
            rest_index += 1
        for i in range(rest_index, len(total_population)):
            Chromosome = total_population_sorted[i]
            if Chromosome.is_child() and len(new_population) < POPULATION_SIZE:
                Chromosome.age += 1
                new_population.append(Chromosome)

        assert(len(new_population) == POPULATION_SIZE)
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
