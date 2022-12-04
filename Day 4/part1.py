from data import data, test_data
import time

tic = time.perf_counter()

contain_ctr = 0

for line in data.splitlines():
    assignment_pairs = line.split(",")

    first_pair = [int(i) for i in assignment_pairs[0].split("-")]
    second_pair = [int(i) for i in assignment_pairs[1].split("-")]

    if (first_pair[0] <= second_pair[0] and first_pair[1] >= second_pair[1]) or (first_pair[0] >= second_pair[0] and first_pair[1] <= second_pair[1]):
        contain_ctr += 1


print(contain_ctr)

toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
