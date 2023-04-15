class BitConverter:
    def __init__(self):
        pass
            
    def bit_vector_convert(self, binary_plant):
        '''Converts a string binary plant gene to an integer bit vector'''
        bit_vector = []
        for gene in binary_plant:
            if gene == '1':
                bit_vector.append(1)
            else:
                bit_vector.append(0)
        return bit_vector

    def binary_plant(self, plant_list):
        '''Converts a list of plants to a list of bit vectors'''
        all_plants_binary = []
        genes = [[bit for bit in plant] for plant in plant_list]
        gene_dict = {
            'W': '100',
            'X': '101',
            'Y': '000',
            'G': '001',
            'H': '010'
        }

        for item in genes:
            binary_plant = ''.join([gene_dict[gene] for gene in item if gene in gene_dict])
            all_plants_binary.append(self.bit_vector_convert(binary_plant))
        return all_plants_binary

    def triplet_convert(self, bit_vector):
        '''Converts a bit vector to a list of string triplets'''
        triplets = []
        for i in range(0, len(bit_vector), 3):
            triplet = ''.join(str(bit) for bit in bit_vector[i:i+3])
            triplets.append(triplet)
        return triplets

    def string_plant(self, bit_vector_list):
        '''Converts a list of bit vectors to a list of string plant genes'''
        gene_dict = {
            '100': 'W',
            '101': 'X',
            '000': 'Y',
            '001': 'G',
            '010': 'H'
        }
        all_plants_string = []
        for plant in bit_vector_list:
            string_plant = ''.join([gene_dict[triplet] for triplet in self.triplet_convert(plant) if triplet in gene_dict])
            all_plants_string.append(string_plant)
        return all_plants_string
