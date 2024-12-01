# #1# variable
# #*# string data type

# name = "bro" # --> this term is called variable
# print( "hello" + name)
# print(type(name))

# # common practice
# # always use _ as gap. for example First_name
# # string can not be used in any sort of math
# # string is denoted by ""

# #*# int data type

# age = 21
# aged = age + 1
# print(aged)
# # or 
# age = 21
# age = age + 1
# print(age)
# print(type(age))

# # to display both string and int
# print("Your age is " + str(age))
# # we convert int age into string to print the desired value
# # int is used for calculations 

# #*# float data type
# # float is used to store and print decimal values
# height = 250.5
# print(height)
# print(type(height))
# # to display both string and float
# print("Your height is " + str(height))
# # we convert float height into string to print the desired value

# #*# boolean
# # true or false
# human = False
# print(human)
# print(type(human))
# # to display both string and boolean
# print("Your height is " + str(human))
# # we convert boolean human into string to print the desired value
# # we use this mostly in if else statement

# #*# multiple assigment = allows us to assign multiple variables at the same time in one line of code
# name , age , attractive = "Bilal" , 18 , True
# print(name)
# print(age)
# print(attractive)
# bilal = age = 18
# print(bilal)
# print(age)
# # --------------------------------------------------------------------------------------------------

# #2#string methods 

# name="bro"
# print(len(name))
# print(name.find("b"))
# print(name.capitalize())
# print(name.lower())
# print(name.upper())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o", "a"))
# print(name*3)
# # --------------------------------------------------------------------------------------------------

# #3# type cast = convert the data type of the value to another data type.

# x = 2
# y = 3.4
# z = "3"
# p = 4.4

# y = int(y)
# z = int(z)


# print(x)
# print(y)
# print(z*3)
# print(p*4)
# # --------------------------------------------------------------------------------------------------

# #4# user input

# name = input("what is your name?: ")
# age = int(input("what is your age?: "))
# height = float(input("what is your height?: "))
# print("hello " + name +",your age is "+ str(age) + " and your height is "+ str(height))
# # --------------------------------------------------------------------------------------------------

# #5# math funcations
# import math

# pi = 3.13
# x=1
# y=2
# z=3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi ,2))
# print(math.sqrt(pi))
# print(max(x,y,z))
# print(min(x,y,z))
# # # --------------------------------------------------------------------------------------------------

# #6# string slicing = create a substring by extracting elements from another string indexing[] or slice() [start:stop:step]

# name = "bro code"
# first_name = name[0:2]
# funky_name = name[0:8:2]
# print(first_name)
# print(funky_name)

# website = "www.google.com"

# slice =  slice(4, -4)
# print(website[slice])
# # # --------------------------------------------------------------------------------------------------

# #7# if statemant 

# age = int(input("what is your age?: "))
# if age >= 18:
#     print("you are an adult")
# elif age < 0:
#     print("you are not born yet")
# else:
#     print("you are a child")
# # # --------------------------------------------------------------------------------------------------

#8#  logical operators (and,or,not) = used to cheak if two or more conditional statement is true

# temp = int(input("what is the temperature? "))

# if not(temp >= 0 and temp <= 30):
#     print("the temperature is good today")
# elif not(temp <0 and temp > 30):
#     print("temperature is not good today")
# # # --------------------------------------------------------------------------------------------------

#9# while loop = (unlimited) a statement that will execute it's block of code, as long as it's condition remains true

# name = ""
# while len(name) == 0:
#          name = input("enter your name: ")
# print("hello" + name)
# # same but different writing method
# name = None
# while not name:
#          name = input("enter your name: ")
# print("hello" + name)
# # # --------------------------------------------------------------------------------------------------

# #10# for loop = limited

# for i in range(10):
#     print(i+1)

# for i in range(50,100+1,2):
#     print(i)
# # # --------------------------------------------------------------------------------------------------

# #11# nested loop = one loop inside an another loop

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end ="")
#     print()
# # # --------------------------------------------------------------------------------------------------

# #12# loop control statement = change a loops execution from its normal sequence

# # break = used to terminated the loop entirely.
# # continue = skips to the next iteration of the loop.
# # pass = does nothing, acts as placeholder.

# while True:
#     name = input("enter your name: ")
#     if name != "":
#         break
# # # --------------------------------------------------------------------------------------------------

# #13# list = used to store multiple items in single variable

# food = ["pizza", "hamburger", "hotbog", "spaghetti", "pudding"]

# food[0] = "sushi"

# food.append("ice cream")
# # many more

# for x in food:
#     print(x)
# # 2d list = a list of lists

# drinks = ["coffe", "water", "cola"]
# dinner = ["pizza" , "hamburger", "tanks"]
# fooood = [drinks, dinner, food]
# print(fooood[0][2])
# # # --------------------------------------------------------------------------------------------------

