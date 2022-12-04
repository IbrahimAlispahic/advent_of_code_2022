from data import data, test_data
import time

tic = time.perf_counter()

no_overlap_ctr = 0
line_ctr = 0

for line in data.splitlines():
    line_ctr += 1
    assignment_pairs = line.split(",")

    first_pair = [int(i) for i in assignment_pairs[0].split("-")]
    second_pair = [int(i) for i in assignment_pairs[1].split("-")]

    if (first_pair[1] < second_pair[0]) or (first_pair[0] > second_pair[1]):
        no_overlap_ctr += 1


print(line_ctr - no_overlap_ctr)

toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
