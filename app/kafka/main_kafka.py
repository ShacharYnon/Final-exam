from .. import config
from .sub import Consumer
from .pub import Publisher
from ..mongoDB.mongoDAL import DALMongo
from ..loading.expenditure import Extracting_Metadata
import logging
from ..Elasticsearch.Indexing_mapping import ElasticSearch_es
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__) 


class Manager:

    def __init__(self,
                kafka_bootstrap,
                topic,
                group_id,
                mongo_uri,
                mongo_name_DB,
                path,
                address_connection,
                mapping,
                index_name
                 ):
        self.metadata = Extracting_Metadata(path=path).get_metadata_from_file()
        self.topic = topic
        self.pub = Publisher(kafka_bootstrap=kafka_bootstrap)
        self.sub = Consumer(topic=topic ,kafka_bootstrap=kafka_bootstrap ,group_id=group_id)
        self.mongo = DALMongo(uri=mongo_uri ,db_name=mongo_name_DB)
        self.es = ElasticSearch_es(address_connection=address_connection ,mapping=mapping,index_name=index_name )
        
        
    def start(self):
        try:
            num = 0
            # publish messages
            self.pub.publish(topic=self.topic ,messages=self.metadata)
            # subscribe messages 
            while True:
                message = self.sub.consume_messages()
                num += 1
                logger.info(f"Received: {message}\n")
                # Generated unique id
                fields = message["file path"],message["name"],message["time_details"]["created_time"]
                field_id =  "".join(fields)
                unique_id = hash(field_id)
                logger.info(f"Generated {num} unique id: {unique_id} for file: {fields}\n ")
                # update unique id to the messages
                message.update({"unique_id":unique_id})
                logger.info(f"message value {message}\n ")
                # send the file to mongo
                self.mongo.upload_big_files(message["file path"] ,message["name"] ,unique_id)
                #send the metadata to ES
                self.es.es_indexing(message)


               
        except Exception as e:
            logger.error(f"ERROR: From Manager.start ,ManagerKafka: {e}")
            raise RuntimeError(f"ERROR: From Manager.start ,ManagerKafka: {e}")


if __name__ == "__main__":
    run = Manager(
        config.KAFKA_BOOTSTRAP,
        config.KAFKA_TOPIC,
        config.KAFKA_GROUP_ID,
        config.MONGO_URI,
        config.MONGO_DB,
        config.PATH_LOAD,
        config.ES_ADDRESS_CONNECTION,
        config.ES_MAPPING,
        config.ES_INDEX_NAME
        )
    run.start()


# python -m app.kafka.main_kafka

