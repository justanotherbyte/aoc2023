import re

with open("input.txt", "r") as f:
    lines = f.readlines()

total = 1

def get_win_count(line: str) -> int:
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

    return matches

def clean_line(line: str) -> str:
    _, line = line.split(":")
    line = line.strip()
    return line

cards = [1] * len(lines)

for idx, line in enumerate(lines):
    line = clean_line(line)
    wins = get_win_count(line)
    cards[idx] += wins
    next_indexes = list(range(idx + 1, idx + 1 + wins))
    for nidx in next_indexes:
        cards[nidx] += cards[idx]

print(sum(cards))