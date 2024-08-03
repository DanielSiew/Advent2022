import json

file = open("input.txt", "r")
text = file.readlines()

originalStacks = {}
for block in range(1, 10):
    originalStacks[str(block)] = []

for lines in text:
    row = lines.strip("\n")
    length = (len(row) + 1) // 4

    if row[1].isdigit():
        break

    for block in range(length):
        crate = row[block * 4 + 1]
        if crate != ' ':
            originalStacks[str(block + 1)].insert(0, crate)

commands = []
for lines in text:
    if lines[0] != "m":
        continue
    commands.append(lines.strip())


def move_crates(part):
    stacks = json.loads(json.dumps(originalStacks))
    for command in commands:
        move_command, from_to_command = command.split("from ")
        move_command.strip(), from_to_command.strip()

        amount = int(move_command.strip("move "))
        start, end = from_to_command.split(" to ")

        crates_moved = stacks[start][0 - amount:]
        del stacks[start][0 - amount:]

        if part == 'one':
            crates_moved.reverse()

        stacks[end].extend(crates_moved)
    return stacks


print(move_crates('one'), '\n', move_crates('two'))
