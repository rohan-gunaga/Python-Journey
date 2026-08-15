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