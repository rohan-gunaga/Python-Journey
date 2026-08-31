# problem 1:

name = input("enter the name: ")
marks = int(input("enter the marks: "))

if marks >= 90:
    print(name, "'s Grade: A")
elif marks >= 75:
    print(name, "'s Grade: B")
elif marks >= 60:
    print(name, "'s Grade: C")
elif marks >= 40:
    print(name, "'s Grade: D")
else:
    print(name, "'s Grade: F")

# problem 2:

numbers = [10, 25, 8, 42, 17, 30]
count = 0
sum = 0

for number in numbers:
    sum = sum + number

print(sum)

for number in numbers:
    if number % 2 == 0:
        count = count + 1

print(count)

largest = numbers [0]

for number in numbers:
    if number > largest:
        largest = number

print(largest) 

# problem 3:

numbers = [10, 20, 30, 40, 50]

def find_average(numbers):
    total = 0

    for number in numbers:
        total = total + number

    average = total / len(numbers)

    return average

print(find_average(numbers))
                              
# problem 4:

student = {
    "name": "Rohan",
    "marks": 85,
    "branch": "EEE"
}

def display_student(student):

   print("Name:", student["name"])
   print("Marks:", student["marks"])
   print("Branch:", student["branch"])

display_student(student)

# problem 5:

student = {
    "name": "Rohan",
    "marks": 85
}

def calculate_grade(student):

    marks = student["marks"]

 
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    return grade

grade = calculate_grade(student)

print("Student:", student["name"])
print("Grade:", grade)

# problem 6:

def square(number):
    return number * number

answer = square(5)
print(answer)

# problem 7:

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_even(17)
print(result)

# problem 8:

def test():
    return "Hello"

result = test()
print(result)

# problem 9:

students = [
    {"name": "Rohan", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Anu", "marks": 67}
]

def get_grade(marks):

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "F"

        return grade

for student in students:
    
    grade = get_grade(student["marks"])

    print(student["name"], "-", grade)
