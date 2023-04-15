import itertools

FITNESS_CUTTOFF = 11  # the fitness cuttoff for the fitness_split function


class CrossBreeder:
    def __init__(self):
        pass

    def add_fitness(self, plants):
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

    def remove_fitness(self, plants):
        """Removes the fitness from the plants"""
        for i in range(len(plants)):
            plants[i] = plants[i][1]
        return plants

    def q_crossbreed(self, plants):  # quick crossbreed
        """Prunes the plant list and crossbreeds the 8 fittest plants"""
        all_combos = []
        plants = self.add_fitness(plants)  # sorts the plants by fitness then removes fitness value
        fittest_parent = max(plants)
        print(f'fittest_parent: {fittest_parent}')  # TODO: remove
        plants = self.remove_fitness(plants)
        for r in range(2,9):
            for combination in itertools.combinations(plants[:8], r):
                try:
                    all_children = self.crossbreed(combination)
                    split_children = self.fitness_split(all_children, cutoff=fittest_parent[0])
                    all_combos.append(split_children)
                except:
                    print('ERR: Crossbreed failed')
                    return None
        return all_combos


    def fitness_split(self, plants, cutoff=FITNESS_CUTTOFF):  # splits the plants into a smaller list based on FITNESS_CUTTOFF
        rated_plants = self.add_fitness(plants)
        split_list = [list(group) for key, group in itertools.groupby(rated_plants, lambda x: x[0] >= cutoff) if key]
        return split_list

    def crossbreed(self, plants):
        """Crossbreeds a list of up to plants"""
        # TODO: allow for multiple uses of the same plant
        rated_plants = self.add_fitness(plants)
        if len(rated_plants) > 8 or len(rated_plants) < 2:
            print(f'ERR: Incorrect amount of parent plants for crossbreed. amount: {len(rated_plants)}')
        else:
            gene_dict = {'W': 0, 'X': 1, 'Y': 2, 'G': 3, 'H': 4}
            gene_translate = {0: 'W', 1: 'X', 2: 'Y', 3: 'G', 4: 'H'}
            parents = []
            all_children = []

            for i in range(len(rated_plants)):  # add the 8 first plants to the parents list
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
                        if child not in all_children and child:
                            all_children.append(child)

            if not all_children:
                print('ERR: No children found')
                return None
            return all_children
