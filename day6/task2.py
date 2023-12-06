import re

from tqdm import tqdm

def get_nums(line: str) -> list[int]:
    return [
        int(line[m.start(): m.end()])
        for m in re.finditer(r"\d+", line)
    ]

def calc_distance(speed: int, time: int) -> int:
  return speed * time

with open("input.txt", "r") as f:
    lines = f.readlines()

times, distances = get_nums(lines[0]), get_nums(lines[1])
_time = ""
_distance = ""

for t in times:
    _time += str(t)

for d in distances:
    _distance += str(d)

times = [int(_time)]
distances = [int(_distance)]

out = 1

for idx, time in enumerate(times):
    distance = distances[idx]

    ds = []
    for hold_time in tqdm(range(time)):
        time_travelling = time - hold_time
        speed = hold_time
        d = calc_distance(speed, time_travelling)
        ds.append(d)

    ways_to_beat = 0
    for d in tqdm(ds):
        if d > distance:
            ways_to_beat += 1


    out *= ways_to_beat

print(out)