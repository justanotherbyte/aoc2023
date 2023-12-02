with open("input.txt", "r") as f:
    games = f.readlines()

total = 0

for idx, game in enumerate(games, start=1):
    game = game.replace(f"Game {idx}: ", "")
    subsets = game.split("; ")

    game_possible = True
    for subset in subsets:
        cubes = subset.split(", ")
        for cube in cubes:
            count, name = cube.split(" ")
            name = name.strip()
            count = int(count)

            if name == "red" and count > 12:
                game_possible = False
            elif name == "green" and count > 13:
                game_possible = False
            elif name == "blue" and count > 14:
                game_possible = False

    if game_possible:
        total += idx

print(total)