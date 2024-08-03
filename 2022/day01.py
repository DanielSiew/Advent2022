file = open("input.txt", "r")
text = file.readlines()

elfCalories = [0]
index = 0

for line in text:
    calorie = line.strip()
    if calorie != "":
        elfCalories[index] += int(calorie)
    else:
        index += 1
        elfCalories.append(0)

elfCalories.sort()


def part_one():
    highest = elfCalories[-1]
    return highest


def part_two():
    highest_three = sum(elfCalories[-3:])
    return highest_three


print(part_one(), part_two())