
# problem 1:

numbers = [2, 4, 6, 8, 10]

triples = [number * 3 for number in numbers ]

print(triples)

# problem 2:

numbers = [5, 12, 7, 20, 3, 18, 9, 30]

number_list = [number for number in numbers if number > 20]

print(number_list)

# problem 3:

numbers = [5, 12, 7, 20, 3, 18, 9, 30]

numbers_list = [number * 2 for number in numbers if number % 2 == 0]

print(numbers_list)

# problem 4:

names = ["Rohan", "rahul", "Kiran", "arjun", "Ravi", "ananya"]

new_list = [name for name in names if name.startswith("R")]

print(new_list)

# problem 5:

numbers = [1, 2, 3, 4, 5]

squares = {number: number ** 2 for number in numbers}

print(squares)

# problem 6:

names = ["Rohan", "Rahul", "Kiran"]

name_length = {name: len(name) for name in names}

print(name_length)