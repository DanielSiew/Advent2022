# Part 1

file = open("day 1.txt", "r")
text = file.readlines()

elfCalories = [0]
index = 0

for line in text:
    lines = line.strip()

    if lines != "":
        elfCalories[index] += int(lines)
    else:
        index += 1
        elfCalories.append(0)

highest = max(elfCalories)
print(highest)
