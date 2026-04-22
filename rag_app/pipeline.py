# Loading the required librarbeis
from rag_app.retriever import get_retriever
from rag_app.generator import get_answer
retriever = get_retriever()
def answer(query):
    
    docs = retriever.invoke(query)
    answer = get_answer(docs,query)

    return answer