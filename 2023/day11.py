import time


def part_one(file):
    st = time.perf_counter_ns()

    _map = []
    indices = []
    empty = [[], []]

    for idx, line in enumerate(file):
        _map.append([i for i in line.strip()])
        if len(set(line.strip())) == 1 and line[0] == ".":
            empty[0].append(idx)

    for i in range(len(_map[0])):
        dub = True
        for j in range(len(_map)):
            if _map[j][i] == "#":
                dub = False
                break
        if dub:
            empty[1].append(i)

    for y, i in enumerate(_map):
        for x, j in enumerate(i):
            if j == "#":
                indices.append([y, x])

    res = 0

    for idx, i in enumerate(indices[:-1]):
        for j in indices[idx+1:]:
            additional = 0

            for row in empty[0]:
                additional += (j[0] <= row <= i[0] or i[0] <= row <= j[0])
            for col in empty[1]:
                additional += (j[1] <= col <= i[1] or i[1] <= col <= j[1])

            res += abs(j[1] - i[1]) + abs(j[0] - i[0]) + additional

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")

    return res


def part_two(file):
    st = time.perf_counter_ns()

    _map = []
    indices = []
    empty = [[], []]

    for idx, line in enumerate(file):
        _map.append([i for i in line.strip()])
        if len(set(line.strip())) == 1 and line[0] == ".":
            empty[0].append(idx)

    for i in range(len(_map[0])):
        dub = True
        for j in range(len(_map)):
            if _map[j][i] == "#":
                dub = False
                break
        if dub:
            empty[1].append(i)

    for y, i in enumerate(_map):
        for x, j in enumerate(i):
            if j == "#":
                indices.append([y, x])

    res = 0

    for idx, i in enumerate(indices[:-1]):
        for j in indices[idx+1:]:
            additional = 0

            for row in empty[0]:
                additional += (j[0] < row < i[0] or i[0] < row < j[0]) * 999_999
            for col in empty[1]:
                additional += (j[1] < col < i[1] or i[1] < col < j[1]) * 999_999

            res += abs(j[1] - i[1]) + abs(j[0] - i[0]) + additional

    et = time.perf_counter_ns()
    elapsed = et - st
    print("\nExecution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")

    return res

print("Part one:", part_one(open("input.txt", "r")))
print("Part two:", part_two(open("input.txt", "r")))

