from datetime import date


class Assessment:
    pass


class Trainee:
    def __init__(self, name: str, email: str, date_of_birth: date, assessments):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        if assessments is None:
            self.assessments = []
        else:
            self.assessments = assessments

    def get_age(self) -> int:
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        self.assessments.append(assessment)


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
