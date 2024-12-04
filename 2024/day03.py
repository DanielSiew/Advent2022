import time
import re


def part_one(file):
    st = time.perf_counter_ns()

    res = 0
    
    for txt in file:
        cmds = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", txt)
        for cmd in cmds:
            cmd = tuple(map(int, cmd[4:-1].split(",")))
            res += cmd[0] * cmd[1]

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


def part_two(file):
    st = time.perf_counter_ns()

    res = 0

    enable = True

    for txt in file:
        cmds = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don't\\(\\)", txt)
        for cmd in cmds:
            if cmd == "do()":
                enable = True
                continue
            if cmd == "don't()":
                enable = False
                continue
            if not enable:
                continue
            cmd = tuple(map(int, cmd[4:-1].split(",")))
            res += cmd[0] * cmd[1]
    
    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
