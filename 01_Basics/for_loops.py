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

# problem 12:

numbers = [5, 12, 7, 20, 3, 18]
count = 0
for number in numbers:
    if number > 10:
        count = count + 1

print(count)

# problem 13:

numbers = [2, 4, 6, 8, 10]

for number in numbers:
    square = number * number
    print(square)

# problem 14:

numbers = [3, 6, 9, 12, 15]
sum = 0
for number in numbers:
    if number % 3 == 0:
        sum = sum + number

print(sum)

# problem 15:

numbers = [4, 7, 10, 13, 16, 19]

for number in numbers:
    if number % 2 != 0:

        print(number)

# problem 16:

numbers = [5, 10, 15, 20, 25]

for number in numbers:
    if number % 5 == 0:
        print(number)

# problem 17:

numbers = [2, 5, 8, 11, 14, 17, 20]
count = 0

for number in numbers:
    if number % 2 != 0:
        count = count + 1

print(count)

# problem 18:

numbers = [4, 8, 12, 16, 20]
total = 0
for number in numbers:
    total = total + number

average = total / 5 
print(average)

# problem 19:

for i in range(20, 1, -2):
    print(i)

# problem 20:

total = 0
for i in range(1, 11):
    total = total + i

print(total)

# problem 21:

total = 0

for i in range(1,21):
    if i % 2 == 0:
        total = total + i

print(total)

# problem 22:

count = 0

for i in range(1, 21):
    if i % 2 == 0:
        count = count + 1

print(count)

# problem 23:

count = 0

for i in range(1, 31):
    if i % 2 != 0:
        count = count + 1

print(count)

# problem 24:

for i in range(1, 11):
    table = 7 * i

    print(table)

# problem 25:
total = 0
for i in range(1, 31):
    if i % 3 == 0:
        total = total + i

print(total)

# problem 26:

numbers = [12, 45, 7, 89, 23, 56]


largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)

# problem 27:

numbers = [34, 12, 56, 7, 89, 23]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(smallest)

# problem 28:

numbers = [12, 67, 45, 89, 23, 56, 34, 91]

count = 0

for number in numbers :
    if number > 50:
        count = count + 1

print(count)

# problem 29:

numbers = [12, 67, 45, 89, 23, 56, 34, 91]

total = 0

for number in numbers:
    if number > 50:
        total = total + number

print(total)

# problem 30:

numbers = [-5, 10, -2, 8, 0, -7, 15, 3]
count = 0

for number in numbers:
    if number > 0:
        count = count + 1

print(count)