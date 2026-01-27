
# from rag.vectorstore import get_vectorstore


# def retrieve_chunks(query: str, top_k: int = 5):
#     vector_store = get_vectorstore()

#     results = vector_store.similarity_search(
#         query=query,
#         k=top_k,
#     )

#     return results


from db.qdrant_connection import models, get_qdrant_client, COLLECTION_NAME
from rag.ollama_embeddings import get_embedding_model
from utils.timing import log_time

QDRANT_CLIENT = get_qdrant_client()
EMBEDDINGS = get_embedding_model()

@log_time("Qdrant Retriever")
def retrieve_chunks(query, top_k=5, company_id=None):
    query_vector = EMBEDDINGS.embed_query(query)

    q_filter = None
    if company_id:
        q_filter = models.Filter(
            must=[
                models.FieldCondition(
                    key="company_id",
                    match=models.MatchValue(value=company_id),
                )
            ]
        )

    results = QDRANT_CLIENT.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        query_filter=q_filter,
        with_payload=["page_content"],
        limit=top_k,
    )

    return [
        {
            "text": p.payload["page_content"],
            # "metadata": p.payload,
            "score": p.score,
        }
        for p in results.points
    ]
