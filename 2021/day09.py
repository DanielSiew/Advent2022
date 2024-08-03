import time

file = open("input.txt", "r")
text = file.readlines()


def part_one():
    st = time.time()

    height_map = [[10] * (len(text[0].strip()) + 2)]
    low_points = []

    for line in text:
        line = line.strip()
        lst = [10]
        lst.extend([int(char) for char in line])
        lst.append(10)

        height_map.append(lst)

    lst = [10] * (len(text[0].strip()) + 2)
    height_map.append(lst)

    for row in range(1, len(height_map) - 1):
        for col in range(1, len(height_map[row]) - 1):
            adj = [height_map[row-1][col], height_map[row][col+1], height_map[row+1][col], height_map[row][col-1]]
            if height_map[row][col] not in adj:
                adj.append(height_map[row][col])
                if min(adj) == height_map[row][col]:
                    low_points.append(height_map[row][col])

    output = sum([item + 1 for item in low_points])

    et = time.time()
    elapsed_time = et - st

    print(f"Part One:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms\n")


def part_two():
    st = time.time()

    height_map = [[9] * (len(text[0].strip()) + 2)]
    nines = []

    for line in text:
        line = line.strip()
        lst = [9]
        lst.extend([int(char) for char in line])
        lst.append(9)

        height_map.append(lst)

    lst = [9] * (len(text[0].strip()) + 2)
    height_map.append(lst)

    for row in range(len(height_map)):
        for col in range(len(height_map[row])):
            if height_map[row][col] == 9:
                height_map[row][col] = 0
            else:
                height_map[row][col] = 1

    basin_size = {}
    basin_id = 2
    for row in range(1, len(height_map) - 1):
        for col in range(1, len(height_map[row]) - 1):
            def get_adjacent(coord):
                x = coord[0]
                y = coord[1]
                up = x - 1
                ri = y + 1
                do = x + 1
                le = y - 1

                adjacent = [(up, y), (x, ri), (do, y), (x, le)]

                return adjacent

            # adjacent = [height_map[u][col], height_map[row][r], height_map[d][col], height_map[row][l]]

            def expand(identifier, adj):
                for coord in adj:
                    if height_map[coord[0]][coord[1]] == 1:
                        height_map[coord[0]][coord[1]] = identifier
                        basin_size[identifier] += 1
                        new_adj = get_adjacent((coord[0], coord[1]))
                        expand(identifier, new_adj)

            if height_map[row][col] == 1:  # part of a basin, un-identified
                current_id = basin_id
                basin_id += 1
                height_map[row][col] = current_id
                basin_size[current_id] = 1
                expand(current_id, get_adjacent((row, col)))

    largest_three = sorted(basin_size.values(), reverse=True)[0:3]
    output = 1
    for item in largest_three:
        output *= item


    et = time.time()
    elapsed_time = et - st

    print(f"Part Two:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms")


part_one()
part_two()
