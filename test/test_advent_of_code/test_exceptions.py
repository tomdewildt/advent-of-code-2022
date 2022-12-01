from advent_of_code.exceptions import ChallengeNotFound, InputNotFound


class TestChallengeNotFound:
    def test_challenge_not_found(self):
        exception = ChallengeNotFound(1)

        assert str(exception) == "challenge 1 does not exist"


class TestInputNotFound:
    def test_input_not_found(self):
        exception = InputNotFound("/tmp/test.txt")

        assert str(exception) == "input /tmp/test.txt does not exist"
