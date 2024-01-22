import csv

class Student:
    def __init__(self, name, surname, school_class, year_of_birth, grade_avg):
        self.name = name
        self.surname = surname
        self.school_class = school_class
        self.year_of_birth = year_of_birth
        self.grade_avg = grade_avg

    @classmethod
    def from_file(cls, file, class_name=None):
        students = []
        with open(file) as students_file:
            for row in csv.reader(students_file):
                if class_name is None or class_name == row[2]:
                    students.append(
                        cls(row[0], row[1], row[2], int(row[3]), float(row[4]))
                    )
        return students
