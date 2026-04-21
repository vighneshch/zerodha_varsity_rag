# Loading the required libraries
import os
from langchain_community.document_loaders import PyPDFLoader
from app.config import config

def load_documents(folder):
    docs = []

    # Looping through the files in the given folder
    for file in os.listdir(folder):
        if file.endswith('.pdf'):
            loader = PyPDFLoader(os.path.join(folder,file))
            pdf_docs = loader.load()

            for document in pdf_docs:
                document.metadata["source"] = file
            
            docs.extend(pdf_docs)
        
    return docs