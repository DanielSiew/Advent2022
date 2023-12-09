# oneliners are at the bottom
import timeit


def part_one(file):
    total = 0

    for line in file:
        digits = [i for i in line if i.isdigit()]
        total += int(digits[0] + digits[-1])

    return total


def part_two(file):
    total = 0

    for line in file:
        for index, num in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            line = line.replace(num, num + str(index + 1) + num)
        digits = [i for i in line if i.isdigit()]
        total += int(digits[0] + digits[-1])

    return total


print("Part 1:", part_one(open("input.txt", "r")))
print("\nPart 2:", part_two(open("input.txt", "r")))

# welcome to the messy one-line zone
print("\nPart 1:", sum(int(digits[0] + digits[-1]) for digits in [[i for i in j if i.isdigit()] for j in
[line.strip() for line in open("input.txt", "r").readlines()]]))

print("\nPart 2:", sum(int(digits[0] + digits[-1]) for digits in [[i for i in j if i.isdigit()] for j in
[line for line in [i.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three")
.replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven",
"seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine") for i in [line.strip() for
line in open("input.txt", "r").readlines()]]]]))
