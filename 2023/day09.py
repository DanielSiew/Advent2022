import time


def get_differences(lst, running):
    if len(set(lst)) == 1 and lst[0] == 0:
        return running
    _next = list(map(lambda x: lst[x + 1] - lst[x], range(len(lst) - 1)))
    running.append(_next)
    return get_differences(_next, running)


def part_one(file):
    st = time.perf_counter_ns()

    total = 0
    for line in file:
        starting = list(map(int, line.strip().split(" ")))
        differences = get_differences(starting, [starting])

        for index, lst in enumerate(differences[::-1]):
            if index == 0:
                differences[len(differences) - index - 1].append(0)
                continue
            new = lst[-1] + differences[len(differences) - index][-1]
            differences[len(differences) - index - 1].append(new)

        total += differences[0][-1]


    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")

    return total


def part_two(file):
    st = time.perf_counter_ns()

    total = 0
    for line in file:
        starting = list(map(int, line.strip().split(" ")))
        differences = get_differences(starting, [starting])

        for index, lst in enumerate(differences[::-1]):
            if index == 0:
                differences[len(differences) - index - 1].append(0)
                continue
            new = lst[0] - differences[len(differences) - index][0]
            differences[len(differences) - index - 1] = [new] + differences[len(differences) - index - 1]

        total += differences[0][0]


    et = time.perf_counter_ns()
    elapsed = et - st
    print("\nExecution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")

    return total


print("Part one:", part_one(open("input.txt", "r")))
print("Part two:", part_two(open("input.txt", "r")))

