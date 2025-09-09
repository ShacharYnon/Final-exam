from .pub import Publisher
from app.loading.expenditure import Extracting_Metadata
from app import config
from .sub import Consumer
# from .. import config as cfg
import time
import logging

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__) 

class Manager_kafka:

    def __init__(self):
        self. group_id = config.GROUP_ID
        self.kafka_bootstrap = config.KAFKA_BOOTSTRAP
        self.topic = config.TOPIC_
        self.path = config.PATH
        self.publisher = Publisher(kafka_bootstrap=self.kafka_bootstrap)
        self.consumer = Consumer(
            topic=self.topic,
            kafka_bootstrap=self.kafka_bootstrap,
            group_id=self.group_id
        )
        self.metadata = Extracting_Metadata(self.path).get_metadata_from_file()
        
        self.time_sleep_seconds = time.sleep(60)

    def generate_unique_id(self ,field_id):
        try:
            unique_id = hash(field_id)
            logger.info(f"Generated a unique id {unique_id} for file ")
            return unique_id
        except Exception as e:
            logger.error(f"ERROR: From in Manager.generate_unique_id : {e}") 


    def main(self):
        count = 0
        try:
            id_fields = self.metadata["file path"],self.metadata["details"]["name"],self.metadata["details"]["created_time"]
            field_id =  "".join(id_fields)
            unique_id = Manager_kafka().generate_unique_id(field_id)

            for doc in self.consumer.consume_messages():
                self.publisher.publish(self.topic ,doc)
                logger.info(f"Published from topic:{self.topic} docs:{doc}")
                count += 1
            logger.info(f"Published {count} documents")
            time.sleep(self.time_sleep_seconds)
        except Exception as e:
            logger.error(f"ERROR: From Manager_kafka.main : {e}")
        finally:
            self.publisher.close()

if __name__ == "__main__":
    mge = Manager_kafka()
    mge.main()
    

# python -m app.kafka.main_kafka
