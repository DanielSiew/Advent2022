import time
import json


def part_one(file):
    st = time.perf_counter_ns()

    _map = []
    start = []
    for idx, line in enumerate(file):
        _map.append([i for i in line.strip()])
        if "S" in _map[idx]:
            start = [idx, _map[idx].index("S")]

    def valid_path(prev, current, shape, length, _init=False):
        if current == start and not _init:
            return length
        _next = []
        next_shape = ''
        match shape:
            case '|':
                if prev[0] == current[0]:
                    return 0
                _next = [current[0] + current[0] - prev[0], current[1]]
                try:
                    next_shape = _map[_next[0]][_next[1]]
                except IndexError:
                    return 0
            case '-':
                if prev[1] == current[1]:
                    return 0
                _next = [current[0], current[1] + current[1] - prev[1]]
                try:
                    next_shape = _map[_next[0]][_next[1]]
                except IndexError:
                    return 0
            case 'L':
                if prev[1] == current[1] - 1 or prev[0] == current[0] + 1:
                    return 0
                _next = [current[0] - (prev[1] - current[1]), current[1] + current[0] - prev[0]]
                try:
                    next_shape = _map[_next[0]][_next[1]]
                except IndexError:
                    return 0
            case 'J':
                if prev[1] == current[1] + 1 or prev[0] == current[0] + 1:
                    return 0
                _next = [current[0] - (current[1] - prev[1]), current[1] - (current[0] - prev[0])]
                try:
                    next_shape = _map[_next[0]][_next[1]]
                except IndexError:
                    return 0
            case '7':
                if prev[1] == current[1] + 1 or prev[0] == current[0] - 1:
                    return 0
                _next = [current[0] + current[1] - prev[1], current[1] - (prev[0] - current[0])]
                try:
                    next_shape = _map[_next[0]][_next[1]]
                except IndexError:
                    return 0
            case 'F':
                if prev[1] == current[1] - 1 or prev[0] == current[0] - 1:
                    return 0
                _next = [current[0] + prev[1] - current[1], current[1] + prev[0] - current[0]]
                try:
                    next_shape = _map[_next[0]][_next[1]]
                except IndexError:
                    return 0
            case '.':
                return 0

        return [current, _next, next_shape, length + 1]

    res = set()

    for i in "|-LJ7F":
        for d in [-1, 1]:
            temp = [[start[0] + d, start[1]], start, i, 0, True]
            while not isinstance(temp, int):
                temp = valid_path(*temp)
            res.add(temp)

            if len(res) > 1:
                break

            temp = [[start[0], start[1] + d], start, i, 0, True]
            while not isinstance(temp, int):
                temp = valid_path(*temp)
            res.add(temp)

            if len(res) > 1:
                break
        if len(res) > 1:
            break

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")

    return max(res) / 2


