from population import *


if __name__ == '__main__':
    population = get_starting_population()
    
    gen, no_improvement, reset_counter = 0, 0, 0
    reset = False
    fitness = population.get_best_chromosome().fitness

    for _ in range(NUM_GENERATIONS):
        if reset_counter >= 200:
            reset = True
            reset_counter = 0
        else:
            reset = False

        population = Population(population.get_next_population(reset), gen)
        gen += 1

        cur_best_fitness = population.get_best_chromosome().fitness

        if cur_best_fitness == fitness:
            no_improvement += 1
            reset_counter += 1
        else:
            fitness = cur_best_fitness
            no_improvement = 0
            reset_counter = 0
            
        if no_improvement > 400:
            break
        
        print("generation:", gen, "fitness:", cur_best_fitness)
    
    print("\nBest fitness found :", fitness, "in", gen, "generations")
    print(fitness)
