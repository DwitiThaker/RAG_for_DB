from langchain_core.documents import Document

def ingest_chunks(
        mongo_docs
):
    documents = []

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
                    }                    
                )
            )

    except Exception as e:
        print(f"Exception --------> {e}")

    return documents