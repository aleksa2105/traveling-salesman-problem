from population import *


if __name__ == '__main__':
    population = get_starting_population()
    
    gen, no_improvement = 0, 0
    fitness = population.get_best_chromosome().fitness
    reset = False

    for _ in range(NUM_GENERATIONS):
        reset = True if no_improvement > 200 else False

        population = Population(population.get_next_population(reset), gen)
        gen += 1

        cur_best_fitness = population.get_best_chromosome().fitness

        if cur_best_fitness == fitness:
            no_improvement += 1
        else:
            fitness = cur_best_fitness
            no_improvement = 0
            
        if no_improvement > 400:
            break
        
        print("generation:", gen, "fitness:", cur_best_fitness)
    
    print("\nBest fitness found:", fitness, "in", gen, "generations")
    print(fitness)
