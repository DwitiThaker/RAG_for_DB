def hybrid_rank_fusion(
    bm25_results,
    vector_results,
    bm25_weight=0.3,
    vector_weight=0.7,
    top_k=5,
):
    combined = {}

    bm25_len = max(len(bm25_results), 1)
    vector_len = max(len(vector_results), 1)

    # BM25
    for rank, r in enumerate(bm25_results):
        doc_id = r["metadata"].get("mongo_id")
        if not doc_id:
            continue

        combined.setdefault(doc_id, {
            "content": r["content"],
            "metadata": r["metadata"],
            "hybrid_score": 0.0,
            "sources": set(),
            "matched_words": [],
            "bm25_score": None,
            "vector_score": None,
        })

        score = bm25_weight * (1 - rank / bm25_len)
        combined[doc_id]["hybrid_score"] += score
        combined[doc_id]["sources"].add("bm25")
        combined[doc_id]["matched_words"] = r.get("matched_words", [])
        combined[doc_id]["bm25_score"] = r.get("score")

    # Vector
    for rank, r in enumerate(vector_results):
        doc_id = r["metadata"].get("mongo_id")
        if not doc_id:
            continue

        combined.setdefault(doc_id, {
            "content": r["content"],
            "metadata": r["metadata"],
            "hybrid_score": 0.0,
            "sources": set(),
            "matched_words": [],
            "bm25_score": None,
            "vector_score": None,
        })

        score = vector_weight * (1 - rank / vector_len)
        combined[doc_id]["hybrid_score"] += score
        combined[doc_id]["sources"].add("vector")
        combined[doc_id]["vector_score"] = r.get("vector_score")

    ranked = sorted(
        combined.values(),
        key=lambda x: x["hybrid_score"],
        reverse=True
    )

    for r in ranked:
        r["sources"] = list(r["sources"])

    return ranked[:top_k]
