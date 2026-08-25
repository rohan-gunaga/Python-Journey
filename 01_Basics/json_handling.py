
import json

student = {
    "name": "Rohan",
    "age":20,
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file) 


# problem 1:

with open("student.json", "r") as file:
    data = json.load(file)

print(data)

print(data["name"])
print(data["marks"])

# problem 2:

import json

student = {
    "name": "Rohan",
    "branch": "EEE",
    "cgpa": 7.88
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])
print(data["branch"])
print(data["cgpa"])

# problem 3:

import json

students = [
    {
        "name": "Rohan",
        "branch": "EEE",
        "marks": 85
    },
    {
        "name": "Rahul",
        "branch": "CSE",
        "marks": 92
    },
    {
        "name": "Kiran",
        "branch": "ISE",
        "marks": 78
    }
]

with open("student.json", "w") as file:
    json.dump(students, file)

with open("student.json", "r") as file:
    data = json.load(file)

for student in data:
    print(student["name"], "-", student["branch"], "-", student["marks"])
    