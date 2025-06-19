import argparse

from graph import graph
from vector_store import get_store

vector_store = get_store()


def answer_questions(page: str, context_size: int):
    while True:
        question = input("Enter a question (type 'exit' to quit): ")
        if question == "exit":
            break

        try:
            response = graph.invoke(
                {
                    "question": question,
                    "page": page,
                    "context_size": context_size,
                }
            )
        except ValueError as e:
            print(e)
            exit()

        print(response["answer"])
        print("-" * 100)
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("page", type=str, required=True)
    parser.add_argument("--context-size", type=int, default=5)
    args = parser.parse_args()
    answer_questions(args.page, args.context_size)
