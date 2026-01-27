from pymongo import MongoClient
from config.settings import MONGODB_URI, DB_NAME

def stream_document_chunks(batch_size: int = 500):
    client = MongoClient(MONGODB_URI)
    try:
        db = client[DB_NAME]
        cursor = db.document_chunks.find(
            {"is_deleted": False},
            no_cursor_timeout=True
        ).batch_size(batch_size)

        for doc in cursor:
            yield doc
    finally:
        cursor.close()
        client.close()


