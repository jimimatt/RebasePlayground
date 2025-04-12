import importlib.resources
import json
import zipfile


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
    """Load questions and return a list of MathQuestion objects."""
    with (
        importlib.resources.path("mathquiz.data", "math_questions.zip") as data_path,
        zipfile.ZipFile(data_path) as zip_file,
        zip_file.open('math_questions.json') as json_file,
    ):
        data = json.load(json_file)

    questions: list[MathQuestion] = []
    for item in data:
        questions.append(MathQuestion(**item))
    return questions
