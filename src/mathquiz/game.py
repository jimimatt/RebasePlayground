import random

import click

from mathquiz.game_data import MathQuestion, load_questions


class MathQuiz:
    def __init__(self) -> None:
        self.data: list[MathQuestion] = load_questions()

    def run_game(self, total_questions: int = 10) -> None:
        if total_questions <= 0:
            raise ValueError("Total questions must be greater than 0.")
        print("Welcome to the Math Quiz Game!")
        print(f"You will be asked {total_questions} math question{'s' if total_questions > 1 else ''}.")
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


@click.command()
@click.option('--total_questions', default=10, help='Number of questions.')
def main(total_questions: int) -> None:
    quiz = MathQuiz()
    quiz.run_game(total_questions=total_questions)


if __name__ == "__main__":
    main()
