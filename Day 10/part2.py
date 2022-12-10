from data import data, test_data

import time

tic = time.perf_counter()


def draw_pixel(cycle_ctr, X):
    new_line = "\n" if cycle_ctr % 40 == 0 else ""
    if abs(((cycle_ctr-1) % 40) - X) <= 1:
        symbol = "#"
    else:
        symbol = " "
    print(symbol, end=new_line)


cycle_ctr = 1
X = 1
pixel_pos = 0

for instruction in data.splitlines():
    if instruction == "noop":
        draw_pixel(cycle_ctr, X)
        cycle_ctr += 1
    else:
        [_, value] = instruction.split()
        for i in range(2):
            draw_pixel(cycle_ctr, X)
            if i == 1:
                X += int(value)
            cycle_ctr += 1


toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
