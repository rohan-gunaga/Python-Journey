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