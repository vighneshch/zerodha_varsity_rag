# Loading the required libraries
from app.config import config
from langchain_qdrant import Qdrant
from langchain_huggingface import HuggingFaceEmbeddings
from qdrant_client import QdrantClient

def embed_and_store(chunks,embed_model):
    embeddings = HuggingFaceEmbeddings(model=embed_model)

    qdrantClient = QdrantClient(url = config['qdrant']['url'])
    vector_store = Qdrant(
        client= qdrantClient,
        embeddings=embeddings,
        collection_name = config['qdrant']['collection_name']
    )

    vector_store.add_documents(chunks)

    return vector_store