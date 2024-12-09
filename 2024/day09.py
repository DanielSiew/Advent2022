import time


def part_one(file):
    st = time.perf_counter_ns()

    res = 0
    file_blocks = []
    free_space = []

    for index, digit in enumerate(file.readlines()[0].strip()):
        [file_blocks, free_space][index % 2] += [int(digit)]

    counter = 0
    current_id = [0, len(file_blocks) - 1]
    for index in range(len(file_blocks) + len(free_space)):
        if current_id[0] > current_id[1]:
            break
        if index % 2 == 0:
            cur = file_blocks[index // 2]
            id_sum = int((cur / 2) * (2 * counter + (cur - 1)))
            res += id_sum * current_id[0]
            file_blocks[current_id[0]] = 0
            current_id[0] += 1
            counter += cur
        else:
            cur = free_space[index // 2]
            if file_blocks[current_id[1]] <= cur:  
                while cur > 0:
                    diff = min(cur, file_blocks[current_id[1]])
                    id_sum = int((diff / 2) * (2 * counter + (diff - 1)))
                    res += id_sum * current_id[1]
                    cur -= diff
                    file_blocks[current_id[1]] -= diff
                    counter += diff
                    if file_blocks[current_id[1]] < 1:
                        current_id[1] -= 1
            else:
                id_sum = int((cur / 2) * (2 * counter + (cur - 1)))
                res += id_sum * current_id[1]
                counter += cur
                file_blocks[current_id[1]] -= cur
                if file_blocks[current_id[1]] < 1:
                    current_id[1] -= 1
            
    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


def part_two(file):
    st = time.perf_counter_ns()

    res = 0
    file_blocks = []
    free_space = []
    all_spaces = []

    for index, digit in enumerate(file.readlines()[0].strip()):
        [file_blocks, free_space][index % 2] += [int(digit)]
        if index % 2 == 0:
            all_spaces += [[(int(digit), index // 2)]]
        else:
            all_spaces += [int(digit)]
            
    for idx_1, file_block in enumerate(file_blocks[::-1]):
        file_idx = len(file_blocks) - idx_1 - 1
        for idx_2, space in enumerate(free_space[:file_idx]):
            if file_block > space:
                continue
            all_spaces[2*idx_2] += [(file_block, file_idx)]
            del all_spaces[2*(file_idx)][0]
            free_space[idx_2] -= file_block
            free_space[file_idx - 1] += file_block
            all_spaces[2*idx_2 + 1] = free_space[idx_2]
            all_spaces[2*(file_idx - 1) + 1] = free_space[file_idx - 1]
            break
        
    counter = 0
    for idx, space in enumerate(all_spaces):
        if idx % 2 == 0:
            for file_block in space:
                idx_sum = int((file_block[0] / 2) * (2 * counter + (file_block[0] - 1)))
                res += idx_sum * file_block[1]
                counter += file_block[0]
        else:
            counter += space

    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
