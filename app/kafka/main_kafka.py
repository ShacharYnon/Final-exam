from .pub import Publisher
from app.loading.expenditure import Extracting_Metadata
from app import config
# from .sub import Consumer
# from bson import json_util
from .. import config
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
        self.publisher = Publisher(config.KAFKA_BOOTSTRAP)
        self.kafka_bootstrap = config.KAFKA_BOOTSTRAP
        self.path = config.PATH
        self.topic = config.TOPIC_
        self.data = None
        self.unique_id = None

    def generate_unique_id(self ,field):
        try:
            unique_id = hash(field)
            logger.info(f"Generated a unique id {unique_id} for file ")
            return unique_id
        except Exception as e:
            logger.error(f"ERROR: From in Manager.generate_unique_id : {e}") 

        

    def main(self):
        count = 0
        
        try:
            self.data = Extracting_Metadata(self.path).get_details_from_file()
            id_fields = self.data["file path"],self.data["details"]["name"],self.data["details"]["created_time"]
            field_id =  "".join(id_fields)
            self.unique_id = Manager_pub().generate_unique_id(field_id)
            for docs in self.data:
                self.publisher.publish(self.topic ,docs)
                count += 1
            logger.info(f"Published {count} documents")
            time.sleep(20)
        except Exception as e:
            logger.error(f"ERROR: From Manager.main : {e}")
        finally:
            self.publisher.close()

if __name__ == "__main__":
    mge = Manager_pub()
    mge.main()
    

# python -m app.kafka.main_pub
