import timeit


def part_one(file):
    total = 0
    whole = []
    for line in file:
        whole.append(['.'] + [i for i in line.strip()] + ['.'])

    whole = [['.'] * len(whole[0])] + whole + [['.'] * len(whole[0])]

    for row, line in enumerate(whole):
        if row in [0, len(whole)-1]:
            continue
        finished = False
        num = ''
        neighbours = []
        for col, char in enumerate(line):
            if col in [0, len(line)-1]:
                continue
            if char.isdigit() and not finished:
                num += char
            else:
                finished = True

            if whole[row][col+1] == '.':
                finished = True

            for idx in [
                (row+1, col+1),
                (row+1, col-1),
                (row-1, col+1),
                (row-1, col-1),
                (row+1, col),
                (row-1, col),
                (row, col+1),
                (row, col-1),
            ]:
                cur = whole[idx[0]][idx[1]]
                if not cur.isdigit() and cur != '.' and cur not in neighbours:
                    neighbours += cur

            if num and col == len(line) - 2:
                finished = True

            if finished:
                if neighbours:
                    total += int(num) if num != '' else 0
                neighbours = []
                finished = False
                num = ''

    return total


def part_two(file):
    total = 0
    whole = []
    nums = []
    for line in file:
        whole.append(['.'] + [i for i in line.strip()] + ['.'])

    whole = [['.'] * len(whole[0])] + whole + [['.'] * len(whole[0])]

    for row, line in enumerate(whole):
        if row in [0, len(whole)-1]:
            continue
        num = ''
        finished = False
        symbol = None
        for col, char in enumerate(line):
            if col in [0, len(line)-1]:
                continue

            if char.isdigit() and not finished:
                num += char
            else:
                finished = True

            if whole[row][col+1] == '.':
                finished = True

            for idx in [
                (row+1, col+1),
                (row+1, col-1),
                (row-1, col+1),
                (row-1, col-1),
                (row+1, col),
                (row-1, col),
                (row, col+1),
                (row, col-1),
            ]:
                cur = whole[idx[0]][idx[1]]
                if cur == '*':
                    symbol = (idx[0], idx[1])

            if num and col == len(line) - 2:
                finished = True

            if finished:
                if symbol is not None and num:
                    nums.append([int(num), symbol])
                finished = False
                symbol = None
                num = ''

    nums = sorted(nums, key=lambda x: x[1])

    temp = 1
    index = None
    for i in nums:
        if index is None:
            index = i[1]
            temp = i[0]
            continue

        if index == i[1]:
            total += i[0] * temp
            index = None
            temp = 1
        else:
            index = i[1]
            temp = i[0]
            continue

    return total


print("Part one:", part_one(open("input.txt", "r")))
print("\nPart two:", part_two(open("input.txt", "r")))
