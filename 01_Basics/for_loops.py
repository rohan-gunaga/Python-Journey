# for_loops

for i in range(1, 6):
    print(i)


# problem 1:

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)

# problem 2:

total = 0

for i in range(1,11):
    total = total + i

print(total)

# problem 3:

students = ["Rohan", "Rahul", "Anjali", "Kiran"]

for student in students:
    print(student)


# problem 4:

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)

# problem 5:

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number*2)

# problem 6:

numbers = [5, 10, 15, 20, 25]

for number in numbers:

    if number > 10:
        print(number)

 # problem 7:

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        print(number)

# problem 8:

numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total = total + number

print(total)

# problem 9:

numbers = [3, 7, 2, 9, 4]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)

# problem 10:

numbers = [3, 7, 2, 9, 4]
count = 0

for number in numbers:
    if number % 2 == 0:
        count = count + 1

print(count)
        
# problem 11:

numbers = [2, 5, 8, 11, 14]

total = 0

for number in numbers:
    if number % 2 == 0:
     total = total + number

print(total)
