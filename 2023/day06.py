import timeit


def solution(num, limit):
    for i in range(limit // num, num + 1):
        if i * (num - i) >= limit:
            return num - (i * 2) + 1


def part_one(file):
    total = 1
    file = list(file)
    time = [int(i.strip()) for i in file[0].strip().split(" ") if i.isnumeric()]
    distance = [int(i.strip()) for i in file[1].split(" ") if i.isnumeric()]
    for (tme, dst) in zip(time, distance):
        total *= solution(tme, dst)
    return total


def part_two(file):
    file = list(file)
    time = ""
    distance = ""
    time = [time := time + i for i in file[0].strip().split(" ") if i.isnumeric()]
    distance = [distance := distance + i for i in file[1].split(" ") if i.isnumeric()]
    return solution(int(time[-1]), int(distance[-1]))


print("Part one:", part_one(open("input.txt", "r")))
print("\nPart two:", part_two(open("input.txt", "r")))


# print("Part one:", f'{part_one(open("input.txt", "r")):<10}', f'({timeit.timeit(repr(part_one(open("input.txt", "r"))), number=10)}s)')
# print("\nPart two:", f'{part_two(open("input.txt", "r")):<10}', f'({timeit.timeit(repr(part_one(open("input.txt", "r"))), number=10)}s)')
