# 31-31,32-40
def part1(challenge_input):
    count = 0

    for line in challenge_input.split("\n"):
        if line == "":
            continue

        first, second = line.split(",")

        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")
        first_start, first_end = int(first_start), int(first_end)
        second_start, second_end = int(second_start), int(second_end)

        if (first_start >= second_start and first_end <= second_end) or (
            second_start >= first_start and second_end <= first_end
        ):
            count += 1

    return count


def part2(challenge_input):
    count = 0
    for line in challenge_input.split("\n"):
        if line == "":
            continue

        first, second = line.split(",")

        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")
        first_start, first_end = int(first_start), int(first_end)
        second_start, second_end = int(second_start), int(second_end)

        if max(first_start, second_start) <= min(first_end, second_end):
            count += 1

    return count
