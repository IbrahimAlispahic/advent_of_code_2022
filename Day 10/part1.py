from data import data, test_data

import time

tic = time.perf_counter()


def add_to_signal(cycle_ctr, X):
    if cycle_ctr == 20 or (cycle_ctr - 20) % 40 == 0:
        signal.append(cycle_ctr * X)


cycle_ctr = 1
X = 1
signal = []

for instruction in data.splitlines():
    if instruction == "noop":
        add_to_signal(cycle_ctr, X)
        cycle_ctr += 1
    else:
        [_, value] = instruction.split()
        for i in range(2):
            add_to_signal(cycle_ctr, X)
            if i == 1:
                X += int(value)
            cycle_ctr += 1

print(signal)
print(sum(signal))
toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
