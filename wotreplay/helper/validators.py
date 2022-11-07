from os import path

from wotreplay.utils.loader import DataHandler


class Validator:

    @staticmethod
    def check_if_file_was_processed(file: str, model: object, db_name: str, db_path: str):
        """
        Checks if the file has been processed already
        """

        file_id = DataHandler.query_file_id(model=model, filename=file, db_name=db_name, db_path=db_path)
        if file_id:
            raise FileExistsError('File was processed before and will not be re-processed.')

    @staticmethod
    def check_if_file_exists(file: str):
        """
        Validates that file exists at the defined path
        """
        if not path.exists(file):
            raise FileNotFoundError('File was not found. Please check the location of the replay.')
