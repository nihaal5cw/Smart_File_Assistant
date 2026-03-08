# Smart File Assistant – AI Document Q&A System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![AI](https://img.shields.io/badge/AI-RAG%20Pipeline-green)
![VectorDB](https://img.shields.io/badge/Vector%20Database-FAISS-orange)
![Embeddings](https://img.shields.io/badge/Embeddings-SentenceTransformers-red)

Developed as part of Internship / AI Project  
Author: **Nihal Rao**

---

# 📖 Project Overview

Smart File Assistant is an AI-powered document analysis system that allows users to ask questions about PDF documents and receive intelligent answers.

The system processes PDF files, extracts text, converts the content into semantic embeddings, and stores them in a vector database. When a user asks a question, the system retrieves the most relevant document sections and uses an AI model to generate an accurate response.

This project demonstrates how **Retrieval-Augmented Generation (RAG)** can be used to build an intelligent document assistant.

---

# 🎯 Objective

The goal of this project is to build a system that can:

- Extract and process text from documents
- Convert document content into semantic embeddings
- Store embeddings in a vector database for fast retrieval
- Perform semantic search on documents
- Generate AI-powered answers based on document content

This enables users to interact with documents using **natural language queries**.

---

# 🏗 Project Architecture

```
PDF Document
      ↓
Text Extraction
      ↓
Text Cleaning
      ↓
Text Chunking
      ↓
Embedding Generation (Sentence Transformers)
      ↓
Vector Database (FAISS)
      ↓
Semantic Search
      ↓
Context Retrieval
      ↓
Retrieval-Augmented Generation (RAG)
      ↓
AI Generated Answer
```

---

# 🚀 Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python | Main programming language |
| Sentence Transformers | Generate semantic embeddings |
| FAISS | Vector similarity search |
| OpenAI API | LLM response generation |
| PyPDF | PDF text extraction |
| NumPy | Numerical operations |
| Visual Studio Code | Development environment |
| GitHub | Version control |

Key libraries used:

- sentence-transformers  
- faiss-cpu  
- numpy  
- pypdf  
- openai  

---

# ✅ Milestone 1 – Document Processing

## Tasks Completed

- Extracted text from PDF documents
- Implemented text cleaning and preprocessing
- Removed unnecessary formatting and characters
- Structured extracted text for further processing

## Output

Clean document text ready for chunking and embedding.

---

# ✅ Milestone 2 – Text Chunking & Embedding Generation

## Step 1: Text Chunking

Large document text is divided into smaller chunks to improve retrieval accuracy.

Example:

```
Document
   → Chunk 1
   → Chunk 2
   → Chunk 3
```

Chunking ensures the system retrieves **specific relevant sections instead of the entire document**.

---

## Step 2: Embedding Generation

Each text chunk is converted into vector embeddings using the model:

```
all-MiniLM-L6-v2
```

Embeddings represent the **semantic meaning of text**, allowing the system to match queries even if exact keywords differ.

Example:

User Query

```
device not starting
```

Matching document content

```
system fails to boot
```

---

# ✅ Milestone 3 – Semantic Search & RAG Pipeline

## Objective

Enable intelligent document search and automated answer generation using a **Retrieval-Augmented Generation (RAG) pipeline**.

---

## Step 1: Vector Database (FAISS)

Embeddings are stored in a FAISS vector database for efficient similarity search.

Generated files:

```
faiss_index.index
chunks.pkl
```

| File | Description |
|-----|-------------|
| faiss_index.index | Stores vector embeddings |
| chunks.pkl | Stores document text chunks |

---

## Step 2: Semantic Search

User queries are converted into embeddings and compared against the FAISS index.

Example Query:

```
How can I fix system startup issues?
```

The system retrieves document sections discussing:

- boot failures
- troubleshooting steps
- startup errors

Even when **exact keywords are not present**.

---

## Step 3: Retrieval-Augmented Generation (RAG)

The retrieved document chunks are passed to the language model as contextual information.

Pipeline:

```
User Query
     ↓
Query Embedding
     ↓
Semantic Search (FAISS)
     ↓
Retrieve Relevant Chunks
     ↓
Context Injection
     ↓
LLM Answer Generation
```

---

## Example Interaction

User Query

```
What is the main topic of this document?
```

System Process

1. Convert query into embedding  
2. Search FAISS vector database  
3. Retrieve most relevant chunks  
4. Provide context to the AI model  
5. Generate a response  

Generated Response

The system produces an answer based on the **retrieved document content**.

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Smart_File_Assistant.git
cd Smart_File_Assistant
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install faiss-cpu
pip install sentence-transformers
pip install numpy
pip install pypdf
pip install openai
```

---

# ▶ Running the Project

Run the main program:

```bash
python main.py
```

The system will:

1. Load the FAISS vector index  
2. Accept user queries  
3. Retrieve relevant document sections  
4. Generate AI-powered responses  

---

# 📁 Project Structure

```
Smart_File_Assistant
│
├── main.py
│
├── extract.py
├── cleaning.py
├── chunk.py
├── embeddings.py
├── vector_store.py
├── retriever.py
├── openai_integration.py
│
├── faiss_index.index
├── chunks.pkl
│
├── sample.pdf
│
└── README.md
```

---

# 📊 Current Status

| Milestone | Status |
|----------|--------|
| Milestone 1 – Document Processing | ✅ Completed |
| Milestone 2 – Chunking & Embeddings | ✅ Completed |
| Milestone 3 – Semantic Search & RAG Pipeline | ✅ Completed |
| Milestone 4 – Web Interface / Deployment | 🔜 Upcoming |

---

# 📌 Future Work

Planned improvements:

- Web-based document assistant interface
- Support for multiple documents
- Advanced document summarization
- Integration with enterprise document systems
- Real-time document indexing

---

# ✅ Final Outcome

The Smart File Assistant functions as an **AI-powered document assistant** capable of:

- Processing PDF documents
- Understanding natural language queries
- Performing semantic search over document content
- Retrieving relevant information
- Generating intelligent AI responses

---

⭐ If you found this project useful, consider giving it a star on GitHub!
