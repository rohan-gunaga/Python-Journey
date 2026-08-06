names = ["Rohan", "Satwik", "Tushar", "Bhavana"]
print(names)

# .append operation:
names.append("Rohit")
print(names)

# .pop operation:
names.pop(0)
print(names)

# .remove operation:
names.remove("Bhavana")
print(names)

# insert operation:
names.insert(1 , "Tanmay")
print(names)

# change operation:

names[2]= "Rohan"
print(names)

# Slicing operation:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[2:6])
print(numbers[2:4:1])
print(numbers[:4])
print(numbers[0::4])

# problem 1:

names = ["Aman", "Riya", "Kiran"]

# Add Any name
names.append("Rohan")

# remove any name
names.remove("Riya")

# print the final list
print(names)

# problem 2:
marks = [55, 65, 75, 90, 95]

# remove any element using pop()
removed_mark =marks.pop(2)

print("removed mark is:", removed_mark)
print("updated marks list is:", marks )