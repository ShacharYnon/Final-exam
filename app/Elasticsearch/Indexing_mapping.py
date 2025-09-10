from elasticsearch import Elasticsearch ,helpers
from .. import config
import logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

class ElasticSearch_es:

    def __init__(self,
                 address_connection,
                 mapping,
                 index_name):
        self.es = Elasticsearch(address_connection)
        self.data = None
        self.index_name = index_name
        self.mapping = mapping
        self.query = None

    def connection_to_es(self):
        try:
            es = self.es
            logger.info("Connection to ES successful")
            return es
        except Exception as e:
            logger.info(f"ERROR: from Processing.connection_to_es: {e}")

    def es_mapping(self):
        try:
            if not self.es.indices.exists(index=self.index_name):
                self.es.indices.create(index= self.index_name ,body=self.mapping)
                logger.info(f"The index was successful.")
            results = helpers.scan(self.es,index=self.index_name, body=self.query)
            return results
        except Exception as e:
            logger.info(f"ERROR: From Processing.indexing: {e}")

    def es_indexing(self ,data = None):
        if not self.es:
            raise ValueError("Elasticsearch connection not established")

        try:
            actions = [{"_index": self.index_name, "_source": doc} for doc in data]
            helpers.bulk(client=self.es, actions=actions)
            logger.info(f"Successfully indexed {len(data)} documents into {index_name}")
            return len(data)
        except Exception as e:
            logger.error(f"Failed to index data: {e}")
            raise

    
# if __name__ == "__main__":
#     es = ElasticSearch_es(
#          config.ES_ADDRESS_CONNECTION,
#          config.ES_MAPPING,
#          config.ES_INDEX_NAME
#         )
#     es.connection_to_es()
#     es.es_mapping()
#     es.es_indexing()

