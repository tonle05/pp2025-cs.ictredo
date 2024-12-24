from domains.school import School
from input import input_students, input_courses, input_marks
from output import list_students, list_courses, list_marks, list_gpa

def Menu(school):
    while True:
        print("\nMenu:")
        print("0. Exit.")
        print("1. Input the number of students and their info. ")
        print("2. Input the number of courses and their info. ")
        print("3. Input the new score for a course. ")
        print("4. List all the students.")
        print("5. List all the courses.")
        print("6. Show the marks for a course.")
        print("7. Show the GPA for all students. ")

        try:
            choice = int(input("I need a number: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if choice == 1:
            input_students(school)
        elif choice == 2:
            input_courses(school)
        elif choice == 3:
            input_marks(school)
        elif choice == 4:
            list_students(school)
        elif choice == 5:
            list_courses(school)
        elif choice == 6:
            list_marks(school)
        elif choice == 7:
            list_gpa(school)
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Main
if __name__ == "__main__":
    school = School()
    Menu(school)
