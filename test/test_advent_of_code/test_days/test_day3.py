import pytest

from advent_of_code.days import day3


class TestPart1:
    @pytest.mark.parametrize(
        "challenge_input,challenge_output",
        [
            ("", 0),
            (
                # pylint: disable=line-too-long
                "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw",
                157,
            ),
        ],
    )
    def test_part1(self, challenge_input, challenge_output):
        assert day3.part1(challenge_input) == challenge_output


class TestPart2:
    @pytest.mark.parametrize(
        "challenge_input,challenge_output",
        [
            ("", 0),
            (
                # pylint: disable=line-too-long
                "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw",
                70,
            ),
        ],
    )
    def test_part2(self, challenge_input, challenge_output):
        print(challenge_input)
        assert day3.part2(challenge_input) == challenge_output
