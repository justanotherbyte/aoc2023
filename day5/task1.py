import re

with open("input.txt", "r") as f:
    lines = f.readlines()

def get_numbers_from_line(line: str) -> list[int]:
    return [
        int(line[m.start(): m.end()])
        for m in re.finditer(r"\d+", line)
    ]

def get_category_map_name(line: str) -> str | None:
    re_match = re.match(r"^(.*?)(map:)", line)
    if not re_match:
        return None
    
    group = re_match.group(1)
    if not group:
        return None
    return group

seed_numbers = get_numbers_from_line(lines[0])
category_maps = {}

last_category_map = None
num_rows = []

def expand_nums(nums: list[int]) -> list[tuple[int, int]]:
    drs, srs, rl = nums
    mind, maxd = drs, drs + rl
    mins, maxs = srs, srs + rl
    return [
        (mind, maxd),
        (mins, maxs)
    ]

categories = []

for idx, line in enumerate(lines):
    if line == "\n" or idx == 0:
        continue
    
    category_map_name = get_category_map_name(line.strip())
    if category_map_name:
        category_maps[last_category_map] = num_rows.copy()
        num_rows.clear()
        last_category_map = category_map_name
        categories.append(category_map_name)
    else:
        nums = get_numbers_from_line(line.strip())
        num_rows.append(expand_nums(nums))

    if idx == len(lines) - 1:
        category_maps[last_category_map] = num_rows.copy()
        break

del category_maps[None]

locs = []

for seed_num in seed_numbers:
    dest, src = seed_num, seed_num

    for idx, category in enumerate(categories):
        lines = category_maps[category]
        for line in lines:
            mind, maxd = line[0]
            mins, maxs = line[1]

            if dest in range(mins, maxs):
                diff = (dest - mins)
                dest = diff + mind
                break

    locs.append(dest)


print(min(locs))