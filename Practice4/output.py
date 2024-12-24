def list_students(school):
    print("\nStudents:")
    for student in school.students.values():
        print(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

def list_courses(school):
    print("\nCourses:")
    for course in school.courses.values():
        print(f"ID: {course.course_id}, Name: {course.name}")

def list_marks(school):
    course_id = input("Enter the course ID to view marks: ")
    if course_id not in school.marks:
        print("No marks available for this course.")
        return
    course_name = school.courses[course_id].name
    print(f"\nMarks for course {course_name}:")
    for student_id, mark in school.marks[course_id].items():
        student_name = school.students[student_id].name
        print(f"Student {student_name} (ID: {student_id}): {mark}")

def list_gpa(school):
    school.calculate_gpa()
    sorted_gpa = sorted(school.GPA.items(), key=lambda x: x[1], reverse=True)
    print("\nGPA for all students (sorted by GPA):")
    for student_id, gpa in sorted_gpa:
        student_name = school.students[student_id].name
        print(f"Student {student_name} (ID: {student_id}): GPA = {gpa}")
