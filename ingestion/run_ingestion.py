# Loading the required libraries
from app.config import config
from ingestion.loader import load_documents
from ingestion.chunking import chunk_documents
from ingestion.embed_store import embed_and_store
from vectorstore.scehma import create_collection

def run():
    try:
        documents = load_documents(config['paths']['data_dir'])
        print("Documents are loaded successfully")

        chunks = chunk_documents(documents=documents,chunk_length=config['chunking']['chunk_length'],
                                 chunk_overlap = config['chunking']['chunk_overlap'])
        print("Chunking process completed")

        create_collection()

        vector_store = embed_and_store(chunks=chunks,embed_model=config['model']['embedding_model'])
        print("Embedding and storing completed")
    
    except Exception as e:
        print(f"Ingestion failed: {e}")

if __name__ == "__main__":
    run()