# pylint: disable=too-few-public-methods
"""Assessment and marking system with OOP"""


from datetime import date


class Assessment:
    """Class for Assessment"""

    def __init__(self, name: str, type: str, score: float):
        """Initialises Assessment"""
        valid_types = ["multiple-choice", "technical", "presentation"]
        if not isinstance(name, str):
            raise TypeError("name has to be a string")
        self.name = name

        if type not in valid_types:
            raise ValueError("Not valid assessment type")
        self.type = type

        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")
        self.score = score


class Trainee:
    """Represents a trainee who can take assessments"""

    def __init__(self, name: str, email: str, date_of_birth: date, assessments=None):
        """initialises trainee"""
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = assessments if assessments is not None else []

    def get_age(self) -> int:
        """calculates the age of the trainee"""
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """add an assessment to the trainee"""
        if not isinstance(assessment, Assessment):
            raise TypeError("assessment must be an Assessment object")
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """Returns the assessment by name"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """return assessments of a specific type"""
        matching_assessments = []
        for assessment in self.assessments:
            if assessment.type == type:
                matching_assessments.append(assessment)
        return matching_assessments


class MultipleChoiceAssessment(Assessment):
    """For the Multiple choice Assessment"""

    def __init__(self, name: str, score: float):
        """initialise multiple choice assessment"""
        super().__init__(name, "multiple-choice", score)

    def calculate_score(self) -> float:
        """return weighted score"""
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    """for the Technical Assessment"""

    def __init__(self, name: str, score: float):
        """initialise technical assessment"""
        super().__init__(name, "technical", score)

    def calculate_score(self) -> float:
        """return weighted score"""
        return self.score * 1


class PresentationAssessment(Assessment):
    """Presentation Assessment"""

    def __init__(self, name: str, score: float):
        """initialise presentation assessment"""
        super().__init__(name, "presentation", score)

    def calculate_score(self) -> float:
        """return weighted score"""
        return self.score * 0.6


class Question:
    """Represents a quiz question"""

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        """initialise quiz question"""
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:
    """Represents quiz containing questions"""

    def __init__(self, questions: list, name: str, type: str):
        """Initialise quiz"""
        self.questions = questions
        self.name = name
        self.type = type


class Marking:
    """Marks the quiz and generates the assessment"""

    def __init__(self, quiz: Quiz) -> None:
        """Initialise the quiz"""
        self._quiz = quiz

    def mark(self) -> int:
        """Returns the quiz score as a percentage"""
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
        """Generate the correct assessment type"""
        score = self.mark()
        if self._quiz.type == "multiple-choice":
            return MultipleChoiceAssessment(self._quiz.name, score)
        elif self._quiz.type == "technical":
            return TechnicalAssessment(self._quiz.name, score)
        else:
            #        elif self._quiz.type == "presentation":
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
    questions = [
        Question("What is 1 + 3? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 2 + 3? A:2 B:4 C:5 D:8", "C", "C"),
        Question("What is 3 + 5? A:2 B:4 C:6 D:8", "D", "D"),
        Question("What is 4 + 1? A:2 B:4 C:5 D:8", "C", "C"),
        Question("What is 5 + 3? A:10 B:4 C:5 D:8", "D", "D"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")
