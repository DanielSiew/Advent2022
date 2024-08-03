# part 1 was lost to time apparently

with open('input.txt', 'r') as file:
    text = list(file.readlines())

octopi = []

for lines in text:
    line = lines.strip()
    octopi.append([int(i) for i in line])

flashes = [0, 0]
flashed = []


def addNeighbours(coords):
    _row, _column = coords
    neighbours = [
        [_row - 1, _column - 1],
        [_row - 1, _column    ],
        [_row - 1, _column + 1],
        [_row    , _column + 1],
        [_row + 1, _column + 1],
        [_row + 1, _column    ],
        [_row + 1, _column - 1],
        [_row    , _column - 1],
    ]
    valid_neighbours = []
    for idx in range(len(neighbours)):
        j = neighbours[idx]
        if (0 <= j[0] <= 9) and (0 <= j[1] <= 9) and (j not in flashed):
            valid_neighbours.append(j)

    to_add = []
    for x, y in valid_neighbours:
        octopi[x][y] += 1
        if octopi[x][y] > 9:
            flashes[1] += 1
            octopi[x][y] = 0
            flashed.append([x, y])
            to_add.append([x, y])

    for x, y in to_add:
        addNeighbours([x, y])

flag = True
i = 1
while flag:
    flashed = []
    temp_add = []
    for row in range(len(octopi)):
        for column in range(len(octopi[row])):
            octopi[row][column] += 1
            if octopi[row][column] > 9:
                flashes[1] += 1
                octopi[row][column] = 0
                flashed.append([row, column])
                temp_add.append([row, column])

    for row, column in temp_add:
        addNeighbours([row, column])

    if flashes[1] - flashes[0] == 100:
        flag = False

    flashes[0] = flashes[1]
    i += 1

print(i-1)