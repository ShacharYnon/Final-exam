from kafka import KafkaConsumer
from bson import json_util
from .. import config


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
                logger.info(f"Received: {message.value}\n")
                fields = message.value["file path"],message.value["details"]["name"],message.value["details"]["created_time"]
                field_id =  "".join(fields)
                unique_id = hash(field_id)
                logger.info(f"Generated {num} unique id: {unique_id} for file: {fields}\n ")
                message.value.update({"unique_id":unique_id})
                print(message.value)

                # send to mongo
                #send to ES
               
        except Exception as e:
            logger.error(f"Error consuming messages: {e}")
            raise RuntimeError(f"Error consuming messages: {e}")


if __name__ == "__main__":
    cons = Consumer(config.TOPIC_ ,config.KAFKA_BOOTSTRAP ,config.GROUP_ID)
    cons.consume_messages()


# python -m app.kafka.sub

