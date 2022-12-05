file = open("day 5.txt", "r")
text = file.readlines()

stacks = {
    '1': ['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'],
    '2': ['N', 'V', 'G', 'P', 'H', 'W', 'B'],
    '3': ['F', 'W', 'B', 'J', 'G'],
    '4': ['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S'],
    '5': ['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H'],
    '6': ['B', 'C', 'W', 'G', 'F', 'S'],
    '7': ['H', 'T', 'P', 'M', 'Q', 'B', 'W'],
    '8': ['F', 'S', 'W', 'T'],
    '9': ['N', 'C', 'R']
}

for line in text:
    move, positions = line.split("from")
    amount = int(move[5:].strip())
    positions = positions.split("to")
    positions = [string.strip() for string in positions]

    stackInitial = stacks[positions[0]]
    stackFinal = stacks[positions[1]]

    amount = 0 - amount

    blocksMoved = stackInitial[amount:]
    blocksMoved.reverse()

    for item in blocksMoved:
        stackFinal.append(item)
    del stackInitial[amount:]

    stacks[positions[0]] = stackInitial
    stacks[positions[1]] = stackFinal

    print(stackInitial)
    print(stackFinal)

for key in stacks.keys():
    print("{0}: {1}".format(key, stacks[key]))
