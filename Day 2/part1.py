from data import data, test_data
import time

tic = time.perf_counter()

total_score = 0

for line in data.splitlines():
    mine = line.split()[1]

    current_score = 0
    if mine == 'X':
        current_score += 1
    elif mine == 'Y':
        current_score += 2
    else:
        current_score += 3

    if line == 'A Y' or line == 'B Z' or line == 'C X':
        current_score += 6
    elif line == 'A X' or line == 'B Y' or line == 'C Z':
        current_score += 3
    else:
        current_score += 0

    total_score += current_score


print(total_score)

toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
