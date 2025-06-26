from chromosome import Chromosome
import random


class RouletteTable:
    """ Rank based roulette selection of parent Chromosomes """
    def __init__(self, chromosomes:list[Chromosome]):
        self.chromosomes = chromosomes
    
    def get_parents(self) -> list[Chromosome]:
        """ Form list of parents that are used for making children for next generation """
        n = len(self.chromosomes)
        parents = list()
        ranks = self._calculate_ranks()
        
        # take two best ranked chromosomes for each iteration
        # which makes total of n chromosomes for new generation
        for _ in range(n//2):
            scores = [ranks[i]*self._rand() for i in range(n)]
            i1, i2 = self._find_two_best_scores(scores)
            parents.append(self.chromosomes[i1])
            parents.append(self.chromosomes[i2])

        return parents
        
    def _calculate_ranks(self):
        """ 
        Rank each Chromosome based on his fitness value
        Index of rank is linked to index of Chromosome 
        """
        indices = sorted(range(len(self.chromosomes)), key=lambda i: self.chromosomes[i].calc_fitness())
        ranks = [0] * len(indices)
        for rank, i in enumerate(indices):
            ranks[i] = len(indices) - rank
        return ranks
    
    def _find_two_best_scores(self, scores:list) -> tuple:
        """ Find and return indices of two best scores """
        s1, s2 = 0, 0
        for i, score in enumerate(scores):
            if score > scores[s1]:
                s1, s2 = i, s1
            elif score > scores[s2]:
                s2 = i
        return s1, s2
    
    def _rand(self):
        """ Return random number in range (0,1) """
        x = random.random()
        while x == 0:
            x = random.random()
        return x
