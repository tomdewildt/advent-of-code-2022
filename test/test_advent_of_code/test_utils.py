import mock

from advent_of_code.utils import load_input


class TestLoadInput:
    @mock.patch("advent_of_code.utils.open")
    def test_load_input(self, mock_open):
        mock_open.side_effect = [mock.mock_open(read_data="content").return_value]

        content = load_input("/tmp/test.txt")

        mock_open.assert_called_once_with("/tmp/test.txt", "r", encoding="utf-8")

        assert content == "content"
