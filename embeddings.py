from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text_list):
    embeddings = model.encode(text_list)
    return np.array(embeddings).astype("float32")


# TEST BLOCK (for running separately)
if __name__ == "__main__":
    sample_texts = [
        "Indian agriculture depends on monsoon.",
        "Agriculture provides employment."
    ]

    print("Generating embeddings...")
    vectors = embed_text(sample_texts)

    print("Embedding shape:", vectors.shape)
    print("First vector:\n", vectors[0])
