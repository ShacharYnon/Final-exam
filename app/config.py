import os 

# load
PATH_LOAD = r"C:/Users/Work/OneDrive/Desktop/The_muezzin/podcasts"

# kafka
KAFKA_BOOTSTRAP = os.getenv("SERVER_ADDRESS", "localhost:9092")
KAFKA_TOPIC = os.getenv("TOPIC", "topic_TheMuezzin")
KAFKA_GROUP_ID = os.getenv("GROUP_ID", "pipeline-The-muezzin")

# mongo
MONGO_URI = os.getenv("MONGO_URI", "localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "The_muezzin")
MONGO_COL = os.getenv("MONGO_COLLECTION", "podcasts")

# Elastic
ES_ADDRESS_CONNECTION = os.getenv("ELASTIC_CONNECTION" ,"http://localhost:9200") 
ES_INDEX_NAME = os.getenv("ES_INDEX_NAME" ,"podcasts")
ES_MAPPING = {
                "mappings": {
                    "properties": {
                        "UniqueID":{"type": "Keyword"},
                        "FilePath": {"type": "Keyword"},
                        "FileName":{"type": "Keyword"},
                        "FileSize": {"type": "Keyword"},
                        "details":{
                            "type": "object",
                                "CreateDate": {"type": "datetime" ,"format": "yyyy-MM-dd"},
                                "ModifiedTime": {"type": "datetime" ,"format": "yyyy-MM-dd"},  
                                    }
                                    }
                            }   
            }

# test
MESSAGE_TEST = os.getenv("MESSAGE" ,"hello word") 
FILE_PATH_TEST = r"C:/Users/Work/OneDrive/Desktop/The_muezzin/podcasts/download (1).wav"
FILE_NAME_TEST = os.getenv("FILE_NAME_TEST" ,"test1")
FILE_ID_TEST = os.getenv("FILE_ID_TEST" ,"123123")

