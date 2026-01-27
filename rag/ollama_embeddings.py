
from langchain_openai import OpenAIEmbeddings
from utils.timing import log_time

@log_time("Embeddings...")
def get_embedding_model():
    return OpenAIEmbeddings(
        model="text-embedding-3-small"
    )
