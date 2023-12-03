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

def is_adjacent(pos: int, start: int, end: int, *, backwards: bool) -> bool:
    if backwards:
        if end == pos:
            return True
        elif (end - 1) == pos:
            return True
        elif (end - 1) == pos + 1:
            return True
        else:
            return False
    else:
        if start == pos:
            return True
        elif (start - pos) == 1:
            return True
        else:
            return False

def get_number(row: str, pos: int, *, backwards: bool = False) -> int | None:
    for match in re.finditer(r'\d+', row):
        start, end = match.span()
        if is_adjacent(pos, start, end, backwards=backwards):
            return int(row[start: end])
        
    return None

def get_adjacent_numbers_in_row(row: str, pos: int) -> list[int | None]:
    return [
        get_number(row, pos, backwards=True),
        get_number(row, pos)
    ]

def get_truthies(values: list[int | None]) -> list[int]:
    truthies = []
    for value in values:
        if value:
            truthies.append(value)

    return truthies

for row_idx, row in enumerate(sanitized_lines):
    for match in re.finditer(r"[*]", row):
        pos, _ = match.span()

        before_prev_row, after_prev_row = get_adjacent_numbers_in_row(sanitized_lines[row_idx - 1], pos)
        before_this_row, after_this_row = get_adjacent_numbers_in_row(row, pos)
        before_next_row, after_next_row = get_adjacent_numbers_in_row(sanitized_lines[row_idx + 1], pos)

        adjacents = get_truthies([
            before_prev_row,
            after_prev_row,
            before_next_row,
            after_next_row,
            before_this_row,
            after_this_row
        ])
        adjacents = list(set(adjacents))

        if len(adjacents) == 2:
            multiplied = adjacents[0] * adjacents[1]
            total += multiplied

print(total)