import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_llm(context, question):
    prompt = f"""
You are a research assistant.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content


# 🔥 This makes the file runnable independently
if __name__ == "__main__":
    from extract import extract_text_from_pdf
    from cleaning import clean_text
    from chunk import chunk_text

    file_path = "sample.pdf"

    print("Reading PDF...")
    text = extract_text_from_pdf(file_path)

    print("Cleaning text...")
    cleaned = clean_text(text)

    print("Creating chunks...")
    chunks = chunk_text(cleaned)

    question = input("\nEnter your question: ")

    answer = ask_llm(chunks[0], question)

    print("\nAI Answer:\n")
    print(answer)
