
with open("python_notes.txt", "w") as file:
    file.write("I am learning Python.\n")
    file.write("I am practicing everyday.\n")
    file.write("I want to become a software engineer.\n")

with open("python_notes.txt", "r") as file:
        data = file.read()

print(data)

# problem 1:
with open("python_notes.txt", "a") as file:
    file.write("I am building real Python projects.\n")


# problem 2:
students = ["Rohan", "Rahul", "Kiran", "Arjun"]

with open("students.txt", "w") as file:
    for student in students :
        file.write(student + "\n")

# problem 3:

numbers = [10, 20, 30, 40, 50]

with open("practice.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n" )

# problem 4:

numbers = [12, 7, 24, 9, 16, 31, 40, 55]

with open("practice.txt", "w") as file:
    for number in numbers:
        if number % 2 == 0:

            file.write(str(number) + "\n")

# problem 5:

names = ["Arjun", "Rohan", "Ananya", "Kiran", "Amit", "Rahul"]

with open("practice.txt", "w") as file:
    for name in names:
        if name.startswith ("A"):
            file.write(name + "\n")

# problem 6:

new_students = ["Sneha", "Pooja", "Varun"]

with open("practice.txt", "a") as file:
    for new_student in new_students:
        file.write(new_student + "\n")

# problem 7:

marks = {
    "Rohan": 85,
    "Rahul": 72,
    "Kiran": 91,
    "Arjun": 64
}

with open("practice.txt", "w") as file:
    for name, mark in marks.items():
        file.write(name + " - " + str(mark) + "\n")