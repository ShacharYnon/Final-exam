from .. import config
from .connection import MongoDBConnection
from pymongo import MongoClient
import gridfs
import logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class DALMongo:
    def __init__(self, uri: str, db_name: str):
        self.db_connection = MongoDBConnection()
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db)
        

    def get_collection_names_from_DB(self):
        """Return a collection handle by name.
        if not exsist return name DB  """
        try:
            logger.info(f"The collections in DB: {self.db} ")
            return self.db.list_collection_names()
        except Exception as e:
            logger.error(f"ERROR: From DALMongo.get_collections_from_DB in DB {self.db}: {e}")
            return self.db

    def create_collection(self, name: str):
        """Create a collection if not exists."""
        try:
            if name in self.db.list_collection_names():
                logger.info(f"The collection {name}, already exists in DB: {self.db}.")
            create_collection = self.db[name]
            logger.info(f"The collection {name} created in DB: {self.db}\n")
            logger.info(f"Info collection: {create_collection}")
        except Exception as e :
            logger.error(f"ERROR: From DALMongo.create_collection: {e}")

    def upload_big_files(self ,file_path ,file_name ,file_id ):
        try:
            with open(file_path, 'rb') as file_data:
                data = file_data.read()
            self.fs.put(data ,filename= file_name ,filepath= file_path ,id=file_id)
            logger.info(f"The file was uploaded successfully, file name: {file_name}. ID: {file_id}")
        except Exception as e:
            logger.error(f"ERROR: From DALMongo.upload_big_files: {e}")
            

if __name__ == "__main__":
    dal = DALMongo(config.MONGO_URI ,config.MONGO_DB)
    dal.create_collection(config.MONGO_COL)
    dal.get_collection_names_from_DB()
    dal.upload_big_files(config.FILE_PATH_TEST ,config.FILE_NAME_TEST ,config.FILE_ID_TEST )
    

# python -m app.mongoDB.mongoDAL
    
       


