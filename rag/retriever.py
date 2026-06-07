from rag.vector_store import (
    collection
)


def retrieve_documents(
    query: str
):

    results = collection.query(
        query_texts=[query],
        n_results=2
    )

    return results["documents"][0]