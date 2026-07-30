first_name = "Rohan"
last_name = "Gunaga"

full_name = first_name + " " + last_name

print(full_name)

message = "Warning! "*10
print(message) # print(messege*10)

# String Methods:

print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("Warning", "Error"))


name = '''Rohan said "hello"
        virat said "hi"'''
print (name)

print(len(name))

name = "Rohan"

print(name[2]) 
print(name[2:4])
print(name[2:])
print(name[:4])
print(name[-2])
print(name[::2])
print(name[-4:2])