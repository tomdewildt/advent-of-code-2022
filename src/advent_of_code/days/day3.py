def part1(challenge_input):
    total = 0

    for line in challenge_input.split("\n"):
        if line == "":
            continue

        first = line[0 : len(line) // 2]
        second = line[len(line) // 2 :]

        for item in first:
            if item in second:
                total += ord(item) - 96 if item.islower() else ord(item) - 38
                break

    return total


def part2(challenge_input):
    total = 0

    current = []
    for idx, line in enumerate(challenge_input.split("\n")):
        if line == "":
            continue

        current.append(line)

        if (idx + 1) % 3 == 0:
            for item in current[0]:
                if item in current[1] and item in current[2]:
                    total += ord(item) - 96 if item.islower() else ord(item) - 38
                    break

            current = []

    return total
