from db.qdrant_connection import models, get_qdrant_client, COLLECTION_NAME
from rag.ollama_embeddings import get_embedding_model
from utils.timing import log_time

QDRANT_CLIENT = get_qdrant_client()
EMBEDDINGS = get_embedding_model()

@log_time("Qdrant Retriever")
def retrieve_chunks(query, top_k=5):  #, company_id=None
    try:
        query_vector = EMBEDDINGS.embed_query(query)

        # q_filter = None
        # if company_id:
        #     q_filter = models.Filter(
        #         must=[
        #             models.FieldCondition(
        #                 key="company_id",
        #                 match=models.MatchValue(value=company_id),
        #             )
        #         ]
        #     )

        results = QDRANT_CLIENT.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            # query_filter=q_filter,
            with_payload=True,
            limit=top_k,
        )
    except Exception as e:
        print(f"Exception -----------> {e}")

    return [
    {
        "text": p.payload.get("page_content"),
        "mongo_id": p.payload.get("metadata", {}).get("mongo_id"),
        "page": p.payload.get("metadata", {}).get("page"),
        "chunk_index": p.payload.get("metadata", {}).get("chunk_index"),
        "score": p.score,
    }
    for p in results.points
    if p.payload.get("metadata", {}).get("mongo_id") is not None
]

