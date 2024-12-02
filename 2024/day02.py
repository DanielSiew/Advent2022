import time


def part_one(file):
    st = time.perf_counter_ns()

    res = 0

    for row, line in enumerate(file):
        safe = True
        nums = list(map(int, line.split()))
        inc = nums[1] > nums[0]
        for index, num in enumerate(nums[1:]):
            if abs(nums[index] - num) > 3 or nums[index] == num:
                safe = False
            if inc and num < nums[index] or not inc and num > nums[index]:
                safe = False

        if safe:
            res += 1

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


def part_two(file):
    st = time.perf_counter_ns()

    def check(lst, flag, asc):
        for i in range(1, len(lst)):
            prev = lst[i - 1]
            now = lst[i]
            if (abs(prev - now) > 3 or prev == now) or\
                    (asc and prev > now or not asc and now > prev):
                if flag:
                    return False
                return check(lst[:i] + lst[i+1:], True, asc) or check(lst[:i - 1] + lst[i:], True, asc)
        return True

    res = 0

    for row, line in enumerate(file):
        nums = list(map(int, line.split()))

        res += check(nums, False, False) or check(nums, False, True)

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
