import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("research_memory")

def save_memory(text: str):
    collection.add(documents=[text], ids=[str(len(collection.get()["ids"]))])

def retrieve_memory(query: str):
    return collection.query(query_texts=[query], n_results=3)
