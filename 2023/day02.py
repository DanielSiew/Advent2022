# oneliners are at the bottom
import math
import timeit


def part_one(file):
    total = 0

    cubes = {
        "blue": 0,
        "red": 0,
        "green": 0
    }

    for line in file:
        invalid = False
        game, rest = line.split(":")
        *_, game = game.split(" ")
        game = game.strip()
        game = int(game)
        sets = rest.split(";")

        for one in sets:
            cubes_set = one.split(", ")
            for cube in cubes_set:
                cube = cube.strip()
                num, name = cube.split(" ")
                cubes[name] += int(num)

            if any([cubes["red"] > 12, cubes["green"] > 13, cubes["blue"] > 14]):
                invalid = True

            for i in ["blue", "red", "green"]: cubes[i] = 0

        if not invalid:
            total += game

    return total


def part_two(file):
    total = 0

    for line in file:
        _, rest = line.split(":")
        sets = rest.split(";")

        cubes = {
            "blue": 0,
            "red": 0,
            "green": 0
        }

        minimum = [0, 0, 0]

        for one in sets:
            cubes_set = one.split(", ")
            for cube in cubes_set:
                cube = cube.strip()
                num, name = cube.split(" ")
                cubes[name] += int(num)

            for idx, i in enumerate(["blue", "red", "green"]):
                minimum[idx] = max(minimum[idx], cubes[i])
                cubes[i] = 0

        total += math.prod(minimum)

    return total


print("Part 1:", part_one(open("input.txt", "r")))
print("\nPart 2:", part_two(open("input.txt", "r")))

# welcome to the messy one-line zone
print("\nPart 1:", (sum(game[0] if all([not any([part[0] > 12, part[1] > 13, part[2] > 14]) for part in
[[sum([int(_set[0]) for _set in _sets if _set[1] == col]) for col in ["red", "green", "blue"]] for _sets
in game[1]]]) else 0 for game in [[int(line[0].split(" ")[-1]), [[cube.strip().split(" ") for cube in
cubes.split(",")] for cubes in line[1].split(";")]] for line in [line.split(":") for line in [lines.strip()
for lines in open("input.txt", "r").readlines()]]])))


print("\nPart 2:", sum(math.prod(j[0][n*3:n*3+3]) for j in [[i, len(i)] for i in [[max(color) for color in
[[part[n] for part in[[sum([int(_set[0]) for _set in _sets if _set[1] == col]) for col in ["red", "green",
"blue"]] for _sets in game[1]]] for game in [[int(line[0].split(" ")[-1]), [[cube.strip().split(" ") for cube
in cubes.split(",")] for cubes in line[1].split(";")]] for line in [line.split(":") for line in [lines.strip()
for lines in open("input.txt", "r").readlines()]]] for n in range(3)]]]] for n in range(j[1]//3)))


