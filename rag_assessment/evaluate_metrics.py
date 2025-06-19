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

    return response["answer"]


if __name__ == "__main__":
    questions = [
        "Create a brief summary of key discoveries in modern physics",
        "Provide the structure of a NDA as a bullet points list.",
    ]
    answers = [
        answer_question(
            "https://en.wikipedia.org/wiki/History_of_physics",
            questions[0],
        ),
        answer_question(
            "https://en.wikipedia.org/wiki/Non-disclosure_agreement",
            questions[1],
        ),
    ]

    print("Rouge scores:")
    rouge_scores = rouge.compute(predictions=answers, references=questions)
    for key, value in rouge_scores.items():
        print(f"{key}: {value}")

    print()
    print("Bleu scores:")
    bleu_scores = bleu.compute(predictions=answers, references=questions)
    for key, value in bleu_scores.items():
        print(f"{key}: {value}")
