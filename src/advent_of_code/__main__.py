import os

import click

from advent_of_code.exceptions import ChallengeNotFound, InputNotFound
from advent_of_code.utils import load_input
from advent_of_code.days import (
    day1,
    day2,
    day3,
    day4,
    day5,
    day6,
    day7,
)


_CHALLENGES = {
    1: day1,
    2: day2,
    3: day3,
    4: day4,
    5: day5,
    6: day6,
    7: day7,
}


@click.command()
@click.argument("challenge", type=click.IntRange(1, 25))
@click.argument("file", type=click.Path())
def main(challenge, file):
    if not _CHALLENGES.get(challenge, None):
        raise ChallengeNotFound(challenge)
    if not os.path.exists(file):
        raise InputNotFound(file)

    challenge_input = load_input(file)

    challenge_output_1 = _CHALLENGES[challenge].part1(challenge_input)
    challenge_output_2 = _CHALLENGES[challenge].part2(challenge_input)

    print(
        f"[INFO] challenge={challenge} part1={challenge_output_1} part2={challenge_output_2}"
    )


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
