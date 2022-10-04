import unittest
import datetime
from wotreplay.helper.extractor import Extractor


class TestExtractor(unittest.TestCase):

    def test_get_file_name(self):
        file = '/home/user/replays/x.wotreplay'
        file_name = Extractor.get_file_name(file)
        expected = 'x.wotreplay'
        self.assertEqual(file_name, expected)

    def test_get_replay_date(self):
        data = {"dateTime": "01.02.202003:00:00"}
        date_obj = Extractor.get_replay_date(data)
        date_expected = datetime.datetime(day=1, month=2, year=2020, hour=3, minute=0, second=0)
        self.assertEqual(date_obj, date_expected)

    def test_get_file_data(self):
        file = '/home/user/replays/x.wotreplay'
        data = Extractor.get_file_data(file)
        expected = [{"filename": "x.wotreplay"}]
        self.assertEqual(data, expected)

    def test_get_account_id(self):
        data = {"playerID": "1234"}
        data = Extractor.get_account_id(data)
        expected = '1234'
        self.assertEqual(data, expected)
