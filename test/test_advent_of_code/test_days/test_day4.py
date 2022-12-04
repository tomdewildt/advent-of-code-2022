import pytest

from advent_of_code.days import day4


class TestPart1:
    @pytest.mark.parametrize(
        "challenge_input,challenge_output",
        [
            ("", 0),
            ("5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8\n", 2),
        ],
    )
    def test_part1(self, challenge_input, challenge_output):
        assert day4.part1(challenge_input) == challenge_output


class TestPart2:
    @pytest.mark.parametrize(
        "challenge_input,challenge_output",
        [
            ("", 0),
            ("5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8\n", 4),
        ],
    )
    def test_part2(self, challenge_input, challenge_output):
        print(challenge_input)
        assert day4.part2(challenge_input) == challenge_output
