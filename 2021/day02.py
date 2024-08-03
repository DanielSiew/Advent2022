import time

file = open("input.txt", "r")
text = file.readlines()


def part_one():
    st = time.time()
    depth = 0
    horizontal_position = 0

    for line in text:
        line.strip()
        command, magnitude = line.split(" ")
        magnitude = int(magnitude)

        match command:
            case 'forward':
                horizontal_position += magnitude
            case 'down':
                depth += magnitude
            case 'up':
                depth -= magnitude

    output = horizontal_position * depth

    et = time.time()
    elapsed_time = et - st

    print(f"Part One:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms\n")


def part_two():
    st = time.time()
    depth = 0
    horizontal_position = 0
    aim = 0

    for line in text:
        line.strip()
        command, magnitude = line.split(" ")
        magnitude = int(magnitude)

        match command:
            case 'forward':
                horizontal_position += magnitude
                depth += aim * magnitude
            case 'up':
                aim -= magnitude
            case 'down':
                aim += magnitude

    output = horizontal_position * depth

    et = time.time()
    elapsed_time = et - st

    print(f"Part Two:\nOutput => {output}\nElapsed time: {elapsed_time}s")


part_one()
part_two()
