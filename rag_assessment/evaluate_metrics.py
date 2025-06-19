import evaluate
from graph import graph

rouge = evaluate.load("rouge")
bleu = evaluate.load("bleu")


def answer_question(page, question):
    response = graph.invoke(
        {
            "question": question,
            "page": page,
            "context_size": 5,
        }
    )

    return response["answer"], response["context"]


if __name__ == "__main__":
    questions = [
        (
            "https://en.wikipedia.org/wiki/History_of_physics",
            "Create a brief summary of key discoveries in modern physics",
        ),
        (
            "https://en.wikipedia.org/wiki/Non-disclosure_agreement",
            "Provide the structure of a NDA as a bullet points list.",
        ),
    ]

    answers = []
    contexts = []

    for page, question in questions:
        answer, context = answer_question(page, question)
        answers.append(answer)
        contexts.append("\n".join([doc.page_content for doc in context]))

    print("COMPARING ANSWERS TO QUESTIONS")
    print("Rouge scores:")
    rouge_scores = rouge.compute(predictions=answers, references=questions)
    for key, value in rouge_scores.items():
        print(f"{key}: {value}")

    print()
    print("Bleu scores:")
    bleu_scores = bleu.compute(predictions=answers, references=questions)
    for key, value in bleu_scores.items():
        print(f"{key}: {value}")

    print("--------------------------------")
    print("COMPARING ANSWERS TO CONTEXTS")
    print("Rouge scores:")
    rouge_scores = rouge.compute(predictions=answers, references=contexts)
    for key, value in rouge_scores.items():
        print(f"{key}: {value}")

    print()
    print("Bleu scores:")
    bleu_scores = bleu.compute(predictions=answers, references=contexts)
    for key, value in bleu_scores.items():
        print(f"{key}: {value}")
