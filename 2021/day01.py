import time

file = open("input.txt", "r")
text = file.readlines()


def part_one():
    st = time.time()
    previous = 0
    output = -1

    for line in text:
        line.strip()
        current = int(line)
        if current > previous:
            output += 1
        previous = current

    et = time.time()
    elapsed_time = et - st

    print(f"Part One:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms\n")


def part_two():
    st = time.time()
    previous = 0
    output = -1

    for index in range(len(text) - 2):
        current_sum = sum([int(num) for num in text[index:index+3]])
        if current_sum > previous:
            output += 1
        previous = current_sum

    et = time.time()
    elapsed_time = et - st

    print(f"Part Two:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms")


part_one()
part_two()
