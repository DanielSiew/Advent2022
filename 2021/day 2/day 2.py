file = open("day 2.txt", "r")
text = file.readlines()

movementDirection = []
movementMagnitude = []

for line in text:
    direction, magnitude = line.split(" ")
    movementDirection.append(direction)
    movementMagnitude.append(int(magnitude))

# part 1
def multiply_horizontal_depth():  # NOQA
    horizontal_position = 0
    depth = 0

    for index in range(len(movementDirection)):
        match movementDirection[index]:
            case 'forward':
                horizontal_position += movementMagnitude[index]
            case 'down':
                depth += movementMagnitude[index]
            case 'up':
                depth -= movementMagnitude[index]

    product = horizontal_position * depth
    return product

# part 2
def multiply_horizontal_aimed_depth():  # NOQA
    horizontal_position = 0
    depth = 0
    aim = 0

    for index in range(len(movementDirection)):
        match movementDirection[index]:
            case 'forward':
                horizontal_position += movementMagnitude[index]
                depth += movementMagnitude[index] * aim
            case 'down':
                aim += movementMagnitude[index]
            case 'up':
                aim -= movementMagnitude[index]

    product = horizontal_position * depth
    return product


print(multiply_horizontal_depth(), multiply_horizontal_aimed_depth())
