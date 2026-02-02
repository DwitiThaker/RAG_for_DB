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


import re
from langchain_core.documents import Document

def tokenize(text: str):
    return re.findall(r"\w+", text.lower())


def tokenize_documents(documents: list[Document]):
    tokenized_docs = []

    for doc in documents:
        tokens = tokenize(doc.page_content)
        tokenized_docs.append({
            "tokens": tokens,
            "metadata": doc.metadata
        })

    return tokenized_docs

