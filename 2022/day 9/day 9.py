file = open("day 9.txt", "r")
text = file.readlines()

startingPos = [0, 0]
headPos = [0, 0]
tailPos = [0, 0]

visitedPositions = [startingPos]

for lines in text:
    lines.strip()
    direction, amount = lines.split(" ")

    # head moves
    for move in range(1, int(amount) + 1):
        match direction:
            case 'U':
                headPos[1] += 1
            case 'D':
                headPos[1] -= 1
            case 'R':
                headPos[0] += 1
            case 'L':
                headPos[0] -= 1

        head_x = headPos[0]
        head_y = headPos[1]

        tail_x = tailPos[0]
        tail_y = tailPos[1]

        if not (tail_x in range(head_x - 1, head_x + 2) and tail_y in range(head_y - 1, head_y + 2)):
            if tail_x == head_x:
                if tail_y < head_y:
                    tailPos[1] += 1
                elif tail_y > head_y:
                    tailPos[1] -= 1
            elif tail_y == head_y:
                if tail_x < head_x:
                    tailPos[0] += 1
                elif tail_x > head_x:
                    tailPos[0] -= 1
            else:
                if tail_x < head_x:
                    tailPos[0] += 1
                elif tail_x > head_x:
                    tailPos[0] -= 1

                if tail_y < head_y:
                    tailPos[1] += 1
                elif tail_y > head_y:
                    tailPos[1] -= 1

        if tailPos not in visitedPositions:
            visitedPositions.append(list(tailPos))