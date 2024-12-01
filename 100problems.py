# User will input (3ages).Find the oldest one!

# age1 = int(input("please enter your age1: "))
# age2 = int(input("please enter your age2: "))
# age3 = int(input("please enter your age3: "))

# if age1 > age2 and age3:
#     print("age1 is eldest")

# elif age2 > age1 and age3:
#     print("age2 is greater")
# else:
#     print("age 3 is greater")

# set method

# age1 = int(input("Please enter your age: "))
# age2 = int(input("Please enter your age: "))
# age3 = int(input("Please enter your age: "))

# ages = {age1, age2, age3}
# eldest = max(ages)
# print(f"The eldest age is: {eldest}")
# print(ages)

# loop + list method

# ages = []
# for i in range(5):
#     age = int(input("Please enter your age: "))
#     ages.append(age)

# eldest = max(ages)
# print(f"The eldest age is: {eldest}")

# # # ----------------------------------------------------------------------------------------------

# Write a program that will convert celsius value to fahrenheit

# Celcius = int(input("Enter the temperature in Celcius and we will convert into feherenhite: "))
# feherenhite = Celcius*33.8
# print(feherenhite)

# function method 

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter the temperature in Celsius and we will convert it to Fahrenheit: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"The temperature in Fahrenheit is: {fahrenheit}")



