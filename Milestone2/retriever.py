from modules.vector_store import collection
from modules.embeddings import embed_query


def retrieve_chunks(query, n_results=5):
    """
    Retrieve most relevant chunks from vector database
    """

    query_embedding = embed_query(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]
