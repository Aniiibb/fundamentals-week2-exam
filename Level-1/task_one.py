# pylint: disable=too-few-public-methods
"""Assessment and marking system with OOP"""
from datetime import date


class Assessment:
    """Class for Assessment"""

    def __init__(self, name: str, type: str, score: float):
        """Initialises Assessment"""
        valid_types = ["multiple-choice", "technical", "presentation"]
        if not isinstance(name, str):
            raise TypeError("")
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
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """Returns the assessment by name"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
