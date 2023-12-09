import re

with open("input.txt", "r") as f:
    lines = f.readlines()

def extract_nums(line: str) -> list[int]:
    matches = re.finditer(r"-?\d+", line)
    return [
        int(line[m.start(): m.end()])
        for m in matches
    ]

def calc_differences(nums: list[int]) -> list[int]:
    diffs = []
    for idx in range(0, len(nums) - 1):
        num1 = nums[idx]
        num2 = nums[idx + 1]
        diffs.append(num2 - num1)

    return diffs

def check_all_zeroes(diffs: list[int]) -> bool:
    return diffs == [0] * len(diffs)

def generate_sequences(line: str) -> list[list[int]]:
    nums = extract_nums(line)
    finished = False
    s = []
    s.append(nums)
    while not finished:
        new_nums = calc_differences(nums)
        if check_all_zeroes(new_nums):
            finished = True
        else:
            nums = new_nums

        s.append(new_nums)

    return s

def append_zeroes(sequences: list[list[int]]):
    for seq in sequences:
        seq.append(0)

terms = []

for line in lines:
    s = generate_sequences(line)
    append_zeroes(s)
    for idx in range(len(s) - 2, -1, -1):
        s[idx][-1] = s[idx][-2] + s[idx + 1][-1]

    terms.append(s[0][-1])

print(sum(terms))