from .pub import Publisher
from app.loading.expenditure import Extracting_Metadata
from app import config
from .sub import Consumer
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

class Manager:

    def __init__(self):
        self.publisher = Publisher(config.KAFKA_BOOTSTRAP)
        self.kafka_bootstrap = config.KAFKA_BOOTSTRAP
        self.path = config.PATH
        self.topic = config.TOPIC_
        self.data = None

    def main(self):
        count = 0
        try:
            self.data = Extracting_Metadata(self.path).get_details_from_file()
            for docs in self.data:
                self.publisher.publish(self.topic ,docs)
                count += 1
            time.sleep(180)
            logger.info(f"Published {count} documents")
        except Exception as e:
            logger.error(f"ERROR: From in Manager.main : {e}")
        finally:
            self.publisher.close()

if __name__ == "__main__":
    mge = Manager()
    mge.main()
