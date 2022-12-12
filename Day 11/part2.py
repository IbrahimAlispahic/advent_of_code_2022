import math

from data import data, test_data

import time
import re

tic = time.perf_counter()

monkeys = [{}, {}, {}, {}, {}, {}, {}, {}]
curr_monkey = 0

for line in data.splitlines():
    if line.startswith("Monkey"):
        curr_monkey = re.search("[0-9]", line).group()
        curr_monkey = int(curr_monkey)
    elif line.startswith("  Starting items"):
        [_, starting_items] = line.split("Starting items: ")
        starting_items = starting_items.split(", ")
        starting_items = [eval(i) for i in starting_items]
        monkeys[curr_monkey]["items"] = starting_items
    elif line.startswith("  Operation"):
        operation = "+" if line.find("+") != -1 else "*"
        monkeys[curr_monkey]["operation"] = operation
        operand = line.split(operation + " ")[1]
        monkeys[curr_monkey]["operand"] = operand

    elif line.startswith("  Test"):
        devisible_by = line.split("  Test: divisible by ")[1]
        monkeys[curr_monkey]["devisible_by"] = int(devisible_by)
    elif line.startswith("    If true:"):
        throw_to_true = re.search("[0-9]", line).group()
        monkeys[curr_monkey]["throw_to_true"] = int(throw_to_true)
    elif line.startswith("    If false:"):
        throw_to_false = re.search("[0-9]", line).group()
        monkeys[curr_monkey]["throw_to_false"] = int(throw_to_false)
    monkeys[curr_monkey]["inspect_ctr"] = 0

print(monkeys)

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]
MOD = math.prod(PRIMES)

for i in range(10000):
    print(i)
    for monkey in monkeys:
        for item in range(len(monkey["items"])):
            # print(monkey["items"][0])
            monkey["inspect_ctr"] += 1
            if monkey["operand"] == "old":
                monkey["items"][0] = monkey["items"][0] ** 2
                testy = monkey["items"][0]
            elif monkey["operation"] == "*":
                monkey["items"][0] *= int(monkey["operand"])
            else:
                monkey["items"][0] += int(monkey["operand"])

            monkey["items"][0] = monkey["items"][0] % MOD

            if monkey["items"][0] % monkey["devisible_by"] == 0:
                monkey_index = monkey["throw_to_true"]
                monkeys[monkey_index]["items"].append(monkey["items"][0])
                monkey["items"].pop(0)
            else:
                monkey_index = monkey["throw_to_false"]
                monkeys[monkey_index]["items"].append(monkey["items"][0])
                monkey["items"].pop(0)


ctrs = []
[ctrs.append(monkey["inspect_ctr"]) for monkey in monkeys]
monkey_business = 1
monkey_business *= max(ctrs)
ctrs.remove(max(ctrs))
monkey_business *= max(ctrs)


print(monkeys)
print(monkey_business)
toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")
