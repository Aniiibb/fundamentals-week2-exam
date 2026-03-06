

from datetime import date


class Assessment:
    def __init__(self, name: str, type: str, score: float):
        valid_types = ["multiple-choice", "technical", "presentation"]
        if not isinstance(name, str):
            raise TypeError("name has to be a string")
        self.name = name

        if type not in valid_types:
            raise ValueError("Not valid assessment type")
        self.type = type

        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100")
        self.score = score


class Trainee:
    def __init__(self, name: str, email: str, date_of_birth: date, assessments=None):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = assessments if assessments is not None else []

    def get_age(self) -> int:
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        if not isinstance(assessment, Assessment):
            raise TypeError("assessment must be an Assessment object")
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        matching_assessments = []
        for assessment in self.assessments:
            if assessment.type == type:
                matching_assessments.append(assessment)
        return matching_assessments


class MultipleChoiceAssessment(Assessment):
    """For the Multiple choice Assessment"""

    def __init__(self, name: str, score: float):
        super().__init__(name, "multiple-choice", score)

    def calculate_score(self) -> float:
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    """for the Technical Assessment"""

    def __init__(self, name: str, score: float):
        super().__init__(name, "technical", score)

    def calculate_score(self) -> float:
        return self.score * 1


class PresentationAssessment(Assessment):
    def __init__(self, name: str, score: float):
        super().__init__(name, "presentation", score)

    def calculate_score(self) -> float:
        return self.score * 0.6


#####
#
# COPY YOUR CODE FROM LEVEL 2 ABOVE
#
#####


class Question:

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz

    def mark(self) -> int:
        total_questions = len(self._quiz.questions)
        if total_questions == 0:
            return 0

        correct_count = 0
        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                correct_count += 1

        percentage = (correct_count / total_questions) * 100
        return round(percentage)

    def generate_assessment(self) -> Assessment:
        score = self.mark()
        if self._quiz.type == "multiple-choice":
            return MultipleChoiceAssessment(self._quiz.name, score)
        elif self._quiz.type == "technical":
            return TechnicalAssessment(self._quiz.name, score)
        elif self._quiz.type == "presentation":
            return PresentationAssessment(self._quiz.name, score)


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
