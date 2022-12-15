import pytest

from advent_of_code.days import day5


class TestPart1:
    @pytest.mark.parametrize(
        "challenge_input,challenge_output",
        [
            ("\n\n", ""),
            (
                # pylint: disable=line-too-long
                "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2",
                "CMZ",
            ),
        ],
    )
    def test_part1(self, challenge_input, challenge_output):
        assert day5.part1(challenge_input) == challenge_output


class TestPart2:
    @pytest.mark.parametrize(
        "challenge_input,challenge_output",
        [
            ("\n\n", ""),
            (
                # pylint: disable=line-too-long
                "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2",
                "MCD",
            ),
        ],
    )
    def test_part2(self, challenge_input, challenge_output):
        assert day5.part2(challenge_input) == challenge_output
