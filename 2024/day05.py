import time

def part_one(file):
    st = time.perf_counter_ns()

    res = 0
    rules = {}
    pages = []

    lines = file.readlines()
    rules_txt, pages_txt = lines[:lines.index("\n")], lines[lines.index("\n") + 1:]

    for rule in rules_txt:
        rule = tuple(map(int, rule.strip().split("|")))
        rules[rule[0]] = [rule[1]] if rule[0] not in rules.keys() else rules[rule[0]] + [rule[1]]
        if rule[1] not in rules.keys():
            rules[rule[1]] = []

    for page in pages_txt:
        pages += [list(map(int, page.strip().split(",")))]
      
    for _pages in pages:
        valid = True
        _pages = _pages[::-1]
        for index, page in enumerate(_pages):
            if any([_page in rules[page] for _page in _pages[index+1:]]):
                valid = False
                break
        if valid:
            res += _pages[len(_pages) // 2]
            
    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


def part_two(file):
    st = time.perf_counter_ns()

    def resolve(_pages, index=0):
        if index == len(_pages) - 1:
            return _pages
        
        k = 1
        page = _pages[index]
        new_idx = -1
        for idx, _page in enumerate(_pages[index+1:]):
            if _page in rules[page]:
                new_idx = max(new_idx, idx + index + 1)
        
        if new_idx != -1:
            _pages.pop(index)
            _pages.insert(new_idx, page)
            k = 0
        
        return resolve(_pages, index + k)
        
    res = 0
    rules = {}
    pages = []

    lines = file.readlines()
    rules_txt, pages_txt = lines[:lines.index("\n")], lines[lines.index("\n") + 1:]

    for rule in rules_txt:
        rule = tuple(map(int, rule.strip().split("|")))
        rules[rule[0]] = [rule[1]] if rule[0] not in rules.keys() else rules[rule[0]] + [rule[1]]
        if rule[1] not in rules.keys():
            rules[rule[1]] = []

    for page in pages_txt:
        pages += [list(map(int, page.strip().split(",")))]
      
    for _pages in pages:
        valid = True
        _pages = _pages[::-1]
        for index, page in enumerate(_pages):
            if any([_page in rules[page] for _page in _pages[index+1:]]):
                valid = False
        if valid:
            continue
        
        res += resolve(_pages)[len(_pages) // 2]


    et = time.perf_counter_ns()
    elapsed = et - st
    print("Execution time:", f"{elapsed / 10**9}s" if (elapsed / 10**9 >= 0.1) else f"{elapsed / 10**6}ms")
    return res


print("Part 1:", part_one(open("input.txt", "r")), "\n")
print("Part 2:", part_two(open("input.txt", "r")))
