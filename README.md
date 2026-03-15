# Smart File Assistant – AI Document Q&A System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![AI](https://img.shields.io/badge/AI-RAG%20Pipeline-green)
![Vector Database](https://img.shields.io/badge/Vector%20Database-ChromaDB-orange)
![Embeddings](https://img.shields.io/badge/Embeddings-SentenceTransformers-red)

Developed as part of Internship / AI Project  
Author: **Nihal Rao**

---

# 📖 Project Overview

Smart File Assistant is an **AI-powered document analysis system** that allows users to upload PDF documents and ask questions about their content.

The system processes PDF files, extracts text, converts the content into **semantic embeddings**, and stores them in a **vector database**. When a user asks a question, the system retrieves the most relevant document sections and uses an **AI language model** to generate an accurate response.

This project demonstrates how **Retrieval-Augmented Generation (RAG)** can be used to build an intelligent document assistant capable of understanding natural language queries.

---

# 🎯 Objective

The goal of this project is to build a system that can:

- Extract and process text from documents
- Convert document content into semantic embeddings
- Store embeddings in a vector database for fast retrieval
- Perform semantic search on documents
- Generate AI-powered answers based on document content

This enables users to interact with documents using **natural language queries** instead of manually searching through files.

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
Vector Database (ChromaDB)
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
|-----------|--------|
| Python | Main programming language |
| Streamlit | Web interface |
| Sentence Transformers | Generate semantic embeddings |
| ChromaDB | Vector similarity search |
| OpenAI API | AI response generation |
| PyMuPDF | PDF text extraction |
| Visual Studio Code | Development environment |
| GitHub | Version control |

### Key Libraries Used

```
streamlit
sentence-transformers
chromadb
pymupdf
openai
numpy
```

---

# ✅ Milestone 1 – Document Processing

## Tasks Completed

- Extracted text from uploaded PDF documents
- Implemented text cleaning and preprocessing
- Removed unnecessary formatting and characters
- Structured extracted text for further processing

### Output

Clean document text ready for **chunking and embedding generation**.

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

Each text chunk is converted into **vector embeddings** using the model:

```
all-MiniLM-L6-v2
```

Embeddings represent the **semantic meaning of text**, allowing the system to match queries even if keywords differ.

Example:

User Query

```
device not starting
```

Matching document content

```
system fails to boot
```

Even though keywords differ, the **semantic meaning is similar**, allowing accurate retrieval.

---

# ✅ Milestone 3 – Semantic Search & RAG Pipeline

## Objective

Enable intelligent document search and automated answer generation using a **Retrieval-Augmented Generation (RAG) pipeline**.

---

## Step 1: Vector Database (ChromaDB)

Embeddings are stored in a **ChromaDB vector database** for efficient similarity search.

| Component | Description |
|----------|-------------|
| Embeddings | Vector representation of document chunks |
| Documents | Original text chunks |
| Metadata | Optional chunk identifiers |

---

## Step 2: Semantic Search

User queries are converted into embeddings and compared against stored document embeddings.

Example Query:

```
What are the benefits of agriculture?
```

The system retrieves document sections discussing:

- Economic importance of agriculture
- Employment generation
- Agricultural development

Even when **exact keywords are not present** in the document.

---

## Step 3: Retrieval-Augmented Generation (RAG)

The retrieved document chunks are passed to the language model as contextual information.

Pipeline:

```
User Query
     ↓
Query Embedding
     ↓
Semantic Search (ChromaDB)
     ↓
Retrieve Relevant Chunks
     ↓
Context Injection
     ↓
AI Answer Generation
```

---

## Example Interaction

User Query

```
What is the main topic of this document?
```

System Process

- Convert query into embedding
- Search ChromaDB vector database
- Retrieve most relevant chunks
- Provide context to the AI model
- Generate a response

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

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install streamlit
pip install sentence-transformers
pip install chromadb
pip install pymupdf
pip install openai
```

---

# ▶ Running the Project

Run the Streamlit application:

```bash
streamlit run app.py
```

The system will:

- Load the document processing modules
- Allow users to upload PDF documents
- Convert document text into embeddings
- Perform semantic search
- Generate AI-powered responses

---

# 📁 Project Structure

```
Smart_File_Assistant
│
├── app.py
│
├── modules
│   ├── extract.py
│   ├── cleaning.py
│   ├── chunk.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── openai_integration.py
│
├── sample.pdf
│
└── README.md
```

---

# 📊 Current Status

| Milestone | Status |
|-----------|--------|
| Milestone 1 – Document Processing | ✅ Completed |
| Milestone 2 – Chunking & Embeddings | ✅ Completed |
| Milestone 3 – Semantic Search & RAG Pipeline | ✅ Completed |
| Milestone 4 – Testing & Documentation | 🔜 Upcoming |

---

# 📌 Future Work

Planned improvements include:

- Support for **multiple document uploads**
- Document **summarization**
- **Improved UI features**
- Integration with enterprise knowledge bases
- Cloud deployment for public access

---

# ✅ Final Outcome

The Smart File Assistant functions as an **AI-powered document assistant** capable of:

- Processing PDF documents
- Understanding natural language queries
- Performing semantic search over document content
- Retrieving relevant information
- Generating intelligent AI responses

---

⭐ If you found this project useful, consider **starring the repository on GitHub!**
