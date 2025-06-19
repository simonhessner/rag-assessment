# RAG assessment

## Install ollama and download llama3.2:latest

TODO explain

## Fill database
```
uv run rag_assessment/vector_store.py
```

## Interactive question answering

e.g.

```
uv run rag_assessment/main.py https://en.wikipedia.org/wiki/History_of_physics
```

## Run evaluation

```
uv run rag_assessment/evaluate_metrics.py
```