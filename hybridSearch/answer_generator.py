from hybridSearch.hybrid_prompt import build_final_prompt
from utils.timing import log_time
from hybridSearch.context_builder import build_rag_context


@log_time("LLM Answer Generation")
def generate_answer(llm, hybrid_results, question: str):
    """
    Generates final answer using hybrid results + RAG prompt
    """

    context = build_rag_context(hybrid_results)

    if not context.strip():
        return "The provided context does not contain enough information to answer this question."

    prompt = build_final_prompt(
        context=context,
        question=question,
    )

    response = llm.invoke(prompt)

    return response.content.strip()
