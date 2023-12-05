import timeit
from copy import copy


def part_one(file):
    file = list(file)
    maps = {}
    name = ""

    seeds = list(map(int, file[0].split(":")[-1].strip().split(" ")))

    for line in file[2:]:
        if not line[0].isalnum():
            continue
        if line[0].isalpha():
            name = "->".join(line.split(" ")[0].strip().split("-")[0:3:2])
            maps[name] = {}
            continue
        destination, source, length = map(int, [i.strip() for i in line.split(" ")])
        maps[name][repr([source, source + length - 1])] = [destination, destination + length - 1]

    for name in maps:
        cur = maps[name]
        for index, seed in enumerate(seeds):
            for _range in cur:
                _range = eval(_range)
                if _range[0] <= seed <= _range[1]:
                    seeds[index] = seed - _range[0] + cur[repr(_range)][0]

    return min(seeds)


def part_two(file):
    file = list(file)
    maps = {}
    name = ""
    seeds = []

    old_seeds = list(map(int, file[0].split(":")[-1].strip().split(" ")))
    for index, seed in enumerate(old_seeds[::2]):
        index = 2*index
        seeds.append([seed, seed + old_seeds[index+1] - 1])

    for line in file[2:]:
        if not line[0].isalnum():
            continue
        if line[0].isalpha():
            name = "->".join(line.split(" ")[0].strip().split("-")[0:3:2])
            maps[name] = {}
            continue
        destination, source, length = map(int, [i.strip() for i in line.split(" ")])
        maps[name][repr([source, source + length - 1])] = [destination, destination + length - 1]

    def check_all(seed_indices, level, limit):
        res = []
        additional = []
        counter = 0
        cur = maps[list(maps.keys())[level]]
        start, end = seed_indices
        for src, dst in cur.items():
            source_start, source_end = eval(src)
            destination_start, destination_end = dst
            if end < source_start or start > source_end:
                counter += 1
                continue
            if source_start <= start <= end <= source_end:
                res.append([destination_start + start - source_start, destination_start + end - source_start])
            elif start < source_start <= end <= source_end:
                res.append([destination_start, destination_start + end - source_start])
                additional += check_all([start, source_start - 1], level, limit)
            elif source_start <= start <= source_end < end:
                res.append([destination_start + start - source_start, destination_end])
                additional += check_all([source_end + 1, end], level, limit)
            elif start < source_start < source_end < end:
                res.append([destination_start, destination_end])
                additional += check_all([start, source_start - 1], level, limit)
                additional += check_all([source_end + 1, end], level, limit)

        res += additional

        if counter >= limit:
            res += [seed_indices]

        res = [eval(i) for i in set([repr(j) for j in res])]

        return res

    final = copy(seeds)

    for i, current in enumerate(maps):
        new = []
        for seed in final:
            new += check_all(seed, i, len(maps[current]))
        final = copy(new)

    return sorted(final, key=lambda x: x[0])[0][0]


print("Part one:", part_one(open("input.txt", "r")))
print("\nPart two:", part_two(open("input.txt", "r")))


# print("Part one:", f'{part_one(open("input.txt", "r")):<10}', f'(execution time: {timeit.timeit(repr(part_one(open("input.txt", "r"))), number=10_000_000)}s)')
# print("\nPart two:", f'{part_two(open("input.txt", "r")):<10}', f'(execution time: {timeit.timeit(repr(part_one(open("input.txt", "r"))), number=10_000000)}s)')