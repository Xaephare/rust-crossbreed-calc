PRUNE_THRESHOLD = 3

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