def part_two(file):
    st = time.perf_counter_ns()

    _map = []
    start = []
    for idx, line in enumerate(file):
        _map.append([i for i in line.strip()])
        if "S" in _map[idx]:
            start = [idx, _map[idx].index("S")]

    def valid_path(prev, current, shape, valid, _init=False):
        if current == start and not _init:
            return tuple([valid, len(valid)])
        _next = []
        next_shape = ''
        match shape:
            case '|':
                if prev[0] == current[0]:
                    return 0
                _next = [current[0] + current[0] - prev[0], current[1]]
                try:
                    next_shape = _map[_next[0]][_next[1]]
                except IndexError:
                    return 0
            case '-':
                if prev[1] == current[1]:
                    return 0
                _next = [current[0], current[1] + current[1] - prev[1]]
                try:
                    next_shape = _map[_next[0]][_next[1]]
                except IndexError:
                    return 0
            case 'L':
                if prev[1] == current[1] - 1 or prev[0] == current[0] + 1:
                    return 0
                _next = [current[0] - (prev[1] - current[1]), current[1] + current[0] - prev[0]]
                try:
                    next_shape = _map[_next[0]][_next[1]]
                except IndexError:
                    return 0
            case 'J':
                if prev[1] == current[1] + 1 or prev[0] == current[0] + 1:
                    return 0
                _next = [current[0] - (current[1] - prev[1]), current[1] - (current[0] - prev[0])]
                try:
                    next_shape = _map[_next[0]][_next[1]]
                except IndexError:
                    return 0
            case '7':
                if prev[1] == current[1] + 1 or prev[0] == current[0] - 1:
                    return 0
                _next = [current[0] + current[1] - prev[1], current[1] - (prev[0] - current[0])]
                try:
                    next_shape = _map[_next[0]][_next[1]]
                except IndexError:
                    return 0
            case 'F':
                if prev[1] == current[1] - 1 or prev[0] == current[0] - 1:
                    return 0
                _next = [current[0] + prev[1] - current[1], current[1] + prev[0] - current[0]]
                try:
                    next_shape = _map[_next[0]][_next[1]]
                except IndexError:
                    return 0
            case '.':
                return 0

        return [current, _next, next_shape, valid + [[current, shape]]]

    for i in "|-LJ7F":
        for d in [-1, 1]:
            temp = [[start[0] + d, start[1]], start, i, [], True]
            while isinstance(temp, list):
                temp = valid_path(*temp)

            if isinstance(temp, tuple):
                break

            temp = [[start[0], start[1] + d], start, i, [], True]
            while isinstance(temp, list):
                temp = valid_path(*temp)

            if isinstance(temp, tuple):
                break

        if isinstance(temp, tuple):
            break

    plot = [['.'] * len(_map[0]) * 3] * len(_map) * 3
    plot = json.loads(json.dumps(plot))

    temp[0][0][1] = "7"

    for thing in temp[0]:
        coords, shape = thing
        draw = []
        match shape:
            case '-':
                draw = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
            case '|':
                draw = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
            case '7':
                draw = [[0, 0, 0], [1, 1, 0], [0, 1, 0]]
            case 'J':
                draw = [[0, 1, 0], [1, 1, 0], [0, 0, 0]]
            case 'L':
                draw = [[0, 1, 0], [0, 1, 1], [0, 0, 0]]
            case 'F':
                draw = [[0, 0, 0], [0, 1, 1], [0, 1, 0]]

        for y, i in enumerate(draw):
            plot[coords[0] * 3 + y][coords[1] * 3 :coords[1] * 3 + 3] = ['.' if j == 0 else "#" for j in i]

    def fill(i, j, start, update):
        queue = [(i, j)]

        while len(queue) > 0:
            x, y = queue.pop(0)
            if not (0 <= x <= len(plot) - 1 and 0 <= y <= len(plot[0]) - 1):
                continue

            if any([plot[x][y] != start, plot[x][y] == update]):
                continue


            plot[x][y] = update

            neighbors = [(x - 1, y),
                         (x + 1, y),
                         (x - 1, y - 1),
                         (x + 1, y + 1),
                         (x - 1, y + 1),
                         (x + 1, y - 1),
                         (x, y - 1),
                         (x, y + 1)]

            for n in neighbors:
                if 0 <= n[0] <= len(plot) - 1 and 0 <= n[1] <= len(plot[0]) - 1:
                    queue.append(n)

    fill(11, 93, ".", "0")

    for i in plot:
        print(''.join(i))

    # for i in plot:
    #     print(''.join(i))

    res = 0

    for y, i in enumerate(plot[::3]):
        for x, j in enumerate(i[::3]):
            filled = True
            for dy in range(3):
                for dx in range(3):
                    if plot[y * 3+ dy][x * 3 + dx] != '0':
                        filled = False
                        break
                if not filled:
                    break
            if filled:
                res += 1


    et = time.perf_counter_ns()
    elapsed = et - st
    print("\nExecution time:", f"{elapsed / 10 ** 9}s" if (elapsed / 10 ** 9 >= 0.1) else f"{elapsed / 10 ** 6}ms")

    return res

# print("Part one:", part_one(open("input.txt", "r")))
print("Part two:", part_two(open("input.txt", "r")))

