import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="projectpilot_docs"
)


def store_document(doc_id, text):
    collection.add(
        ids=[doc_id],
        documents=[text]
    )


def retrieve_documents(query):

    results = collection.query(
        query_texts=[query],
        n_results=2
    )

    return results["documents"][0]