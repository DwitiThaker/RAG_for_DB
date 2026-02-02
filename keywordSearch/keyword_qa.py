# import time
# from utils.timing import log_time
# from rag.qdrant_retriever import retrieve_chunks
# from rag.prompt_builder import build_prompt
# from rag.gemini_llm import get_openai_llm



# @log_time("keyword_qa")
# def answer_question(question: str, top_k: int = 5):
#     chunks = retrieve_chunks(question, top_k=top_k)
#     context_chunks = [c["text"] for c in chunks]

#     prompt = build_prompt(
#         context_chunks=context_chunks,
#         question=question
#     )

#     llm = get_openai_llm()
#     response = llm.invoke(prompt)

#     return {
#         "answer": response.content
#     }