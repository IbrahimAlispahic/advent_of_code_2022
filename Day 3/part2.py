from data import data, test_data
import time

tic = time.perf_counter()

sum_of_priorities = 0
letter_value = 0
line_ctr = 0

for line in data.splitlines():
    if line_ctr == 0:
        first_elf = line
        line_ctr += 1
    elif line_ctr == 1:
        second_elf = line
        line_ctr += 1
    elif line_ctr == 2:
        third_elf = line
        common_letter = list(set(first_elf) & set(second_elf) & set(third_elf))[0]
        if 'a' <= common_letter <= 'z':
            letter_value = ord(common_letter) - ord('a') + 1
        elif 'A' <= common_letter <= 'Z':
            letter_value = ord(common_letter) - ord('A') + 27

        sum_of_priorities += letter_value
        line_ctr = 0


print(sum_of_priorities)

toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
