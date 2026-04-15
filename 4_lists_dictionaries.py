# ================================================
# DAY 4 - Lists and Dictionaries
# ================================================
# Goal: Learn Lists, Dictionaries and how to work with them

print("=== Day 4 - Lists and Dictionaries Started ===\n")

# 1. Lists (Ordered collection)
print("1. Lists:")

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

print(f"Fruits list: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Number of fruits: {len(fruits)}\n")

# Adding and removing items
fruits.append("Pineapple")        # Add at the end
fruits.insert(2, "Strawberry")    # Add at specific position
print(f"After adding: {fruits}")

fruits.remove("Banana")           # Remove by value
print(f"After removing Banana: {fruits}\n")

# Looping through a list
print("Looping through fruits:")
for fruit in fruits:
    print(f"I like {fruit}")
print()

# 2. Dictionaries (Key-Value pairs)
print("2. Dictionaries:")

person = {
    "name": "JAY",
    "age": 25,
    "city": "Regina",
    "province": "Saskatchewan",
    "is_student": True
}

print(f"Person dictionary: {person}")
print(f"Name: {person['name']}")
print(f"City: {person['city']}\n")

# Adding new key-value
person["job"] = "Learning Python"
print(f"After adding job: {person}\n")

# Looping through dictionary
print("Looping through dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

print()

# 3. List of Dictionaries (Very Common in Real Projects)
print("3. List of Dictionaries - Tasks Example:")

tasks = [
    {"id": 1, "title": "Learn Python basics", "done": True},
    {"id": 2, "title": "Practice GitHub", "done": True},
    {"id": 3, "title": "Build first FastAPI project", "done": False},
    {"id": 4, "title": "Push code daily", "done": False}
]

print("My Tasks:")
for task in tasks:
    status = "✅ Done" if task["done"] else "⏳ Pending"
    print(f"{task['id']}. {task['title']} → {status}")

print()

# 4. Useful List Methods
numbers = [5, 2, 8, 1, 9, 3]

print(f"Original numbers: {numbers}")
numbers.sort()
print(f"Sorted: {numbers}")
numbers.reverse()
print(f"Reversed: {numbers}")
print(f"Sum of numbers: {sum(numbers)}")
print(f"Max number: {max(numbers)}")
print(f"Min number: {min(numbers)}")

print("\n=== Day 4 Completed Successfully! ===")