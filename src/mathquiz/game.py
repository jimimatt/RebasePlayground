import random

from mathquiz.game_data import MathQuestion, load_questions


class MathQuiz:
    def __init__(self) -> None:
        self.data: list[MathQuestion] = load_questions()

    def run_game(self, total_questions: int = 10, category: str | None = None) -> None:
        print("Welcome to the Math Quiz Game!")
        print(f"You will be asked a series of {category or ''} math questions.")
        print("Try to answer them correctly!")
        print("Let's start!\n")

        score = 0

        for i, idx in enumerate(random.sample(range(len(self.data)), k=total_questions)):
            math_question = self.data[idx]
            user_answer = input(f"Question {i + 1}: {math_question.question}\n")

            if math_question.check_answer(answer=user_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is '{math_question.answer}'.\n")

        print(f"Game Over! Your score is {score}/{total_questions}.")


def main() -> None:
    quiz = MathQuiz()
    quiz.run_game()


if __name__ == "__main__":
    main()
