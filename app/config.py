import os 

# load
PATH = r"C:/Users/Work/OneDrive/Desktop/The_muezzin/podcasts"

# kafka
KAFKA_BOOTSTRAP = os.getenv("SERVER_ADDRESS", "localhost:9092")
TOPIC_ = os.getenv("TOPIC", "topic_publisher_test_test_test")
MESSAGE_ = os.getenv("MESSAGE" ,"hello word") 
GROUP_ID = os.getenv("GROUP_ID", "pipeline-The-muezzin")

# mongo
MONGO_URI = os.getenv("MONGO_URI", "localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "my_database")
MONGO_COL = os.getenv("MONGO_COLLECTION", "my_collection")

# Elastic
ELASTIC_CONNECTION = os.getenv("ELASTIC_CONNECTION" ,"http://localhost:9200") 





