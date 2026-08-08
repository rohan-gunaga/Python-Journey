# tuples and sets 

genders = ("male", "female","others")
print(genders[1:3])

# tuple concatenation 

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

# tuple repetation 

repeated_tuple = (1, 2)*3
print(repeated_tuple)

# tuple methods
items = (6, 7, 4, 8, 1, 9, 3, 6, 4, 2, 6)
print(items.count(6))
print(items.index(4))

# Sets
s = {11, 26, 3}
print(s)

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 | s2) 
print(s1 & s2)

# set methods
s = {1, 2, 3, 4, 5}

s.add(6)
s.remove(2)
s.discard(3)

print(s)

a = s.pop()
print(a)