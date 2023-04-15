import itertools

FITNESS_CUTTOFF = 11


class CrossBreeder:
    def __init__(self):
        pass

    def fitness(self, plants):
        """Returns the fitness of a plant"""
        fit_plants = []
        for plant in plants:
            fitness = 0
            for gene in plant:
                if gene == 'Y' or gene == 'G':
                    fitness += 2
                else:
                    fitness += 1
            rated_plant = (fitness, plant)
            fit_plants.append(rated_plant)
        sorted_plants = sorted(fit_plants, key=lambda x: x[0], reverse=True)
        return sorted_plants


    def q_crossbreed(self, plants):  # quick crossbreed
        """Crossbreeds a list of plants"""
        
        rated_plants = self.fitness(plants)
        # TODO: make this function just do the calculation for however many parents it is fed
        gene_dict = {'W': 0, 'X': 1, 'Y': 2, 'G': 3, 'H': 4}
        gene_translate = {0: 'W', 1: 'X', 2: 'Y', 3: 'G', 4: 'H'}
        parents = []
        all_children = []

        for i in range(8):  # add the 8 first plants to the parents list
            parents.append(rated_plants[i][1])
            child = [[],[],[],[],[],[]]

            if len(parents) >= 2:
                for j in range(6):
                    gene_table = [0, 0, 0, 0, 0]  # [W, X, Y, G, H]

                    for plant in parents:
                        if plant[j] == 'W' or plant[j] == 'X':
                            gene_table[gene_dict[plant[j]]] += 1
                        else:
                            gene_table[gene_dict[plant[j]]] += 0.6
                    max_indices = [i for i, x in enumerate(gene_table) if x == max(gene_table)]

                    for index in max_indices:
                        child[j].append(gene_translate[index])

                children = [''.join(child) for child in set(itertools.product(*child))]
                
                for child in children:
                    if child not in all_children:
                        all_children.append(child)

        split_children = self.fitness_split(all_children)

        return split_children


    def fitness_split(self, plants):
        rated_plants = self.fitness(plants)
        split_list = [list(group) for key, group in itertools.groupby(rated_plants, lambda x: x[0] >= FITNESS_CUTTOFF) if key]
        return split_list

    def crossbreed(self, plants):
        pass
