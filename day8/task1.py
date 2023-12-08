from typing import Generator


with open("input.txt", "r") as f:
    lines = f.readlines()

def iterate_instructions(line: str) -> Generator[str, None, None]:
    line = line.strip()
    current_idx = 0
    while True:
        try:
            _ = line[current_idx]
        except IndexError:
            current_idx = 0

        yield line[current_idx]
        current_idx += 1

def parse_node(line: str):
    element, values = line.split(" = ")
    values = values.strip("()")
    values = values.split(", ")
    return (element, values)

network = {}

for idx, line in enumerate(lines):
    if idx < 2:
        continue
    
    node = parse_node(line.strip())
    network[node[0]] = node[1]

steps = 0
current_key = "AAA"

for instruction in iterate_instructions(lines[0]):
    steps += 1
    pair = network[current_key]
    loc = None
    if instruction == "L":
        loc = pair[0]
    else:
        loc = pair[1]

    if loc == "ZZZ":
        break

    current_key = loc

print(steps)