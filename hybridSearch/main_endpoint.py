from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from keywordSearch.bm25_index import load_bm25_index
from keywordSearch.searcher import bm25_search
from rag.qdrant_retriever import retrieve_chunks
from hybridSearch.merge_search import hybrid_rank_fusion
# from hybridSearch.answer_generator import generate_answer
from rag.ollama_embeddings import get_embedding_model
from hybridSearch.normalize import vector_results_adapter

app = FastAPI(
    title="Hybrid RAG API",
    version="1.0.0",
    description="Hybrid BM25 + Vector RAG system"
)

bm25_index = load_bm25_index()
bm25 = bm25_index["bm25"]
documents = bm25_index["documents"]

llm = get_embedding_model()

class QueryRequest(BaseModel):
    query: str
    top_k: Optional[int] = 10

class SourceChunk(BaseModel):
    mongo_id: Optional[str]
    page: Optional[int]
    chunk_index: Optional[int]
    source: List[str]

class QueryResponse(BaseModel):
    query:str
    answer: str
    sources: List[SourceChunk]


@app.post("/rag/query")
def rag_query(req: QueryRequest):
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Empty query")

    # 1️⃣ BM25
    bm25_results = bm25_search(
        query=req.query,
        bm25=bm25,
        documents=documents,
        top_k=req.top_k,
    )

    # 2️⃣ VECTOR (RAW)
    raw_vector_results = retrieve_chunks(
        query=req.query,
        top_k=req.top_k,
    )

    # 3️⃣ NORMALIZE (THIS WAS MISSING)
    vector_results = vector_results_adapter(raw_vector_results)

    # 4️⃣ HYBRID FUSION
    hybrid_results = hybrid_rank_fusion(
        bm25_results=bm25_results,
        vector_results=vector_results,
        top_k=req.top_k,
    )

    return {
        "query": req.query,
        "results": hybrid_results,
    }