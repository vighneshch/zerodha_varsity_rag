# Loading the required libraries
from langchain_qdrant import QdrantVectorStore
from app.config import config
from langchain_huggingface import HuggingFaceEmbeddings
from qdrant_client import QdrantClient


def test_retreiver():
    embeddings = HuggingFaceEmbeddings(model_name=config['model']['embedding_model'])
    client = QdrantClient(url=config['qdrant']['url'])

    vector_store = QdrantVectorStore(client=client,
                                     collection_name=config['qdrant']['collection_name'],
                                     embedding=embeddings
    )
    
    retreived_docs = vector_store.similarity_search(query="What is fundamental analysis?",k=3)

    for doc in retreived_docs:
        print("\n---")
        print(doc.page_content[:300])
    
    return

if __name__ == "__main__":
    test_retreiver()
    