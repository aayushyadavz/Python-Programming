# 1. If Else 
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoater.")
# else:
#     print("You have to grow taller before you can ride.")

# 2. Modulo operator
# print(10 % 3)

# Task - Check Odd or Even
# number_to_check = int(input("What is the number you want to check?\n"
# ""))
# if number_to_check % 2 == 0:
#     print(f"{number_to_check} is even number.")
# else:
#     print(f"{number_to_check} is odd number.")
    
# 3. Nested Conditionals & elif
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoater.")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12.")
# else:
#     print("You have to grow taller before you can ride.")

# 4. Multiple if statements
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoater.")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         bill = 5
#         print("Please pay $5.")
#     elif age <= 18:
#         bill = 7
#         print("Please pay $7")
#     else:
#         bill = 12
#         print("Please pay $12.")

#     want_photos = input("Do you want to have a photo take? Type y for Yes and n for No. ")
#     if want_photos == "y":
#         bill += 3

#     print(f"Your final bill is ${bill}")
# else:
#     print("You have to grow taller before you can ride.")

# Task - Pizza Order Practice
print("Welcome to Python Pizza Diliveries!")
size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("You typed the wrong inputs.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")