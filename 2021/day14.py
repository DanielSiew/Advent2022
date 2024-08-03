# Part One
with open('input.txt', 'r') as file:
    text = list(file.readlines())

characters = []
mapping = {}

for lines in text[2:]:
    line = lines.strip()
    pair, inserted = line.split(" -> ")
    chars = [pair[0], pair[1], inserted]
    for char in chars:
        if char not in characters:
            characters.append(char)
    mapping[pair] = pair[0] + inserted + pair[1]


def iterate(current, limit=1, iteration=0):
    if iteration >= limit:
        return current
    _next = ''
    for idx in range(len(current) - 1):
        _chars = current[idx] + current[idx+1]
        new_chars = mapping[_chars]
        if len(_next) > 0:
            _next = _next[:-1]
        _next += new_chars
    return iterate(_next, limit, iteration+1)


original = text[0].strip()

for i in range(1, 11):
    finished = iterate(original, i)
    frequency = sorted([finished.count(_char) for _char in characters])
    print(max(frequency),min(frequency))


# Part Two
with open('input.txt', 'r') as file:
    text = list(file.readlines())

mapping = {}
freq = {}
cache = {}

for lines in text[2:]:
    line = lines.strip()
    pair, inserted = line.split(" -> ")
    chars = [pair[0], pair[1], inserted]
    for char in chars:
        if char not in freq.keys():
            freq[char] = 0
    mapping[pair] = inserted


def iterate(first, second, depth):
    cache_key = str(depth) + first + second
    if cache_key in cache:
        return cache[cache_key]
    if depth == 0:
        return {}

    insert = mapping[first + second]

    temp = {insert: 1}

    cache_1 = iterate(first, insert, depth-1)
    for key in cache_1.keys():
        if key not in temp:
            temp[key] = cache_1[key]
        else:
            temp[key] += cache_1[key]

    cache_2 = iterate(insert, second, depth-1)
    for key in cache_2.keys():
        if key not in temp:
            temp[key] = cache_2[key]
        else:
            temp[key] += cache_2[key]

    cache[cache_key] = temp
    return cache[cache_key]


original = text[0].strip()
for char in original:
    freq[char] += 1

limit = 40
for idx in range(len(original) - 1):
    iterate(original[idx], original[idx+1], limit)
    for key in cache[str(limit)+original[idx]+original[idx+1]].keys():
        freq[key] += cache[str(limit)+original[idx]+original[idx+1]][key]

frequencies = sorted(freq.items(), key=lambda x: x[1])
print(frequencies[-1][1] - frequencies[0][1])