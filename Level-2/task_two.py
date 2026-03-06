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
