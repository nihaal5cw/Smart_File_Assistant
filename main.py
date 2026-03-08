import os

from extract import extract_text_from_pdf
from cleaning import clean_text
from chunk import chunk_text
from embeddings import embed_text
from retriever import retrieve
from openai_integration import ask_llm

from vector_store import (
    create_faiss_index,
    save_index,
    load_index,
    save_chunks,
    load_chunks
)


def build_index(pdf_path):

    text = extract_text_from_pdf(pdf_path)
    cleaned = clean_text(text)
    chunks = chunk_text(cleaned)

    embeddings = embed_text(chunks)

    index = create_faiss_index(embeddings)

    save_index(index)
    save_chunks(chunks)

    return index, chunks


def load_existing_index():

    index = load_index()
    chunks = load_chunks()

    return index, chunks


def main():

    pdf_path = "sample.pdf"

    if os.path.exists("faiss_index.index"):
        index, chunks = load_existing_index()
        print("Loaded existing FAISS index")
    else:
        index, chunks = build_index(pdf_path)
        print("Created new FAISS index")

    while True:

        question = input("\nAsk a question (type exit to stop): ")

        if question.lower() == "exit":
            break

        results = retrieve(index, question, chunks)

        context = "\n".join(results)

        answer = ask_llm(context, question)

        print("\nAnswer:\n", answer)


if __name__ == "__main__":
    main()
