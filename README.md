# 📄 Smart File Assistant – AI Document Q&A System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![AI](https://img.shields.io/badge/AI-RAG%20Pipeline-green)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)

Developed as part of Internship / AI Project  
Author: **Nihaal Rao**

---

# 📖 Project Overview

Smart File Assistant is an AI-powered document analysis system that allows users to upload PDF documents and ask questions about their content.

The system processes PDF files, extracts text, organizes the content into structured chunks, and retrieves the most relevant sections based on user queries. These sections are then used by an AI model to generate accurate and context-based responses.

The system ensures that answers are strictly based on the uploaded document. If a question is unrelated, it informs the user instead of generating incorrect information.

This project demonstrates how a Retrieval-Augmented Generation (RAG) system can be implemented in a simple and effective way.

---

# 🎯 Objective

The goal of this project is to build a system that can:

- Extract and process text from documents  
- Organize document content into smaller chunks  
- Retrieve relevant information based on user queries  
- Generate AI-powered answers using document context  
- Restrict responses to only document-related queries  

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
Chunk Storage
      ↓
User Query
      ↓
Relevant Chunk Retrieval
      ↓
Relevance Check
      ↓
AI Answer Generation
```

---

# 🚀 Technologies Used

| Technology | Purpose |
|----------|--------|
| Python | Main programming language |
| Streamlit | Web interface |
| OpenAI API | AI response generation |
| PyMuPDF | PDF text extraction |
| NumPy | Data handling |
| Visual Studio Code | Development environment |
| GitHub | Version control |

---

# 📦 Key Libraries Used

- streamlit  
- pymupdf  
- openai  
- numpy  

---

# ✅ Milestone 1 – Document Processing

### Tasks Completed
- Extracted text from uploaded PDF documents  
- Implemented text cleaning and preprocessing  
- Removed unnecessary formatting and characters  
- Structured extracted text for further processing  

### Output
Clean and structured document text ready for chunking.

---

# ✅ Milestone 2 – Text Chunking & Retrieval Setup

### Step 1: Text Chunking  
Large document text is divided into smaller chunks to improve retrieval efficiency.

Example:

```
Document
   → Chunk 1
   → Chunk 2
   → Chunk 3
```

Chunking allows the system to focus only on relevant portions instead of processing the entire document.

---

### Step 2: Retrieval Setup  
- Stored processed chunks for later use  
- Implemented logic to retrieve relevant chunks based on user queries  
- Selected top matching chunks to form context for answering  

---

# ✅ Milestone 3 – Semantic Search & RAG Pipeline

### Objective  
Enable intelligent document search and answer generation using a Retrieval-Augmented Generation (RAG) approach.

---

### Step 1: Chunk Retrieval  
User queries are compared with stored chunks to identify the most relevant sections.

Example Query:

```
What is the importance of agriculture?
```

The system retrieves chunks discussing:
- agricultural benefits  
- economic contribution  
- development aspects  

---

### Step 2: Relevance Check  

Before generating an answer, the system verifies whether the question is related to the document.

If unrelated:

```
The question you asked is not related to the uploaded PDF.
```

---

### Step 3: Retrieval-Augmented Generation (RAG)

The retrieved chunks are passed as context to the AI model.

Pipeline:

```
User Query
     ↓
Retrieve Relevant Chunks
     ↓
Context Preparation
     ↓
Relevance Validation
     ↓
AI Answer Generation
```

---

### Example Interaction

User Query:

```
What is the main topic of this document?
```

System Process:
- Retrieve relevant chunks  
- Validate relevance  
- Generate response using context  

Generated Response:
Answer is produced strictly based on document content.

---

# ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```
git clone https://github.com/yourusername/Smart_File_Assistant.git
cd Smart_File_Assistant
```

---

### 2️⃣ Create Virtual Environment
```
python -m venv venv
```

Activate environment:

Windows
```
venv\Scripts\activate
```

Mac/Linux
```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies
```
pip install streamlit
pip install pymupdf
pip install openai
pip install numpy
```

---

# ▶ Running the Project

Run the Streamlit application:

```
streamlit run app.py
```

The system will:
- Allow users to upload PDF documents  
- Process and chunk document text  
- Retrieve relevant information  
- Generate AI-based answers  
- Restrict unrelated queries  

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
|----------|--------|
| Milestone 1 – Document Processing | ✅ Completed |
| Milestone 2 – Chunking & Retrieval | ✅ Completed |
| Milestone 3 – RAG Pipeline | ✅ Completed |
| Milestone 4 – Testing & Documentation | 🔜 Upcoming |

---

# 📌 Future Work

Planned improvements include:

- Support for multiple document uploads  
- Chat history functionality  
- Improved retrieval accuracy  
- Enhanced UI design  
- Deployment for public access  

---

# ✅ Final Outcome

The Smart File Assistant functions as an AI-powered document assistant capable of:

- Processing PDF documents  
- Understanding user queries  
- Retrieving relevant document content  
- Generating accurate AI-based responses  
- Preventing unrelated or incorrect answers  

---

⭐ If you found this project useful, consider giving it a star on GitHub!
