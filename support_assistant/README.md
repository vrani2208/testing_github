# Module 3 — Support Assistant

This module implements a Zepto policy support assistant using document retrieval, embeddings, ChromaDB, LangGraph, structured Pydantic output, and FastAPI.

The required implementation uses MOCK_LLM mode for deterministic offline execution.

## Pipeline Architecture

User Question
→ Intent Classification
→ Policy Document Retrieval
→ LangGraph Support Assistant
→ Structured Pydantic Response
→ FastAPI `/ask` Endpoint

Policy questions are answered using the Zepto policy corpus stored in the `docs/` folder.

General questions are handled directly without policy document retrieval.

## Example Call Transcripts

### Test 1 — Delivery Policy

Question:
What is the delivery fee?

Intent:
policy

Answer:
Standard delivery is free for orders above INR 149. Orders below INR 149 have a delivery fee of INR 25. Priority delivery is available for an additional INR 15.

Source:
Zepto policy documents

### Test 2 — Cancellation Policy

Question:
Can I cancel my order after it is packed?

Intent:
policy

Answer:
Orders cannot normally be cancelled after they have reached the Packed stage.

Source:
Zepto policy documents

### Test 3 — General Question

Question:
What is 10 + 20?

Intent:
general

Answer:
10 + 20 = 30

Source:
None

## API Testing

The FastAPI application was tested using the `/` and `/ask` endpoints.

The endpoint tests returned HTTP 200 successfully.

## Project Files

- `03_support_assistant.ipynb` — notebook implementation and tests
- `docs/` — 8 policy documents
- `rag.py` — RAG and support response logic
- `main.py` — FastAPI application
- `requirements.txt` — Python dependencies
- `Dockerfile` — container configuration
- `README.md` — module documentation
