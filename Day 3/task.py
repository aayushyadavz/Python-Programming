# 1. If Else 
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoater.")
# else:
#     print("You have to grow taller before you can ride.")

# 2. Modulo operator
# print(10 % 3)

# Task (i) - Check Odd or Even
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

# Task (ii) - Pizza Order Practice
# print("Welcome to Python Pizza Diliveries!")
# size = input("What size do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0

# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25
# else:
#     print("You typed the wrong inputs.")

# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}")

# 5. Logical Operators
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
#     elif age >= 45 and age <= 55:
#         bill = 0
#         print("Everything is ok. You can ride for free!")
#     else:
#         bill = 12
#         print("Please pay $12.")

#     want_photos = input("Do you want to have a photo take? Type y for Yes and n for No. ")
#     if want_photos == "y":
#         bill += 3

#     print(f"Your final bill is ${bill}")
# else:
#     print("You have to grow taller before you can ride.")

# Treasure Island Project
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go?\n Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake.\n Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("Gameover, You typed the wrong input.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")