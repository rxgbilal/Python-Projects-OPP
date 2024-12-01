# for i in range(5):
#     print(i)

# # Example of a for loop
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# # Example of a while loop
# i = 0
# while i < 3:
#     j = 0
#     while j < 2:
#         print(i, j)
#         j += 1
#     i += 1

# # Using a boolean condition to control a loop
# number = 1
# while True:  # Infinite loop
#     print(number)
#     if number == 5:
#         break  # Exit the loop when number reaches 5
#     number += 1

# # Using boolean values in a for loop
# fruits = ["apple", "banana", "cherry", "date"]
# for fruit in fruits:
#     if fruit == "cherry":
#         break  # Exit the loop when "cherry" is found
#     print(fruit)

# Using lambda function with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Output: [1, 4, 9, 16, 25]
print(squared_numbers)
