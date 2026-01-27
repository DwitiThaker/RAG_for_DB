import time
from langchain_core.documents import Document
from rag.vectorstore import get_vectorstore
from google.api_core.exceptions import ResourceExhausted
from utils.retry import retry_with_backoff
from httpx import WriteTimeout
from qdrant_client.http.exceptions import ResponseHandlingException



def ingest_chunks_to_qdrant(
    mongo_docs,
    batch_size: int = 15,
):
    vectorstore = get_vectorstore()

    start = time.time()

    documents = []
    count = 0

    try: 
        for doc in mongo_docs:
            text = doc.get("text", "")
            if not text:
                continue

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "mongo_id": str(doc["_id"]),
                        "page": doc.get("page"),
                        "chunk_index": doc.get("chunk_index"),
                        "company_id": str(doc.get("company_id")),
                    }
                )
            )

            count += 1

            if len(documents) >= batch_size:
                def upsert_batch():
                    vectorstore.add_documents(documents)

                retry_with_backoff(
                    upsert_batch,
                    retries=3,
                    delay=5,
                    exceptions=(WriteTimeout, ResponseHandlingException),
                    label="Qdrant upsert",
                )

                print(f"Inserted batch. Total embedded = {count}")
                documents.clear()

        if documents:
            vectorstore.add_documents(documents)

    except ResourceExhausted as e:
        print("⚠️ Gemini quota exceeded. Stopping ingestion safely.")
        print(f"Inserted batch, total = {count}")
        return count

    minutes = (time.time() - start) / 60
    print(f"\n✅ Ingestion completed: {count} chunks in {minutes:.2f} minutes")
    return count
