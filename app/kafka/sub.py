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
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            value_deserializer=lambda v:
              json_util.loads(v.decode('utf-8')),
        )
        logger.info(
            f"KafkaConsumer created. topics={topic}, bootstrap={kafka_bootstrap}, group_id={group_id}"
            )
        

    def consume_messages(self):
        try:
            for message in self.consumer:
                val = message.value
                logger.info(f"Received: {message.value}")
                if not isinstance(val, dict):
                    logger.warning(
                        f"Expected dict payload but got {type(val).__name__}; wrapping into dict."
                    )
                    val = {"payload": val}
                logger.debug(f"Consumed from {message.topic}@{message.partition}/{message.offset}")
                yield val
            yield message.value
        except Exception as e:
            logger.error(f"Error consuming messages: {e}")
            raise RuntimeError(f"Error consuming messages: {e}")

    def close(self):
        
        self.consumer.close()

if __name__ == "__main__":
    cons = Consumer(config.TOPIC_ ,config.KAFKA_BOOTSTRAP ,config.GROUP_ID)
    cons.consume_messages()
    time.sleep(60)

# python -m app.kafka.sub

