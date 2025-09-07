from ..import config
from pathlib import Path

import logging
logger = logging.getLogger(__name__) 


class Load_Wav:

    def __init__(self ,file_path = config.FILE_PATH):
        self.file_path = Path(file_path)
        self._file = None

    def get_file(self):
        if self._file is None:
                self._file = self.file_path
        try:
            logger.info(f"The file {self._file.name} loaded")
            return self._file
        except Exception as e :
            logger.error(f"ERROR: From Load_Wav.get_file :{e}")


if __name__ == "__main__":
    load = Load_Wav(config.FILE_PATH)
    load.get_file()



