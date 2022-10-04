import unittest
from sqlalchemy import create_engine

from wotreplay.orm.data_model import Base, DataModel, FileModel
from wotreplay.utils.loader import DataHandler

data = [
    {
        "filename": "test",
        "processing_time": None,
        "is_replay_complete": False,
        "processed": False
    }
]


class TestDataModelLoader(unittest.TestCase):
    engine = create_engine('sqlite:///:memory:')

    def test_db_setUp(self):
        DataModel.create_tables(self.engine)

    def test_multiple_insert(self):
        DataHandler.insert(FileModel, data, db_engine=self.engine, db_path='', db_name='')

    def test_supply_data_count(self):
        result = DataHandler.query_file_id(FileModel, db_engine=self.engine, db_path='', db_name='', filename='test')
        expected = 1
        self.assertEqual(result, expected)

    def test_xdb_tearDown(self):
        # The 'zdb' is not a typo. The database still needs to be available for the rest of the tests to run.
        # The unittest module is taking the methods in an alphabetical order so it had to be prefixed with a "z".
        Base.metadata.drop_all(self.engine)