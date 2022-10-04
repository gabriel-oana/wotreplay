from wotreplay.action.extract_data_from_replay import Replay
from wotreplay.utils.file_handler import FileHandler
from tqdm import tqdm


class ReplayData:

    def __init__(self, file_path: str, db_path: str, db_name: str, load: bool):
        self.file = file_path
        self.db_path = db_path
        self.db_name = db_name
        self.replay = Replay(file=file_path, db_path=db_path, db_name=db_name, load=load)
        self.battle_metadata = self.replay.get_battle_metadata()
        self.battle_performance = self.replay.get_battle_performance()
        self.common = self.replay.get_common()
        self.battle_frags = self.replay.get_battle_frags()
        self.battle_economy = self.replay.get_battle_economy()
        self.battle_xp = self.replay.get_battle_xp()
        if load:
            self.replay.update_database()


class ProcessReplays:

    @staticmethod
    def process_all(replay_dir: str, db_path: str, db_name: str) -> None:
        """
        Processes all the replay files and loads data into a sqlite database.
        """

        replay_files = FileHandler.list_files(replay_dir)

        for replay in tqdm(replay_files):
            try:
                ReplayData(file_path=replay, db_path=db_path, db_name=db_name, load=True)
            except:
                pass