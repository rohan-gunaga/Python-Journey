import json

class Student:

    def __init__(self, name, age, branch, marks):
        self.name = name
        self.age = age
        self.branch = branch
        self.marks = marks


students = []



def save_students():
    print("Saving students...")
    
    data = []

    for student in students:
        data.append({
            "name": student.name,
            "age": student.age,
            "branch": student.branch,
            "marks": student.marks
        })

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

def load_students():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)

            for item in data:
                student = Student(
                    item["name"],
                    item["age"],
                    item["branch"],
                    item["marks"]
                )

                students.append(student)

    except FileNotFoundError:
        pass


load_students()

while True:
    print("==== STUDENT MANAGEMENT SYSTEM ====")
    
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Grade")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("Add Student selected")

        try:
            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            branch = input("Enter branch: ")
            marks = int(input("Enter marks: "))                          
        
            student = Student(name, age, branch, marks)
            students.append(student)
            save_students()

            print("student added successfully!")

        except ValueError:

            print("please enter numbers for age and marks!")

    elif choice == "2":

        print("View Students selected")

        if not students:
            print("No students found!")

        else:
            for student in students:
            
                print("Name:",student.name)
                print("Age:",student.age)
                print("Branch:",student.branch)
                print("Marks:",student.marks)
                print()

    elif choice == "3":

        print("Search Student selected")

        search_name = input("Enter student name to search: ")

        found = False

        for student in students:

            if search_name == student.name:
                print("Student found!")
                print("Name:", student.name)
                print("Age:", student.age)
                print("Branch:", student.branch)
                print("Marks:", student.marks)

                found = True

        if found == False:
            print("Student not found!")
    

    elif choice == "4":
    
        print("Calculate Grade selected")

        search_name = input("Enter student name: ")

        found = False
        
        for student in students:

            if search_name == student.name:


                if student.marks >= 90:
                    grade = "A"

                elif student.marks >= 75:
                    grade = "B"
                elif student.marks >= 60:
                    grade = "C"
                elif student.marks >= 40:
                    grade = "D"
                else:
                    grade = "F"
            
                print("Student:", student.name)
                print("Marks:", student.marks)
                print("Grade:", grade)

                found = True

        if found == False:
            print("Student not found!")

    elif choice == "5":
        print("Exiting...")
        break

    else:
      print("Invalid choice")


