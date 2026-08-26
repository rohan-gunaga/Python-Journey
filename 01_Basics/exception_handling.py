# problem 1:

try: 
    age = int(input("enter your age: "))
    print("your age is", age)

except ValueError:
    print("please enter a valid age.")


# problem 2:

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

try:
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

# problem 3:
try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    result = num1 / num2
    print("Result", result)

except ValueError:
    print("please enter valid number.")

except ZeroDivisionError:
    print("cannot divide by zero.")

# problem 4:
try:
    num = int(input("enter the number: "))

    result = 100 / num
    print("Result", result)

except ValueError:
    print("please enter valid number.")

except ZeroDivisionError:
    print("cannot divide by zero.")

finally:
    print("Calculation Completed.")



