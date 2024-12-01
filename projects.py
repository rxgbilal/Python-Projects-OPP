# quiz game start
# print("welcome to my computer quiz")

# playing = input("do you want to play?: ")

# if playing.lower() != "yes":
#     quit()

# print("Okay!, lets play")
# score = 1

# answer = input("What does the CPU stand for?: ")
# if answer == "central processing unit":
#     print("correct")
#     score += 1
# else:
#     print("incorrect")
#     score -= 1
# print("you got " + str(score) + " marks")
#quiz game end
# # --------------------------------------------------------------------------------------------------

#guess game start
# import random

# top_of_range = input ("Type a number: ")
# if top_of_range.isnumeric():
#     top_of_range = int(top_of_range)

#     if top_of_range <= 0:
#         print("please type bigger number than 0")
#         quit()
# else:
#     print("please type a number")
#     quit()

# random_number = random.randint(0, top_of_range)
# print(random_number)

# while True:
#     print("you won!")
#     break
#guess game end
# # --------------------------------------------------------------------------------------------------

# rock, paper ,scissors game start
# import random

# user_wins = 0
# computer_wins = 0
# options = ["rock","paper","scissors"]

# while True:
#     user_input = input("play rock/paper/scissors or q to quit").lower()

#     if user_input == "q":
#         break

#     if user_input not in options:
#         continue

#     random_number = random.randint(0,2)
#     computer_pick = options[random_number]

#     print("computer pick", computer_pick + ".")

#     if user_input == "rock" and computer_pick == "scissors":
#         print("you won!")
#         user_wins += 1
#     elif user_input == "paper" and computer_pick == "rock":
#         print("you won!")
#         user_wins += 1
#     elif user_input == "scissors" and computer_pick == "paper":
#         print("you won!")
#         user_wins += 1
#     else:
#         print("you lost!")
#         computer_wins += 1

# print("the user won " + str(user_wins))
# print("the computer won " + str(computer_wins))
# print("goodbye!")
# rock, paper, scissors end 
# # --------------------------------------------------------------------------------------------------
# master_pwd = input("what is the master passsword? ")

# def view():
#     with open('password.txt','r') as f:
#         for line in f.readlines():
#             data = line.rstrip()
#             user, passw = data.split("|")
#             print("user: ",user,"password: ",passw)

# def add():
#     name = input("name: ")
#     pwd = input("password: ")

#     with open('password.txt','a') as f:
#         f.write(name+" | "+ pwd + "\n")

# while True:
#     mode = input("would you like to add a new password? or not: ")
#     if mode == "q":
#         break

#     if mode == "view":
#         view()

#     elif mode == "add":
#         add()
#     else:
#         print("invalid mode.")
#         continue
# # --------------------------------------------------------------------------------------------------
# import random

# def roll():
#     min_value = 1
#     max_value = 6
#     roll = random.randint(min_value,max_value)
#     return roll

# while True:
#     players = input("enter number of players (2-4)")
#     if players.isdigit():
#         players = int(players)
#         if  2 <= players <= 4:
#             break
#         else:
#             print("please enter the number from 2-4")
#     else:
#         print("please enter a number")

# max_score = 50
# player_score = [0 for _ in range(players)]

# while max(player_score) < max_score:
    
#     for player_idx in range(players):
#         print("\nplayer", player_idx + 1,"turn has started!\n")
#         current_score = 0

#         while True:
#              should_roll = input("whould you like to roll (y)?")
#              if should_roll.lower() != "y":
#                     break
             
#              value = roll()
#              if value == 1:
#                  print("you roll a 1! turn done!")
#                  current_score = 0
#                  break
#              else:
#                 current_score += value
#                 print("yoou roll a:", value)

#              print("your score is:", current_score)

#         player_score[player_idx] += current_score
#         print("your total score is:", player_score[player_idx])

# max_score = max(max_score)
# winning_idx = player_score.index(max_score)
# print("player number",winning_idx +1 ," is the winner", max_score)
# # ----------------------------------------------------------------------------------------------







# # Define a class named MyClass
# class MyClass:
#     # Define the constructor (__init__) method
#     def __init__(self, value):
#         self.value = value  # Initialize the 'value' attribute with the provided value

# # Create an instance of MyClass with the value 10
# obj = MyClass(10)

# # Access and print the value attribute of the instance
# print(obj.value)  # Output: 10

# # # ----------------------------------------------------------------------------------------------

# def create_instance(value):
#     return {'value': value}

# # In the second code snippet, obj is not an object in the object-oriented programming sense. 
# # It's a dictionary returned by the create_instance function. 
# # In Python, we typically reserve the term "object" for instances of classes or instances of
# #  built-in types like lists, dictionaries, etc.

# # So, in the second code snippet, obj is a dictionary, not an object in the OOP sense.
# obj = create_instance(12)

# # Access and print the value attribute of the instance
# print(obj['value'])  # Output: 12




# class person:
#     def __init__(self, name, a):
#         self.name = name
#         self.age = a
        
# e1 = person("bilal", 18)
# print(e1.name)



# def ass(n, a):
#     name = n 
#     return n, a

# print(ass("bilal",18))









class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Initializing Vehicle of brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        self.model = model
        print(f"Initializing Car of brand: {brand}, model: {self.model}")
        super().__init__(model)  # Call parent class constructor

car = Car("Toyota", "Camry")





