import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,]', '', text)
    return text.strip()

if __name__ == "__main__":
    from extract import extract_text_from_pdf

    file_path = "sample.pdf"
    raw_text = extract_text_from_pdf(file_path)
    cleaned = clean_text(raw_text)

    print("\nCleaned Text (First 1000 characters):\n")
    print(cleaned[:1000])
