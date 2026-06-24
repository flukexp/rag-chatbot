# Chatbot Financial Q&A with Grounded RAG

A question-answering chatbot that answers financial questions about U.S. public companies using **structured SQL data** and **10-K filing text** from a vector store. Every answer is grounded in the provided data — the assistant never hallucinates.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 16, assistant-ui, shadcn/ui, Tailwind CSS 4, Zustand |
| **Backend** | FastAPI, LangChain, LangGraph, OpenAI GPT-4o |
| **SQL Database** | PostgreSQL 16 (192 rows, ~48 companies, 2022–2025) |
| **Vector Database** | Pinecone (FY2025 10-K filings: Alphabet, Amazon, Apple, Meta) |
| **Auth** | JWT (pyjwt) + Argon2 |
| **Local Infra** | Docker Compose (Postgres + pinecone-local) |


## Getting Started

### 1. Prerequisites

- Docker & Docker Compose
- Python 3.11+
- Node.js 22+

### 2. Environment

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

Required values: `OPENAI_API_KEY`, `SECRET_KEY`, DB credentials, Pinecone credentials.

> Local Pinecone runs at `localhost:5080` by default. The `pinecone-local` image is pulled from `ghcr.io/pinecone-io/pinecone-local:latest`.

### 3. Launch the full stack

```bash
docker compose up -d
```

This starts:
- **PostgreSQL** — port 5432 (with auto-seeded financial data)
- **Pinecone** — port 5080–5081
- **Ingestion job** — loads SQL data + upserts vector embeddings (runs once, then exits)
- **Backend API** — port 8000 (FastAPI)
- **Frontend** — port 3000 (Next.js)

### 4. Open the app

Navigate to [http://localhost:3000](http://localhost:3000), register an account, and start chatting.

## Services

| Service | Port | Description |
|---------|------|-------------|
| `frontend` | 3000 | Next.js UI |
| `backend` | 8000 | FastAPI REST API |
| `db` | 5432 | PostgreSQL 16 |
| `pinecone` | 5080–5081 | Local Pinecone vector DB |
| `ingestion` | — | One-shot data loader |
