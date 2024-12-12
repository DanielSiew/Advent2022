import time


def part_one(file):
    st = time.perf_counter_ns()
    
    res = 0
    grid = dict()

    for y, row in enumerate(file):
        for x, char in enumerate(row.strip()):
            grid[(y, x)] = char

    queue = [(0, 0)]

    while queue:
        start = queue.pop(0)
        seen = set()
        current_queue = [start]
        region_char = grid[start]
        perimeter = 0
        area = 0

        while current_queue:
            current = current_queue.pop(0)
            if grid[current] == ".":
                continue

            seen.add(current)
            grid[current] = "."
            area += 1

            for neighbour in [
                (current[0] + dy, current[1] + dx)
                for dy, dx in [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1)
                ]
            ]:
                if neighbour in seen or neighbour in current_queue:
                    continue
                if neighbour not in grid:
                    perimeter += 1
                    continue
                char = grid[neighbour]
                if char != region_char:
                    if char != ".":
                        queue += [neighbour]
                    perimeter += 1
                    continue
                current_queue += [neighbour]
              
        res += area * perimeter

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


def part_two(file):
    st = time.perf_counter_ns()
    
    res = 0
    grid = dict()
    
    def is_same_side(coord, other, direction):
        c_y, c_x = coord
        o_y, o_x = other
        if direction in [0, 1]:
            if c_y == o_y and abs(c_x - o_x) == 1:
                return True
            return False
        if direction in [2, 3]:
            if c_x == o_x and abs(c_y - o_y) == 1:
                return True
            return False
        return False
        

    for y, row in enumerate(file):
        for x, char in enumerate(row.strip()):
            grid[(y, x)] = char

    queue = [(0, 0)]

    while queue:
        start = queue.pop(0)
        seen = set()
        current_queue = [start]
        region_char = grid[start]
        sides = []
        area = 0

        while current_queue:
            current = current_queue.pop(0)
            if grid[current] == ".":
                continue

            seen.add(current)
            grid[current] = "."
            area += 1

            for neighbour in [
                (current[0] + dy, current[1] + dx)
                for dy, dx in [
                    (1, 0),
                    (-1, 0), 
                    (0, 1), 
                    (0, -1) 
                ]
            ]:
                if neighbour in seen:
                    continue
                if neighbour in grid:
                    char = grid[neighbour]
                    if char != region_char and char != ".":
                        queue += [neighbour]
                    else:
                        if neighbour not in current_queue:
                            current_queue += [neighbour]
        
        if not seen:
            continue
        
        for point in sorted(list(seen), key=lambda x: (x[0], x[1])):
            for neighbour, _direction in [
                [(point[0] + dy, point[1] + dx), _dir]
                for _dir, (dy, dx) in enumerate([
                    (1, 0),  # to down, from up
                    (-1, 0),  # to up, from down
                    (0, 1),  # to right, from left
                    (0, -1)  # to left, from right
                ])
            ]:
                if neighbour in seen:
                    continue
                side_exists = False
                for idx, _sides in enumerate(sides):
                    for side, direction in _sides:
                        side_exists = is_same_side(side, neighbour, _direction) and _direction == direction
                        if side_exists:
                            sides[idx] += [(neighbour, _direction)]
                            break
                    if side_exists:
                        break
                if not side_exists:
                    sides.append([(neighbour, _direction)])
                        
        res += area * len(sides)

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
