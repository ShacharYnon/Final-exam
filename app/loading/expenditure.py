from .load_wav import Load_Wav
from .. import config
import pathlib
from datetime import datetime
import logging

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class Extracting_Metadata:

    def __init__(self ,path):
        self.files = Load_Wav(path).get_files()
        self.file = None
        self.file_details = None
        self.name = None
        self.created_time =None
        self.modified_time = None
        self.file_size = None


    def get_metadata_from_file(self): 
        if self.files is None:
            logger.info("self.files is None")
        count = 0 
        try:
            all_metadata_files = []
            for file in self.files:
                count += 1
                sf = file
                name = file.name
                created_time = sf.stat().st_ctime
                modified_time = sf.stat().st_mtime
                file_size = sf.stat().st_size
                
                file_metadata = {
                    "file path" : str(sf),
                    "details" : {
                        "name" : str(name) ,
                        "created_time" : str(datetime.fromtimestamp(created_time)) ,
                        "modified_time" : str(datetime.fromtimestamp(modified_time)) ,
                        "file_size" : str(file_size)
                    }
                }
                
                logger.info(f"Creating metadata: number of file:{count},\n name of file: {name},\n metadata of file:{file_metadata}\n\n")
                all_metadata_files.append(file_metadata)
            # print(all_metadata_files)
            return all_metadata_files
        
        except Exception as e :
            logger.error(f"ERROR: From Extracting_details.get_details_from_file: {e}")

if __name__ == "__main__":
    extracting = Extracting_Metadata(config.PATH)
    extracting.get_metadata_from_file()

# python -m app.loading.expenditure