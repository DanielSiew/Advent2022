
with open("input.txt", "r") as file:
    text = file.readlines()

monkeys = {}
monkey_id = 0

for lines in text:
    if lines[0] == "M":
        _, monkey_id = lines.split(" ")
        monkey_id = monkey_id[0]
        monkeys[monkey_id] = {"inspected": 0}
        continue

    lines = lines.strip()
    if lines == "":
        continue

    if lines[0] == "S":
        _, items = lines.split(": ")
        items = list(items.split(", "))
        items = [item.strip() for item in items]
        monkeys[monkey_id]["items"] = items  # NOQA
        continue

    if lines[0] == "O":
        _, operation = lines.split("old ")
        operation = operation.strip()
        if operation[2:] == "old":
            operation = operation[0]+"* 2"
        monkeys[monkey_id]["operation"] = operation
        continue

    if lines[0] == "T":
        _, test = lines.split("by ")
        monkeys[monkey_id]["test"] = int(test)

    if lines[0] == "I":
        condition, target = lines.split(": ")
        _, condition = condition.split(" ")
        condition = condition.strip()
        target = target.strip()
        target = target[-1]
        monkeys[monkey_id][condition] = target

all_test = [monkeys[ID]['test'] for ID in monkeys.keys()]
divide = 1
for val in all_test:
    divide *= val

# range(20) for part 1
# range(10000) for part 2
for turn in range(10000):
    new_items = {key: [] for key in monkeys.keys()}
    for monkey in monkeys.keys():
        for item in monkeys[monkey]['items']:
            monkeys[monkey]["inspected"] += 1
            new = item + monkeys[monkey]["operation"]
            worry_level = eval(new)
            # part 1
            # worry_level //= 3

            # part 2
            worry_level %= divide

            if worry_level % monkeys[monkey]["test"] == 0:
                monkeys[monkeys[monkey]['true']]['items'].append(str(worry_level))
            else:
                monkeys[monkeys[monkey]['false']]['items'].append(str(worry_level))

        monkeys[monkey]['items'] = []


sorted_amount = [monkeys[amount]['inspected'] for amount in monkeys.keys()]
sorted_amount.sort()

print(sorted_amount)
print(sorted_amount[-2] * sorted_amount[-1])