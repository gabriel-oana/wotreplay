import time

from wotreplay.utils.file_handler import FileHandler
from wotreplay.helper.cleaners import Parser
from wotreplay.helper.extractor import Extractor
from wotreplay.utils.loader import DataHandler
from wotreplay.orm.data_model import BattlePerformanceModel, ReplayMetadataModel, CommonModel, FileModel, BattleFrags, \
    BattleEconomyModel, BattleXpModel
from wotreplay.utils.engine import create_db_engine
from wotreplay.orm.data_model import DataModel
from wotreplay.helper.validators import Validator


class Replay:

    def __init__(self, file: str, db_path: str, db_name: str, load=True):
        self.start_time = time.time()
        self.file = file
        self.db_path = db_path
        self.db_name = db_name
        self.load = load
        self.short_name = Extractor.get_file_name(self.file)

        # Validate input
        Validator.check_if_file_exists(self.file)

        if load:
            # Initialization of database process
            engine = create_db_engine(path=self.db_path, db_name=self.db_name)
            DataModel.create_tables(engine=engine)
            Validator.check_if_file_was_processed(file=self.short_name, db_path=self.db_path, db_name=self.db_name,
                                                  model=FileModel)

            file_data = [
                {
                    "filename": self.short_name,
                    "processing_time": None,
                    "is_replay_complete": False,
                    "processed": True
                }
            ]
            DataHandler.insert(FileModel, file_data, db_path=self.db_path, db_name=self.db_name)

            self.file_id = DataHandler.query_file_id(model=FileModel, filename=self.short_name, db_name=self.db_name,
                                                     db_path=self.db_path)
        else:
            self.file_id = 0

        # Extract Data
        self._extract_data()
        self._assign_replay_date()
        self._assign_account_id()

    def _extract_data(self):
        """
        Extract data from one single replay.
        """

        # Open file
        file_object = FileHandler.open_file(self.file)

        # Clean the string file
        c = Parser(file_object)

        self.battle_data = c.battle_data
        self.meta_data = c.replay_metadata

    def _assign_account_id(self):
        """
        Gets the account_id from the metadata
        """
        self.account_id = Extractor.get_account_id(self.meta_data)

    def _assign_replay_date(self):
        """
        Gets the account_id from the metadata
        """
        self.replay_date = Extractor.get_replay_date(self.meta_data)

    def get_battle_metadata(self) -> list:
        """
        Extracts and loads
        """

        battle_metadata = Extractor.get_replay_metadata(data=self.meta_data, account_id=self.account_id,
                                                        file_id=self.file_id, replay_date=self.replay_date)

        if self.load:
            DataHandler.insert(ReplayMetadataModel, battle_metadata, db_path=self.db_path, db_name=self.db_name)

        return battle_metadata

    def get_battle_performance(self) -> list:
        """
        Extracts the battle performance data
        """
        performance = Extractor.get_battle_performance(data=self.battle_data, account_id=self.account_id,
                                                       file_id=self.file_id, replay_date=self.replay_date)

        if self.load:
            DataHandler.insert(BattlePerformanceModel, performance, db_path=self.db_path, db_name=self.db_name)

        return performance

    def get_common(self):
        common = Extractor.get_common(data=self.battle_data, account_id=self.account_id, file_id=self.file_id,
                                      replay_date=self.replay_date)

        if self.load:
            DataHandler.insert(CommonModel, common, db_path=self.db_path, db_name=self.db_name)

        return common

    def get_battle_frags(self):
        players = Extractor.get_battle_frags(data=self.battle_data, account_id=self.account_id, file_id=self.file_id,
                                             replay_date=self.replay_date)

        if self.load:
            DataHandler.insert(BattleFrags, players, db_path=self.db_path, db_name=self.db_name)

        return players

    def get_battle_economy(self):
        economy = Extractor.get_battle_economy(data=self.battle_data, account_id=self.account_id, file_id=self.file_id,
                                               replay_date=self.replay_date)

        if self.load:
            DataHandler.insert(BattleEconomyModel, economy, db_path=self.db_path, db_name=self.db_name)

        return economy

    def get_battle_xp(self):
        xp = Extractor.get_battle_xp(data=self.battle_data, account_id=self.account_id, file_id=self.file_id,
                                     replay_date=self.replay_date)

        if self.load:
            DataHandler.insert(BattleXpModel, xp, db_path=self.db_path, db_name=self.db_name)

        return xp

    def update_database(self):
        """
        Updates the database to close the file.
        """
        end_time = time.time()

        data = {
            "processing_time": end_time - self.start_time,
            "is_replay_complete": True,
            "processed": True,
        }
        DataHandler.update(model=FileModel, row_id=self.file_id, db_path=self.db_path, db_name=self.db_name, data=data)

