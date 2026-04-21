# Loading the required librarbeis
from rag_app.retriever import get_retriever
from rag_app.generator import get_answer

def answer(query):
    retriever = get_retriever()
    docs = retriever.get_relevant_documents(query)
    answer = get_answer(docs,query)

    return answer