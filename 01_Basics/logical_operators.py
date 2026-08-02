x = 5
y = 10
z = 15

# and operator
print (x < y and y < z)

# or operator 
print (x > 10 or z > 10)

# not operator 
print (not(x < 10))


# problem 1:

age = int(input("Enter your age: "))

print("Eligible to work?")
print(age >= 18 and age <= 60)

# problem 2:

maths_marks = int(input("Enter the maths marks: "))
science_marks = int(input("Enter the science marks: "))

print("pass?")
print(maths_marks >= 35)
print(science_marks >= 35)


