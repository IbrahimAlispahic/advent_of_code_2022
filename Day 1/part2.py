from data import data, test_data
import numpy as np
import time

tic = time.perf_counter()

ctr = 0
max_ctr = np.array([0, 0, 0])

for line in data.splitlines():
    if line != '':
        ctr = ctr + int(line)
    else:
        if min(max_ctr) < ctr:
            index = np.where(max_ctr == min(max_ctr))[0][0]
            max_ctr[index] = ctr
        ctr = 0

toc = time.perf_counter()

print(max_ctr)
print(sum(max_ctr))

print(f"Execution time is {toc - tic:0.4f} seconds")


