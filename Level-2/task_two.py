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


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
