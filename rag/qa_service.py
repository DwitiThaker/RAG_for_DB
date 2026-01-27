import time
from rag.qdrant_retriever import retrieve_chunks
from rag.prompt_builder import build_prompt
from rag.gemini_llm import get_openai_llm
from utils.timing import log_time


@log_time("qa_service")
def answer_question(question: str, top_k: int = 5):
    
    
    chunks = retrieve_chunks(question, top_k=top_k)
    context_chunks = [c["text"] for c in chunks]

    prompt = build_prompt(
        context_chunks=context_chunks,
        question=question,
    )
    
    llm = get_openai_llm()
    start_time = time.time()
    response = llm.invoke(prompt)

    end_time = time.time()

    return {
        "answer": response.content,
        "time_taken_seconds": round(end_time - start_time, 2),

        
        # "chunks": chunks
    }
