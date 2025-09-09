from ..import config
from pathlib import Path

import logging
logger = logging.getLogger(__name__) 


class Load_Wav:

    def __init__(self ,path):
        self.path = Path(path)

    def get_files(self ):
        try:
            
            all_files = [file for file in self.path.iterdir() if file.is_file()]
            logger.info( f"\nlist all file in folder {self.path} \n")
            return all_files
        except Exception as e:
            logger.error(f"ERROR: From Load_Wav.get_files : {e}")


if __name__ == "__main__":
    load = Load_Wav(config.PATH)
    load.get_files()

# python -m app.loading.load_wav

