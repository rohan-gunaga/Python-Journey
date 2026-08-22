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
