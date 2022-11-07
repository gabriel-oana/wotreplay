from wotreplay.action.extract_data_from_replay import Replay
from wotreplay.utils.file_handler import FileHandler
from tqdm import tqdm


class ReplayData:

    def __init__(self, file_path: str, db_path: str = None, db_name: str = None, load: bool = False):
        self.file = file_path
        self.db_path = db_path
        self.db_name = db_name
        self.replay = Replay(file=file_path, db_path=db_path, db_name=db_name, load=load)
        if load:
            self.replay.update_database()

    @property
    def battle_metadata(self):
        return self.replay.get_battle_metadata()

    @property
    def battle_performance(self):
        return self.replay.get_battle_performance()

    @property
    def common(self):
        return self.replay.get_common()

    @property
    def battle_frags(self):
        return self.replay.get_battle_frags()

    @property
    def battle_economy(self):
        return self.replay.get_battle_economy()

    @property
    def battle_xp(self):
        return self.replay.get_battle_xp()


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