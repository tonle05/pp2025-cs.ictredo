# Define class
class Student: 
    def __init__(self, student_id, name, dob):
        self.name = name
        self.student_id = student_id 
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class School:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

# Input
    # Students
    def input_students(self):
        num = int(input("Enter the number of students: "))
        for _ in range(num):
            student_id = input("Enter the student ID: ")
            name = input("Enter the student name: ")
            dob = input("Enter the student DOB (DD/MM/YYYY): ")
            self.students[student_id] = Student(student_id, name , dob)
    # Courses
    def input_courses(self):
        num = int(input("Enter the number of courses: "))
        for _ in range(num):
            course_id = input("Enter the course ID: ")
            name = input("Enter the course name: ")
            self.courses[course_id] = Course(course_id, name)
    
    # Marks
    def input_marks(self):
        course_id = input("Enter the course ID to input mark for: ")
        if course_id not in self.courses:
            print("Invalid ID. Please try again.")
            return 
        if course_id not in self.marks:
            self.marks[course_id] = {}
        for student_id, student in self.students.items():
            try:
                mark = float(input(f"Enter the mark for student {student.name} (ID: {student_id}): "))
                self.marks[course_id][student_id] = mark
            except ValueError:
                print("Invalid identify. Marks must be a real number")

# List
    def list_students(self):
        print("\nStudents: ")
        for student in self.students.values():
            print(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")
    def list_course(self):
        print("\nCourses:")
        for course in self.courses.values():
            print(f"ID: {course.course_id}, Name: {course.name}")
    def list_marks(self):
        course_id = input("Enter the course ID to view marks: ")
        if course_id not in self.marks:
            print("No marks available for this course. ")
            return

        course_name = self.courses[course_id].name
        print(f"\nMarks for course {course_name}: ")
        for student_id, mark in self.marks[course_id].items():
            student_name = self.students[student_id].name
            print(f"Student {student_name} (ID: {student_id}): {mark}")
        
# Menu
    def Menu(self):
        while True:
            print("\nMenu:")
            print("0. Exit.")
            print("1. Input the number of students and their info. ")
            print("2. Input the number of courses and their info. ")
            print("3. Input the new score for a course. ")
            print("4. List all the students.")
            print("5. List all the courses.")
            print("6. Show the marks for a course.")

            try :
                choice = int(input("I need a number: "))
            except ValueError:
                print("Invalid number. Please try again")
                continue
            
            if choice == 1:
                self.input_students()
            elif choice == 2:
                self.input_courses()
            elif choice == 3:
                self.input_marks()
            elif choice == 4:
                self.list_students()
            elif choice == 5:
                self.list_course()
            elif choice == 6:
                self.list_marks()
            elif choice == 0:
                print("Exiting")
                break
            else:
                print(f"Invalid choice. Please try again")

# Main
if __name__ == "__main__" :
    school = School()
    school.Menu()

        

        


    

        
        
