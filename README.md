# 📚 End-to-End RAG System (LangChain + Qdrant + HuggingFace + Llama 3)

This project is a production-style Retrieval-Augmented Generation (RAG) system that allows querying PDF documents using semantic search and large language models. It implements a full pipeline from PDF ingestion to final answer generation.

The pipeline works as: PDF documents → chunking → embeddings → vector database → retrieval → LLM → final answer.

The system uses LangChain for orchestration, Qdrant as the vector database, HuggingFace embeddings for semantic representation, and Cerebras-hosted Llama 3 for generation.

## Project Structure

Project_1/
config/
config.yaml
ingestion/
run_ingestion.py
loader.py
rag_app/
pipeline.py
retriever.py
generator.py
vectorstore/
schema.py
tests/
test_retrieval.py
test_pipeline.py
data/
docs/
requirements.txt
README.md

## Setup Instructions

First create a virtual environment using python -m venv venv and activate it using venv\Scripts\activate on Windows. Then install dependencies using pip install -r requirements.txt.

Start the Qdrant vector database using Docker command: docker run -p 6333:6333 qdrant/qdrant.

## Configuration

All configuration is managed through config/config.yaml. It contains paths for data, embedding model details, Qdrant connection details, and chunking parameters.

Example configuration:

paths:
  data_dir: data/docs

model:
  embedding_model: sentence-transformers/all-MiniLM-L6-v2
  model_name: llama3.1-8b

qdrant:
  url: http://localhost:6333
  collection_name: rag_collection

chunking:
  chunk_length: 500
  chunk_overlap: 100

## Data Ingestion

Run ingestion using:

python -m ingestion.run_ingestion

This step loads PDF documents, splits them into chunks, generates embeddings using HuggingFace models, and stores them in Qdrant vector database.

## Retrieval Testing

Run retrieval test using:

python -m tests.test_retrieval

This verifies that the vector database is working correctly and returns relevant chunks based on semantic search queries.

## RAG Pipeline Usage

The RAG pipeline can be tested using:

from rag_app.pipeline import answer
print(answer("What is fundamental analysis?"))

The system retrieves relevant chunks from Qdrant and sends them along with the query to the LLM, which generates a final response.

## API Option

The system can optionally be exposed using FastAPI:

uvicorn app.main:app --reload

Then access using:
GET /query?q=your question

## Architecture Flow

PDF documents are processed and split into chunks, embeddings are generated using HuggingFace models, stored in Qdrant vector database, retrieved using semantic search, and passed into LLM (Llama 3 via Cerebras) to generate final answers.

## Common Issues

If Qdrant is not connecting, ensure it is running on http://localhost:6333. If retrieval returns empty results, check chunk size, embedding consistency, and ingestion logs. If import errors occur, upgrade dependencies using pip install -U langchain langchain-core langchain-qdrant.

## Future Improvements

Future enhancements include reranking models for better retrieval quality, async processing for speed, metadata filtering, evaluation frameworks like RAGAS, and Docker-based deployment.

## Tech Stack

Python, LangChain, Qdrant, HuggingFace Transformers, Cerebras API, and FastAPI.

## Author

This project is built as a production-ready RAG system for learning and scalable document question answering applications.