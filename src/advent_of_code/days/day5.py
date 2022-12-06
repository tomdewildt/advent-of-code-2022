import math


def _parse_stacks(stacks_input):
    stacks = []

    for line in reversed(stacks_input.split("\n")):
        if line.startswith(" 1 "):
            num_stacks = math.ceil(len(line) / 4)
            stacks = [[] for _ in range(num_stacks)]
            continue

        for idx in range(0, len(line), 4):
            crate = line[idx : idx + 3]

            if crate.strip() != "":
                stacks[idx // 4].append(crate[1])

    return stacks


def _parse_moves(moves_input):
    moves = []

    for line in moves_input.split("\n"):
        if line == "":
            continue

        parts = line.split(" ")

        moves.append((int(parts[1]), int(parts[3]), int(parts[5])))

    return moves


def part1(challenge_input):
    stacks_input, moves_input = challenge_input.split("\n\n")
    stacks = _parse_stacks(stacks_input)
    moves = _parse_moves(moves_input)

    for qty, from_stack, to_stack in moves:
        for _ in range(qty):
            stacks[to_stack - 1].append(stacks[from_stack - 1].pop())

    return "".join(stack[-1] for stack in stacks)


def part2(challenge_input):
    stacks_input, moves_input = challenge_input.split("\n\n")
    stacks = _parse_stacks(stacks_input)
    moves = _parse_moves(moves_input)

    for qty, from_stack, to_stack in moves:
        stacks[to_stack - 1].extend(stacks[from_stack - 1][-qty:])
        stacks[from_stack - 1] = stacks[from_stack - 1][:-qty]

    return "".join(stack[-1] for stack in stacks)
