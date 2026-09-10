import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "students.json"

class Student:

    def __init__(self, name, age, branch, marks):
        self.name = name
        self.age = age
        self.branch = branch
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"
        
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "branch": self.branch,
            "marks": self.marks
    }

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
        print("Marks:",self.marks)


students = []


def save_students():
    print("Saving students...")
    
    data = []

    for student in students:
        data.append(student.to_dict())

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def load_students():
    try:
        with open(FILE_PATH, "r") as file:
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
        print("students.json file not found!")

load_students()
    

while True:
    print("==== STUDENT MANAGEMENT SYSTEM ====")
    
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Grade")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()


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
                student.display()
                print()

    elif choice == "3":

        print("Search Student selected")

        search_name = input("Enter student name to search: ")

        found = False

        for student in students:

            if search_name == student.name:
                print("Student found!")
                student.display()
                found = True

        if found == False:
            print("Student not found!")
    

    elif choice == "4":
    
        print("Calculate Grade selected")

        search_name = input("Enter student name: ")

        found = False
        
        for student in students:

            if search_name == student.name:


                grade = student.get_grade()

                print("Student:", student.name)
                print("Marks:", student.marks)
                print("Grade:", grade)
        
                found = True

        if found == False:
            print("Student not found!")

    elif choice == "5":

        print("Update Student selected")

        search_name = input("Enter student name to update: ")

        found = False

        for student in students:

            if search_name == student.name:
                found = True

                new_age = int(input("Enter new age: "))
                new_branch = input("Enter new branch: ")
                new_marks = int(input("Enter new marks: "))

                student.age = new_age
                student.branch = new_branch
                student.marks = new_marks

                save_students()

                print("Student updated successfully!")

        if found == False:
            print("Student not found!")


    elif choice == "6":

        print("Delete Student selected")

        search_name = input("Enter student name to delete: ")

        found = False

        for student in students:

            if search_name == student.name:
                found = True

                students.remove(student)
                save_students()

                print("Student deleted successfully!")

        if found == False:
            print("Student not found!")


    elif choice == "7":
        print("Exiting...")
        break

    else:     
      print("Invalid choice")


