from data import data, test_data
import time
import re

tic = time.perf_counter()

stack = {}
for i in range(9):
    stack.update({i+1: []})

reading_stack = True

for line in data.splitlines():
    if line != '' and reading_stack:
        index = 1
        for i in range(len(stack)):
            if line[index] != ' ':
                stack[i+1].append(line[index])
            index += 4
    elif line == '':
        reading_stack = False
    else:
        [no_of_moves, from_position, to_position] = [int(x.group()) for x in re.finditer(r'\d+', line)]
        for x in range(no_of_moves):
            stack[to_position].insert(0, stack[from_position][no_of_moves - x - 1])
            stack[from_position].pop(no_of_moves - x - 1)


print(''.join([stack[i][0] for i in stack]))

toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
