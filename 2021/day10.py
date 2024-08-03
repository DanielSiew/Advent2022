# Part One

with open('input.txt', 'r') as file:
    text = list(file.readlines())

matches = {
    '{': '}',
    '[': ']',
    '<': '>',
    '(': ')'
}
ans = 0
for line in text:
    line = line.strip()
    brackets = ''
    temp = ''
    for c in line:
        if c in '{[<(':
            brackets += c
        else:
            if brackets == '':
                temp = c
                break
            if matches[brackets[-1]] == c:
                brackets = brackets[:-1]
            else:
                temp = c
                break

    if brackets != '':
        if temp not in ')}]>':
            break
        match temp:
            case ')':
                ans += 3
            case ']':
                ans += 57
            case '}':
                ans += 1197
            case '>':
                ans += 25137

print(ans)

# Part Two
with open('input.txt', 'r') as file:
    text = list(file.readlines())

matches = {
    '{': '}',
    '[': ']',
    '<': '>',
    '(': ')'
}
ans = []
for line in text:
    line = line.strip()
    brackets = ''
    temp = ''
    flag = False
    for c in line:
        if c in '{[<(':
            brackets += c
        else:
            if matches[brackets[-1]] == c:
                brackets = brackets[:-1]
            else:
                flag = True
                break

    if flag:
        continue

    temp = 0
    while brackets != '':
        temp *= 5
        new = matches[brackets[-1]]
        match new:
            case ')': temp += 1
            case ']': temp += 2
            case '}': temp += 3
            case '>': temp += 4
        brackets = brackets[:-1]
    if temp != 0:
        ans.append(temp)
ans.sort()
print(ans[len(ans) // 2])
