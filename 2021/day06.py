import time

file = open("input.txt", "r")
text = file.readlines()


def part_one():
    st = time.time()
    to_calc = []

    line = text[0].strip()
    ages = [int(age) for age in line.split(',')]

    def iterate(states, day_counter):
        if day_counter >= 80:
            to_calc.append(len(states))
            return

        new_states = []
        to_add = 0
        for state in states:
            if state == 0:
                new_states.append(6)
                to_add += 1
            else:
                new_states.append(state - 1)

        for i in range(to_add):
            new_states.append(8)

        iterate(new_states, day_counter + 1)

    iterate(ages, 0)
    output = to_calc[0]

    et = time.time()
    elapsed_time = et - st

    print(f"Part One:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms\n")


# gah damn i cant believe i didnt think of this for pt 1  # NOQA
def part_two():
    st = time.time()
    output = 0
    to_calc = []

    line = text[0].strip()
    ages = [int(age) for age in line.split(',')]
    ages = {
        0: ages.count(0),
        1: ages.count(1),
        2: ages.count(2),
        3: ages.count(3),
        4: ages.count(4),
        5: ages.count(5),
        6: ages.count(6),
        7: 0,
        8: 0
    }

    def iterate(states, day_counter):
        if day_counter >= 256:
            to_calc.append(states)
            return

        new_states = {}
        for state in states.keys():
            temp = states[state]
            if state == 0:
                new_states[8] = temp if 8 not in new_states.keys() else new_states[8] + temp
                new_states[6] = temp if 6 not in new_states.keys() else new_states[6] + temp
            else:
                new_states[state - 1] = temp if state - 1 not in new_states.keys() else new_states[state - 1] + temp

        iterate(new_states, day_counter + 1)

    iterate(ages, 0)
    for item in to_calc[0].keys():
        output += to_calc[0][item]

    et = time.time()
    elapsed_time = et - st

    print(f"Part Two:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms")


part_one()
part_two()
