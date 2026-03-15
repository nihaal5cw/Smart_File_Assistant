import chromadb
from modules.embeddings import create_embeddings

# initialize chroma client
client = chromadb.Client()

# create collection
collection = client.get_or_create_collection(name="documents")


def store_chunks(chunks):
    """
    Store document chunks with embeddings in vector database
    """

    embeddings = create_embeddings(chunks)

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )
