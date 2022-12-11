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

    if pixel_position in sprite_position:
        CRT_row[row].append('#')
    else:
        CRT_row[row].append('.')

    sprite_draw = ''.join('#' if pos in sprite_position else '.' for pos in range(40))
    pixel_draw = ''.join(CRT_row[row])
    empty_space = ''.join(' ' for _ in range(len(CRT_row[row]) - 1))
    print(f"CYCLE: {cycle}\nCurrent sprite position{':'.rjust(6)} {sprite_draw}")
    print(f"Current position and status{':'.rjust(2)} {empty_space}{'X' if len(CRT_row[row]) <= 40 else ''} {'aligns with sprite! # is drawn.' if CRT_row[row][-1] == '#' else 'not aligned with sprite! . is drawn.'}")
    print(f"Current CRT line{':'.rjust(13)} {pixel_draw}\n")

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
