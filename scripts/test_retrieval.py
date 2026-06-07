from rag.retriever import (
    retrieve_documents
)

results = retrieve_documents(
    "schema drift missing column"
)

for doc in results:
    print()
    print("=" * 50)
    print(doc)