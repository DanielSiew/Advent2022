with open('input.txt', 'r') as file:
    text = list(file.readlines())

coords = []
commands = []

for lines in text:
    line = lines.strip()
    if line == '':
        continue
    if line[0].isalpha():
        *_, command = line.split()
        axis, pos = command.split('=')
        commands.append([axis, int(pos)])
    else:
        x, y = eval(line)
        coords.append([x, y])

current_width = 0
current_height = 0
for cmd in commands:
    axis, pos = cmd
    limit = len(coords)
    if axis == 'y':
        current_height = pos * 2
        idx = 0
        while idx < limit:
            point = coords[idx]
            if point[1] <= pos:
                idx += 1
                continue
            new_point = [point[0], current_height - point[1]]
            del coords[idx]
            if new_point in coords:
                idx -= 1
                limit -= 1
            else:
                coords.insert(0, new_point)
            idx += 1

    elif axis == 'x':
        current_width = pos * 2
        idx = 0
        while idx < limit:
            point = coords[idx]
            if point[0] <= pos:
                idx += 1
                continue
            new_point = [current_width - point[0], point[1]]
            del coords[idx]
            if new_point in coords:
                idx -= 1
                limit -= 1
            else:
                coords.insert(0, new_point)
            idx += 1

drawing = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
]
for coord in coords:
    drawing[coord[1]][coord[0]] = '#'

for row in drawing:
    print(''.join(row))


# print(coords)
# print(commands, current_width, current_height)