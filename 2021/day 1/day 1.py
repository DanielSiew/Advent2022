file = open("day 1.txt", "r")
text = file.readlines()

# turns text file input into a list
depths = []
for line in text:
    lines = line.strip()
    depths.append(int(lines))

# part 1
def find_increase_count():  # NOQA
    increase_count = 0

    for index in range(len(depths)):
        if index == 0:
            pass
        else:
            if depths[index] - depths[index - 1] > 0:
                increase_count += 1

    return increase_count

# Part 2
def find_grouped_increase_count():  # NOQA
    increase_count = 0
    groups = []

    for index in range(3, len(depths) + 3):
        groups.append(sum(depths[index - 3:index]))

    for index in range(len(groups)):
        if index == 0:
            pass
        else:
            if groups[index] > groups[index - 1]:
                increase_count += 1
            else:
                decrease_count += 1

    return increase_count


print(find_increase_count(), find_grouped_increase_count())
