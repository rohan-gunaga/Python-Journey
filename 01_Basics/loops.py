# while loop

is_failed = True
i = 1

while is_failed:
    if i%2!=0:
        i = i + 1
        continue

    print(f"Attempt {i}")
    i = i + 1
    if i>100:
       break

print("I gave up!")


# problem 1:

i = 0

while i<=10:
    print(i)
    i += 1

# problem 2:

pin = "2026"
trials = 0

while trials<3:
    input_pin = input(f"Trail-{trials} | PIN:")
    trials += 1
    if input_pin == pin:
        print("CORRECT")
        break
    else:
        print("INCORRECT")


# Basic while loop problems:

  # problem 1:

i = 1

while i <= 10:
    print(i)
    i += 1

# problem 2:

i = 10

while i >= 1:
    print(i)
    i = i - 1

# problem 3:
print ("START")
i = 2

while i <= 20:
    print(i)
    i = i + 2

print("END")

# problem 4:

i = 1
total = 0

while i <= 10:
    print(i)
    total = total + i 
    i = i + 1

print(total)

# problem 5:

i = 20


while i >= 2:
    print(i)

    i = i - 2

# problem 6:

i = 1
count = 0

while i <= 10:
    print(i)
    count = count + 1
    i = i + 1

print(count)

# problem 7:

i = 1
count = 0

while i <= 10:
    if i % 2 == 0:
        count = count + 1
    i = i + 1
print(count)

# problem 8:

i = 5 

while i <= 15:
    print(i)
    i = i + 1