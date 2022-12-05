file = open("day 3.txt", "r")
text = file.readlines()

totalPriority = 0
counterGroup = 0
group = []

for line in text:
    lines = line.strip()

    # adds rucksack (current line) into the group
    group.append(lines)
    counterGroup += 1

    # once the group size is 3, find common character in all 3 rucksacks of the group then resets group
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
