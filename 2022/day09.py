# Part One
import snake as s

file = open("input.txt", "r")
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

# Part Two
file = open("input.txt", "r")
text = file.readlines()

snakeParts = [s.Snake.head, s.body_1, s.body_2, s.body_3, s.body_4, s.body_5, s.body_6, s.body_7, s.body_8, s.body_9]

visitedPositions = [[0, 0]]

for lines in text:
    lines.strip()
    direction, amount = lines.split(" ")

    for move in range(1, int(amount) + 1):
        match direction:
            case 'U':
                s.Snake.head.pos[1] += 1
            case 'D':
                s.Snake.head.pos[1] -= 1
            case 'R':
                s.Snake.head.pos[0] += 1
            case 'L':
                s.Snake.head.pos[0] -= 1

        for segment in snakeParts[1:]:
            current_x = segment.pos[0]
            current_y = segment.pos[1]

            reference_x = segment.next.pos[0]
            reference_y = segment.next.pos[1]

            if not (current_x in range(reference_x - 1, reference_x + 2) and current_y in range(reference_y - 1, reference_y + 2)):
                if current_x == reference_x:
                    if current_y < reference_y:
                        segment.pos[1] += 1
                    elif current_y > reference_y:
                        segment.pos[1] -= 1
                elif current_y == reference_y:
                    if current_x < reference_x:
                        segment.pos[0] += 1
                    elif current_x > reference_x:
                        segment.pos[0] -= 1
                else:
                    if current_x < reference_x:
                        segment.pos[0] += 1
                    elif current_x > reference_x:
                        segment.pos[0] -= 1

                    if current_y < reference_y:
                        segment.pos[1] += 1
                    elif current_y > reference_y:
                        segment.pos[1] -= 1

            if s.body_9.pos not in visitedPositions:
                visitedPositions.append(list(s.body_9.pos))

print(len(visitedPositions))
