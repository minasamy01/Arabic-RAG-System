# 🛸 Semantic-RAG: Advanced Arabic Document QA
### *Bridging Semantic Search & Generative AI for Arabic Context*

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-2.0_Flash-orange.svg?style=for-the-badge&logo=googlegemini&logoColor=white)](https://ai.google.dev/)
[![FAISS](https://img.shields.io/badge/Vector_DB-FAISS-green.svg?style=for-the-badge&logo=meta&logoColor=white)](https://github.com/facebookresearch/faiss)
[![Sentence_Transformers](https://img.shields.io/badge/Embeddings-BGE_M3-red.svg?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/BAAI/bge-m3)

---

## 📖 Overview
**Semantic-RAG** is a high-performance **Retrieval-Augmented Generation** engine specifically engineered for Arabic and English semantic understanding. By bridging the gap between local knowledge bases and Large Language Models, this system ensures that AI responses are **fact-based**, **context-aware**, and **hallucination-free**.

## 🏗️ System Architecture
The system follows a professional RAG pipeline to ensure precision:
1. **Document Ingestion**: Extracting text from `arabic.txt` and `english.txt`.
2. **Smart Chunking**: Splitting text into 120-character overlapping chunks to preserve semantic context.
3. **Vectorization**: Creating dense embeddings using the **BGE-M3** multilingual model.
4. **Semantic Search**: Using **FAISS** for lightning-fast similarity retrieval.
5. **Grounded Generation**: Injecting context into **Gemini 2.0 Flash** with strict instructions to prevent hallucinations.

## ✨ Core Highlights
* **🌍 Multilingual Mastery:** Native support for Arabic and English using `BAAI/bge-m3`.
* **⚡ Lightning Retrieval:** In-memory vector search powered by **FAISS**, optimized for sub-millisecond matching.
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

## 📁 Project Structure
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
git clone [https://github.com/minasamy01/Arabic-RAG-System.git](https://github.com/minasamy01/Arabic-RAG-System.git)
cd Arabic-RAG-System
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

## 🔮 Future Roadmap

* [ ] **Streamlit UI**: Developing a web-based chat interface.
* [ ] **PDF Ingestion**: Adding support for reading complex PDF documents.
* [ ] **Hybrid Search**: Combining Keyword (BM25) with Vector search for better accuracy.

---

## 👨‍💻 Author

# **Mina Samy**
### *AI & NLP Engineer*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mina-data-ai/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BaJL%2F1WTcT2eyQjurm1ZczQ%3D%3D) 
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/minasamy01)

---
