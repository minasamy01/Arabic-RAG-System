import os
import re
import pickle
import numpy as np
import faiss
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# ==============================
# Load API Key
# ==============================
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ==============================
# Load Embedding Model
# ==============================
print("Loading embedding model...")
embed_model = SentenceTransformer('BAAI/bge-m3')

# ==============================
# Clean & Chunking
# ==============================
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def chunk_text(text, chunk_size=500, overlap=120):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# ==============================
# Build Index in RAM (No Saving)
# ==============================
print("Processing documents and building index in RAM...")

# قراءة الملف الأصلي
with open("arabic.txt", "r", encoding="utf-8") as f:
    text = f.read()

text = clean_text(text)
chunks = chunk_text(text)

# تحويل النصوص لـ Embeddings
embeddings = embed_model.encode(
    chunks,
    normalize_embeddings=True,
    show_progress_bar=True
)
embeddings = np.array(embeddings).astype("float32")

# إنشاء الـ Index في الذاكرة فقط
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(embeddings)

print("Index Ready in RAM ✅")

# ==============================
# Retrieval Function
# ==============================
def retrieve(query, k=3):
    q_embedding = embed_model.encode([query], normalize_embeddings=True)
    q_embedding = np.array(q_embedding).astype("float32")
    scores, indices = index.search(q_embedding, k)
    return [chunks[i] for i in indices[0]]

# ==============================
# Ask Gemini
# ==============================
def ask(question):
    context = retrieve(question)
    prompt = f"""
    انت مساعد ذكي. جاوب باستخدام المعلومات فقط من السياق التالي:

    السياق:
    {' '.join(context)}

    السؤال:
    {question}

    الإجابة بالعربي:
    """
    # تنبيه: اتأكد من اسم الموديل، الموديل الحالي هو gemini-1.5-flash أو gemini-pro
    model = genai.GenerativeModel("gemini-2.5-flash") 
    response = model.generate_content(prompt)
    return response.text

# ==============================
# Chat Loop
# ==============================
print("\nRAG System Ready ✅ (اكتب exit للخروج)\n")
while True:
    q = input("سؤالك: ")
    if q.lower() == "exit":
        break
    answer = ask(q)
    print("\nالإجابة:\n", answer)