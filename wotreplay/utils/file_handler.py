import io
import glob


class FileHandler:

    @staticmethod
    def list_files(path: str) -> list:
        """
        Lists all the world of tanks replay files in a certain directory.
        :param path: location of directory for which the files will be scanned
        :return: list of files in the directory
        """

        replay_files = glob.glob(path + '/*.wotreplay')

        return replay_files

    @staticmethod
    def open_file(file: str) -> str:
        """
        Opens the world of tanks replay file and puts all the content into a string object.
        :param file: world of tanks replay file
        :return: string object
        """

        with io.open(file, 'r', encoding='utf-8', errors='ignore') as infile:
            for idx, line in enumerate(infile):
                if idx == 0:
                    # Only the first line contains data. The rest is binary metadata to replay the record.
                    raw_data = []
                    raw_line = line.split()
                    for record in raw_line:
                        for letter in record:
                            if ord(letter) < 34 or ord(letter) > 127:
                                pass
                            else:
                                raw_data.append(letter)

        raw_data = ''.join(raw_data)

        return raw_data
