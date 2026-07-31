age = input("Age: ")

print(age)

boy_name = input("Boy_Name: ")
boy_age = int(input("Boy_Age: "))
girl_Name = input("Girl_Name: ")
girl_age = int(input("Girl_Age: "))

age_diff = abs(boy_age - girl_age)

print(boy_name + " loves " + girl_Name + ". Age_difference is " + str(age_diff))

print(f"{boy_name} loves {girl_Name}. Age_difference is {age_diff}")