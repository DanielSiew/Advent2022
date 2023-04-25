import time

file = open("input.txt", "r")
text = file.readlines()


def part_one():
    st = time.time()

    players = {
        1: int(text[0].strip()[-1]),
        2: int(text[1][-1])
    }

    current_turn = 1

    scores = {
        1: 0,
        2: 0
    }

    counter_roll = 0
    dice = [i for i in range(1, 101)]  # stores value 1 - 100 in dice

    while scores[1] < 1000 and scores[2] < 1000:
        # cycles through 3 numbers
        three_faces = dice[0:3]
        roll = sum(three_faces) % 10
        counter_roll += 3
        dice.extend(three_faces)
        del dice[0:3]

        players[current_turn] += roll
        players[current_turn] = players[current_turn] - 10 if players[current_turn] > 10 else players[current_turn]

        scores[current_turn] += players[current_turn]

        current_turn = (current_turn * 2) % 3

    output = counter_roll * min([scores[1], scores[2]])

    et = time.time()
    elapsed_time = et - st

    print(f"Part One:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms\n")


def part_two():
    st = time.time()

    players = {
        1: int(text[0].strip()[-1]),
        2: int(text[1][-1])
    }

    current_turn = 1

    scores = {
        1: 0,
        2: 0
    }

    wins = {
        1: 0,
        2: 0
    }

    # format => <sum of faces>: <number of occurrences>
    # a roll of (2, 1, 1) gives a sum 4 => <sum of faces>
    # (2, 1, 1), (1, 2, 1), (1, 1, 2) all gives a sum 4, for a total of 3 different ways => <number of occurrences>
    # which would give => 4: 3
    rolls = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1
    }
    possible_rolls = [roll for roll in rolls.keys()]  # stores 3 - 9

    def expand(pos, score, turn, duplicates):
        if score[1] >= 21:
            wins[1] += duplicates
            return 0

        if score[2] >= 21:
            wins[2] += duplicates
            return 0

        for roll in possible_rolls:
            new_pos = {
                1: pos[1],
                2: pos[2]
            }

            new_score = {
                1: score[1],
                2: score[2]
            }
            new_pos[turn] += roll
            new_pos[turn] = new_pos[turn] - 10 if new_pos[turn] > 10 else new_pos[turn]

            new_score[turn] += new_pos[turn]

            new_turn = (turn * 2) % 3
            new_duplicates = duplicates * rolls[roll]

            if not (score[1] >= 21 or score[2] >= 21):
                expand(new_pos, new_score, new_turn, new_duplicates)

    expand(players, scores, current_turn, 1)

    et = time.time()
    elapsed_time = et - st

    print(f"Part Two:\nOutput => {wins}\nElapsed time: {elapsed_time}s")


part_one()
part_two()
