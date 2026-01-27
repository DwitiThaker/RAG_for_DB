# main_ingest_chunks.py
from db.mongo_chunks_reader import stream_document_chunks
from pipeline.ingest_chunks_to_qdrant import ingest_chunks_to_qdrant
from db.qdrant_connection import get_qdrant_client, ensure_collection


if __name__ == "__main__":
    print("🚀 Starting Mongo → Qdrant ingestion")

    qdrant_client = get_qdrant_client()
    ensure_collection(qdrant_client)

    docs = stream_document_chunks()
    count = ingest_chunks_to_qdrant(docs)


    print(f"✅ Successfully ingested {count} document chunks into Qdrant")

