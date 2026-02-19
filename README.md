# AI Memory System

## Overview

The AI Memory System is a conversational assistant capable of remembering user facts across interactions and using them to generate personalized responses.

The system extracts personal facts from user messages, stores them as vector embeddings, and retrieves relevant memories using semantic search before generating responses.

The application consists of:

- FastAPI Backend (REST API)
- ChromaDB Vector Database
- Sentence Transformers Embeddings
- LLM-based Fact Extraction and Response Generation
- Streamlit UI
- Docker File

---

# Architecture

User Interaction Flow:

Streamlit UI → FastAPI API → Fact Extraction → Memory Storage → Vector Search → Response Generation

## Retrieval First Architecture

<p align="center">

<img src="assets/image.png" width="700">

</p>

This system follows a retrieval-first strategy where user queries are first matched against stored semantic memories before falling back to an LLM.


### Components

1. Streamlit UI

Provides a simple conversational interface.

Responsible for:

- Sending messages to backend
- Displaying chatbot responses
- Viewing stored memories

---

2. FastAPI Backend

Handles all business logic.

Endpoints:

- POST /memories → store memory
- GET /memories → list memories
- GET /memories/search → semantic search + response
- DELETE /memories/{id} → delete memory

Responsibilities:

- Fact extraction
- Validation
- Memory retrieval
- LLM response generation

---

3. Memory Storage (ChromaDB)

Vector database used for semantic memory retrieval.

Stores:

- Fact text
- Embeddings
- Unique ID


# Install Required libraries
pip install -r requirements.txt

# HuggingFace Token
I have used free-tier  Hugging face Access Token for LLM, you need to create Hugging Face access tokens on https://huggingface.co/settings/tokens and then run the follwing command


huggingface-cli login

Paste your Token when prompted

Verify login command

huggingface-cli whoami

You should see your HuggingFace Username


## Start Server

uvicorn backend.api:app --reload


---

Store Memory

curl -X POST http://127.0.0.1:8000/memories \
-H "Content-Type: application/json" \
-d "{\"text\":\"My name is Priya\"}"


---

Search Memory

curl "http://127.0.0.1:8000/memories/search?q=name"


---

Get All Memories

curl http://127.0.0.1:8000/memories


---

Delete Memory

curl -X DELETE http://127.0.0.1:8000/memories/<memory_id>


# Start UI
In a new terminal


streamlit run streamlit_app.py


# Swagger UI for testing Endpoints

http://127.0.0.1:8000/docs


# Docker 

Build:

docker build -t ai-memory .

Run:

docker run -p 8000:8000 ai-memory
