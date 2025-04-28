# 1.Subscripting
# print("Ayush"[0]) 
# print("Ayush"[-1]) # Get hold of the last character in the string 

# 2. Integar - Whole number
# print(123 + 345)
# Large Integars - eg. 123,456,789
# print(123_456_789) # commas replaced with "_" in python 

# 3. Float - floating point number
# print(3.14159) 

# Boolean
# print(True)
# print(False)

# Note: The len() function takes arguments such as strings.

# 4. Type checking
# print(type("xyz"))
# print(type(123))
# print(type(True))
# print(type(3.2))

# 5. Type conversion
# print(int("123") + int("456"))
# print(int("abc") + int("456")) # ValueError
# Other -
str()
float()
bool()

# Task (i) - print("Number of letters in your name: " + len(input("Enter your name")))
# print("Number of letters in your name: " + str(len(input("Enter your name"))))

# 6. Mathematical Operations
# print(123 + 456)
# print(7 - 3)
# print(3 * 2)
# print(6 / 3) # 2.0
# print(6 // 3) # 2

# Be careful
# print(5 / 3) # 1.6666666666666667
# print(5 // 3) # 1

# print(2 ** 3) # 2 to the power of 3

# (i) PEMDAS - Parentheses, Exponents, Multiplication/Divison, Addition/Substraction
# ()
# **
# * OR /
# + OR -

# Task (ii) - What is the output of this code:
# print(3 * 3 + 3 / 3 - 3) # 7.0

# Task (iii) - Change the code so it output 3
# print(3 * (3 + 3) / 3 - 3) # 3.0

# 7. Number Manipulation
bmi = 84 / 1.65 ** 2
# print(bmi) # 30.85399449035813

# Flooring a number:
# print(int(bmi)) # 30

# Rounding a number:
# print(round(bmi)) # 31, because bmi value is more than 30.5
# print(round(bmi, 2)) # 30.85

# (i) - Assignment Operators: +=, -=, *=, /=
score = 0
# score = score + 1 # intead of doing this
score += 1 # we can do this
# print(score)

# 8. f-strings
score = 0
height = 1.8
is_winning = True
# print("Your score is " + str(score) + ", your height is " + str(height) +  ". You are winning is " + str(is_winning)) # instead of doing this
print(f"Your score is {score}, your height is {height}. You are winning is {is_winning}")