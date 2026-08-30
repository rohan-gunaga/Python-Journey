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
                              
