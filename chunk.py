def chunk_text(text, chunk_size=800, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks


if __name__ == "__main__":
    from extract import extract_text_from_pdf
    from cleaning import clean_text

    file_path = "sample.pdf"

    text = extract_text_from_pdf(file_path)
    cleaned = clean_text(text)
    chunks = chunk_text(cleaned)

    print("\nTotal Chunks:", len(chunks))
    print("\nFirst Chunk:\n")
    print(chunks[0])
