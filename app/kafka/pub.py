from kafka import KafkaProducer
from bson import json_util
from .. import config
import time
import logging
from ..loading.expenditure import Extracting_Metadata
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__) 


class Publisher:
    def __init__(self ,kafka_bootstrap):

        self.producer = KafkaProducer(
            bootstrap_servers=kafka_bootstrap,
            value_serializer=lambda x:
              json_util.dumps(x).encode('utf-8'),
        )
        logger.info(f"KafkaProducer created. bootstrap={kafka_bootstrap}")

    def publish(self ,topic, messages:list):
        count = 0
        try: 
            for message in messages:
                self.producer.send(topic, value=message)
                count += 1
                logger.info(f" Number published: {count},\n Message: {message}. \nPublished to topic: {topic}.\n\n")
                self.producer.flush()
            logger.info(f"Published {count} message(s) to topic '{topic}'.")
        except Exception as e:
            logger.error(f"Failed to publish to '{topic}': {e}")
            raise RuntimeError(f"Failed to publish to '{topic}': {e}")


    def close(self):
        time.sleep(30)
        self.producer.close()

if __name__ == "__main__":
    metadata = Extracting_Metadata(config.PATH).get_metadata_from_file()
    pub = Publisher(config.KAFKA_BOOTSTRAP)
    pub.publish(config.TOPIC_ ,metadata)
    
    #pub.close()


# python -m app.kafka.pub



