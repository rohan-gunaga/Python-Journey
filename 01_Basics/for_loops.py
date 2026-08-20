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


# problem 31:

numbers = [2, 5, 9, 4, 7, 8, 3]

for number in numbers:
    if number == 7:
        print("found 7")
        break

# problem 32:

numbers = [10, 25, 34, 18, 7, 42, 15]

for number in numbers:
    print(number)
    if number == 7:
        break

# problem 33:

numbers = [4, 8, 12, 16, 20, 25, 30]

for number in numbers:
    if number > 20:
        print("limit reached")
        break
    
    print(number)

# problem 34:

numbers = [1, 2, 3, 4, 5, 6, 7]

for number in numbers:
    if number % 2 == 0:
        continue

    print(number)

# problem 35:

numbers = [10, 15, 20, 25, 30, 35, 40]

for number in numbers:
    if number % 10 == 0:
        continue
    print(number)

# problem 36:

numbers = [5, -2, 8, -7, 10, -3, 15]

for number in numbers:
    if number < 0:
        continue
    print(number)

# problem 37:

for i in range(3):
    for j in range(3):
        print(1, end=" ")
    print()


# problem 38:

for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()

# problem 39:

for i in range(1, 4):
    for j in range(1, i + 1):
                  
        print(j, end=" ")
    print()

# problem 40:

for i in range(1, 4):
    for j in range(i): 
        print(i, end=" ")
    print()

# problem 41:
number = 1

for i in range(1, 4):
    for j in range(i): 
        print(number, end=" ")
        number = number + 1
    print()

# problem 42:

for i in range(1, 4):
    for j in range(3):
        print("*", end=" ")
    print()

# problem 43:

for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()

# problem 44:

for i in range(1, 4):
    for s in range(3 - i):
        print(" ", end="")

        
    for j in range(i):
        print("*", end=" ")
    print()

# problem 45:

for i in range(1, 4):
    for j in range(4 - i):
        print("*", end=" ")
    print()

# problem 46:

for i in range(1, 4):
    for s in range(3 - i):
        print(" ", end="")

    for j in range(i):
        print("*", end=" ")
    print()

for i in range(1, 3):
    for s in range(i):
        print(" ", end="")

    for j in range(3 - i):
        print("*", end=" ")
    print()

# problem 47:
print()
for i in range(1, 4):
    for s in range(i - 1):
        print(" ", end="")

    for j in range(4 - i):
        print("*", end=" ")
    print()

for i in range(2, 4):
    for s in range(3 - i):
        print(" ", end="")

    for j in range(i):
        print("*", end=" ")
    print()

# problem 48:

for i in range(1, 4):
    # 1. Increasing loop (1 to i)
    for j in range(1, i + 1):
        print(j, end=" ")
        
    # 2. Decreasing loop (i - 1 down to 1)
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
        
    print()

# problem 49:

numbers = [12, 5, 8, 21, 16, 7, 30]

for number in numbers:
    if number % 2 != 0:
        continue
    print(number)

# problem 50:

numbers = [10, 25, 8, 42, 15, 30, 7]

for number in numbers:
    if number <= 20:
        continue
    print(number)

# problem 51:

numbers = [5, 12, -3, 18, -7, 25, 10]

for number in numbers:
    if number < 0:
        continue

    print(number)

    if number == 25:
        break
    
# problem 52:

numbers = [3, 8, 15, 22, 7, 30, 11, 40]

for number in numbers:
    if number % 2!= 0:
        continue

    print(number)

    if number > 20:
        break

# problem 53:

numbers = [12, -5, 8, 0, 15, -3, 20, 7]

for number in numbers:
    if number < 0:
        continue
    
    if number == 0:
        break

    print(number)

# problem 54:

for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# problem 55:

for i in range(1, 6):
    for j in range(1, 7 - i):
       print(j, end="")
    print() 

# problem 56:
number = 1

for i in range(1, 5):
    for j in range(i):
        print(number, end="")
        number = number + 1
    print()

# problem 57:

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()

# problem 58:

for i in range(1, 6):
    for s in range(5 - i):
        print(" ", end="")

    for j in range(i):
        print("*", end="")
    print()

# problem 59:

for i in range(1, 6):
    for s in range(5 - i):
        print(" ", end="")
    for j in range(2 * i - 1 ):
        print("*", end="")
    print()

# problem 60:

for i in range(1, 6):
    for s in range(5 - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print(j, end="")
        
    print()

# problem 61:

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# problem 62:

for i in range(1, 6):
    for j in range(1, 11):
        print( i, "x" , j, "=", i*j)
    print()
    