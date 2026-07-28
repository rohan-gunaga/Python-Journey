a = 14
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print(a*b+b-a**b)






# swaaping problem 
a = 10
b = 20

# program: 

print("before Swapping")
print("a =", a)
print("a =", b)

temp = a 
a = b
b = temp 

print ("After swapping")
print ("a=", a)
print ("b=", b)




# Arithmetic Operators problem

balance = 5000
deposit = 2000
withdraw = 1500
friends = 3


# 1. Deposit amount add madu (+)

# 2. Withdraw amount subtract madu (-)

# 3. Suppose bank offers 2x reward points for every ₹1000 deposited.
#    Reward points = deposit * 2

# 4. Calculate each friend's share using division (/)

# 5. Find whole amount each friend gets using floor division (//)

# 6. Find remaining money after equal distribution using modulus (%)

# 7. Find bonus using exponent (**)
#    Example: 2 ** friends


# solution :

balance_after_deposit = balance + deposit

final_balance = balance_after_deposit - withdraw

share = final_balance / friends

whole_share = final_balance // friends

remaining = final_balance % friends 

reward = deposit * 2

bonus = 2 ** 3

print(balance_after_deposit)
print(final_balance)
print(share)
print(whole_share)
print(remaining)
print(reward)
print(bonus)


# problem 3 

salary = 45000
bonus = 5000
tax = 3500
family_members = 4

incrimented_salary = salary + bonus 

final_salary = incrimented_salary - tax

share = final_salary / family_members

whole_share = final_salary // family_members

remaining_amount = final_salary % family_members

bonus_times_3 = bonus * 3 

power = 2 ** family_members 

print("incrimented_salary:", incrimented_salary)
print("final_salary:",final_salary)
print("share:", share)
print("whole_share:", whole_share)
print("remaining_amount", remaining_amount)
print("bonus_times_3:", bonus_times_3)
print("power:", power)