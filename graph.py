from typing import List, TypedDict

from langchain import hub
from langchain_core.documents import Document
from langchain_ollama.llms import OllamaLLM
from langgraph.graph import START, StateGraph

from vector_store import vector_store

prompt = hub.pull("rlm/rag-prompt")  # TODO other prompts
llm = OllamaLLM(model="llama3.2:latest")  # TODO other models


class State(TypedDict):
    """
    Internal state of the langgraph.
    question: The question to answer
    context_size: The number of documents to retrieve from the vector store
    context: The documents retrieved from the vector store
    answer: The answer to the question
    page: The page to retrieve documents from. This is used to filter the documents retrieved from the vector store.
    """

    question: str
    context_size: int
    context: List[Document]
    answer: str
    page: str


def retrieve(state: State) -> dict:
    """
    Retrieve documents from the vector store. The result is added to the state automatically.
    """
    context = vector_store.similarity_search(
        state["question"],
        k=state["context_size"],
        filter={"page": state["page"]},
    )
    if not context:
        raise ValueError(f"No context found for page {state['page']}")
    return {"context": context}


def answer_question(state: State) -> dict:
    """
    Answer the question using the context. The result is added to the state automatically.
    """
    messages = prompt.invoke(
        {
            "question": state["question"],
            "context": "\n\n".join([doc.page_content for doc in state["context"]]),
        }
    )
    return {"answer": llm.invoke(messages)}


graph_builder = StateGraph(State).add_sequence([retrieve, answer_question])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()
