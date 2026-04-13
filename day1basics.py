# ================================================
# DAY 1 - Python Basics
# ================================================
# Goal: Learn variables, data types, f-strings, and input()

print("=== Day 1 - Python Basics Started ===\n")

# 1. Variables - Storing data
name = "JAY"                    # String (text)
age = 25                        # Integer (whole number)
height = 5.8                    # Float (decimal number)
is_student = True               # Boolean (True or False)

print("1. Variables Example:")
print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My height is {height} feet")
print(f"Am I a student? {is_student}\n")

# 2. Basic Data Types
print("2. Data Types:")
print(f"name is type: {type(name)}")
print(f"age is type: {type(age)}")
print(f"height is type: {type(height)}")
print(f"is_student is type: {type(is_student)}\n")

# 3. f-strings (Formatted Strings) - Very Important!
print("3. f-string Examples:")
city = "Regina"
province = "Saskatchewan"

print(f"Hello, my name is {name} and I live in {city}, {province}.")
print(f"Next year I will be {age + 1} years old.")
print(f"Double my age is {age * 2}\n")

# 4. Getting input from user
print("4. Using input() function:")

# Ask user for their name
user_name = input("What is your name? ")

# Ask user for their age (input always returns string, so we convert it)
user_age = int(input("How old are you? "))

print(f"\nNice to meet you, {user_name}!")
print(f"You are {user_age} years old.")
print(f"You will be {user_age + 5} years old in 5 years.\n")

# 5. Simple Calculations
print("5. Simple Math Examples:")
num1 = 10
num2 = 3

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} raised to power {num2} = {num1 ** num2}")

print("\n=== Day 1 Completed Successfully! ===")