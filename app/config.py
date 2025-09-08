import os 

# load
PATH = r"C:/Users/Work/OneDrive/Desktop/The_muezzin/podcasts"
# FILE_PATH = os.getenv("FILE_PATH" , )
# kafka
KAFKA_BOOTSTRAP = os.getenv("SERVER_ADDRESS", "localhost:9092")
TOPIC_ = os.getenv("TOPIC", "topic_publisher")
MESSAGE_ = os.getenv("MESSAGE" ,"hello word") 
GROUP_ID = os.getenv("GROUP_ID", "pipeline-The-muezzin")

# IN_TOPIC = os.getenv("IN_TOPIC", "input-topic")
# OUT_TOPIC = os.getenv("OUT_TOPIC", "output-topic")



