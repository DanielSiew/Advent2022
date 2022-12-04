file = open("day 4.txt", "r")
text = file.readlines()

counter = 0

for line in text:
    lines = line.strip()
    rangeString1, rangeString2 = lines.split(",")
    rangeList1 = rangeString1.split("-")
    rangeList2 = rangeString2.split("-")

    rangeList1 = [int(num) for num in rangeList1]
    rangeList2 = [int(num) for num in rangeList2]

    if rangeList1[0] <= rangeList2[0] <= rangeList1[1]:
        counter += 1
    elif rangeList2[0] <= rangeList1[0] <= rangeList2[1]:
        counter += 1

print(counter)
