from kafka import KafkaConsumer
from bson import json_util
from .. import config
import time
import logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__) 


class Consumer:
    

    def __init__(self, topic, kafka_bootstrap, group_id):

        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=kafka_bootstrap,
            group_id=group_id,
            value_deserializer=lambda v:
              json_util.loads(v.decode('utf-8')),
        )
        

    def consume_messages(self):
       
        for msg in self.consumer:
            logger.info(f"Received: {msg.value}")
            yield msg.value

    def close(self):
        time.sleep(10)
        self.consumer.close()

if __name__ == "__main__":
    cons = Consumer(config.TOPIC_ ,config.KAFKA_BOOTSTRAP ,config.GROUP_ID)
    cons.consume_messages()

# python -m app.kafka.sub

