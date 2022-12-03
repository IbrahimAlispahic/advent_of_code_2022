from data import data, test_data
import time

tic = time.perf_counter()

sum_of_priorities = 0
letter_value = 0

for line in data.splitlines():
    res_first = line[0:len(line) // 2]
    res_second = line[len(line) // 2:]

    common_letter = list(set(res_first) & set(res_second))[0]
    if 'a' <= common_letter <= 'z':
        letter_value = ord(common_letter)-ord('a')+1
    elif 'A' <= common_letter <= 'Z':
        letter_value = ord(common_letter)-ord('A')+27

    sum_of_priorities += letter_value


print(sum_of_priorities)

toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
