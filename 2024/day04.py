import time


def part_one(file):
    st = time.perf_counter_ns()
    
    res = 0
    board = []

    for line in file:
        board.append(line.strip())

    height = len(board)
    width = len(board[0])

    def search(i, j, string, direction=""):
        if any([i < 0, j < 0, i >= height, j >= width]):
            return False
        
        if board[i][j] != "XMAS"[len(string)]:
            return False
        
        string += board[i][j]

        if len(string) == 4:
            return string == "XMAS"
        
        if direction == "":
          return sum([
              search(i + 1, j, string, 0),
              search(i - 1, j, string, 1),
              search(i, j + 1, string, 2),
              search(i, j - 1, string, 3),
              search(i + 1, j + 1, string, 4),
              search(i + 1, j - 1, string, 5),
              search(i - 1, j + 1, string, 6),
              search(i - 1, j - 1, string, 7)
          ])
        
        match(direction):
          case 0:
            return search(i + 1, j, string, 0)
          case 1:
            return search(i - 1, j, string, 1)
          case 2:
            return search(i, j + 1, string, 2)
          case 3:
            return search(i, j - 1, string, 3)
          case 4:
            return search(i + 1, j + 1, string, 4)
          case 5:
            return search(i + 1, j - 1, string, 5)
          case 6:
            return search(i - 1, j + 1, string, 6)
          case 7:
            return search(i - 1, j - 1, string, 7)
    
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char == "X":
                res += search(i, j, "")

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


def part_two(file):
    st = time.perf_counter_ns()

    res = 0
    board = []

    for line in file:
        board.append(line.strip())

    for i, row in enumerate(board[1:-1]):
       for j, char in enumerate(row[1:-1]):
          if char != "A":
             continue
          res += (
            "".join(board[i+k+1][j+k+1] for k in range(-1, 2)) in ["MAS", "SAM"]
            and
            "".join(board[i-k+1][j+k+1] for k in range(-1, 2)) in ["MAS", "SAM"]
          )

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res

print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
