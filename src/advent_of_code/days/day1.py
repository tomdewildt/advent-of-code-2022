import bisect


def part1(challenge_input):
    if len(challenge_input) == 0:
        return None

    calories = []
    current = []
    for line in challenge_input.split("\n"):
        if line == "":
            bisect.insort(calories, sum(current))
            current = []
        else:
            current.append(int(line))

    return calories[-1]


def part2(challenge_input):
    if len(challenge_input) == 0:
        return None

    calories = []
    current = []
    for line in challenge_input.split("\n"):
        if line == "":
            bisect.insort(calories, sum(current))
            current = []
        else:
            current.append(int(line))

    return calories[-1] + calories[-2] + calories[-3]
