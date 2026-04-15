# ================================================
# DAY 7 - Modules, Error Handling & Code Organization
# ================================================
# Goal: Learn how to organize code, handle errors, and use modules

print("=== Day 7 - Modules, Error Handling Started ===\n")

# 1. Using Built-in Modules
print("1. Using Python Built-in Modules:")

import math
import random
from datetime import datetime

print(f"Pi value: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Random number between 1-100: {random.randint(1, 100)}")

# Current date and time
now = datetime.now()
print(f"Current date & time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

# 2. Error Handling (Try - Except)
print("2. Error Handling:")

# Example 1: Division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero!")

# Example 2: Converting string to number
try:
    number = int("abc")        # This will cause error
except ValueError:
    print("❌ Error: Invalid number format!")

# Example 3: File not found
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("❌ Error: File not found!")

print("✅ Error handling examples completed.\n")

# 3. Creating Your Own Module (Best Practice)
print("3. Creating and Using Custom Module:")

# We will create a separate file called utils.py (see below)

# For now, let's simulate using a custom function
def calculate_age(birth_year):
    """Calculate age from birth year"""
    current_year = 2026
    return current_year - birth_year

def is_adult(age):
    """Check if person is adult"""
    return age >= 18

# Using our custom functions
age = calculate_age(2001)
print(f"Age calculated: {age} years")
print(f"Is adult? {is_adult(age)}")

print("\n=== Day 7 Completed Successfully! ===")

# ================================================
# EXTRA: How to create a real custom module (utils.py)
# ================================================
"""
Create a new file named: utils.py  (in the same folder)

# Content of utils.py:
def calculate_age(birth_year):
    return 2026 - birth_year

def greet_user(name):
    return f"Hello {name}, welcome to Python learning!"

def add_numbers(a, b):
    return a + b
"""

print("\nTip: In real projects, we put helper functions in separate files (modules).")