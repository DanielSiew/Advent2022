file = open("day 2.txt", "r")
text = file.readlines()

pointsTotal = 0

for line in text:
    lines = line.strip()
    opponentShape, playerShape = lines.split(" ")

    match playerShape:
        case 'X':
            pointsTotal += 0

            match opponentShape:
                case 'A':
                    pointsTotal += 3
                case 'B':
                    pointsTotal += 1
                case 'C':
                    pointsTotal += 2
        case 'Y':
            pointsTotal += 3

            match opponentShape:
                case 'A':
                    pointsTotal += 1
                case 'B':
                    pointsTotal += 2
                case 'C':
                    pointsTotal += 3
        case 'Z':
            pointsTotal += 6

            match opponentShape:
                case 'A':
                    pointsTotal += 2
                case 'B':
                    pointsTotal += 3
                case 'C':
                    pointsTotal += 1

print(pointsTotal)
