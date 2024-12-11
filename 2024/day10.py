import time


def part_one(file):
    st = time.perf_counter_ns()

    def resolve(coord, seen, prev=-1):
        if not 0 <= coord[0] < len(board) or not 0 <= coord[1] < len(board[0]):
            return seen
        if board[coord[0]][coord[1]] != prev + 1:
            return seen
        if board[coord[0]][coord[1]] == 9:
            seen.add(coord)
            return seen

        for dy,dx in [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]:
            resolve((coord[0] + dy, coord[1] + dx), seen, board[coord[0]][coord[1]])
        
        return seen
        

    res = 0
    board = []
    starts = []

    for y, line in enumerate(file):
        board.append([])
        for x, num in enumerate(line.strip()):
            board[y].append(int(num))
            if num == '0':
                starts.append((y, x))
    
    for coord in starts:
        res += len(resolve(coord, set()))

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


def part_two(file):
    st = time.perf_counter_ns()

    def resolve(coord, seen, prev=-1):
        if coord in seen:
            return 0
        if not 0 <= coord[0] < len(board) or not 0 <= coord[1] < len(board[0]):
            return 0
        if board[coord[0]][coord[1]] != prev + 1:
            return 0
        if board[coord[0]][coord[1]] == 9:
            return 1
        
        ans = 0

        for dy,dx in [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]:
            ans += resolve((coord[0] + dy, coord[1] + dx), seen | {coord}, board[coord[0]][coord[1]])
        
        return ans

    res = 0
    board = []
    starts = []

    for y, line in enumerate(file):
        board.append([])
        for x, num in enumerate(line.strip()):
            board[y].append(int(num) if num != "." else ".")
            if num == '0':
                starts.append((y, x))
    
    for coord in starts:
        res += resolve(coord, set())
    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


# print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
