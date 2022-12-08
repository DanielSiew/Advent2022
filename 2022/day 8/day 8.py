file = open("day 8.txt", "r")
text = file.readlines()

forest = []

for lines in text:
    tree_row = list(lines.strip())
    tree_row = [int(tree) for tree in tree_row]
    forest.append(tree_row)


def part_one():
    visible_trees = 0
    for row in range(len(forest)):
        for col in range(len(forest[row])):
            if row in [0, len(forest[row]) - 1] or col in [0, len(forest[row]) - 1]:
                visible_trees += 1
                continue

            # look from left
            visibility_left = 0
            left = list(range(0, col))
            for tree in left:
                if forest[row][col] <= forest[row][tree]:
                    visibility_left = 0
                    break
                visibility_left = 1

            # look from right
            visibility_right = 0
            right = list(range(col + 1, len(forest[row])))
            for tree in right:
                if forest[row][col] <= forest[row][tree]:
                    visibility_right = 0
                    break
                visibility_right = 1

            # look from up
            visibility_up = 0
            up = list(range(0, row))
            for tree in up:
                if forest[row][col] <= forest[tree][col]:
                    visibility_up = 0
                    break
                visibility_up = 1

            # look from down
            visibility_down = 0
            down = list(range(row + 1, len(forest[row])))
            for tree in down:
                if forest[row][col] <= forest[tree][col]:
                    visibility_down = 0
                    break
                visibility_down = 1

            visibility = visibility_left + visibility_right + visibility_down + visibility_up

            if visibility > 0:
                visible_trees += 1

    return visible_trees


def part_two():
    highest_scenic_score = []
    for row in range(len(forest)):
        for col in range(len(forest[row])):
            # edges always return 0, skip them
            if row in [0, len(forest[row]) - 1] or col in [0, len(forest[row]) - 1]:
                continue

            current_tree = forest[row][col]

            # look left
            visibility_left = 0
            left = list(range(0, col))
            left.reverse()
            for tree in left:
                visibility_left += 1
                if current_tree <= forest[row][tree]:
                    break

            # look right
            visibility_right = 0
            right = list(range(col + 1, len(forest[row])))
            for tree in right:
                visibility_right += 1
                if current_tree <= forest[row][tree]:
                    break

            # look up
            visibility_up = 0
            up = list(range(0, row))
            up.reverse()
            for tree in up:
                visibility_up += 1
                if current_tree <= forest[tree][col]:
                    break

            # look down
            visibility_down = 0
            down = list(range(row + 1, len(forest[row])))
            for tree in down:
                visibility_down += 1
                if current_tree <= forest[tree][col]:
                    break

            scenic_score = visibility_left * visibility_up * visibility_down * visibility_right
            highest_scenic_score.append(scenic_score)

    highest_scenic_score.sort(reverse=True)
    return highest_scenic_score


print(part_one(), part_two()[0])
