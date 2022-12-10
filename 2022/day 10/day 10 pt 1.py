file = open("day 10.txt", "r")
text = file.readlines()

cycle = 1
x_value = 1
cycleRange = [20, 60, 100, 140, 180, 220]
signalStrength = []


def get_signal_strength(_cycle, _x_value):
    signal_strength = _cycle * _x_value

    return signal_strength


for lines in text:
    command = lines
    command.strip()

    match command[0]:
        case 'n':
            if cycle in cycleRange:
                signalStrength.append(get_signal_strength(cycle, x_value))
            cycle += 1

        case 'a':
            command, amount = command.split(" ")
            amount.strip()
            amount = int(amount)
            for wait in range(2):
                if cycle in cycleRange:
                    signalStrength.append(get_signal_strength(cycle, x_value))
                cycle += 1
            x_value += amount

print(sum(signalStrength))


