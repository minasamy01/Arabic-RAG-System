# 🛸 Semantic-RAG: Advanced Arabic Document QA
### *Bridging Semantic Search & Generative AI for Arabic Context*

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-2.0_Flash-orange.svg?style=for-the-badge&logo=googlegemini&logoColor=white)](https://ai.google.dev/)
[![FAISS](https://img.shields.io/badge/Vector_DB-FAISS-green.svg?style=for-the-badge&logo=meta&logoColor=white)](https://github.com/facebookresearch/faiss)
[![Sentence_Transformers](https://img.shields.io/badge/Embeddings-BGE_M3-red.svg?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/BAAI/bge-m3)

---

## 📖 Overview
**Semantic-RAG** is a high-performance **Retrieval-Augmented Generation** engine specifically engineered for Arabic and English semantic understanding. By bridging the gap between local knowledge bases and Large Language Models, this system ensures that AI responses are **fact-based**, **context-aware**, and **hallucination-free**.

## ✨ Core Highlights
* **🌍 Multilingual Mastery:** Native support for Arabic and English using `BAAI/bge-m3`.
* **⚡ Lightning Retrieval:** In-memory vector search powered by **FAISS**, optimized for sub-millisecond similarity matching.
* **🧠 Deep Contextualization:** 120-character overlapping chunks ensure semantic continuity.
* **🛡️ Reliability:** Strict grounding instructions force the LLM to answer *only* from your provided text.

---

## 🛠️ Technical Stack
| Component | Technology | Role |
| :--- | :--- | :--- |
| **Language** | `Python 3.x` | Core Logic |
| **LLM** | `Google Gemini 2.0 Flash` | Generative Intelligence |
| **Embeddings** | `BGE-M3 (FlagEmbedding)` | Multi-stage Semantic Encoding |
| **Vector DB** | `FAISS (FlatIP)` | Similarity Search Engine |

---

## 📁 Project Architecture
```bash
.
├── 📂 venv/              # Isolated environment
├── 📄 .env               # API Configuration (Sensitive)
├── 📝 arabic.txt         # Arabic Knowledge Base
├── 📝 english.txt        # English Knowledge Base
├── 🐍 rag.py             # Main Pipeline Engine
└── 📦 requirements.txt   # Dependency Manifest

```

---

## 🚀 Setup & Deployment

### 1️⃣ Installation

```bash
git clone [https://github.com/minasamy01/session-5.git](https://github.com/minasamy01/session-5.git)
cd session-5
pip install -r requirements.txt

```

### 2️⃣ Configuration

Create a `.env` file and insert your credentials:

```env
GEMINI_API_KEY=your_gemini_api_key_here

```

### 3️⃣ Launch

```bash
python rag.py

```

---

## 👨‍💻 Author

**Mina Samy** *AI & NLP Developer*

---
