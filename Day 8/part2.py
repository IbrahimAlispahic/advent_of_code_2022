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
scentic_score = []
for row in forest:
    column_ctr = 0
    for element in row:
        top_ctr = 0
        for i in reversed(range(row_ctr)):
            top_ctr += 1
            if forest[i, column_ctr] >= element:
                break
        bottom_ctr = 0
        for i in range(row_ctr+1, len(row)):
            bottom_ctr += 1
            if forest[i, column_ctr] >= element:
                break
        left_ctr = 0
        for i in reversed(range(column_ctr)):
            left_ctr += 1
            if forest[row_ctr, i] >= element:
                break
        right_ctr = 0
        for i in range(column_ctr+1, len(row)):
            right_ctr += 1
            if forest[row_ctr, i] >= element:
                break

        scentic_score.append(top_ctr * bottom_ctr * left_ctr * right_ctr)
        column_ctr += 1
    row_ctr += 1

# print(scentic_score)
print(max(scentic_score))
toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
