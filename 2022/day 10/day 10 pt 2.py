file = open("day 10.txt", "r")
text = file.readlines()

cycle = 1
x_value = 1
CRT_row = {}
currently_adding = False
commands = []
cycleAmount = 0

for lines in text:
    command = lines

    match command[0]:
        case 'n':
            command = command.strip()
            commands.append(command)
            cycleAmount += 1
        case 'a':
            command, amount = command.split(" ")
            amount.strip()
            amount = int(amount)
            commands.append([command, amount])
            cycleAmount += 2

command_counter = 0
for cycle_current in range(cycleAmount):
    row = (cycle - 1) // 40 + 1
    if (cycle - 1) % 40 == 0:
        CRT_row[row] = []

    sprite_position = list(range(x_value - 1, x_value + 2))
    pixel_position = len(CRT_row[row])

    print(row)
    print(sprite_position)
    print(pixel_position)
    print()

    if pixel_position in sprite_position:
        CRT_row[row].append('#')
    else:
        CRT_row[row].append('.')

    if not currently_adding:
        if commands[command_counter] == 'noop':
            command_counter += 1
        else:
            currently_adding = True
    else:
        amount = commands[command_counter][1]
        x_value += amount
        currently_adding = False
        command_counter += 1

    cycle += 1

for row in CRT_row.keys():
    string = ''
    for pixel in CRT_row[row]:
        string += pixel
    print(string)
