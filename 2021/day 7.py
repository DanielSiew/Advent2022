import time

file = open("input.txt", "r")
text = file.readlines()


def part_one():
    st = time.time()

    line = text[0].strip()
    crabs = [int(crab) for crab in line.split(',')]

    all_fuel_used = []
    for value in range(min(crabs), max(crabs)):
        fuel_used = 0
        for crab in crabs:
            fuel_used += abs(crab - value)

        all_fuel_used.append(fuel_used)

    output = sorted(all_fuel_used)[0]

    et = time.time()
    elapsed_time = et - st

    print(f"Part One:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms\n")


def part_two():
    st = time.time()

    line = text[0].strip()
    crabs = [int(crab) for crab in line.split(',')]

    all_fuel_used = []
    for value in range(min(crabs), max(crabs)):
        fuel_used = 0
        for crab in crabs:
            difference = abs(crab - value)
            for magnitude in range(1, difference + 1):
                fuel_used += magnitude

        all_fuel_used.append(fuel_used)

    output = sorted(all_fuel_used)[0]

    et = time.time()
    elapsed_time = et - st

    print(f"Part Two:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms")


part_one()
part_two()
