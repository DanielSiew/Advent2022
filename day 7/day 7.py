file = open('day 7.txt', 'r')
text = file.readlines()


def find_parent(full_dict, target_dir):
    currentDir = full_dict
    for item in target_dir:
        currentDir = currentDir[item]

    return currentDir


def get_dir_name(dir_list):
    dir_name = "/"
    for item in dir_list[1:]:
        dir_name += item + "/"

    return dir_name


for line in text:
    if line[0] == '$':
        command = line[2:4]
        if command == "cd":
            directory = line[5:].strip()

            match directory:
                case '/':
                    directories = {'/': {}}
                    currentDirectory = ['/']
                    dirSize = {'/': 0}
                    currentDirectoryShow = directories['/']
                case '..':
                    del currentDirectory[-1]
                    previousDirectory = find_parent(directories, currentDirectory)
                    currentDirectoryShow = previousDirectory

                case _:
                    currentDirectory.append(directory)
                    currentDirectoryShow = currentDirectoryShow[currentDirectory[-1]]

        elif command == "ls":
            pass

    # when a dir is added
    if line[0:3] == 'dir':
        newDir = line[4:].strip()
        currentDirectoryShow[newDir] = {}
        dirName = get_dir_name(currentDirectory) + newDir
        dirSize[dirName] = 0

    # when a file is added
    if line[0].isdigit():
        size, name = line.strip().split(" ")
        currentDirectoryShow[name] = int(size)
        dirName = get_dir_name(currentDirectory)
        for name in dirSize.keys():
            if name in dirName:
                dirSize[name] += int(size)

def part_one():
    # find the total sizes of all directories with size less than 100,000
    total = 0

    for item in dirSize.keys():
        if dirSize[item] <= 100_000:
            total += dirSize[item]

    return total


def part_two():
    total_used = dirSize['/']
    unused_space = 70_000_000 - dirSize['/']
    deleteable_dir = []

    for name in dirSize.keys():
        if dirSize[name] + unused_space >= 30_000_000:
            deleteable_dir.append(name)

    smallest = str(deleteable_dir[0])
    for item in deleteable_dir:
        if dirSize[item] < dirSize[smallest]:
            smallest = str(item)

    return dirSize[smallest]


print(part_one(), part_two())
