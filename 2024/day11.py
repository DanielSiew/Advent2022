import time
from collections import defaultdict


def part_one(file):
    st = time.perf_counter_ns()
    
    seen = defaultdict(lambda: [])
    stones = defaultdict(lambda: 0)
    res = 0

    lst = list([int(x) for x in file.readlines()[0].strip().split()])
    for num in lst:
        stones[num] += 1

    for _ in range(25):
        nxt_stones = defaultdict(lambda: 0)
        for num, count in stones.items():
            if num not in seen:
                num_str = str(num)
                if num == 0:
                    nxt_stones[1] += count
                    seen[num] += [1]
                elif len(num_str) % 2 == 0:
                    left = int(num_str[:len(num_str) // 2])
                    right = int(num_str[len(num_str) // 2:])
                    seen[num] += [left, right]
                    nxt_stones[left] += count
                    nxt_stones[right] += count
                else:
                    ans = num * 2024
                    seen[num] += [ans]
                    nxt_stones[ans] += count
            else:
                for nxt_num in seen[num]:
                    nxt_stones[nxt_num] += count
        stones = nxt_stones.copy()

    for count in stones.values():
        res += count

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


def part_two(file):
    
    st = time.perf_counter_ns()
    
    seen = defaultdict(lambda: [])
    stones = defaultdict(lambda: 0)
    res = 0

    lst = list([int(x) for x in file.readlines()[0].strip().split()])
    for num in lst:
        stones[num] += 1

    for _ in range(25):
        nxt_stones = defaultdict(lambda: 0)
        for num, count in stones.items():
            if num not in seen:
                num_str = str(num)
                if num == 0:
                    nxt_stones[1] += count
                    seen[num] += [1]
                elif len(num_str) % 2 == 0:
                    left = int(num_str[:len(num_str) // 2])
                    right = int(num_str[len(num_str) // 2:])
                    seen[num] += [left, right]
                    nxt_stones[left] += count
                    nxt_stones[right] += count
                else:
                    ans = num * 2024
                    seen[num] += [ans]
                    nxt_stones[ans] += count
            else:
                for nxt_num in seen[num]:
                    nxt_stones[nxt_num] += count
        stones = nxt_stones.copy()

    for count in stones.values():
        res += count

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
