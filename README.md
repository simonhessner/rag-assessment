# RAG assessment

## Install ollama and download llama3.2:latest

1. Download ollama from https://ollama.com/ 
2. pull llama3.2:latest using `ollama pull llama3.2:latest`

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

## Report

in progress