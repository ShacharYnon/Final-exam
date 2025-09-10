from elasticsearch import Elasticsearch
# from .. import config

import logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
# es = Elasticsearch(config.ES_CONNECTION)

# Define the mapping


# Create the index with the specified mapping

es = Elasticsearch("http://localhost:9200")
mapping = {
                "mappings": {
                    "properties": {
                        "UniqueID":{"type": "keyword"},
                        "FilePath": {"type": "keyword"},
                        "FileName":{"type": "keyword"},
                        "FileSize": {"type": "keyword"},
                        "details":{
                            "type": "object",
                                "CreateDate":{"type": "datetime"},
                                "ModifiedTime":{"type": "datetime"},
                                    }
                                    }
                            }   
            }

index_name = "podcasts"
try:
    es.indices.create(index=index_name, body=mapping )
    logger.info(f"Index '{index_name}' created successfully with custom mapping.")
except Exception as e:
    if "resource_already_exists_exception" in str(e):
        logger.info(f"Index '{index_name}' already exists. Skipping creation.")
    else:
        logger.error(f"Error creating index: {e}")
