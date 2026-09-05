# # problem 1:

# name = input("enter the name: ")
# marks = int(input("enter the marks: "))

# if marks >= 90:
#     print(name, "'s Grade: A")
# elif marks >= 75:
#     print(name, "'s Grade: B")
# elif marks >= 60:
#     print(name, "'s Grade: C")
# elif marks >= 40:
#     print(name, "'s Grade: D")
# else:
#     print(name, "'s Grade: F")

# # problem 2:

# numbers = [10, 25, 8, 42, 17, 30]
# count = 0
# sum = 0

# for number in numbers:
#     sum = sum + number

# print(sum)

# for number in numbers:
#     if number % 2 == 0:
#         count = count + 1

# print(count)

# largest = numbers [0]

# for number in numbers:
#     if number > largest:
#         largest = number

# print(largest) 

# # problem 3:

# numbers = [10, 20, 30, 40, 50]

# def find_average(numbers):
#     total = 0

#     for number in numbers:
#         total = total + number

#     average = total / len(numbers)

#     return average

# print(find_average(numbers))
                              
# # problem 4:

# student = {
#     "name": "Rohan",
#     "marks": 85,
#     "branch": "EEE"
# }

# def display_student(student):

#    print("Name:", student["name"])
#    print("Marks:", student["marks"])
#    print("Branch:", student["branch"])

# display_student(student)

# # problem 5:

# student = {
#     "name": "Rohan",
#     "marks": 85
# }

# def calculate_grade(student):

#     marks = student["marks"]

 
#     if marks >= 90:
#         grade = "A"
#     elif marks >= 75:
#         grade = "B"
#     elif marks >= 60:
#         grade = "C"
#     elif marks >= 40:
#         grade = "D"
#     else:
#         grade = "F"

#     return grade

# grade = calculate_grade(student)

# print("Student:", student["name"])
# print("Grade:", grade)

# # problem 6:

# def square(number):
#     return number * number

# answer = square(5)
# print(answer)

# # problem 7:

# def check_even(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# result = check_even(17)
# print(result)

# # problem 8:

# def test():
#     return "Hello"

# result = test()
# print(result)

# # problem 9:

# students = [
#     {"name": "Rohan", "marks": 85},
#     {"name": "Rahul", "marks": 92},
#     {"name": "Anu", "marks": 67}
# ]

# def get_grade(marks):

#         if marks >= 90:
#             grade = "A"
#         elif marks >= 75:
#             grade = "B"
#         elif marks >= 60:
#             grade = "C"
#         elif marks >= 40:
#             grade = "D"
#         else:
#             grade = "F"

#         return grade

# for student in students:
    
#     grade = get_grade(student["marks"])

#     print(student["name"], "-", grade)

# # problem 10:

# def multiply_numbers(*args):
#     total = 1

#     for number in args:
#         total = total * number

#     return total

# result = multiply_numbers(2, 3, 4)
# print(result)

# # problem 11:

# def find_max(*args):

#     max_value = args[0]

#     for number in args:
#         if number > max_value:
#             max_value = number

#     return max_value

# result = find_max(10, 45, 23, 78, 12)
# print(result)

# # problem 12:

# def student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# student_info(name="Rohan", age=20, branch="EEE")

# # problem 13:

# def student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# student_info(name="Rohan", age=20, branch="EEE", college="SIT", cgpa=7.88)

# # problem 14:

# def student_report(**kwargs):
#     print("===== STUDENT REPORT =====")
#     for key, value in kwargs.items():
#         print(key, ":", value)

# student_report(name="Rohan", branch="EEE", cgpa=7.88, college="SIT")
     
# # problem 15:

# name = "Rohan"

# def greet():
#     name = "Rahul"
#     print(name)

# greet()
# print(name)

# # problem 16:

# x = 10

# def test():
#     x = 20
#     print(x)

# test()
# print(x)

# x = 10

# def test():
#     global x
#     x = x + 5
#     print(x)

# test()

# # problem 17:

# import math

# number = 5

# result = math.ceil(number)

# print(result)

# # problem 18:

# import math

# number = 7.8

# result = math.floor(number)

# print(result)

# # problem 19:

# from calculator import add

# number1 = int(input("enter the number1: "))
# number2 = int(input("enter the number2: "))

# sum = add(number1,number2)
# square_number = square(sum)

# print("Sum: ",sum)


# # problem 20:

# from calculator import add, subtract, multiply


# number1 = int(input("enter the number1: "))
# number2 = int(input("enter the number2: "))

# addition = add(number1,number2)
# subtraction = subtract(number1,number2)
# multiplication = multiply(number1,number2)

# print("Addition: ",addition)
# print("Subtraction: ",subtraction)
# print("Multiplication: ",multiplication)

# # problem 21:

# try:
#     number = int("hello")
#     result = 10 / number

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# except ValueError:
#     print("Invalid number")

# # problem 22:
# try:
#     number1 = int(input("Enter the number1: "))
#     number2 = int(input("Enter the number2: "))

#     result = number1 / number2

#     print(result)

# except ValueError:
#     print("please enter numbers only")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("program finished")

# # problem 23:

# try:
#     num = int(input("Enter the number: "))
#     print(num)

# except ValueError:
#     print("Invalid number")

# finally:
#     print("Program ended")


# problem 30:

import json

student = {
    "name": "Rohan",
    "age": 20,
    "branch": "EEE",
    "cgpa": 7.88
}

with open("student.json", "w") as file:

    json.dump(student, file)

# problem 31: 

import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])
print(data["age"])
print(data["branch"])
print(data["cgpa"])

# problem 32:

import json

students = [
    {"name": "Rohan", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Anu", "marks": 67}
]

with open("students.json", "w") as file:
    json.dump(students, file)

# problem 33:
import json

with open("students.json", "r") as file:
    data = json.load(file)

    for student in data:
        print(student["name"], "-", student["marks"])

# problem 34:

import json

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    if student["name"] == "Rahul":
        student["marks"] = 95

with open("students.json", "w") as file:
    json.dump(students, file)

# problem 35:

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Rohan", 20) 

print(student1.name)
print(student1.age)

# problem 36:

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Rohan", 20)
student2 = Student("Rahul", 21)

print(student1.name, "-", student1.age)
print(student2.name, "-", student2.age)

