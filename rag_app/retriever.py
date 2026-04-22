# Loading the required libraries
from app.config import config
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

def get_retriever():
    qdrant_url = config['qdrant']['url']
    qdrant_collection_name = config['qdrant']['collection_name']
    embeddings = HuggingFaceEmbeddings(model=config['model']['embedding_model'])

    client = QdrantClient(url=qdrant_url)

    vector_db  = QdrantVectorStore(client=client,
                                   collection_name=qdrant_collection_name,
                                   embedding=embeddings)
    retreiver = vector_db.as_retriever(search_type="mmr",search_kwargs={"k":5,"fetch_k":10})

    return retreiver