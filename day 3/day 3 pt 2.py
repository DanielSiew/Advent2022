file = open("day 3.txt", "r")
text = file.readlines()

totalPriority = 0
counterGroup = 0
group = []

for line in text:
    lines = line.strip()
    rucksack = lines

    group.append(rucksack)
    counterGroup += 1

    if counterGroup == 3:
        common_itemType = list(set(group[0]).intersection(group[1], group[2]))[0]

        if common_itemType.isupper():
            priority = int(ord(common_itemType)) - 38  # returns value from 27 to 52
        else:
            priority = int(ord(common_itemType)) - 96  # returns value from 1 to 26

        totalPriority += priority

        group = []
        counterGroup = 0

print(totalPriority)
