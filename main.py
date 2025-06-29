from population import *


if __name__ == '__main__':
    population = get_starting_population()
    
    gen, fitness_counter = 0, 0
    fitness = population.get_best_chromosome().calc_fitness()

    for _ in range(NUM_GENERATIONS):
        if fitness_counter >= 200:
            print("there were 200 same results...")
            print("program terminated")
            break

        population = Population(population.get_next_population())
        gen += 1
        cur_best_fitness = population.get_best_chromosome().calc_fitness()
        if cur_best_fitness == fitness:
            fitness_counter += 1
        else:
            fitness = cur_best_fitness
            fitness_counter = 0
        print("generation:", gen, "fitness:", cur_best_fitness)
    
    print("\nBest fitness found:", fitness, "in", gen, "generations")
    print(fitness)
