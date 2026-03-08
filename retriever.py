from embeddings import embed_text
from vector_store import create_faiss_index

def retrieve(index, query, chunks, top_k=3):
    query_embedding = embed_text([query])
    distances, indices = index.search(query_embedding, top_k)
    return [chunks[i] for i in indices[0]]


# TEST BLOCK
if __name__ == "__main__":
    print("Testing retriever...")

    chunks = [
        "Indian agriculture depends on rainfall.",
        "Monsoon plays a major role in farming.",
        "Technology improves crop yield."
    ]

    # Generate embeddings
    embeddings = embed_text(chunks)

    # Create FAISS index
    index = create_faiss_index(embeddings)

    # Ask query
    query = "How does monsoon affect agriculture?"

    results = retrieve(index, query, chunks)

    print("\nQuery:", query)
    print("\nTop Retrieved Chunks:")
    for r in results:
        print("-", r)
