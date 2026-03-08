Smart File Assistant – AI Document Q&A System

Developed as part of Internship / AI Project Author: Nihal Rao

📖 Project Overview

Smart File Assistant is an AI-powered document analysis system that allows users to ask questions about PDF documents and receive intelligent answers.

The system processes PDF files, extracts text, converts the content into semantic embeddings, and stores them in a vector database. When a user asks a question, the system retrieves the most relevant document sections and uses a language model to generate an accurate response.

This project demonstrates how Retrieval-Augmented Generation (RAG) can be applied to build an intelligent document assistant.

🎯 Objective

The goal of this project is to build a system that can:

• Extract and process text from documents • Convert document content into semantic embeddings • Store embeddings in a vector database for fast retrieval • Perform semantic search on documents • Generate AI-powered answers based on document content

This enables users to interact with documents using natural language queries.

🏗 Project Architecture

PDF Document ↓ Text Extraction ↓ Text Cleaning ↓ Text Chunking ↓ Embedding Generation (Sentence Transformers) ↓ Vector Database (FAISS) ↓ Semantic Search ↓ Context Retrieval ↓ Retrieval-Augmented Generation (RAG) ↓ AI Generated Answer

🚀 Technologies Used

Python Pandas / Text Processing Sentence Transformers FAISS (Vector Database) OpenAI API / LLM PyPDF / PyMuPDF NumPy Visual Studio Code GitHub

Key libraries used:

• sentence-transformers • FAISS

✅ Milestone 1 – Document Processing

Tasks Completed

• Extracted text from PDF documents • Implemented text cleaning and preprocessing • Removed unwanted characters and formatting • Structured the extracted text for further processing

Output

Clean document text ready for chunking and embedding.

✅ Milestone 2 – Chunking & Embedding Generation

Step 1: Text Chunking

Large documents were divided into smaller chunks to improve retrieval accuracy.

Example:

Document Text → Chunk 1 → Chunk 2 → Chunk 3

This allows the system to search specific sections of a document rather than the entire file.

Step 2: Embedding Generation

Text chunks were converted into vector embeddings using the model:

all-MiniLM-L6-v2

Embeddings represent semantic meaning, enabling the system to find similar content even if exact keywords are not present.

Example

User Query: "device is not starting"

Matching document content:

"system fails to boot"

✅ Milestone 3 – Semantic Search & RAG Pipeline

Objective

Enable intelligent document search and answer generation using a Retrieval-Augmented Generation pipeline.

Step 1: Vector Database

Embeddings were stored using FAISS for efficient similarity search.

Generated Files

vector_index.faiss chunks.pkl

Purpose

File | Description vector_index.faiss | Stores vector embeddings chunks.pkl | Stores document text chunks

Step 2: Semantic Search

User queries are converted into embeddings and compared against the FAISS index.

Example Query

"How do I troubleshoot system startup issues?"

The system retrieves document sections discussing:

• boot failures • system errors • startup troubleshooting

even if exact keywords do not match.

Step 3: Retrieval-Augmented Generation (RAG)

Retrieved document chunks are passed to the language model as context.

Pipeline

User Query ↓ Query Embedding ↓ Semantic Search (FAISS) ↓ Retrieve Relevant Chunks ↓ Context Injection ↓ LLM Answer Generation

Example Interaction

User Query

"What is the main topic of the document?"

System Process

Convert query into embedding

Search FAISS index

Retrieve relevant document chunks

Provide context to the LLM

Generated Response

The system produces a summarized answer based on the relevant document content.

⚙️ Installation & Setup

Clone the Repository

git clone cd SmartFileAssistant

Create Virtual Environment

python -m venv venv

Activate Environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

Install Dependencies

pip install faiss-cpu pip install sentence-transformers pip install openai pip install python-dotenv pip install pypdf pip install numpy

📁 Project Structure

SmartFileAssistant

SmartFileAssistant │ ├── main.py │ ├── extract.py ├── cleaning.py ├── chunk.py ├── embeddings.py ├── vector_store.py ├── retriever.py ├── openai_integration.py │ ├── faiss_index.index ├── chunks.pkl │ ├── sample.pdf │ └── README.md

📊 Current Status

Milestone 1 – Document Processing ✅ Completed Milestone 2 – Chunking & Embeddings ✅ Completed Milestone 3 – Semantic Search & RAG Pipeline ✅ Completed Milestone 4 – User Interface / Deployment 🔜 Upcoming

📌 Future Work

Planned improvements for the project:

• Web interface for document interaction • Support for multiple documents • Advanced document summarization • Integration with enterprise document systems • Real-time document indexing

Final Outcome

The Smart File Assistant now functions as an AI-powered document question-answering system capable of:

• Processing PDF documents • Understanding natural language queries • Performing semantic search over document content • Retrieving relevant information • Generating intelligent responses using an AI model