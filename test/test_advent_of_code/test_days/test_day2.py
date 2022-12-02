import pytest

from advent_of_code.days import day2


class TestPart1:
    @pytest.mark.parametrize(
        "challenge_input,challenge_output",
        [
            ("", 0),
            ("A Y\nB X\nC Z\n", 15),
        ],
    )
    def test_part1(self, challenge_input, challenge_output):
        assert day2.part1(challenge_input) == challenge_output


class TestPart2:
    @pytest.mark.parametrize(
        "challenge_input,challenge_output",
        [
            ("", 0),
            ("A Y\nB X\nC Z\n", 12),
        ],
    )
    def test_part2(self, challenge_input, challenge_output):
        assert day2.part2(challenge_input) == challenge_output
