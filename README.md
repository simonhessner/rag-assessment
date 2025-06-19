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

## Evaluation results

    COMPARING ANSWERS TO QUESTIONS
    Rouge scores:
    rouge1: 0.19537815126050423
    rouge2: 0.15317073170731707
    rougeL: 0.1834733893557423
    rougeLsum: 0.1834733893557423

    Bleu scores:
    bleu: 0.06997126969587249
    precisions: [0.12626262626262627, 0.07142857142857142, 0.05670103092783505, 0.046875]
    brevity_penalty: 1.0
    length_ratio: 9.0
    translation_length: 198
    reference_length: 22
    --------------------------------
    COMPARING ANSWERS TO CONTEXTS
    Rouge scores:
    rouge1: 0.20230544049947163
    rouge2: 0.0957633271485879
    rougeL: 0.12816451467926684
    rougeLsum: 0.19757066333037765

    Bleu scores:
    bleu: 0.000711387435016773
    precisions: [0.6666666666666666, 0.29591836734693877, 0.14432989690721648, 0.08854166666666667]
    brevity_penalty: 0.003174753610867076
    length_ratio: 0.1480927449513837
    translation_length: 198
    reference_length: 1337