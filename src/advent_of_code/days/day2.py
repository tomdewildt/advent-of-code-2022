OUTCOMES = {
    # me  opp  out act
    ("X", "C"): 6 + 1,
    ("Y", "A"): 6 + 2,
    ("Z", "B"): 6 + 3,
    ("X", "A"): 3 + 1,
    ("Y", "B"): 3 + 2,
    ("Z", "C"): 3 + 3,
    ("X", "B"): 0 + 1,
    ("Y", "C"): 0 + 2,
    ("Z", "A"): 0 + 3,
}


def part1(challenge_input):
    total_score = 0

    for line in challenge_input.split("\n"):
        if line == "":
            continue

        opponent, me = line.split(" ")

        total_score += OUTCOMES[(me, opponent)]

    return total_score


STRATEGIES = {
    # str opp  out act
    ("X", "A"): 0 + 3,
    ("X", "B"): 0 + 1,
    ("X", "C"): 0 + 2,
    ("Y", "A"): 3 + 1,
    ("Y", "B"): 3 + 2,
    ("Y", "C"): 3 + 3,
    ("Z", "A"): 6 + 2,
    ("Z", "B"): 6 + 3,
    ("Z", "C"): 6 + 1,
}


def part2(challenge_input):
    total_score = 0

    for line in challenge_input.split("\n"):
        if line == "":
            continue

        opponent, strategy = line.split(" ")

        total_score += STRATEGIES[(strategy, opponent)]

    return total_score
