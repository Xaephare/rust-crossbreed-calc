import csv
from bit_converter import BitConverter


plants = []

with open('binary_plants.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        plants.append(row)

bit_vector_list = BitConverter().binary_plant(plants)

with open('binary_plants.csv', 'w', newline='') as csvfile:
    data = csv.writer(csvfile)
    for plant in bit_vector_list:
        data.writerow(plant)
