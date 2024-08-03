file = open("input.txt", "r")
text = file.readlines()

rucksacks = []

for line in text:
    rucksacks.append(line.strip())


def get_char_value(character):
    if character.isupper():
        value = int(ord(character)) - 38  # Value ranges from 27 to 52
    else:
        value = int(ord(character)) - 96  # Value ranges from 1 to 26

    return value


def part_one():
    total_priority = 0
    for elf in rucksacks:
        # Splits each rucksack into 2 compartments of equal length
        compartment_first = elf[slice(0, len(elf) // 2)]
        compartment_second = elf[slice(len(elf) // 2, len(elf))]

        common_type = list(set(compartment_first).intersection(compartment_second))[0]
        total_priority += get_char_value(common_type)

    return total_priority


def part_two():
    groups = []
    total_priority = 0

    # Splits rucksacks into groups of 3
    for elf in range(0, len(rucksacks), 3):
        groups.append(list(rucksacks[elf: elf + 3]))

    for group_counter in groups:
        common_type = list(set(group_counter[0]).intersection(group_counter[1], group_counter[2]))[0]
        total_priority += get_char_value(common_type)

    return total_priority


print(part_one(), part_two())
