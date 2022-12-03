file = open("day 1.txt", "r")
text = file.readlines()

elfCounter = 1
elfCalories = {'1': []}
totalCalories = {'1': 0}

for line in text:
    lines = line.strip()

    if lines != "":
        elfCalories[str(elfCounter)].append(int(lines))
    else:
        elfCounter += 1
        elfCalories[str(elfCounter)] = []
        totalCalories[str(elfCounter)] = 0

for key in elfCalories:
    for calories in elfCalories[key]:
        totalCalories[key] += int(calories)

highestThree = 0

sorted_totalCalories = dict(sorted(totalCalories.items(), key=lambda x:x[1], reverse=True)) # NOQA
key = list(sorted_totalCalories.keys())
for counter in range(3):
    highestThree += sorted_totalCalories[key[counter]]

print(highestThree)
