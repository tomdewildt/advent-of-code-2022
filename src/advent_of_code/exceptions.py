class ChallengeNotFound(Exception):
    def __init__(self, challenge):
        super().__init__(f"challenge {challenge} does not exist")


class InputNotFound(Exception):
    def __init__(self, file):
        super().__init__(f"input {file} does not exist")
