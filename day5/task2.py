import re
import threading

from tqdm import tqdm

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
        print(num_rows)
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
done_seeds = []

new_seed_nums = []
new_seed_sizes = []



flag = True
for seed in seed_numbers:
    if flag:
        new_seed_nums.append(seed)
        flag = False
    else:
        new_seed_sizes.append(seed)
        flag = True

total_seeds = sum(new_seed_sizes)
pbar = tqdm(total=total_seeds)

def calc_locs(sn: list[int]):
    for seed_num in sn:
        dest, _ = seed_num, seed_num

        for category in categories:
            lines = category_maps[category]
            for line in lines:
                mind, _ = line[0]
                mins, maxs = line[1]

                if dest in range(mins, maxs):
                    diff = (dest - mins)
                    dest = diff + mind
                    break

        locs.append(dest)
        pbar.update(1)
        # print(f"{seed_num} => {dest}")

t = []

for idx, seed in enumerate(new_seed_nums):
    size = new_seed_sizes[idx]
    r = range(seed, seed + size)
    thread = threading.Thread(target=calc_locs, args=(r,), daemon=True)
    t.append(thread)

for _t in t:
    _t.start()

for _t in t:
    _t.join()

print(min(locs))
pbar.close()