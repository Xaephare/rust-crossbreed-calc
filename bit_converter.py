class BitConverter:
    def __init__(self):
        pass
            
    def bit_vector_convert(self, binary_plant):
        bit_vector = []
        for gene in binary_plant:
            if gene == '1':
                bit_vector.append(1)
            else:
                bit_vector.append(0)
        return bit_vector

    def binary_plant(self, plant_list):
        all_plants_binary = []
        genes = [[bit for bit in plant[0]] for plant in plant_list]
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