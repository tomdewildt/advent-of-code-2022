import pytest

from advent_of_code.days import day1


class TestPart1:
    @pytest.mark.parametrize(
        "challenge_input,challenge_output",
        [
            ("", None),
            ("1\n2\n3\n4\n5\n", 15),
            ("1\n2\n3\n4\n5\n\n6\n7\n8\n9\n10\n", 40),
        ],
    )
    def test_part1(self, challenge_input, challenge_output):
        assert day1.part1(challenge_input) == challenge_output


class TestPart2:
    @pytest.mark.parametrize(
        "challenge_input,challenge_output",
        [
            ("", None),
            ("1\n1\n\n2\n2\n\n3\n3\n", 12),
            ("1\n1\n\n2\n2\n\n3\n3\n\n4\n4\n\n5\n5\n\n6\n6\n", 30),
        ],
    )
    def test_part2(self, challenge_input, challenge_output):
        assert day1.part2(challenge_input) == challenge_output
