import math
from .student import Student
from .course import Course

class School:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}
        self.GPA = {}

    def calculate_gpa(self):
        for student_id in self.students.keys():
            total_marks = 0
            total_credits = 0

            for course_id, course in self.courses.items():
                if course_id in self.marks and student_id in self.marks[course_id]:
                    total_marks += self.marks[course_id][student_id] * int(course.credit)
                    total_credits += int(course.credit)

            if total_credits > 0:
                self.GPA[student_id] = round(total_marks / total_credits, 2)
            else:
                self.GPA[student_id] = 0
