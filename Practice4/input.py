from domains.student import Student
from domains.course import Course

import math

def input_students(school):
    num = int(input("Enter the number of students: "))
    for _ in range(num):
        student_id = input("Enter the student ID: ")
        name = input("Enter the student name: ")
        dob = input("Enter the student DOB (DD/MM/YYYY): ")
        school.students[student_id] = Student(student_id, name, dob)

def input_courses(school):
    num = int(input("Enter the number of courses: "))
    for _ in range(num):
        course_id = input("Enter the course ID: ")
        name = input("Enter the course name: ")
        credit = input("Enter the credit of the course: ")
        school.courses[course_id] = Course(course_id, name, credit)

def input_marks(school):
    course_id = input("Enter the course ID to input marks for: ")
    if course_id not in school.courses:
        print("Invalid course ID. Please try again.")
        return
    if course_id not in school.marks:
        school.marks[course_id] = {}

    for student_id, student in school.students.items():
        try:
            mark = float(input(f"Enter the mark for student {student.name} (ID: {student_id}): "))
            mark = math.floor(mark * 10) / 10
            school.marks[course_id][student_id] = mark
        except ValueError:
            print("Invalid mark. Marks must be a real number.")
