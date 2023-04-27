import time

file = open("input.txt", "r")
text = file.readlines()


def part_one():
    st = time.time()
    output = 0

    for line in text:
        line = line.strip()
        _, output_values = line.split(" | ")
        output_values = output_values.split(" ")

        for char in output_values:
            if len(char) in [2, 3, 4, 7]:
                output += 1

    et = time.time()
    elapsed_time = et - st

    print(f"Part One:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms\n")


def part_two():
    st = time.time()
    to_calc = []

    # hard-coding what number correlates to which segments that light up
    segments = {
        '0': [0, 1, 2, 4, 5, 6],
        '1': [2, 5],
        '2': [0, 2, 3, 4, 6],
        '3': [0, 2, 3, 5, 6],
        '4': [1, 2, 3, 5],
        '5': [0, 1, 3, 5, 6],
        '6': [0, 1, 3, 4, 5, 6],
        '7': [0, 2, 5],
        '8': [0, 1, 2, 3, 4, 5, 6],
        '9': [0, 1, 2, 3, 5, 6]
    }

    for line in text:
        line = line.strip()
        signal_patterns, output_values = line.split(" | ")
        signal_patterns, output_values = signal_patterns.split(" "), output_values.split(" ")
        five_long = [signal for signal in signal_patterns if len(signal) == 5]
        six_long = [signal for signal in signal_patterns if len(signal) == 6]

        displayed_numbers = {}
        mapping = {}
        for signal in signal_patterns:
            match len(signal):
                case 2:
                    displayed_numbers['1'] = set(signal)
                case 3:
                    displayed_numbers['7'] = set(signal)
                case 4:
                    displayed_numbers['4'] = set(signal)
                case 7:
                    displayed_numbers['8'] = set(signal)

        mapping['0'] = displayed_numbers['7'] - displayed_numbers['1']

        for item in six_long:
            if not displayed_numbers['1'].issubset(set(item)):
                mapping['2'] = displayed_numbers['8'] - set(item)

        mapping['5'] = displayed_numbers['1'] - mapping['2']

        for item in five_long:
            if displayed_numbers['1'].issubset(set(item)):
                three_and_six = set(set(item) - displayed_numbers['7'])

        for item in five_long:
            if not displayed_numbers['1'].issubset(set(item)):
                if mapping['2'].issubset(set(item)):
                    mapping['4'] = set(item) - three_and_six - mapping['0'] - mapping['2']
                if mapping['5'].issubset(set(item)):
                    mapping['1'] = set(item) - three_and_six - mapping['0'] - mapping['5']

        for item in six_long:
            if mapping['4'].issubset(set(item)) and mapping['2'].issubset(set(item)):
                displayed_numbers['0'] = set(item)

        mapping['6'] = displayed_numbers['0'] - mapping['0'] - mapping['1'] - mapping['2'] - mapping['4'] - mapping['5']
        mapping['3'] = displayed_numbers['4'] - mapping['1'] - mapping['2'] - mapping['5']

        new_mapping = {}
        for item in mapping.keys():
            new_mapping[int(item)] = str(list(mapping[item])[0])

        string_to_number = {}
        for number in segments.keys():
            string = ''
            for segment in segments[number]:
                string += new_mapping[segment]

            for item in output_values:
                if set(string) == set(item):
                    string_to_number[item] = number

        string = ""
        for item in output_values:
            string += string_to_number[item]

        to_calc.append(int(string))

    output = sum(to_calc)

    et = time.time()
    elapsed_time = et - st

    print(f"Part Two:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms")


part_one()
part_two()
