from data import data, test_data1, test_data2, test_data3, test_data4
import time

tic = time.perf_counter()

char_ctr = 0
marker = ''
for character in data:
    char_ctr += 1
    marker += character

    if len(set(marker)) != len(marker):
        marker = marker[1:]

    if len(marker) == 4 and len(set(marker)) == len(marker):
        break

print(marker)
print(char_ctr)

toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
