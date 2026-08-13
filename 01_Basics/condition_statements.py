# If statement 

x = 21

if x%2==0:
    print("x is even")
else:
    print("x is odd")


# if-elif-else
signal = "yellow"

if signal =="red":
    print("STOP")
elif signal =="yellow":
    print("READY")
else:
    print("GO")

# problem 1:

age = 18 

if age>=18:
    print("student eligible for voting")
else:
    print("student is not eligible for voting")

# problem 2:

att = 65
is_teacher_friend = False

if att>=75 or is_teacher_friend:
    print("EXAM")
else:
    print("NO EXAM")

# problem 3:

gender = input("gender:")
age = int (input("age:"))

if gender=="female":
    print("Ticket is free")
else:
    if age < 5:
        print("Ticket is free")
    elif age <= 12:
        print("You get a child discount.")
    elif age >= 60:
        print("You get a senior citizen discount.")
    else:
        print("You pay the full fair")


# problem 4:

marks = int(input("marks:"))

if marks>=40:
    print("The student is pass")
else:
    print("The student is fail")

# problem 5:

a = 25
b = 42

if a > b:
    print(a)
else:
    print(b)

# problem 6:

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

# problem 7:

a = 20 
b = 5 
operator = "*"

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("invalid operator")
 
