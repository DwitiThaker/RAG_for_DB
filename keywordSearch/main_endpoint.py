from fastapi import FastAPI
from pydantic import BaseModel
from keywordSearch.keyword_qa import answer_question

app = FastAPI()

class AskInKeyword(BaseModel):
    question: str
    top_k: int = 5

@app.post("/askInKeyword")
def ask(req: AskInKeyword):
    result = answer_question(
        question=req.question,
        top_k=req.top_k
    )

    return {
        "answer": result["answer"],  
    }