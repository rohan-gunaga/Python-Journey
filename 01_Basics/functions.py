def greet():
    print("Hello bro!")

greet()

def welcome():
    print("welcome to python journey!")

welcome()


# problem 1:

def greet():
    print("oh! bhrame")

greet()
greet()
greet()
greet()

# problem 2:

def tables(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

tables(5)
print()
tables(6)
print()
tables(7)

# problem 3:

def cricket(batsman, bowler):
    print(f"Batsman is {batsman}")
    print(f"Bowler is {bowler}")
    print(f"{batsman} hit a six aginst {bowler}")

cricket("Virat Kohli","mitchel starc")

# problem 4:

def greet():
    print("Hello, Rohan!")

greet()

# problem 5:

def add(a, b):
    print(a + b)

add(10, 20)

# problem 6:

def square(number):
    return number * number

result = square(5)
print(result)

# problem 7:

def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(check_even(10))
print(check_even(7))

# problem 8:

def find_max(a, b):
    if a > b :
        return a
    else:
        return b

print(find_max(10, 25))
print(find_max(50, 20))

# problem 9:

numbers = [10, 20, 30, 40]

def sum_list(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total 

print(sum_list(numbers))

# problem 10:


def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count = count + 1
    return count
    
numbers = [2, 5, 8, 11, 14, 17, 20]

print(count_even(numbers))

