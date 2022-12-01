from data import data, test_data
import time

tic = time.perf_counter()

ctr = 0
max_ctr = 0

for line in test_data.splitlines():
    if line != '':
        ctr = ctr + int(line)
    else:
        if ctr > max_ctr:
            max_ctr = ctr
        ctr = 0

toc = time.perf_counter()

print(max_ctr)

print(f"Execution time is {toc - tic:0.4f} seconds")
