import chromadb
from sentence_transformers import SentenceTransformer

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# initialize vector database
client = chromadb.Client()

collection = client.create_collection(name="documents")


def store_chunks(chunks):

    embeddings = model.encode(chunks).tolist()

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )


def search_chunks(query, n_results=5):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]
