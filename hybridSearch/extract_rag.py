def build_context_from_hybrid(hybrid_results):
    """
    Extracts document text from hybrid results
    for the RAG prompt.
    """
    return [r["content"] for r in hybrid_results]

# def build_context_from_hybrid(hybrid_results):
#     context_chunks = []

#     for i, r in enumerate(hybrid_results, 1):
#         chunk = (
#             f"[Document {i}]\n"
#             f"{r['content']}"
#         )
#         context_chunks.append(chunk)

#     return context_chunks
