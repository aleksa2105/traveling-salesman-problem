from population import *
import random

if __name__ == '__main__':
    population = get_starting_population()
    
    gen = 0
    for _ in range(GENERATION_SIZE):
        population = Population(population.get_next_population())
        gen += 1
        print("generation:", gen, "fitness:", population.get_best_chromosome().calc_fitness())
    