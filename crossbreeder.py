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
        last_h = False # flag to track last gene
        gene_indices = [0, 3, 6, 9, 12, 15]
        gene_table = [0, 0, 0, 0, 0]
        for gene_index in gene_indices:
            for plant in parents: # [W, X, Y, G, H]
                red_gene = plant[gene_index]
                if not red_gene and plant[gene_index+1] == 1:
                    gene_table[4] += 0.6  # gene H
                    last_h = True
                elif red_gene: # genes W and X
                    if plant[gene_index+2] == 0:
                        gene_table[0] += 1  # gene W
                    else:
                        gene_table[1] += 1  # gene X
                else:  # genes Y and G
                    if plant[gene_index+2] == 0:
                        gene_table[2] += 0.6  # gene Y
                    else:
                        gene_table[3] += 0.6  # gene G
            print(gene_table)
        return child