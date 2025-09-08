import os 


FILE_PATH = os.getenv("FILE_PATH" , "C:/Users/Work/OneDrive/Desktop/The-muezzin/podcasts/download (1).wav")

KAFKA_BOOTSTRAP = os.getenv("SERVER_ADDRESS", "localhost:9092")

TOPIC_ = os.getenv("TOPIC", "topic_publisher")
MESSAGE_ = os.getenv("MESSAGE" ,"hello word") 

