from kafka import KafkaProducer
from bson import json_util
# from .. import config
import time
import logging
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

    def publish(self ,topic, messages):
        count = 0
        try:
            for message in messages:
                self.producer.send(topic, value=message)
                count += 1
            self.producer.flush()
            logger.info(f"Published {count} message(s) to topic '{topic}'.")
        except Exception as e:
            logger.error(f"Failed to publish to '{topic}': {e}")
            raise RuntimeError(f"Failed to publish to '{topic}': {e}")
        #     self.producer.send(topic, value=message)
        #     logger.info(f"Sent to {topic}: {message}")
        # except Exception as e:
        #     logger.error(f"ERROR: From publish : {e} ")


    def close(self):
        time.sleep(30)
        self.producer.close()

# if __name__ == "__main__":
    
#     pub = Publisher(config.KAFKA_BOOTSTRAP)
#     pub.publish(config.TOPIC_ ,config.MESSAGE_)
#     pub.close()


# python -m app.kafka.pub



