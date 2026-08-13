import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

students = []
clear_screen()
def menu(): 
    clear_screen()   
    print("------ 'WELCOME TO STUDENT MANAGEMENT SYSTEM' -------")
    print()
    print("1. Add Student")
    print("2. View Students")   
    print("3. Search Student")
    print("4. Exit")
    print()
    choice = int(input("Choose your option from above: "))
    clear_screen()
    return choice
while True: 
    choice = menu()
    if choice == 1:
        print("------ 'ADD STUDENT' -------")
        print()
        name = input("Enter Student Name : ")
        age = int(input("Enter Student Age : "))
        grade = input("Enter Student Grade : ")
        student = {
            "name": name,
            "age": age,
            "grade": grade
        }
        students.append(student)
        print("Student added successfully!")
        input("Press Enter to continue...")
    elif choice == 2:
        print("------ 'VIEW STUDENTS' -------")
        print()
        if students:
            for i, student in enumerate(students, start=1):
                print(f"Student {i}:")
                print(f"  Name: {student['name']}")
                print(f"  Age: {student['age']}")
                print(f"  Grade: {student['grade']}")
                print()
        else:
            print("No students to display.")
        input("Press Enter to continue...")
    elif choice == 3:
        print("------ 'SEARCH STUDENT' -------")
        print()
        search_name = input("Enter Student Name to Search: ")
        found_students = [student for student in students if student['name'].lower() == search_name.lower()]
        if found_students:
            for student in found_students:
                print(f"  Name: {student['name']}")
                print(f"  Age: {student['age']}")
                print(f"  Grade: {student['grade']}")
                print()
        else:
            print("Student not found.")
        input("Press Enter to continue...")
    elif choice == 4:
        print("Exiting the Student Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")