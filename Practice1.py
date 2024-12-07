
# Initialize to store
students = {}
courses = {}
marks = {}

# Input 
def input_num_of_students():
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth (DD/MM/YYYY): ")
        students[student_id] = {"name": student_name, "dob": student_dob}

def input_num_of_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses[course_id] = {"name": course_name}

def input_marks():
    course_id = input("Enter the course ID to input marks for: ")
    if course_id not in courses:
        print("Invalid course ID.")
        return

    if course_id not in marks:
        marks[course_id] = {}

    for student_id in students:
        student_mark = float(input(f"Enter marks for student {students[student_id]['name']} (ID: {student_id}): "))
        marks[course_id][student_id] = student_mark

# Listing 
def list_courses():
    print("\nCourses:")
    for course_id, course_info in courses.items():
        print(f"ID: {course_id}, Name: {course_info['name']}")

def list_students():
    print("\nStudents:")
    for student_id, student_info in students.items():
        print(f"ID: {student_id}, Name: {student_info['name']}, DoB: {student_info['dob']}")

def show_student_marks():
    course_id = input("Enter the course ID to view marks: ")
    if course_id not in marks:
        print("No marks available for this course.")
        return

    print(f"Marks for course {courses[course_id]['name']}: \n")
    for student_id, mark in marks[course_id].items():
        print(f"Student {students[student_id]['name']} (ID: {student_id}): {mark}")

# Main
while True:
    print("\nMenu:")
    print("0. Exit")
    print("1. Input number of students and their information")
    print("2. Input number of courses and their information")
    print("3. Input marks for a course")
    print("4. List courses")
    print("5. List students")
    print("6. Show student marks for a course")

    choice = int(input("The lucky number is: "))
    print("\n")
  
    if choice == 1:
        input_num_of_students()
    elif choice == 2:
        input_num_of_courses()
    elif choice == 3:
        input_marks()
    elif choice == 4:
        list_courses()
    elif choice == 5:
        list_students()
    elif choice == 6:
        show_student_marks()
    elif choice == 0:
        print("Exiting")
        break
    else:
        print("Invalid number. Please try again.")
