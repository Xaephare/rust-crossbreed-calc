import csv
from random import randint


GEN_AMOUNT = 50
GENES = ('W', 'X', 'Y', 'G', 'H')


with open('rand_dataset.csv', 'w', newline='') as csvfile:
    data = csv.writer(csvfile)
    for i in range(GEN_AMOUNT):
        plant = ''.join(GENES[randint(0, 4)] for number in range(6))
        data.writerows([[plant]])