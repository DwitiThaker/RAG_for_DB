from typing import List, Dict
from keywordSearch.tokenizer import tokenize, tokenize_query


def bm25_search(
    query: str,
    bm25,
    documents: List[Dict],
    top_k: int = 5,
) -> List[Dict]:

    query_tokens = tokenize_query(query)
    print(f"query_tokens: {query_tokens}")

    if not query_tokens:
        return []

    scores = bm25.get_scores(query_tokens)

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )

    results = []

    for i in ranked_indices[:top_k]:
        if scores[i] <= 0:
            continue

        content = documents[i]["content"]
        metadata = documents[i]["metadata"]
        doc_tokens = tokenize(content)   


        matched_words = sorted(set(query_tokens) & set(doc_tokens))

        results.append({
            "matched_words": matched_words,
            
            "score": float(scores[i]),
            "content": content,
            "metadata": metadata,
        })

    return results
