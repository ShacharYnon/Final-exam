from kafka import KafkaProducer
import logging
logger = logging.getLogger(__name__) 
from bson import json_util
from ..loading.expenditure import Extracting_Metadata

class Publisher:
    def __init__(self ,kafka_bootstrap):

        self.producer = KafkaProducer(
            bootstrap_servers=kafka_bootstrap,
            value_serializer=lambda v: json_util.dumps(v).encode('utf-8'),
        )

