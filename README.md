# ScholarAI – AI Research Assistant

ScholarAI is an AI-powered research assistant built to help users understand and interact with academic or technical content more efficiently. It allows users to upload documents, ask questions, and receive context-aware answers generated using modern language models.

The project was initially developed during a hackathon and later extended to improve structure, usability, and overall performance.

---

## Overview

Working with long research papers or technical documents can be time-consuming. ScholarAI addresses this by combining document processing with retrieval-augmented generation (RAG), enabling users to extract relevant insights quickly without manually scanning entire documents.

---

## Key Features

- Upload and process PDF or text documents  
- Ask questions based on uploaded content  
- Generate concise summaries of complex material  
- Retrieve contextually relevant information using embeddings  
- Interactive chat interface for continuous queries  

---

## Tech Stack

**Frontend**
- React
- Tailwind CSS

**Backend**
- FastAPI
- Python

**AI / ML Components**
- Large Language Models (Mistral / OpenAI)
- Retrieval-Augmented Generation (RAG)
- FAISS for vector similarity search
- Text chunking and embedding pipelines

---

## System Workflow

1. A user uploads a document (PDF or text)
2. The backend processes the document and splits it into smaller chunks
3. Each chunk is converted into vector embeddings
4. Embeddings are stored and indexed using FAISS
5. When a query is made, relevant chunks are retrieved
6. The language model generates a response using this context

This approach ensures that responses are grounded in the actual document rather than being generic or hallucinated.

---

## Local Setup

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
