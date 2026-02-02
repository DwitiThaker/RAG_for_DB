from keywordSearch.bm25_index import load_bm25_index
from keywordSearch.searcher import bm25_search


def build_context_from_bm25(results):
    return [r["content"] for r in results]


if __name__ == "__main__":
    print("Keyword searching...")

    index = load_bm25_index()
    bm25 = index["bm25"]
    documents = index["documents"]


    while True:
        query = input("\nEnter query (or 'exit'): ")
        if query.lower() == "exit":
            break

        results = bm25_search(
            query=query,
            bm25=bm25,
            documents=documents,
            top_k=5,
        )

        
        for i, r in enumerate(results, 1):
            print("\n" + "-" * 50)
            print(f"Rank {i}")
            print("-" * 50)

            print(f"Score        : {r['score']:.4f}")
            print(f"Matched words: {', '.join(r['matched_words'])}")
            print(f"Metadata     : {r['metadata']}")

        
