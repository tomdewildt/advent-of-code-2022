import os


def part1(challenge_input):
    directories = {}

    current_directories = []
    for line in challenge_input.split("\n"):
        if line == "":
            continue

        if line.startswith("$"):
            if line.startswith("$ cd .."):
                current_directories.pop()
            elif line.startswith("$ cd "):
                current_directories.append(os.path.join(*current_directories, line[5:]))
        elif not line.startswith("dir"):
            size = int(line[: line.index(" ")])

            for directory in current_directories:
                directories[directory] = directories.get(directory, 0) + size

    return sum(size for size in directories.values() if size <= 100000)


def part2(challenge_input):
    directories = {}

    current_directories = []
    for line in challenge_input.split("\n"):
        if line == "":
            continue

        if line.startswith("$"):
            if line.startswith("$ cd .."):
                current_directories.pop()
            elif line.startswith("$ cd "):
                current_directories.append(os.path.join(*current_directories, line[5:]))
        elif not line.startswith("dir"):
            size = int(line[: line.index(" ")])

            for directory in current_directories:
                directories[directory] = directories.get(directory, 0) + size

    target = 30000000 - (70000000 - directories.get("/", 0))

    return next((size for size in sorted(directories.values()) if size >= target), 0)
