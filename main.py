import csv

from non_bin_crossbreeder import CrossBreeder

plants = []

with open('rand_dataset.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        plants.append(row[0])

# fittest = CrossBreeder().fitness(plants)
# print(fittest) 

quick_options = CrossBreeder().q_crossbreed(plants)
print(f"quick_options: {quick_options}")

# bit_vector_list = BitConverter().binary_plant(plants)
# pruned = CrossBreeder().prune(bit_vector_list)

# with open('binary_plants.csv', 'w', newline='') as csvfile:
#     data = csv.writer(csvfile)
#     for plant in bit_vector_list:
#         data.writerow(plant)

# crossbreeds = CrossBreeder().crossbreed(bit_vector_list)
