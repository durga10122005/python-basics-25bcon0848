from dataclasses import dataclass


@dataclass
class Student:
    roll_no: int
    name: str
    age: int
    department: str


if __name__ == "__main__":
    student = Student(roll_no=101, name="Durga", age=20, department="CSE")
    print(student)
