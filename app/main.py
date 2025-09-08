import config
from .loading import load_wav ,expenditure
from .kafka import pub ,sub
import time
import logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

class Manger:
    def __init__(self):
        pass

    def load(self):
        pass

    def get_and_send_by_kafka(self):
        pass

    def start(self):
        pass

if __name__ == "__main__":
    pass


