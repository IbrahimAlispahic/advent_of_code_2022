from data import data, test_data, test_data1

import time

tic = time.perf_counter()


def move(direct, object, no_moves=1):
    if direct == "R":
        object[0] += no_moves
    elif direct == "L":
        object[0] -= no_moves
    elif direct == "U":
        object[1] += no_moves
    else:
        object[1] -= no_moves


def calc_distance(head_coord, tail_coord):
    # diagonal
    if abs(head_coord[0] - tail_coord[0]) == 1 and abs(head_coord[1] - tail_coord[1]) == 1:
        return 1
    if (abs(head_coord[0] - tail_coord[0]) == 2 and abs(head_coord[1] - tail_coord[1]) == 1) \
            or (abs(head_coord[0] - tail_coord[0]) == 1 and abs(head_coord[1] - tail_coord[1]) == 2):
        return 2
    return abs(head_coord[0] - tail_coord[0]) + abs(head_coord[1] - tail_coord[1])


dist_head_tail = 0
positions_set = set()

head_coord = [0, 0]

prev_head_coords = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
tail_coords = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

for line in data.splitlines():
    [direction, no_moves] = line.split()

    for i in range(int(no_moves)):
        move(direction, head_coord)

        dist_head_tail = calc_distance(head_coord, tail_coords[0])
        if dist_head_tail > 1:
            tail_coords[0] = prev_head_coords[0].copy()

        for j in range(1, 9):
            dist_head_tail = calc_distance(tail_coords[j-1], tail_coords[j])
            if dist_head_tail > 1:
                if tail_coords[j-1][0] > tail_coords[j][0]:
                    move("R", tail_coords[j])
                elif tail_coords[j-1][0] < tail_coords[j][0]:
                    move("L", tail_coords[j])
                if tail_coords[j-1][1] > tail_coords[j][1]:
                    move("U", tail_coords[j])
                elif tail_coords[j - 1][1] < tail_coords[j][1]:
                    move("D", tail_coords[j])

        position_str = "X" + str(tail_coords[8][0]) + "Y" + str(tail_coords[8][1])
        # print(position_str)
        positions_set.add(position_str)

        prev_head_coords[0] = head_coord.copy()

# print(tail_coords)
# print(positions_set)
print(len(positions_set))

toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
