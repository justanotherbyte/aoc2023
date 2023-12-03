import re

with open("input.txt", "r") as f:
    lines = f.readlines()

all_nums = {}
total = 0

sanitized_lines = []
for line in lines:
    new_line = line.strip()
    sanitized_lines.append(new_line)

max_idx = len(sanitized_lines[0].strip()) - 1

for row_idx, row in enumerate(sanitized_lines):
    nums = []
    for match in re.finditer(r'\d+', row):
        start, end = match.span()
        indexes = list(range(start, end))
        number = row[start: end]
        nums.append((number, indexes))

    all_nums[row_idx] = nums

def special_character_in_indexes(s: str, indexes: list[int]) -> bool:
    for idx in indexes:
        if s[idx] != "." and not s[idx].isdigit():
            return True

    return False

def adjacent_to_special_character(row_idx: int, num_idxs: list[int]) -> bool:
    check_idxs = num_idxs.copy()
    check_idxs.insert(0, min(num_idxs) - 1 if min(num_idxs) > 0 else 0)
    check_idxs.append(max(num_idxs) + 1 if max(num_idxs) < max_idx else max_idx)

    if row_idx == 0:
        # first one
        # we just check the row after
        return special_character_in_indexes(sanitized_lines[row_idx + 1], check_idxs)
    if row_idx == len(sanitized_lines) - 1:
        # last one
        # check row before
        return special_character_in_indexes(sanitized_lines[row_idx - 1], check_idxs)
    
    in_before_row = special_character_in_indexes(sanitized_lines[row_idx - 1], check_idxs)
    in_after_row = special_character_in_indexes(sanitized_lines[row_idx + 1], check_idxs)
    in_row = special_character_in_indexes(sanitized_lines[row_idx], check_idxs)

    return in_before_row or in_after_row or in_row

for (row_idx, num_info) in all_nums.items():
    for (num, idxs) in num_info:
        if adjacent_to_special_character(row_idx, idxs):
            total += int(num)

print(total)