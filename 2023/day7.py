import time
import sys

def part_one(file):
    st = time.perf_counter_ns()

    hands = {}

    for line in file:
        worth = "23456789TJQKA"
        line = line.strip()
        hand, bid = line.split(" ")
        bid = int(bid.strip())

        cards = {"A": 0, "T": 0, "J": 0, "Q": 0, "K": 0}
        for i in range(2, 10): cards[str(i)] = 0

        for card in hand:
            if card != "J":
                cards[card] += 1

        highest = sorted(cards.values(), reverse=True)

        rank = 0

        if highest[0] == 5:
            rank = 6
        elif highest[0] == 4:
            rank = 5
        elif highest[0] == 3 and highest[1] == 2:
            rank = 4
        elif highest[0] == 3:
            rank = 3
        elif highest[0] == 2 and highest[1] == 2:
            rank = 2
        elif highest[0] == 2:
            rank = 1
        else:
            rank = 0

        hands[hand] = [rank, bid]

    hands = sorted(hands.items(), key=lambda x: (x[1][0], tuple(worth.find(i) for i in x[0])))
    hands = [i[1][1] for i in hands]

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")

    return sum(i * (index + 1) for index, i in enumerate(hands))


def part_two(file):
    st = time.perf_counter_ns()

    hands = {}

    for line in file:
        worth = "J23456789TQKA"
        line = line.strip()
        hand, bid = line.split(" ")
        bid = int(bid.strip())

        cards = {"A": 0, "T": 0, "J": 0, "Q": 0, "K": 0}
        for i in range(2, 10): cards[str(i)] = 0

        for card in hand:
            if card != "J":
                cards[card] += 1

        highest = sorted(cards.values(), reverse=True)

        rank = 0

        if highest[0] == 5:
            rank = 6
        elif highest[0] == 4:
            rank = 5
        elif highest[0] == 3 and highest[1] == 2:
            rank = 4
        elif highest[0] == 3:
            rank = 3
        elif highest[0] == 2 and highest[1] == 2:
            rank = 2
        elif highest[0] == 2:
            rank = 1
        else:
            rank = 0

        match hand.count("J"):
            case 0:
                pass
            case 1:
                if highest[0] == 3:
                    rank += 1 + (highest[1] != 2)
                elif highest[0] == 2:
                    rank += 2
                else:
                    rank += 1
            case 2:
                if highest[0] == 1:
                    rank = 3
                elif highest[0] == 2:
                    rank += 3 + (highest[1] != 2)
                else:
                    rank = 6
            case 3:
                if highest[0] == 1:
                    rank = 5
                else:
                    rank = 6
            case _:
                rank = 6

        hands[hand] = [rank, bid]

    hands = sorted(hands.items(), key=lambda x: (x[1][0], tuple(worth.find(i) for i in x[0])))
    hands = [i[1][1] for i in hands]

    et = time.perf_counter_ns()
    elapsed = et - st
    print("\nExecution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")

    return sum(i * (index + 1) for index, i in enumerate(hands))

print("Part one:", part_one(open("input.txt", "r")))
print("Part two:", part_two(open("input.txt", "r")))

