import time
import numpy as np


def part_one(file):
    st = time.perf_counter_ns()

    _file = file.readlines()
    res = 0
    for btn_a, btn_b, prize in (_file[n*3+1*n:n*3+3+1*n] for n in range(len(_file) // 4 + 1)):
      btn_a = list(map(lambda x:int(x.split("+")[-1]), btn_a.split(": ")[-1].strip().split(", ")))
      btn_b = list(map(lambda x:int(x.split("+")[-1]), btn_b.split(": ")[-1].strip().split(", ")))
      prize = list(map(lambda x:int(x.split("=")[-1]), prize.split(": ")[-1].strip().split(", ")))
      [x, y] = [0, 0]
      counter_a = 0  # btn_a, btn_b
      valid = []
      
      while x < prize[0] or y < prize[1]:
        x += btn_a[0]
        y += btn_a[1]
        counter_a += 1
        
        rem = [(prize[n] - [x, y][n]) // btn_b[n] for n in range(2)]
        
        if rem[0] == rem[1] and (prize[0] - x) % btn_b[0] == 0 and (prize[1] - y) % btn_b[1] == 0:
        # and prize[0] // x == prize[1] // y:
          valid += [counter_a * 3 + (prize[0] - x) // btn_b[0]]
          
      res += min(valid if valid else [0])

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


def part_two(file):
    st = time.perf_counter_ns()

    _file = file.readlines()
    res = 0
    for btn_a, btn_b, prize in (_file[n*3+1*n:n*3+3+1*n] for n in range(len(_file) // 4 + 1)):
      btn_a = list(map(lambda x:int(x.split("+")[-1]), btn_a.split(": ")[-1].strip().split(", ")))
      btn_b = list(map(lambda x:int(x.split("+")[-1]), btn_b.split(": ")[-1].strip().split(", ")))
      prize = list(map(lambda x:int(x.split("=")[-1]) + 10**13, prize.split(": ")[-1].strip().split(", ")))
      a = np.array([[btn_a[n], btn_b[n]] for n in range(2)])
      b = np.array(prize)
      x = np.linalg.solve(a, b)
      check_1 = x[0] * 3 + x[1]
      check_2 = round(x[0]) * 3 + round(x[1])
      
      if abs(check_1 - check_2) < 0.001:
        res += check_2

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
