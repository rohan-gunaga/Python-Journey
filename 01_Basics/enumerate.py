# problem 1:

names = ["Rohan", "Rahul", "Kiran", "Arjun"]

for index, name in enumerate(names, start=1):
    print(index,".", name)

# problem 2:

names = ["Rohan", "Rahul", "Kiran", "Arjun"]

ages = [20, 21, 19, 22]

for name, age in zip(names, ages):
    print(f"{name} - {age}")

# problem 3(zip):

names = ["Rohan", "Rahul", "Kiran", "Arjun"]
marks = [85, 62, 91, 45]

for name, mark in zip(names, marks):
    if mark > 60:
        print(f"{name} - {mark}")

# problem 4(lambda):

multiply = lambda a, b: a * b 

print(multiply(5, 4))

