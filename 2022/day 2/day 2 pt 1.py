# Part 1
file = open("day 2.txt", "r")
text = file.readlines()

pointsTotal = 0

for line in text:
    lines = line.strip()
    opponentShape, playerShape = lines.split(" ")

    match playerShape:
        case 'X':
            pointsTotal += 1

            match opponentShape:
                case 'A':
                    pointsTotal += 3
                case 'B':
                    pointsTotal += 0
                case 'C':
                    pointsTotal += 6
        case 'Y':
            pointsTotal += 2

            match opponentShape:
                case 'A':
                    pointsTotal += 6
                case 'B':
                    pointsTotal += 3
                case 'C':
                    pointsTotal += 0
        case 'Z':
            pointsTotal += 3

            match opponentShape:
                case 'A':
                    pointsTotal += 0
                case 'B':
                    pointsTotal += 6
                case 'C':
                    pointsTotal += 3

print(pointsTotal)
