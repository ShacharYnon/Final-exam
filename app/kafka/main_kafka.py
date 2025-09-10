from .. import config
from .sub import Consumer
from .pub import Publisher
from ..mongoDB.mongoDAL import DALMongo
from ..loading.expenditure import Extracting_Metadata
import logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__) 


class Manager:

    def __init__(self,
                kafka_bootstrap,
                topic,
                group_id,
                mongo_uri,
                mongo_name_DB,
                path
                 ):
        self.metadata = Extracting_Metadata(path=path).get_metadata_from_file()
        self.topic = topic
        self.pub = Publisher(kafka_bootstrap=kafka_bootstrap)
        self.sub = Consumer(topic=topic ,kafka_bootstrap=kafka_bootstrap ,group_id=group_id)
        self.mongo = DALMongo(uri=mongo_uri ,db_name=mongo_name_DB)
        
        
    def start(self):
        try:
            num = 0
            # publish messages
            self.pub.publish(topic=self.topic ,messages=self.metadata)
            # subscribe messages 
            while True:
                message = self.sub.consume_messages()
                num += 1
                logger.info(f"Received: {message}\n")
                # Generated unique id
                fields = message["file path"],message["details"]["name"],message["details"]["created_time"]
                field_id =  "".join(fields)
                unique_id = hash(field_id)
                logger.info(f"Generated {num} unique id: {unique_id} for file: {fields}\n ")
                # update unique id to the messages
                message.update({"unique_id":unique_id})
                logger.info(f"message.value {message}\n ")
                # send the file to mongo
                self.mongo.upload_big_files(message["file path"] ,message["details"]["name"] ,unique_id)
                #send the metadata to ES
               
        except Exception as e:
            logger.error(f"ERROR: From Manager.start ,ManagerKafka: {e}")
            raise RuntimeError(f"ERROR: From Manager.start ,ManagerKafka: {e}")


if __name__ == "__main__":
    run = Manager(
        config.KAFKA_BOOTSTRAP,
        config.KAFKA_TOPIC,
        config.KAFKA_GROUP_ID,
        config.MONGO_URI,
        config.MONGO_DB,
        config.PATH_LOAD
        )
    run.start()


# python -m app.kafka.main_kafka

