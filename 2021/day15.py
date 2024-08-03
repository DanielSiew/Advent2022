import math
import time

with open('input.txt', 'r') as file:
    text = list(file.readlines())

st = time.time()
board = []
sums = []
for k in range(0, 5):
    for lines in text:
        line = lines.strip()
        temp1 = []
        temp2 = []
        for j in range(0, 5):
            for i in line:
                new = int(i) + j + k
                if new >= 10:
                    new = new % 10 + new // 10
                temp1.append(new)
                temp2.append(math.inf)
        board.append(temp1)
        sums.append(temp2)

height = len(board)
width = len(board[0])
print(height, width)

sums[0][0] = 0
# print(sums)
for _ in range(2):
    for y in range(0, height):
        for x in range(0, width):
            if y == 0 and x == 0:
                continue
            neighbours = [
                [x, y + 1],
                [x, y - 1],
                [x + 1, y],
                [x - 1, y]
            ]

            temp = []
            for neigh in neighbours:
                _x, _y = neigh
                if (0 <= _x < width) and (0 <= _y < height):
                    temp.append([_x, _y])

            sums[y][x] = min([sums[__y][__x] for __x, __y in temp]) + board[y][x]
            # print(repr([x ,y]), temp, min(list([sums[_j][_i] for _i, _j in temp])), sums[y][x])
et = time.time()

print(sums[-1][-1])
print((et - st), 's')