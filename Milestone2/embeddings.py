from sentence_transformers import SentenceTransformer

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(texts):
    """
    Convert list of text chunks into vector embeddings
    """
    embeddings = model.encode(texts)
    return embeddings.tolist()


def embed_query(query):
    """
    Convert user query into embedding
    """
    embedding = model.encode(query)
    return embedding.tolist()
