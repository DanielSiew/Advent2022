import time

file = open("input.txt", "r")
text = file.readlines()


def part_one():
    st = time.time()
    output = 0

    board = []
    for row in range(1000):
        board.append([0] * 1000)

    for line in text:
        line = line.strip()
        point_a, point_b = line.split(" -> ")
        x_a, y_a = point_a.split(',')
        x_b, y_b = point_b.split(',')
        x_a, y_a, x_b, y_b = int(x_a), int(y_a), int(x_b), int(y_b)

        if x_a != x_b and y_a != y_b:
            continue

        if y_a == y_b:
            for length in range(min(x_a, x_b), max(x_a, x_b) + 1):
                board[y_a][length] += 1
        elif x_a == x_b:
            for length in range(min(y_a, y_b), max(y_a, y_b) + 1):
                board[length][x_a] += 1

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] >= 2:
                output += 1

    et = time.time()
    elapsed_time = et - st

    print(f"Part One:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms\n")


def part_two():
    st = time.time()

    output = 0

    board = []
    for row in range(1000):
        board.append([0] * 1000)

    for line in text:
        line = line.strip()
        point_a, point_b = line.split(" -> ")
        x_a, y_a = point_a.split(',')
        x_b, y_b = point_b.split(',')
        x_a, y_a, x_b, y_b = int(x_a), int(y_a), int(x_b), int(y_b)

        if y_a == y_b:
            for length in range(min(x_a, x_b), max(x_a, x_b) + 1):
                board[y_a][length] += 1
        elif x_a == x_b:
            for length in range(min(y_a, y_b), max(y_a, y_b) + 1):
                board[length][x_a] += 1
        else:
            # there has to be a more optimal way to do diagonals...
            start_x = min(x_a, x_b)
            end_x = max(x_a, x_b)
            start_y = y_a if start_x == x_a else y_b
            end_y = y_a if end_x == x_a else y_b

            current_y = start_y
            for length in range(start_x, end_x + 1):
                board[current_y][length] += 1
                current_y = current_y + 1 if start_y < end_y else current_y - 1

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] >= 2:
                output += 1

    et = time.time()
    elapsed_time = et - st

    print(f"Part Two:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms")


part_one()
part_two()
