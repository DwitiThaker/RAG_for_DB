def vector_results_adapter(qdrant_results):
    print("Normalizing..")
    return [
        {
            "content": r["text"], #r["payload"], ,
            "metadata": {
                "mongo_id": r.get("mongo_id"),
                "page": r.get("page"),
                "chunk_index": r.get("chunk_index"),
            },
            # "vector_score": r["score"],
        }
        for r in qdrant_results
    ]
