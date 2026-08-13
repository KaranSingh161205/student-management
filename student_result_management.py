import os
import json
file_path = "students.json"
def load_data():
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)    

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear()
    print("*"*93)
    print("-"*23 +" 'WELCOME TO STUDENT RESULT MANAGEMENT SYSTEM' " + "-"*23)
    print("-"*40 + " 'MAIN MENU' " + "-"*40)
    print("="*93)
    print("*"*93)
    print()
    print("\t\t\t\t1. ADD STUDENT")
    print("\t\t\t\t2. DISPLAY ALL STUDENTS")   
    print("\t\t\t\t3. SEARCH STUDENT")
    print("\t\t\t\t4. UPDATE STUDENT")
    print("\t\t\t\t5. Exit")
    print()
    choice = int(input("Choose your option from above : "))
    clear()
    return choice

def grade_calculator(marks):
    total = sum(marks.values())
    percentage = (total / (len(marks) * 100)) * 100
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

while True:
    choice = menu()
    if choice == 1:
        students = load_data()
        print("*"*93)
        print("-"*39 +" 'ADD STUDENT' " + "-"*39)
        print("="*93)
        print("*"*93)
        print()
        name = input("Enter Student Name : ")
        age = int(input("Enter Student Age : "))
        marks = {
            "Maths"   :  int(input("Enter Maths Marks    : ")),
            "Science" :  int(input("Enter Science Marks  : ")),
            "English" :  int(input("Enter English Marks  : ")),
        }
        grade = grade_calculator(marks)
        students[name] = {
            "name": name,
            "age": age,
            "marks": marks,
            "grade": grade
        }

        save_data(students)
        print()
        print(f"The Student's Grade is : {grade}")
        print()
        print("Student added successfully!")
        input("Press Enter to continue...")

    elif choice == 2:
        students = load_data()
        print("*"*93)
        print("-"*34 +" 'DISPLAY ALL STUDENTS' " + "-"*35)
        print("="*93)
        print("*"*93)
        print()
        if students:
            for i, student in enumerate(students.values(), start=1):
                print(f"Student {i} :")
                print(f"  Name      :   {student['name']}")
                print(f"  Age       :   {student['age']}")
                print(f"  Marks     :   {student['marks']}")
                print(f"  Grade     :   {student['grade']}")
                print()
        else:
            print("No students to display.")
        input("Press Enter to continue...")
    elif choice == 3:
        students = load_data()
        print("*"*93)
        print("-"*37 +" 'SEARCH STUDENT' " + "-"*38)
        print("="*93)
        print("*"*93)
        print()
        search_name = input("Enter Student Name to Search : ")
        student = students.get(search_name)
        if student:
            print()
            print(f"  Name  : {student['name']}")
            print(f"  Age   : {student['age']}")
            print(f"  Marks : {student['marks']}")
            print(f"  Grade : {student['grade']}")
            print()
        else:
            print("Student not found.")
        input("Press Enter to continue...")
    elif choice == 4:
        students = load_data()
        print("*"*93)
        print("-"*37 +" 'UPDATE STUDENT' " + "-"*38)
        print("="*93)
        print("*"*93)
        print()
        update_name = input("Enter Student Name to Update : ")
        student = students.get(update_name)
        if student:
            print(f"Current Age: {student['age']}")
            new_age = int(input("Enter New Age : "))
            student['age'] = new_age

            print(f"Current Marks: {student['marks']}")
            new_marks = {
                "Maths"   :  int(input("Enter New Maths Marks    : ")),
                "Science" :  int(input("Enter New Science Marks  : ")),
                "English" :  int(input("Enter New English Marks  : ")),
            }
            student['marks'] = new_marks
            student['grade'] = grade_calculator(new_marks)

            save_data(students)
            print()
            print(f"The Student's Updated Grade is : {student['grade']}")
            print()
            print("Student updated successfully!")
        else:
            print("Student not found.")
        input("Press Enter to continue...")
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break
