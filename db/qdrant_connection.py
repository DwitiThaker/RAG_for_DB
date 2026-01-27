from qdrant_client import QdrantClient, models
from config.settings import QDRANT_URL, QDRANT_API_KEY
import logging


COLLECTION_NAME = "document_chunks3"
VECTOR_SIZE = 1536


def get_qdrant_client() -> QdrantClient:
    return QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        timeout=250,
    )


def ensure_collection(client: QdrantClient):
    """
    Collection creation.
    Safe to call multiple times.
    """
    try:
        if not client.collection_exists(COLLECTION_NAME):
            client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=models.VectorParams(
                    size=VECTOR_SIZE,
                    distance=models.Distance.COSINE,
                ),
            )
            print("Qdrant collection created.")
        else:
            print("Qdrant collection already exists")

        print("update..")
        client.update_collection(
            collection_name=COLLECTION_NAME,
            hnsw_config=models.HnswConfigDiff(
                m=8,
                ef_construct=50,
                max_indexing_threads=8,
                on_disk=True,
            ),
        )
    
    except Exception as ex:
        logging.exception("Failed to ensure Qdrant collection.")
        raise RuntimeError(
            f"Error ensuring Qdrant collection '{COLLECTION_NAME}'"
        ) from ex


