from .load_wav import Load_Wav
from .. import config
import pathlib
from datetime import datetime
import logging
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


    def get_details_from_file(self): 
        if self.files is None:
            logger.info("self.files is None")
        count = 0 
        try:
            
            for self.file in self.files:
                sf = self.file
                self.name = self.file.name
                self.created_time = sf.stat().st_ctime
                self.modified_time = sf.stat().st_mtime
                self.file_size = sf.stat().st_size
                self.file_details = {
                    "file path" : str(sf),
                    "details" : {
                        "name" : str(self.name) ,
                        "created_time" : str(datetime.fromtimestamp(self.created_time)) ,
                        "modified_time" : str(datetime.fromtimestamp(self.modified_time)) ,
                        "file_size" : str(self.file_size)
                    }
                }
                count += 1
                logger.info(f"{count} ,{self.file_details}")
            return self.file_details
        
        except Exception as e :
            logger.error(f"ERROR: From Extracting_details.get_details_from_file: {e}")

if __name__ == "__main__":
    extracting = Extracting_Metadata(config.PATH)
    extracting.get_details_from_file()

# python -m app.loading.expenditure