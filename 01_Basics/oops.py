# problem 1:

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee1 = Employee("Rohan", 30000)

print(employee1.name)
print(employee1.salary)

# problem 2:

class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self):
        
        self.salary = self.salary + 5000

employee1 = Employee("Rohan", 30000)

employee1.increase_salary()

print(employee1.salary)

# problem 3:

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self):
        self.salary = self.salary + 5000

employee1 = Employee("Rohan", 30000)
employee2 = Employee("Rahul", 40000)

employee1.increase_salary()

print(employee1.name, "-", employee1.salary)
print(employee2.name, "-", employee2.salary)

# problem 4:

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_bonus(self, amount):
        self.salary = self.salary + amount

    def display(self):
        print(f"Name:{self.name}")
        print(f"Salary:{self.salary}")

employee1 = Employee("Rohan", 30000)

employee1.give_bonus(5000)

employee1.display()

# problem 5:

class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed = self.speed + amount


car1 = Car("Toyota", 60)

car1.accelerate(20)

print(car1.brand)
print(car1.speed)

