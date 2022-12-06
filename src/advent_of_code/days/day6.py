def part1(challenge_input):
    marker = []

    for idx, char in enumerate(challenge_input.strip("\n")):
        marker.append(char)

        if len(marker) > 4:
            marker.remove(marker[0])

        if len(set(marker)) == 4:
            return idx + 1

    return 0


def part2(challenge_input):
    marker = []

    for idx, char in enumerate(challenge_input.strip("\n")):
        marker.append(char)

        if len(marker) > 14:
            marker.remove(marker[0])

        if len(set(marker)) == 14:
            return idx + 1

    return 0
