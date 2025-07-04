""" 
Selection of parents(which are used for creating offsprings) for next generation.
"""


import random
from params import *


class TournamentSelection:
    """ For each iteration pick k random chromosomes and return the best one among them """
    
    @staticmethod
    def select(population):
        """ Select half of the population """
        selection = list()
        for _ in range(len(population)//2):
            selection.append(TournamentSelection._compete(population))
        
        return selection
    
    @staticmethod
    def _compete(population):
        """ Pick k random chromosomes and return the best one among them """
        competitors = random.choices(population, k=TOURNAMENT_SELECTION_SIZE)
        return min(competitors, key=lambda c: c.calc_fitness())
    
    
class RouletteSelection:
    """ 
    Rank based roulette selection 
    
    Chromosomes in population are ranked based on their fitness value.
    Smaller the fitness, better the rank of chromosome
    
    Each iteration produces list of scores from which two best chromosomes are chosen
    
    Scores are calculated by multiplying rank with random multiplier in range(0,1)
    """
    
    @staticmethod
    def select(population):
        n = len(population)
        selection = list()
        ranks = RouletteSelection._calculate_ranks(population)
        
        # take two best ranked chromosomes for each iteration
        # which makes total of n chromosomes for new generation
        for _ in range(n//2):
            scores = [ranks[i]*RouletteSelection._rand() for i in range(n)]
            i1, i2 = RouletteSelection._find_two_best_scores(scores)
            selection.append(population[i1])
            selection.append(population[i2])

        return selection
        
    @staticmethod
    def _calculate_ranks(population):
        """ 
        Rank each chromosome based on its fitness value
        Index of rank is linked to index of chromosome 
        """
        indices = sorted(range(len(population)), key=lambda i: population[i].calc_fitness())
        ranks = [0] * len(indices)
        for rank, i in enumerate(indices):
            ranks[i] = len(indices) - rank
        return ranks
    
    @staticmethod
    def _find_two_best_scores(scores:list) -> tuple:
        """ Find and return indices of two best scores """
        s1, s2 = 0, 0
        for i, score in enumerate(scores):
            if score > scores[s1]:
                s1, s2 = i, s1
            elif score > scores[s2]:
                s2 = i
        return s1, s2
    
    @staticmethod
    def _rand():
        """ Return random number in range (0,1) """
        x = random.random()
        while x == 0:
            x = random.random()
        return x
