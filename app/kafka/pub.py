from kafka import KafkaProducer
import logging
logger = logging.getLogger(__name__) 
from bson import json_util
from ..loading.expenditure import Extracting_Metadata
from .. import config

class Publisher:
    def __init__(self ,kafka_bootstrap):

        self.producer = KafkaProducer(
            bootstrap_servers=kafka_bootstrap,
            value_serializer=lambda v: json_util.dumps(v).encode('utf-8'),
        )
        self.logger = logging.getLogger("Publisher")

    def publish(self ,topic, message):
        self.producer.send(topic, value=message)
        self.logger.info(f"Sent to {topic}: {message}")


    def close(self):
        self.producer.close()

if __name__ == "main":
    pub = Publisher(config.KAFKA_BOOTSTRAP)
    pub.publish(config.TOPIC_ ,config.MESSAGE_)