# #14# tuple = collection which is ordered and unchangeable used to group together related data

# student = ("bro",18,"male")

# print(student.count("male"))

# for x in student:
#     print(x)

# if "bro" in student:
#     print("bro is here")
# # # --------------------------------------------------------------------------------------------------

# #15# set = collection which is unordered, unindexed. no duplicate values

# utensils = {"fork","spoon","knife"}
# dishes = {"bowl", "plate","cup", "knife","knife"}

# utensils.clear()
# utensils.update(dishes)

# for x in utensils:
#     print(x)

# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))
# # # --------------------------------------------------------------------------------------------------

# #16# dictonary = a changable, unordered collection of unique key: values pairs fast because they use hashing, allow us to access a value quickly

# capitals = {'USA':'Washinton DC',
#             'India':'New Dehli',
#             'Russia':'Moscow'}
# capitals.update({'USA': 'las vages'})

# # print(capitals['Russia']) --> not recommened method in dictonary
# print(capitals.get('germany'))
# print(capitals.values())

# for key,value in capitals.items():
#     print(key,value)
# # key: value
# # # --------------------------------------------------------------------------------------------------

# #17# index operator [] = gives access to a sequence's element (str,list,tuples) 

# name = "BRO"

# if(name[0].islower()):
#     print(name)

# name1 = "bro Code"

# if(name1[0]):
#     name1 = name1.lower()
#     name1 = name1.capitalize()
#     last_name = name1[1:].upper()
# print(name1)
# print(last_name)
# # # --------------------------------------------------------------------------------------------------
    
# #18# function = a block of code whooch is executed only when it is called.

# def hello(name,work,age):
#     print("test "+ name +" "+ work +" "+ str(age))

# hello("bro", "hello", 21)
# # # --------------------------------------------------------------------------------------------------

# #19# return statement = send values/objects back to the caller

# def multiply(number1, number2):
#     result = number1 * number2
#     return result

# print(multiply(6,10))
# # # --------------------------------------------------------------------------------------------------

# #18# keyboard argument 

# def hello(first,middle,last):
#     print("hello " +first+ " "+ middle+ " "+ last)

# hello(last="bro",middle="dude",first="code")
# # # --------------------------------------------------------------------------------------------------

# #19# nested function call 

# print(round(abs(float(input("Enter a whole positive number: ")))))
# # # --------------------------------------------------------------------------------------------------

# #20# scope global and local variable = global means outside the function and local means inside the function

# def display_name():
#     name = "code"
#     print(name)

# display_name()
# # # --------------------------------------------------------------------------------------------------

# #21# *args  = paramiter that will pack all arguments into a tuple.

# def add(*stuff):
#     sum = 0
#     for i in stuff:
#         sum += i
#     return sum
    
# print(add(1,2,3,4,5,6))
# # # --------------------------------------------------------------------------------------------------

# #22# **kwargs = paramiter that will pack all arguments into a dictonary.

# def hello(**stuff):
#     # print("hello "+ kwargs['first']+" "+ kwargs['last'])
#     print("hello", end = " ")
#     for key,value in stuff.items():
#         print(value, end=" ")

# hello(title="mister",first="bro",middle="dude",last="code")
# # # --------------------------------------------------------------------------------------------------

# #23# string format = gives more control when displaying output

# animal = "cow"
# item = "moon"

# print("the {} jumped over {}".format(animal,item))
# print("the {1} jumped over {0}".format(animal,item))
# print("the {test} jumped over {gone}".format(test="animal",gone="item"))

# name = "bro"

# print("hello my name {0:10}.nice to meet you".format(name))

# number = 3.1234

# print("the number of pi {:.2f}".format(number))
# # # --------------------------------------------------------------------------------------------------

# #24# random numbers
# import random
 
# x = random.randint(1,6)
# y = random.random()

# my_list = [1,2,3,"me","you","love"]
# z = random.choice(my_list)
# print(z)
# print(x)
# print(y)
# cards = [1,2,3,"me","you","love"]
# random.shuffle(cards)
# print(cards)
# # # --------------------------------------------------------------------------------------------------

# #25# exception handiling
 
# try:
#     numenator = int(input("please enter numenator"))
#     denomenator = int(input("please enter denomenator"))
#     result = numenator/denomenator
#     print(result)
# except ZeroDivisionError:
#     print("you are an idiot! can not divide by zero")
# except ValueError:
#    print("Enter only number please")
# finally:
#     print("this will always excecute")
# # # --------------------------------------------------------------------------------------------------

# class person:
#     name = "harry"
#     occupation = "software developer"
#     networth = 10
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a = person()
# b = person()

# a.name = "shubham"
# a.occupation = "accounant"

# a.info()
# b.info()
# name = "bro"
# def display_name():
#     global name
#     name = "code"
#     print(name)

# display_name()




