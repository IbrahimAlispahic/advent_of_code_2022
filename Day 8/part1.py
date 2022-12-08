from data import data, test_data

import time
import numpy as np

tic = time.perf_counter()

forest = []
for line in data.splitlines():
    row = []
    for tree in line:
        row.append(int(tree))
    forest.append(row)

forest = np.array(forest)
# print(forest)

visible_ctr = 0
row_ctr = 0
for row in forest:
    column_ctr = 0
    for element in row:
        # print(forest[row_ctr, column_ctr])
        # print(forest[:row_ctr, column_ctr]) # iznad
        # print(forest[row_ctr+1:, column_ctr]) # ispod
        # print(forest[row_ctr, :column_ctr]) # lijevo
        # print(forest[row_ctr, column_ctr+1:]) # desno

        if np.all(forest[:row_ctr, column_ctr] < element) or np.all(forest[row_ctr+1:, column_ctr] < element)\
                or np.all(forest[row_ctr, :column_ctr] < element) or np.all(forest[row_ctr, column_ctr+1:] < element):
            visible_ctr += 1
        column_ctr += 1
    row_ctr += 1

print(visible_ctr)
toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
