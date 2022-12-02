from data import data, test_data
import time

tic = time.perf_counter()

total_score = 0

for line in data.splitlines():
    need_to_play = line.split()[1]  # X lose, Y draw, Z win

    current_score = 0
    if need_to_play == 'X':
        current_score += 0
    elif need_to_play == 'Y':
        current_score += 3
    else:
        current_score += 6

    if line == 'A Y' or line == 'B X' or line == 'C Z':
        current_score += 1
    elif line == 'A X' or line == 'B Z' or line == 'C Y':
        current_score += 3
    else:
        current_score += 2

    total_score += current_score


print(total_score)

toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
