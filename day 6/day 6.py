file = open("day 6.txt", "r")
text = file.readline()


def part_one():
    character_counter = 4
    for index in range(len(text)):
        if len(set(text[index:index + 4])) == 4:
            break
        else:
            character_counter += 1
    return character_counter


def part_two():
    character_counter = 14
    for index in range(len(text)):
        if len(set(text[index:index + 14])) == 14:
            break
        else:
            character_counter += 1
    return character_counter


print(part_one(),part_two())
