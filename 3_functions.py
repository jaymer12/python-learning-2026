# ================================================
# DAY 3 - Functions in Python
# ================================================
# Goal: Learn how to create and use functions

print("=== Day 3 - Functions Started ===\n")

# 1. Simple Function (No parameters)
def greet():
    print("Hello from Regina!")
    print("Welcome to Day 3 of Python learning.")

# Call the function
greet()
print()   # empty line

# 2. Function with Parameters
def greet_person(name, city="Regina"):
    print(f"Hello {name}!")
    print(f"How is the weather in {city} today?")

# Calling the function with arguments
greet_person("JAY")
print()
greet_person("Sarah", "Saskatoon")
print()

# 3. Function with Return Value
def add_numbers(a, b):
    result = a + b
    return result

sum1 = add_numbers(10, 15)
print(f"Sum of 10 + 15 = {sum1}")

sum2 = add_numbers(45, 27)
print(f"Sum of 45 + 27 = {sum2}\n")

# 4. Function with Default Value
def calculate_age(birth_year, current_year=2026):
    age = current_year - birth_year
    return age

print(f"My age is {calculate_age(2001)}")
print(f"My friend's age is {calculate_age(1998, 2026)}\n")

# 5. Practical Example - Todo List Helper
def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Task added: {new_task}")
    return tasks

# Using the function
my_tasks = ["Learn Python", "Practice Git"]
my_tasks = add_task(my_tasks, "Build FastAPI project")
my_tasks = add_task(my_tasks, "Push code to GitHub")

print("\nMy current tasks:")
for task in my_tasks:
    print(f"- {task}")

print("\n=== Day 3 Completed Successfully! ===")