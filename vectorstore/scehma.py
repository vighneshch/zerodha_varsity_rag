# Loading the required libraries
from app.config import config
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams,Distance

def create_collection():
    client = QdrantClient(url=config['qdrant']['url'])

    collection_name = config['qdrant']['collection_name']
    
    existing_collections = client.get_collections().collections

    existing_collection_names = []
    for collection in existing_collections:
        existing_collection_names.append(collection)
    
    if collection_name in existing_collections:
        print(f"Collection with {collection_name} already exists. Proceeding to use the same")
        return

    client.create_collection(collection_name = collection_name,
                             vectors_config = VectorParams(size = config['vectorstore']['embedding_model_dimension'],
                                                           distance=Distance.COSINE)
                                                           )
    print(f"Collection: {collection_name} has beed created")