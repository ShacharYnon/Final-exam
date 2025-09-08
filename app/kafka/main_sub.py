from .sub import Consumer
from app import config
import uuid
import logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__) 


class Manager_bub:
    def __init__(self):
        self.id = uuid.uuid4()

    def main(self):
        pass

if __name__ == "__main__":
    pass