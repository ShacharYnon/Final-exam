from kafka import KafkaConsumer
from bson import json_util
from .. import config
from ..mongoDB.mongoDAL import DALMongo

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
        logger.info(
            f"KafkaConsumer created. topics={topic}, bootstrap={kafka_bootstrap}, group_id={group_id}"
            )
        
    def consume_messages(self):
        try:
            num = 0
            for message in self.consumer:
                num += 1
                logger.info(f"Received by consumer: {message.value}\n")
                return message.value
        except Exception as e:
            logger.error(f"Error consuming messages: {e}")
            raise RuntimeError(f"Error consuming messages: {e}")


if __name__ == "__main__":
    cons = Consumer(config.TOPIC_ ,config.KAFKA_BOOTSTRAP ,config.GROUP_ID)
    cons.consume_messages()


# python -m app.kafka.sub

