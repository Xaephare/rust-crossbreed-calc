PRUNE_THRESHOLD = 3
COMBINATION_THRESHOLD = 2

import math

class CrossBreeder:
    def __init__(self):
        pass

    def prune(self, bit_vector_list):
        '''Prunes a list of bit vectors based on a 'fitness' threshold'''
        pruned_list = []
        for plant in bit_vector_list:
            fitness = plant[::3]
            if fitness.count(1) <= PRUNE_THRESHOLD:
                pruned_list.append(plant)

        return pruned_list

    def gene_counter(self, parents):
        child = []
        red_gene = None # flag to track red gene
        for i in range(18):
            gene_table = [0,0,0,0,0] # [W, X, Y, G, H]

            # Add up the genes from parent plants
            for plant in parents:
                for i, gene in enumerate(plant):
                    if i == 0 or i % 4 == 3:
                        red_gene = gene
                    elif i % 2 == 1 and red_gene == 0:
                        if gene == 1:
                            gene_table[4] += 0.6  # gene H
                    elif i % 3 == 2:
                        if red_gene == 1:  # genes W and X
                            if gene == 0:
                                gene_table[0] += 1  # gene W
                            else:
                                gene_table[1] += 1  # gene X
                        else:  # genes Y and G
                            if gene == 0:
                                gene_table[2] += 0.6  # gene Y
                            else:
                                gene_table[3] += 0.6  # gene G
        print(gene_table)