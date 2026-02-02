from langchain_core.documents import Document
import re

STOP_WORDS = {
    "the", "is", "a", "an", "of", "to", "in", "on", "for", "with",
    "and", "or", "by", "this", "that", "how", "does", "do", "did",
    "are", "was", "were", "be", "been", "being", "it", "as", "at",
    "which", "what", "who", "when", "where", "why",
    "includes", "include", "gives", "give", "provides", "provide",
}


def tokenize(text: str):
    tokens = re.findall(r"\w+", text.lower())
    return [t for t in tokens if t not in STOP_WORDS]


def tokenize_documents(documents: list[Document]):
    try:

        tokenized_docs = []

        for doc in documents:
            tokens = tokenize(doc.page_content)
            tokenized_docs.append({
            "tokens": tokenize(doc.page_content),
            "content": doc.page_content,
            "metadata": doc.metadata
            })
    
    except Exception as e:
        print(f"Exception --------> {e}")
    
    return tokenized_docs


def tokenize_query(query: str):
    return tokenize(query)

