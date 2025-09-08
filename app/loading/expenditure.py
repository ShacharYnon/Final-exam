from .load_wav import Load_Wav
from .. import config
import pathlib
from datetime import datetime
import logging
logger = logging.getLogger(__name__) 

class Extracting_Metadata:

    def __init__(self):
        self.file = Load_Wav().get_file()
        self.file_details = None
        self.name = None
        self.created_time =None
        self.modified_time = None
        self.file_size = None


    def get_details_from_file(self): 
        if self.file is None:
            self.file = Load_Wav.get_file()
        sf = self.file 

        try:
            self.name = self.file.name
            self.created_time = sf.stat().st_ctime
            self.modified_time = sf.stat().st_mtime
            self.file_size = sf.stat().st_size
            self.file_details = {
                "file path " : config.FILE_PATH,
                "details" : {
                    "name" : self.name ,
                    "created_time" : datetime.fromtimestamp(self.created_time) ,
                    "modified_time" : datetime.fromtimestamp(self.modified_time) ,
                    "file_size" :  self.file_size
                }
            }
            logger.info()
            return self.file_details
        
        except Exception as e :
            logger.error(f"ERROR: From Extracting_details.get_details_from_file: {e}")




if __name__ == "__main__":
    extracting = Extracting_Metadata()
    ex = extracting.get_details_from_file()
    print(ex)


# python -m app.loading.expenditure