# ==========================================
# Student Management System
# ==========================================

# List to store all student records
students = []


# ------------------------------------------
# Function to add a new student
# ------------------------------------------
def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    # Dictionary for one student
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("Student added successfully!")


# ------------------------------------------
# Function to remove a student
# ------------------------------------------
def remove_student():
    print("\n--- Remove Student ---")

    student_id = input("Enter Student ID to remove: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student removed successfully!")
            return

    print("Student not found!")


# ------------------------------------------
# Function to search a student
# ------------------------------------------
def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            return

    print("Student not found!")


# ------------------------------------------
# Function to display all students
# ------------------------------------------
def display_students():
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No students available.")
        return

    for student in students:
        print("---------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])


# ------------------------------------------
# Function to update student details
# ------------------------------------------
def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:

            print("Student Found!")

            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")

            print("Student updated successfully!")
            return

    print("Student not found!")


# ------------------------------------------
# Main Menu Function
# ------------------------------------------
def menu():

    while True:

        print("\n========================")
        print(" STUDENT MANAGEMENT SYSTEM")
        print("========================")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Update Student Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            update_student()

        elif choice == "6":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice! Please try again.")


# ------------------------------------------
# Program Start
# ------------------------------------------
menu()