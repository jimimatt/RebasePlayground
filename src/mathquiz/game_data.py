import importlib.resources

import pandas as pd


class MathQuestion:
    __slots__ = ("question", "answer", "difficulty", "category")

    def __init__(self, question: str, answer: str, difficulty: str, category: str) -> None:
        self.question = question
        self.answer = answer
        self.difficulty = difficulty
        self.category = category

    def check_answer(self, answer: str) -> bool:
        return answer.replace(' ', '').lower() == self.answer.replace(' ', '').lower()


def load_questions() -> list[MathQuestion]:
    """Load questions return a list of MathQuestion objects."""
    with importlib.resources.path("mathquiz.data", "math_questions.zip") as data_path:
        df = pd.read_json(data_path, compression="zip")

    questions: list[MathQuestion] = []
    for _, row in df.iterrows():
        question = MathQuestion(
            question=row["question"],
            answer=row["answer"],
            difficulty=row["difficulty"],
            category=row["category"],
        )
        questions.append(question)
    return questions
