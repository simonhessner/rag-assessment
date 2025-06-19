import argparse
import shutil
from pathlib import Path

import wikipediaapi
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from embedding import embeddings

wikipedia = wikipediaapi.Wikipedia(user_agent="rag-assessment")

PERSIST_DIR = Path("chroma_db")


def get_text_from_page(page: str) -> str:
    page = wikipedia.page(page.split("/")[-1])
    if not page.exists():
        raise ValueError(f"Page {page} does not exist")
    return page.text


def get_store() -> Chroma:
    # Using Chroma because it supports filtering by metadata. That way I can make sure to only
    # retrieve documents from the page that the user is interested in.
    vector_store = Chroma(
        persist_directory=str(PERSIST_DIR), embedding_function=embeddings
    )
    return vector_store


def build_vector_store(chunk_size: int, chunk_overlap: int):
    if PERSIST_DIR.exists():
        print(f"Removing {PERSIST_DIR}")
        shutil.rmtree(PERSIST_DIR)

    vector_store = get_store()

    with open("wikipedia_pages.txt", "r") as f:
        pages = [line.strip() for line in f.readlines()]

    documents = []

    for page in pages:
        print(f"Processing page {page}")
        text = get_text_from_page(page)
        document = Document(page_content=text, metadata={"page": page})
        documents.append(document)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    splits = text_splitter.split_documents(documents)

    vector_store.add_documents(splits)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunk-size", type=int, default=1000)
    parser.add_argument("--chunk-overlap", type=int, default=200)
    args = parser.parse_args()
    build_vector_store(args.chunk_size, args.chunk_overlap)
