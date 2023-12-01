# part one
print("part one:", sum(int(digits[0] + digits[-1]) for digits in [[i for i in j if i.isdigit()] for j in [line.strip() for line in open("input.txt", "r").readlines()]]))

# part two
print("part two:", sum(int(digits[0] + digits[-1]) for digits in [[i for i in j if i.isdigit()] for j in [line for line in [i.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine") for i in [line.strip() for line in open("input.txt", "r").readlines()]]]]))