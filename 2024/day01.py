import time


def part_one(file):
    st = time.perf_counter_ns()

    nums = [[], []]
    for row, line in enumerate(file):
        parsed = list(map(int, line.split()))
        for i in range(2):
            nums[i].append((parsed[i], row))

    nums = [sorted(nums[i], key=lambda x:x[0]) for i in range(2)]
    res = sum(abs(nums[1][i][0] - nums[0][i][0]) for i in range(len(nums[0])))

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


def part_two(file):
    st = time.perf_counter_ns()

    lookup1 = {}
    lookup2 = {}
    nums = [set(), set()]

    for row, line in enumerate(file):
        parsed = list(map(int, line.split()))
        if parsed[1] in lookup2.keys():
            lookup2[parsed[1]] += 1
        else:
            lookup2[parsed[1]] = 1

        if parsed[0] not in lookup2.keys():
            lookup2[parsed[0]] = 0

        if parsed[0] in lookup1.keys():
            lookup1[parsed[0]] += 1
        else:
            lookup1[parsed[0]] = 1

        nums[0].add(parsed[0])
        nums[1].add(parsed[1])

    res = sum(num * lookup1[num] * lookup2[num] for _ in range(len(nums[0])) for num in [nums[0].pop()])

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
