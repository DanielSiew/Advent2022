file = open("input.txt", "r")
text = file.readline()


def get_answer(part):
    match part:
        case 'one':
            counter = 4
        case 'two':
            counter = 14

    value = int(str(counter))

    for index in range(len(text)):
        if len(set(text[index:index + value])) == value:
            break
        counter += 1

    return counter


print(get_answer('one'), get_answer('two'))
