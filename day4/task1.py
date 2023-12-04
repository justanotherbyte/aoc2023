import re

with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

for idx, line in enumerate(lines):
    _, line = line.split(":")
    line = line.strip()

    winning_half, my_half = line.split(" | ")
    winning_nums = [
        int(winning_half[m.start(): m.end()])
        for m in re.finditer(r"\d+", winning_half)
    ]
    my_nums = [
        int(my_half[m.start(): m.end()])
        for m in re.finditer(r"\d+", my_half)
    ]

    winning_nums = set(winning_nums)
    my_nums = set(my_nums)
    matches = len(my_nums.intersection(winning_nums))

    if matches > 0:
        total += 2 ** (matches - 1)

print(total)
