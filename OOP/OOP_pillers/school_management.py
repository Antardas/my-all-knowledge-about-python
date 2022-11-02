from threading import Timer
from time import sleep, time


class School:

    def __init__(self, name, address, principle='') -> None:
        self.name = name
        self.address = address
        self.principle = principle
        self.grades = []

    def add_grade(self, grade, teacher):
        new_grade = Grade(grade, teacher)
        self.grades.append(new_grade)

    def remove_grade(self, grade):
        idx = -1
        for i, g in enumerate(self.grades):
            if g.name == grade:
                idx = i
                break
        if idx != -1:
            del self.grades[idx]


class Grade:

    def __init__(
        self,
        name,
        teacher,
    ) -> None:
        self.teacher = teacher
        self.name = name
        self.students = []

    def __repr__(self) -> str:
        return f'{self.name} at {self.teacher}'

    def __del__(self) -> None:
        print(f'{self.name} is deleted')


oxford = School("Oxford", "Dhaka", "Babu")
oxford.add_grade("1st", "Mr. X")
oxford.add_grade("2nd", "Mr. Y")
oxford.add_grade("3rd", "Mr. Z")

print(oxford.grades)

oxford.remove_grade("2nd")

print(oxford.grades)

sleep(10)
