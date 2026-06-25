# FoundrAI 
### Startup Compliance & Guidance Platform powered by RAG

FoundrAI is a RAG-based AI platform designed to help startup founders navigate the complex landscape of government schemes, compliance requirements, licenses, tax rules, and sector-specific regulations — all in one place.

---

##  What it does

Startup founders often struggle to find and understand government policies, incentives, and compliance requirements scattered across multiple sources. FoundrAI consolidates this information and lets you query it conversationally using semantic search backed by a vector database.

Ask questions like:
- *"How do I register GST in Maharashtra?"*
- *"What MSME schemes are available for tech startups?"*
- *"What are the labor law requirements for hiring in an IT company?"*

---

##  Architecture

```
User Query
    ↓
Streamlit UI (app.py)
    ↓
RAG Chain (rag_chain.py)
    ↓
Retriever (retriever.py) ←→ ChromaDB Vector Store (chroma_db/)
    ↓
Embeddings (embeddings.py) — using Sentence Transformers / HuggingFace
    ↓
Prompt Template (prompt_template.py)
    ↓
QWEN3 LLM via HuggingFace
    ↓
Answer + Sources → Streamlit UI
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| LLM | HuggingFace QWEN3 |
| Embeddings | Sentence Transformers |
| Vector DB | ChromaDB |
| RAG Framework | LangChain |
| Language | Python |

---

## 📁 Project Structure

```
FoundrAI/
├── app.py               # Streamlit UI — main entry point
├── rag_chain.py         # RAG pipeline logic
├── retriever.py         # ChromaDB retriever setup
├── embeddings.py        # Embedding model configuration
├── prompt_template.py   # Prompt templates for the LLM
├── config.py            # Configuration and environment variables
├── chroma_db/           # Persisted vector store
└── requirment.txt       # Python dependencies
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/SamyakDahale/FoundrAI.git
cd FoundrAI
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirment.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:
```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

### 5. Run the app
```bash
streamlit run app.py
```

---

##  Features

- **Conversational Search** — Ask compliance questions in plain language and get context-aware answers
- **Semantic Retrieval** — ChromaDB vector store enables accurate, meaning-based document retrieval
- **Chat History** — Maintains conversation context across multiple queries
- **Key Action Points** — Automatically extracts actionable steps from answers
- **Source Attribution** — Shows which documents the answer was derived from
- **Alerts Panel** — Displays latest updates on government schemes and regulatory changes

--
---

*Final Year Capstone Project — B.Tech Data Science, MGM University, Chh. Sambhajinagar*
