# Any NOQA comments are to remove annoying 'issues' flagged by the IDE so that I don't have to look at yellow squiggly lines  # NOQA <- lol ironic isnt it

file = open("input.txt", "r")
text = file.readlines()


def get_full_path(path_list):
    full_path = '/'
    for dir in path_list[1:]:  # NOQA
        full_path += dir + '/'

    return full_path


for lines in text:
    match lines[0]:
        case '$':
            match lines[2:4]:
                case 'cd':
                    directory = lines[5:].strip()
                    match directory:
                        case '/':
                            directories = {'/': {}}
                            dirSize = {'/': 0}
                            pathList = ['/']
                        case '..':
                            del pathList[-1]  # NOQA
                        case _:
                            pathList.append(directory)
                case 'ls':
                    currentDirectory = directories  # NOQA
                    for dir in pathList:  # NOQA
                        currentDirectory = currentDirectory[dir]
        # For commands starting with 'dir', adds a directory
        case 'd':
            newDirectory = lines[4:].strip()
            currentDirectory[newDirectory] = {}  # NOQA
            fullPath = get_full_path(pathList) + newDirectory
            dirSize[fullPath] = 0  # NOQA
        # For commands starting with anything else, adds a file
        case _:
            size, name = lines.strip().split(" ")
            currentDirectory[name] = int(size)  # NOQA
            fullPath = get_full_path(pathList)
            for dir in dirSize.keys():  # NOQA
                if dir in fullPath:
                    dirSize[dir] += int(size)


def part_one():
    # Sum of all directories of size < 100,000
    total = 0

    for item in dirSize.keys():
        if dirSize[item] <= 100_000:
            total += dirSize[item]

    return total


def part_two():
    unused_space = 70_000_000 - dirSize['/']
    deletable_dir = []

    for name in dirSize.keys():  # NOQA
        if dirSize[name] + unused_space >= 30_000_000:
            deletable_dir.append(name)

    smallest = str(deletable_dir[0])
    for item in deletable_dir:
        if dirSize[item] < dirSize[smallest]:
            smallest = str(item)

    return dirSize[smallest]


print(part_one(), part_two())
