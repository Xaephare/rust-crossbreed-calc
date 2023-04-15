import csv
from random import randint

genes = ['W', 'X', 'Y', 'G', 'H']

with open('rand-dataset.csv', 'w', newline='') as csvfile:
    data = csv.writer(csvfile)
    for i in range(50):
        plant = ''.join(genes[randint(0, 4)] for i in range(6))
        data.writerows([[plant]])