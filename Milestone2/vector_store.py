import faiss
import pickle

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index


def save_index(index, path="faiss_index.index"):
    faiss.write_index(index, path)


def load_index(path="faiss_index.index"):
    return faiss.read_index(path)


def save_chunks(chunks, path="chunks.pkl"):
    with open(path, "wb") as f:
        pickle.dump(chunks, f)


def load_chunks(path="chunks.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)
