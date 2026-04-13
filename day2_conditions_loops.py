# ================================================
# DAY 2 - Operators, Conditions and Loops
# ================================================
# Goal: Learn comparison operators, if conditions, and loops

print("=== Day 2 - Conditions and Loops Started ===\n")

# 1. Comparison Operators
print("1. Comparison Operators:")
a = 10
b = 5

print(f"{a} > {b}  → {a > b}")
print(f"{a} < {b}  → {a < b}")
print(f"{a} == {b} → {a == b}")
print(f"{a} != {b} → {a != b}")
print(f"{a} >= {b} → {a >= b}")
print(f"{a} <= {b} → {a <= b}\n")

# 2. If - Elif - Else Conditions
print("2. Conditional Statements:")

age = 20

if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("You can get a learner's driving license.")
else:
    print("You are too young for these things.")

print()  # empty line

# Example with user input
temperature = int(input("Enter the temperature in Regina today (°C): "))

if temperature > 30:
    print("It's very hot! Stay hydrated.")
elif temperature > 15:
    print("Nice weather today.")
elif temperature > 0:
    print("It's cold, wear a jacket.")
else:
    print("It's freezing! Bundle up.")

print()

# 3. Loops

# For Loop
print("3. For Loop Examples:")
print("Counting from 1 to 5:")
for i in range(1, 6):          # range(1,6) means 1,2,3,4,5
    print(f"Number: {i}")

print("\nLooping through a list:")
fruits = ["Apple", "Banana", "Orange", "Mango"]
for fruit in fruits:
    print(f"I like {fruit}")

print()

# While Loop
print("4. While Loop Example:")
count = 1
while count <= 5:
    print(f"While loop count: {count}")
    count += 1   # same as count = count + 1

print("\n=== Day 2 Completed! ===")