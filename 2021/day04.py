# I AM SO SORRY FROM THE BOTTOM OF MY HEART FOR THIS MESS OF A CODE... IF IT WORKS, IT WORKS RIGHT? HAHA!!!!!!!!!!

import time

file = open("input.txt", "r")
text = file.readlines()


def part_one():
    st = time.time()
    output = 0

    # boards{0: {}} => the 0th (1st) board
    # 0: {0: [], 1: [], ...} => how many numbers are hit in each row/column. (i will call 0:, 1:, ... as 'states')
    # e.g. row [1, 2, 3, 4, 5] and number 1 and 4 has been called out.
    # this would mean that this row has 2 numbers that are hit, which puts the row in 2: [[1, 2, 3, 4, 5]]
    # each board starts out with 10 rows/columns in the 0 state, as columns are treated as rows also.
    boards = {0: {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}}

    # just keeping track of all numbers in a board to count the sum for output later
    full_boards = {0: []}
    board_counter = 0

    for line in text[2:]:
        line = line.strip()
        row = line.split()
        if line == "":
            board_counter += 1
            boards[board_counter] = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
            full_boards[board_counter] = []
        else:
            boards[board_counter][0].append(row)
            to_append = [int(item) for item in row]
            full_boards[board_counter].extend(to_append)

    for board in full_boards.keys():
        # don't ask why this is inconsistent with part two...
        # keeps track of the sum for each board in a list with the actual board itself
        full_boards[board] = [full_boards[board], sum(full_boards[board])]

    for board in boards.keys():
        big_add = []
        for i in range(len(boards[board][0][0])):
            to_add = []
            for j in range(len(boards[board][0][0])):
                value = boards[board][0][j][i]
                to_add.append(value)
            big_add.append(to_add)
        boards[board][0].extend(big_add)

    numbers = text[0]
    numbers = numbers.strip().split(',')

    # oh heavens... oh lord... there's 4-nested
    flag = False
    for number in numbers:
        for board in full_boards.keys():
            if int(number) in full_boards[board][0]:
                full_boards[board][1] -= int(number)

        for board in boards.keys():
            new_board = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
            for state in boards[board].keys():
                for line in boards[board][state]:
                    if number in line:
                        new_state = int(state) + 1
                        new_board[new_state].append(line)
                    else:
                        new_board[state].append(line)

            boards[board] = new_board

        for board in boards.keys():
            if len(boards[board][5]) != 0:
                output = full_boards[board][1] * int(number)
                flag = True

        if flag:
            break

    et = time.time()
    elapsed_time = et - st

    print(f"Part One:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms\n")


def part_two():
    st = time.time()
    output = 0

    boards = {0: {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}}
    full_boards = {0: []}
    board_counter = 0

    for line in text[2:]:
        line = line.strip()
        row = line.split()
        if line == "":
            board_counter += 1
            boards[board_counter] = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
            full_boards[board_counter] = []
        else:
            boards[board_counter][0].append(row)
            to_append = [int(item) for item in row]
            full_boards[board_counter].extend(to_append)

    for board in boards.keys():
        big_add = []
        for i in range(len(boards[board][0][0])):
            to_add = []
            for j in range(len(boards[board][0][0])):
                value = boards[board][0][j][i]
                to_add.append(value)
            big_add.append(to_add)
        boards[board][0].extend(big_add)

    numbers = text[0]
    numbers = numbers.strip().split(',')

    flag = False
    for number in numbers:
        for board in full_boards.keys():
            if int(number) in full_boards[board]:
                del full_boards[board][full_boards[board].index(int(number))]

        for board in boards.keys():
            new_board = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
            for state in boards[board].keys():
                for line in boards[board][state]:
                    if number in line:
                        new_state = int(state) + 1
                        new_board[new_state].append(line)
                    else:
                        new_board[state].append(line)

            boards[board] = new_board

        won = 0
        for board in boards.keys():
            if len(boards[board][5]) != 0:
                won += 1

        if won == len(boards.keys()):
            print(won, number)
            for board in boards.keys():
                for check in boards[board][5]:
                    # checking for <= 2 because a hit number could trigger two different wins at once (diagonals excl.)
                    # (bless prompt for not making diagonal, checking for higher number would have not worked)
                    # also checking <= 2 to find the most recent win
                    # the prompt is worded so that there can only be one board when the last board wins
                    # meaning that if the last number before all boards win is called, no more than one board will win
                    if number in check and len(boards[board][5]) <= 2:
                        output = sum(full_boards[board]) * int(number)
                        flag = True  # silly little flag because yeah!

        if flag:
            break

    et = time.time()
    elapsed_time = et - st

    print(f"Part Two:\nOutput => {output}\nElapsed time: {elapsed_time * 1000}ms")


part_one()
part_two()
