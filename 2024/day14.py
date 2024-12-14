import time


def part_one(file):
    st = time.perf_counter_ns()

    res = 0
    quadrants = [0] * 4
    
    for line in file:
      w, h = 101, 103
      p, v = line.strip().split(" v=")
      p = tuple(map(int, p[2:].split(",")))
      v = tuple(map(int, v.split(",")))

      new_p = tuple((p[n] + v[n] * 100) % [w, h][n] for n in range(2))
      if 0 <= new_p[0] < w // 2 and 0 <= new_p[1] < h // 2:
        quadrants[0] += 1
      if 0 <= new_p[0] < w // 2 and h // 2 + 1 <= new_p[1] < h:
        quadrants[1] += 1
      if w // 2 + 1 <= new_p[0] < w and 0 <= new_p[1] < h // 2:
        quadrants[2] += 1
      if w // 2 + 1 <= new_p[0] < w and h // 2 + 1 <= new_p[1] < h:
        quadrants[3] += 1
        
    res = 1
    for q in quadrants:
      res *= q

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


def part_two(file):
    st = time.perf_counter_ns()
    
    w, h = 101, 103
    grid = []
    for i in range(h):
      grid.append([])
      for j in range(w):
        grid[i].append(".")
    
    res = 0
    pvs = []
    
    for line in file:
      p, v = line.strip().split(" v=")
      p = list(map(int, p[2:].split(",")))
      v = tuple(map(int, v.split(",")))
      pvs.append([p, v])
      
      grid[p[1]][p[0]] = "#"
      
    iteration = 0
    while True:
      flag = False
      for i in grid:
        cnt = 0
        for j in i:
          if j == "#":
            cnt += 1
          else:
            cnt = 0
          if cnt > 10:
            flag = True
            break
        if flag:
          break
      if flag:
        break
      iteration += 1
      for p, v in pvs:
        grid[p[1]][p[0]] = "."
      for p, v in pvs:
        p[0] = (p[0] + v[0]) % w
        p[1] = (p[1] + v[1]) % h
        grid[p[1]][p[0]] = "#"
        
      
    print(iteration, "\n")
    for i in grid:
      for j in i:
        print(end=j)
      print()
    print("\n\n")
    
    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
