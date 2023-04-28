import csv
import time

from crossbreeder import q_crossbreed

plants = []

with open('rand_dataset.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        plants.append(row[0])

start_time = time.perf_counter()

quick_options = q_crossbreed(plants)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Quick options: {quick_options}")
print("Elapsed time: {:.2f} seconds".format(elapsed_time))
