from keywordSearch.bm25_index import load_bm25_index
from keywordSearch.searcher import bm25_search
from rag.qdrant_retriever import retrieve_chunks
from hybridSearch.normalize import vector_results_adapter
from hybridSearch.merge_search import hybrid_rank_fusion


def main():
    print("✅ Hybrid Search Ready")

    index = load_bm25_index()
    bm25 = index["bm25"]
    documents = index["documents"]

    while True:
        query = input("\n👉 Enter query (or 'exit'): ")
        if query.lower() == "exit":
            break

        print("Starting....")
        # 1️⃣ BM25 search
        bm25_results = bm25_search(
            query=query,
            bm25=bm25,
            documents=documents,
            top_k=5,
        )

        
        # 2️⃣ Vector search
        raw_vector_results = retrieve_chunks(
            query=query,
            top_k=5,
        )
        raw_vector_results = retrieve_chunks(query=query, top_k=5)

        # print("\nDEBUG: RAW VECTOR RESULTS")
        # print("Count:", len(raw_vector_results))
        # for i, r in enumerate(raw_vector_results[:5], 1):
        #     print(i, r)

        vector_results = vector_results_adapter(raw_vector_results)

        # print("\nDEBUG: VECTOR RESULTS")
        # for i, r in enumerate(vector_results, 1):
        #     print(
        #         i,
        #         "mongo_id =", r["metadata"].get("mongo_id"),
        #         "| metadata =", r["metadata"]
        #     )


        # 3️⃣ Hybrid fusion
        hybrid_results = hybrid_rank_fusion(
            bm25_results=bm25_results,
            vector_results=vector_results,
            top_k=5,
        )

        # 4️⃣ Print results
        for i, r in enumerate(hybrid_results, 1):
            print("\n" + "-" * 50)
            print(f"Rank {i}")
            print(f"Hybrid score : {r['hybrid_score']:.4f}")
            print(f"Sources      : {', '.join(r['sources'])}")

            if r["matched_words"]:
                print(f"Matched words: {', '.join(r['matched_words'])}")

            print(f"Metadata     : {r['metadata']}")


if __name__ == "__main__":
    main()
