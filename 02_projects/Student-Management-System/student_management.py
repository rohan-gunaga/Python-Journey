while True:
    print("==== STUDENT MANAGEMENT SYSTEM ====")
    
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Grade")
    print("5. Exit")

    choice = input("Enter your choice")

    if choice == "1":
        print("Add Student selected")

        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        branch = input("Enter branch: ")
        marks = int(input("Enter marks: "))

        student1 = {
            "name": name,
            "age": age,
            "branch": branch,
            "marks": marks
        }

        print("student added successfully!")


    elif choice == "2":
        print("View Students selected")

        print (student1["name"])
        print (student1["age"])
        print (student1["branch"])
        print (student1["marks"])


    elif choice == "3":
        print("Search Student selected")

        search_name = input("Enter student name to search: ")

        if search_name == student1["name"]:
            print("student found")
            print("Name:", student1["name"])
            print("Age:", student1["age"])
            print("Branch:", student1["branch"])
            print("Marks:", student1["marks"])
        else:
            print("student not found!")

    elif choice == "4":
        print("Calculate Grade selected")

        if student1["marks"] >= 90:
            grade = "A"
        elif student1["marks"] >= 75:
            grade = "B"
        elif student1["marks"] >= 60:
            grade = "C"
        elif student1["marks"] >= 40:
            grade = "D"
        else:
            grade = "F"
            
        print("Student:", student1["name"])
        print("Marks:", student1["marks"])
        print("Grade:", grade)

    elif choice == "5":
        print("Exiting...")
        break

    else:
      print("Invalid choice")


