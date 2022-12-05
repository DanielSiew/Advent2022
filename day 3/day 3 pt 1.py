file = open("day 3.txt", "r")
text = file.readlines()

totalPriority = 0

for line in text:
    lines = line.strip()
    
    # splits line in text file into two to represent 2 compartments in one rucksack
    compartmentFirst = lines[slice(0, len(lines) // 2)]
    compartmentSecond = lines[slice(len(lines) // 2, len(lines))]
    common_itemType = list(set(compartmentFirst).intersection(compartmentSecond))[0]  # gets the common character found in both compartments

    if common_itemType.isupper():
        priority = int(ord(common_itemType)) - 38  # returns value from 27 to 52
    else:
        priority = int(ord(common_itemType)) - 96  # returns value from 1 to 26

    totalPriority += priority

print(totalPriority)
