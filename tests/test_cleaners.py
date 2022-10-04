import unittest
from wotreplay.helper.cleaners import Parser

data = 'this is a random string which contains {"replay_metadata": "counter_0"} something else here ' \
       '{"battle_metadata": "counter_1"}'


class TestCleaner(unittest.TestCase):
    c = Parser(file_content=data)

    def test_extract_replay_metadata(self):
        expected = {"replay_metadata": "counter_0"}
        self.assertEqual(self.c.replay_metadata, expected)

    def test_extract_battle_data(self):
        expected = [{"battle_metadata": "counter_1"}]
        self.assertEqual(self.c.battle_data, expected)
