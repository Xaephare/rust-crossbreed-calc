import itertools
import threading

FITNESS_CUTOFF = 10  # the fitness cutoff for the fitness_split function


def sort_key(item):
    return item[3], item[2]


def output_sorter(output):
    """Sorts the plants by fitness and chance"""
    output.sort(key=sort_key, reverse=True)
    return output


def add_fitness(plants):
    """Returns the fitness of a plant"""
    fit_plants = []
    for plant in plants:
        fitness = 0
        for gene in plant:
            gene_count = plant.count(gene)
            if gene_count > 4:
                fitness += 0
            elif gene == 'Y' or gene == 'G':
                fitness += 2
            elif gene == 'W' or gene == 'X':
                fitness += 0
            else:
                fitness += 1
        rated_plant = [fitness, plant]
        fit_plants.append(rated_plant)
    sorted_plants = sorted(fit_plants, key=lambda x: x[0], reverse=True)
    return sorted_plants


def remove_fitness(plants):
    """Removes the fitness from the plants"""
    for i in range(len(plants)):
        plants[i] = plants[i][1]
    return plants


def fitness_split(plants,
                  cutoff=FITNESS_CUTOFF):  # splits the plants into a smaller list based on FITNESS_CUTOFF
    rated_plants = add_fitness(plants)
    if cutoff == 12:  # Allows display of god plants even if best parent is already a god plant
        cutoff = 11
    split_list = []
    for key, group in itertools.groupby(rated_plants, lambda x: x[0] > cutoff):
        if key:
            sublist = list(group)
            for item in sublist:
                if item not in split_list:
                    split_list.append(item)
    return split_list


def crossbreed(plants):
    """Crossbreeds a list of up to plants"""
    chance = 0
    rated_plants = add_fitness(plants)
    if len(rated_plants) > 8 or len(rated_plants) < 2:
        print(f'ERR: Incorrect amount of parent plants for crossbreed. amount: {len(rated_plants)}')
        return None
    else:
        gene_dict = {'W': 0, 'X': 1, 'Y': 2, 'G': 3, 'H': 4}
        gene_translate = {0: 'W', 1: 'X', 2: 'Y', 3: 'G', 4: 'H'}
        parents = []
        all_children = []

        for i in range(len(rated_plants)):  # add the 8 first plants to the parents list
            parents.append(rated_plants[i][1])
            child = [[], [], [], [], [], []]

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

                chance = (100 / len(children))
        if not all_children:
            print('ERR: No children found')
            return None
        return all_children, chance


def q_crossbreed(plants):  # quick crossbreed
    """Prunes the plant list and crossbreeds the 8 fittest plants
    returns list of all children of higher tier than parents"""
    all_combos = []
    plants = add_fitness(plants)  # sorts the plants by fitness then removes fitness value
    fittest_parent = max(plants)
    print(f'fittest_parent: {fittest_parent}')  # TODO: remove
    plants = remove_fitness(plants)
    plants = plants[:8]
    counter = 0
    results = []
    lock = threading.Lock()  # Add a lock to synchronize access to shared variables

    def crossbreed_helper(combination):
        nonlocal counter, results
        try:
            all_children, chance = crossbreed(combination)
            split_children = fitness_split(all_children, cutoff=fittest_parent[0])
            if split_children not in all_combos and split_children:
                with lock:
                    for child in split_children:
                        if child not in all_combos:
                            all_combos.append(child)
                            results.append([combination, child[1], chance, child[0]])
            counter += 1
        except:
            print('ERR: Crossbreed failed')

    threads = []
    for r in range(2, 9):
        for combination in itertools.combinations(plants, r):
            # Use threading to parallelize crossbreeding for each combination
            t = threading.Thread(target=crossbreed_helper, args=(combination,))
            t.start()
            threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    if results:
        results = output_sorter(results)
        return results
    else:
        print('ERR: No children of higher tier than parents found')
    return None
