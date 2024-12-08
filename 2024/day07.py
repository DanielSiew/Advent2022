import time


def part_one(file):
    st = time.perf_counter_ns()

    def resolve(target, remaining, test_value=False, total=0):
        if total > target:
            return False
        if len(remaining) == 0:
            if target == total:
                return True
            return False
        
        test_value |= resolve(target, remaining[1:], test_value, remaining[0] if total == 0 else total * remaining[0])
        test_value |= resolve(target, remaining[1:], test_value, total + remaining[0])
        
        return test_value

    res = 0

    for line in file:
        ans, nums = map(lambda x: list(map(int, x.strip().split())), line.split(":"))
        ans = ans[0]
        
        if resolve(ans, nums, False):
            res += ans

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


def part_two(file):
    st = time.perf_counter_ns()

    def resolve(target, remaining, test_value=False, total=0):
        if total > target:
            return False
        if len(remaining) == 0:
            if target == total:
                return True
            return False
        
        test_value |= resolve(target, remaining[1:], test_value, remaining[0] if total == 0 else total * remaining[0])
        test_value |= resolve(target, remaining[1:], test_value, total + remaining[0])
        test_value |= resolve(target, remaining[1:], test_value, int(str(total) + str(remaining[0])))
        
        return test_value

    res = 0

    for line in file:
        ans, nums = map(lambda x: list(map(int, x.strip().split())), line.split(":"))
        ans = ans[0]
        
        if resolve(ans, nums, False):
            res += ans

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
