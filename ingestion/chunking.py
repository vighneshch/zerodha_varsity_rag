# Loading the required libraries
from app.config import config
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents,chunk_length,chunk_overlap):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_length,
        chunk_overlap = chunk_overlap
    )

    return splitter.split_documents(documents)

