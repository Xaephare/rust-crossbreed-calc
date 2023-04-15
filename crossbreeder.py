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

    def crossbreed(self, parents):
        red_gene = None # flag to track red gene
        gene_indices = [0, 3, 6, 9, 12, 15] # jumps through binary by gene size (3 bits)
        for gene_index in gene_indices:
            gene_table = [0, 0, 0, 0, 0] # [W, X, Y, G, H]
            for plant in parents:
                red_gene = plant[gene_index]
                if not red_gene and plant[gene_index+1] == 1:
                    gene_table[4] += 0.6  # gene H
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
            max_indices = [i for i, x in enumerate(gene_table) if x == max(gene_table)]
            print(max_indices)
            # TODO: if max_indices > 1, then we need to do some combination
        return gene_table
        