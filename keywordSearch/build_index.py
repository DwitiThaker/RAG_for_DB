from pymongo import MongoClient
from config.settings import MONGODB_URI, DB_NAME
from keywordSearch.keyword_ingest import ingest_chunks
from keywordSearch.tokenizer import tokenize_documents
from keywordSearch.bm25_index import build_bm25_index, save_bm25_index

if __name__ == "__main__":
    print("Building BM25 index...")

    client = MongoClient(MONGODB_URI)
    collection = client[DB_NAME]["document_chunks"]

    mongo_docs = collection.find({})
    documents = ingest_chunks(mongo_docs)
    tokenized_docs = tokenize_documents(documents)

    bm25 = build_bm25_index(tokenized_docs)
    save_bm25_index(bm25, tokenized_docs)

    print("BM25 index built and saved.")
    
