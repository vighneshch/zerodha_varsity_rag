# Loading the required libraries
from fastapi import FastAPI,Query
from rag_app.pipeline import answer

app =  FastAPI(
    title = "Zerodha Varsity RAG",
    description="PDF based RAG on Zerodha Varsity Documents",
    version = "1.0.0"
)

@app.get("/")
def home():
    return {"message":"RAG API is running"}

@app.get("/query")
def query(q:str = Query(...,description="Ask your question")):
    try:
        result = answer(q)
        return {
            "query":q,
            "answer":result["answer"],
            "sources":result["sources"]
        }
    except Exception as e:
        return {
            "query":q,
            "error":str(e)
        }
    