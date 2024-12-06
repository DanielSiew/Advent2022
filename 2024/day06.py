import time
import sys

sys.setrecursionlimit(10000)


def part_one(file):
    st = time.perf_counter_ns()

    pos = [0, 0]
    visited = set()
    board = []

    for row, line in enumerate(file):
      board.append([])
      for col, char in enumerate(line.strip()):
         board[row].append(char)
         if char == "^":
            pos = [row, col]
  
    visited.add(tuple(pos))

    within_map = True
    direction = "up"

    while within_map:
        match direction:
          case "up":
             if pos[0] == 0:
                within_map = False
                break
             if board[pos[0] - 1][pos[1]] == "#":
                direction = "right"
                continue
             pos[0] -= 1
          case "down":
             if pos[0] == len(board) - 1:
                within_map = False
                break
             if board[pos[0] + 1][pos[1]] == "#":
                direction = "left"
                continue
             pos[0] += 1
          case "left":
             if pos[1] == 0:
                within_map = False
                break
             if board[pos[0]][pos[1] - 1] == "#":
                direction = "up"
                continue
             pos[1] -= 1
          case "right":
             if pos[1] == len(board[0]) - 1:
                within_map = False
                break
             if board[pos[0]][pos[1] + 1] == "#":
                direction = "down"
                continue
             pos[1] += 1
             
        visited.add(tuple(pos))

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return len(visited)


def part_two(file):
    st = time.perf_counter_ns()

    def traverse(_direction, _pos, seen):
        if tuple([_direction, tuple(_pos)]) in seen:
            return True
        seen.append(tuple([_direction, tuple(_pos)]))
        match _direction:
          case "up":
            if _pos[0] == 0:
                return False
            if board[_pos[0] - 1][_pos[1]] == "#":
                _direction = "right"
            else:
              _pos[0] -= 1
          case "down":
            if _pos[0] == len(board) - 1:
                return False
            if board[_pos[0] + 1][_pos[1]] == "#":
                _direction = "left"
            else:
              _pos[0] += 1
          case "left":
            if _pos[1] == 0:
                return False
            if board[_pos[0]][_pos[1] - 1] == "#":
                _direction = "up"
            else:
              _pos[1] -= 1
          case "right":
            if _pos[1] == len(board[0]) - 1:
                return False
            if board[_pos[0]][_pos[1] + 1] == "#":
                _direction = "down"
            else:
              _pos[1] += 1
        return traverse(_direction, _pos, seen)
        
    res = 0
    pos = [0, 0]
    board = []

    for row, line in enumerate(file):
      board.append([])
      for col, char in enumerate(line.strip()):
         board[row].append(char)
         if char == "^":
            pos = [row, col]

    direction = "up"
    within_map = True
    seen_changed = set()

    while within_map:
        changed = [0, 0]
        last = tuple([direction, tuple(pos)])
        match direction:
          case "up":
             if pos[0] == 0:
                within_map = False
                break
             if board[pos[0] - 1][pos[1]] == "#":
                direction = "right"
                changed = [pos[0], pos[1] + 1]
             else:
                pos[0] -= 1
                changed = list(tuple(pos))
          case "down":
             if pos[0] == len(board) - 1:
                within_map = False
                break
             if board[pos[0] + 1][pos[1]] == "#":
                direction = "left"
                changed = [pos[0], pos[1] - 1]
             else:
                pos[0] += 1
                changed = list(tuple(pos))
          case "left":
             if pos[1] == 0:
                within_map = False
                break
             if board[pos[0]][pos[1] - 1] == "#":
                direction = "up"
                changed = [pos[0] - 1, pos[1]]
             else:
                pos[1] -= 1
                changed = list(tuple(pos))
          case "right":
             if pos[1] == len(board[0]) - 1:
                within_map = False
                break
             if board[pos[0]][pos[1] + 1] == "#":
                direction = "down"
                changed = [pos[0] + 1, pos[1]]
             else:
                pos[1] += 1
                changed = list(tuple(pos))
        if board[changed[0]][changed[1]] == "#":
            continue
        if tuple(changed) in seen_changed:
           continue
        seen_changed.add(tuple(changed))
        board[changed[0]][changed[1]] = "#"
        res += traverse(last[0], list(last[1]), [])
        board[changed[0]][changed[1]] = "."

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))  # takes 80 seconds lol
