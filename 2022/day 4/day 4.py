file = open("day 4.txt", "r")
text = file.readlines()

part_one_counter = 0
part_two_counter = 0

for line in text:
    assignmentRange = line.strip()

    # Splits assignment pairs into 2 strings
    rangeString1, rangeString2 = assignmentRange.split(",")

    # Splits each string into a list with starting and ending value of a range, e.g. ['3', '5'] for range 3 to 5
    rangeList1 = rangeString1.split("-")
    rangeList2 = rangeString2.split("-")

    # changes the value in the list from string to integer for conditional statements later, e.g. ['3', '5'] to [3, 5]
    rangeList1 = [int(num) for num in rangeList1]
    rangeList2 = [int(num) for num in rangeList2]

    if rangeList1[0] <= rangeList2[0] and rangeList1[1] >= rangeList2[1] or \
            rangeList1[0] >= rangeList2[0] and rangeList1[1] <= rangeList2[1]:
        part_one_counter += 1
    if rangeList1[0] <= rangeList2[0] <= rangeList1[1] or \
            rangeList2[0] <= rangeList1[0] <= rangeList2[1]:
        part_two_counter += 1

print(part_one_counter, part_two_counter)
