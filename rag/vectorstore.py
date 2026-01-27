from langchain_qdrant import QdrantVectorStore
from rag.ollama_embeddings import get_embedding_model
from config.settings import QDRANT_URL, QDRANT_API_KEY



from utils.timing import log_time

@log_time("Vector store (Qdrant)")
def get_vectorstore():
    embeddings = get_embedding_model()

    return QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name="document_chunks3",
    )
