from copy import deepcopy
from chromosome import Chromosome
from utils import *
from random import sample


def PMX_crossover(parents:list):
        x_point = random_list_index(len(parents[0].genes), 0) # crossover point
        children = list()
        for i in range(len(parents) - 1):
            p1, p2 = parents[i], parents[i + 1]
            p1_map, p2_map = {}, {}
            for j in range(len(p1.genes)): # map genome value to its index
                p1_map[p1.genes[j]] = j
                p2_map[p2.genes[j]] = j

            c1 = deepcopy(p1.genes)
            c2 = deepcopy(p2.genes)

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
    
    
def OX1_crossover(parents:list) -> list:
        children = list()
        num_genes = len(parents[0].genes)
        for i in range(len(parents) - 1):
            p1, p2 = parents[i], parents[i+1] # take parents in pairs
            off1, off2 = [0] * num_genes, [0] * num_genes
            pcg1, pcg2 = set(), set() # parent crossover genes

            point1, point2 = sorted(sample(range(num_genes), 2)) # crossover points for subtour

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
 