import logging
from kafka import KafkaConsumer
from bson import json_util
logger = logging.getLogger(__name__) 
from .. import config

class Consumer:
    

    def __init__(self, topic, kafka_bootstrap, group_id):

        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=kafka_bootstrap,
            group_id=group_id,
            value_deserializer=lambda v: json_util.loads(v.decode('utf-8')),
        )
        self.logger = logging.getLogger("Consumer")

    def consume_messages(self):
       
        for msg in self.consumer:
            self.logger.info(f"Received: {msg.value}")
            yield msg.value

    def close(self):
        self.consumer.close()

if __name__ == "main":
    cons = Consumer(config.TOPIC_ ,config.KAFKA_BOOTSTRAP ,config.GROUP_ID)
    cons.consume_messages()

# python -m app.kafka.sub

