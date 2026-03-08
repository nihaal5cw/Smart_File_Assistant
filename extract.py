import fitz

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text("text")
    return text


# This must be at the bottom of the file
if __name__ == "__main__":
    file_path = "sample.pdf"
    text = extract_text_from_pdf(file_path)
    print("\nExtracted Text (First 1000 characters):\n")
    print(text[:1000])
