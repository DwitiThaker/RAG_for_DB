from rank_bm25 import BM25Okapi
import pickle
from typing import List, Dict


def build_bm25_index(tokenized_docs: List[Dict]):
    """
    tokenized_docs: [
        {
            "tokens": [...],
            "metadata": {...},
            "content": "original text"
        }
    ]
    """
    corpus = [doc["tokens"] for doc in tokenized_docs]
    bm25 = BM25Okapi(corpus)
    return bm25


def save_bm25_index(bm25, tokenized_docs, path="bm25_index.pkl"):
    """
    Save BM25 object + content + metadata (aligned by index)
    """
    payload = {
        "bm25": bm25,
        "documents": [
            {
                "content": doc["content"],
                "metadata": doc["metadata"]
            }
            for doc in tokenized_docs
        ]
    }

    with open(path, "wb") as f:
        pickle.dump(payload, f)


def load_bm25_index(path="bm25_index.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)
