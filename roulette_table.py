from unit import Unit
import random


class RouletteTable:
    """ Rank based roulette selection of parent units """
    def __init__(self, units:list[Unit]):
        self.units = units
    
    def get_parents(self) -> list[Unit]:
        """ Form list of parents that are used for making children for next generation """
        n = len(self.units)
        parents = list()
        ranks = self._calculate_ranks()
        
        # take two best ranked units for each iteration
        # which makes total of n units for new generation
        for _ in range(n//2):
            scores = [ranks[i]*self._rand() for i in range(n)]
            i1, i2 = self._find_two_best_scores(scores)
            parents.append(self.units[i1])
            parents.append(self.units[i2])

        return parents
        
    def _calculate_ranks(self):
        """ 
        Rank each unit based on his fitness value
        Index of rank is linked to index of unit 
        """
        indices = sorted(range(len(self.units)), key=lambda i: self.units[i].calc_fitness())
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
