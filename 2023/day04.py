import timeit


def part_one(file):
    total = 0
    for line in file:
        hits = 0

        card, rest = line.strip().split(":")
        winning, nums = rest.split("|")
        winning = [int(i) for i in winning.split(" ") if i.isnumeric()]
        nums = [int(i) for i in nums.split(" ") if i.isnumeric()]

        for i in winning:
            hits += 1 if i in nums else 0

        total += 2**(hits-1) if hits != 0 else 0

    return total


def part_two(file):
    cards = {}

    for i in range(1, len(list(open("input.txt", "r")))+1):
        cards[i] = 1
    total = 0

    for line in file:
        hits = 0

        card, rest = line.strip().split(":")
        card = int(card.split(" ")[-1].strip())
        winning, nums = rest.split("|")
        winning = [int(i) for i in winning.split(" ") if i.isnumeric()]
        nums = [int(i) for i in nums.split(" ") if i.isnumeric()]

        for i in winning:
            hits += 1 if i in nums else 0

        for i in range(1, hits+1):
            cards[card + i] += cards[card]

        total += 2 ** (hits - 1) if hits != 0 else 0

    total = 0
    for i in cards:
        total += cards[i]

    return total


print("Part one:", part_one(open("input.txt", "r")))
print("\nPart two:", part_two(open("input.txt", "r")))

# welcome to the messy one-line zone
print("\nPart one:", sum(i for i in [2**([j in i[1] for j in i[0]].count(True)-1) for i in [[[int(i) for i in
thing[n].strip().split(" ") if i.isnumeric()] for n in range(2)] for thing in [row.split("|") for row in
[line.strip().split(":")[-1] for line in open("input.txt", "r").readlines()]]]] if i >= 1))

print("\nPart two:" + repr(current := [0, [(1, i[1]) for i in [[card[0], [i in card[1][1] for i in card[1][0]]
.count(True)] for card in [[int(row[0].split(" ")[-1]), [[int(i) for i in nums.split("|")[n].split(" ") if
i.isnumeric()] for nums in [row[1]] for n in range(2)]] for row in [line.strip().split(":") for line in
open("input.txt", "r").readlines()]]]]])[-1].strip("]").strip(), [current := [current[0] + current[1][0][0],
[(thing[0] + (current[1][0][1] > index) * current[1][0][0], thing[1]) for index, thing in enumerate(current[1][1:])]]
for _ in range(len(current[1]))][-1][0])  # this is the pinnacle of my one-line codes
