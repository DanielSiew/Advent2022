import time


def part_one(file):
    st = time.perf_counter_ns()

    coords = {}
    width = height = 0

    for row, line in enumerate(file):
        for col, char in enumerate(line.strip()):
            width = max(width, col)
            height = max(height, row)

            if char != ".":
                if char not in coords.keys():
                    coords[char] = []
            
                coords[char] += [tuple([row, col])]

    seen = set()

    for char, all_pos in coords.items():
        for idx, pos in enumerate(all_pos):
            for other in all_pos[idx+1:]:
                new_pos = tuple([
                    pos[0] + (pos[0] - other[0]),
                    pos[1] + (pos[1] - other[1])
                ])
                if 0 <= new_pos[0] <= height and 0 <= new_pos[1] <= width:
                    seen.add(new_pos)
                new_pos = tuple([
                    other[0] + (other[0] - pos[0]),
                    other[1] + (other[1] - pos[1])
                ])
                if 0 <= new_pos[0] <= height and 0 <= new_pos[1] <= width:
                    seen.add(new_pos)

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return len(seen)


def part_two(file):
    st = time.perf_counter_ns()

    coords = {}
    width = height = 0

    for row, line in enumerate(file):
        for col, char in enumerate(line.strip()):
            width = max(width, col)
            height = max(height, row)

            if char != ".":
                if char not in coords.keys():
                    coords[char] = []
            
                coords[char] += [tuple([row, col])]

    seen = set()

    for char, all_pos in coords.items():
        for idx, pos in enumerate(all_pos):
            for other in all_pos[idx+1:]:
                for new_pos, new_other in [[pos, other], [other, pos]]:
                    dy = new_pos[0] - new_other[0]
                    dx = new_pos[1] - new_other[1]
                    while 0 <= new_pos[0] <= height and 0 <= new_pos[1] <= width:
                      seen.add(new_pos)
                      new_pos = tuple([
                          new_pos[0] + dy,
                          new_pos[1] + dx
                      ])
                  
    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return len(seen)


print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
