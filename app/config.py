import os 

# load
FILE_PATH = os.getenv("FILE_PATH" , "C:/Users/Work/OneDrive/Desktop/The-muezzin/podcasts/download (1).wav")

# kafka
KAFKA_BOOTSTRAP = os.getenv("SERVER_ADDRESS", "localhost:9092")
TOPIC_ = os.getenv("TOPIC", "topic_publisher")
MESSAGE_ = os.getenv("MESSAGE" ,"hello word") 
GROUP_ID = os.getenv("GROUP_ID", "pipeline-The-muezzin")
# IN_TOPIC = os.getenv("IN_TOPIC", "input-topic")
# OUT_TOPIC = os.getenv("OUT_TOPIC", "output-topic")



