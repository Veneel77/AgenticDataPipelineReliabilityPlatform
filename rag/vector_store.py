import chromadb
from pathlib import Path

client = chromadb.PersistentClient(
    path="vectorstore"
)

collection = client.get_or_create_collection(
    name="pipeline_docs"
)


def load_documents():

    docs_folder = Path("docs")

    for file in docs_folder.glob("*.txt"):

        content = file.read_text(
            encoding="utf-8"
        )

        collection.add(
            documents=[content],
            ids=[file.stem]
        )

    print("Documents Loaded")