from fastapi import FastAPI
from pydantic import BaseModel
from rag.qa_service import answer_question

app = FastAPI()


class AskRequest(BaseModel):
    question: str
    top_k: int = 5


@app.post("/ask")
def ask(req: AskRequest):
    result = answer_question(
        question=req.question,
        top_k=req.top_k
    )

    return {
        "answer": result["answer"],
        "time_taken_seconds": result["time_taken_seconds"],
        # "retrieved_chunks": [
        #     {
        #         "score": c["score"],
        #         "text": c["text"][:1500],
        #         "metadata": c["metadata"],
        #     }
        #     for c in result["chunks"]
        # ]
    }
