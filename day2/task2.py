with open("input.txt", "r") as f:
    games = f.readlines()

total = 0

for idx, game in enumerate(games, start=1):
    game = game.replace(f"Game {idx}: ", "")
    subsets = game.split("; ")

    game_possible = True
    colours = {
        "red": [],
        "blue": [],
        "green": []
    }
    for subset in subsets:
        cubes = subset.split(", ")
        for cube in cubes:
            count, name = cube.split(" ")
            name = name.strip()
            count = int(count)

            colours[name].append(count)

    power = 1
    for colour, counts in colours.items():
        highest = max(counts)
        power *= highest
    
    total += power

print(total)