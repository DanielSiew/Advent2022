import time
import math


def part_one(file):
    st = time.perf_counter_ns()
    file = list(file.readlines())
    instruction = [i for i in file[0].strip()]

    maps = {}
    for line in file[2:]:
        key, val = line.split("=")
        key = key.strip()
        val = tuple(val.strip()[1:-1].split(", "))
        maps[key] = val

    steps = 0
    current = "AAA"

    while current != "ZZZ":
        for i in instruction:
            if i == "L":
                current = maps[current][0]
            else:
                current = maps[current][1]
            steps += 1
            if current == "ZZZ":
                break
        if current == "ZZZ":
            break

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")

    return steps


def part_two(file):
    st = time.perf_counter_ns()
    file = list(file.readlines())
    instruction = [i for i in file[0].strip()]

    starts = []

    maps = {}
    for line in file[2:]:
        key, val = line.split("=")
        key = key.strip()
        if key[-1] == "A":
            starts += [[key, 0]]
        val = tuple(val.strip()[1:-1].split(", "))
        maps[key] = val

    steps = 0

    hits = [False] * len(starts)
    final = [0] * len(starts)

    while not all(hits):
        for i in instruction:
            for idx, label in enumerate(starts):
                if i == "L":
                    starts[idx] = [maps[label[0]][0], starts[idx][1] + 1]
                else:
                    starts[idx] = [maps[label[0]][1], starts[idx][1] + 1]

                if starts[idx][0][-1] == "Z":
                    hits[idx] = True
                    final[idx] = starts[idx][1]

    final = math.lcm(*final)

    et = time.perf_counter_ns()
    elapsed = et - st
    print("\nExecution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")

    return final


print("Part one:", part_one(open("input.txt", "r")))
print("Part two:", part_two(open("input.txt", "r")))

