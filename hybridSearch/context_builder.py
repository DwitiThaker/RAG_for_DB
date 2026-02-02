def build_rag_context(hybrid_results, max_chunks: int = 5):
    """
    Converts hybrid search results into a single context string
    """
    context_blocks = []

    for i, r in enumerate(hybrid_results[:max_chunks], 1):
        block = f"""
        [Passage {i}]
        Source: {", ".join(r["sources"])}
        Content:
        {r["content"]}
        """
        context_blocks.append(block.strip())

    return "\n\n".join(context_blocks)
