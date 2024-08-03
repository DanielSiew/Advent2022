import time

file = open("input.txt", "r")
text = file.readlines()


def part_one():
    st = time.time()
    bits = {}
    gamma = ""
    epsilon = ""
    for index in range(len(text[0]) - 1):
        bits[index] = {
            0: 0,
            1: 0
        }

    for line in text:
        line = line.strip()
        for index in range(len(line)):
            current_bit = int(line[index])
            bits[index][current_bit] += 1

    for bit in bits.keys():
        if bits[bit][0] > bits[bit][1]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    output = gamma * epsilon

    et = time.time()
    elapsed_time = et - st

    print(f"Part One:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms\n")


def part_two():
    st = time.time()

    oxygen = [line.strip() for line in text]
    carbon = [line.strip() for line in text]
    to_calculate = []

    def iterate_oxygen(lst, bit_pos):
        if len(lst) <= 1:
            to_calculate.append(lst[0])
            return 0

        new_lst = []
        frequency = {
            0: 0,
            1: 0
        }
        for byte in lst:
            frequency[int(byte[bit_pos])] += 1

        if frequency[1] > frequency[0] or frequency[0] == frequency[1]:
            for index in range(len(lst)):
                if lst[index][bit_pos] == '1':
                    new_lst.append(lst[index])
        else:
            for index in range(len(lst)):
                if lst[index][bit_pos] == '0':
                    new_lst.append(lst[index])

        new_pos = bit_pos + 1

        iterate_oxygen(new_lst, new_pos)

    def iterate_carbon(lst, bit_pos):
        if len(lst) <= 1:
            to_calculate.append(lst[0])
            return 0

        new_lst = []
        frequency = {
            0: 0,
            1: 0
        }
        for byte in lst:
            frequency[int(byte[bit_pos])] += 1

        if frequency[0] < frequency[1] or frequency[0] == frequency[1]:
            for index in range(len(lst)):
                if lst[index][bit_pos] == '0':
                    new_lst.append(lst[index])
        else:
            for index in range(len(lst)):
                if lst[index][bit_pos] == '1':
                    new_lst.append(lst[index])

        new_pos = bit_pos + 1
        iterate_carbon(new_lst, new_pos)

    iterate_oxygen(oxygen, 0)
    iterate_carbon(carbon, 0)

    to_calculate = [int(binary, 2) for binary in to_calculate]
    output = to_calculate[0] * to_calculate[1]

    et = time.time()
    elapsed_time = et - st

    print(f"Part Two:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms")


part_one()
part_two()
