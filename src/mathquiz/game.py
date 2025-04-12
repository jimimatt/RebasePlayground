import random

import click

from mathquiz.game_data import AreaOfMathematics, MathQuestion, load_questions


class MathQuiz:
    def __init__(self, category: list[str]) -> None:
        self.data: list[MathQuestion] = load_questions(categories=category)

    def run_game(self, total_questions: int = 10) -> None:
        if total_questions <= 0:
            raise ValueError("Total questions must be greater than 0.")
        if total_questions > len(self.data):
            total_questions = len(self.data)
            print(f"Warning: Only {len(self.data)} questions available. Adjusting total questions to {len(self.data)}.")
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
@click.option('--total-questions', default=10, help='Number of questions.')
@click.option(
    '--category',
    '-c',
    multiple=True,
    type=click.Choice([category.value for category in AreaOfMathematics], case_sensitive=False),
    help='Areas of mathematics to include',
)
def main(total_questions: int, category: list[str]) -> None:
    quiz = MathQuiz(category=category)
    quiz.run_game(total_questions=total_questions)


if __name__ == "__main__":
    main()
