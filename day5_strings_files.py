# ================================================
# DAY 5 - String Methods, File Handling & Mini Project
# ================================================
# Name: JAY
# Date: April 13, 2026
# Goal: Learn useful string methods and basic file handling

print("=== Day 5 - Strings and File Handling Started ===\n")

# 1. Useful String Methods
print("1. String Methods:")

text = "  Hello From Regina, Saskatchewan!  "

print(f"Original: '{text}'")
print(f"Lowercase: '{text.lower()}'")
print(f"Uppercase: '{text.upper()}'")
print(f"Title Case: '{text.title()}'")
print(f"Stripped: '{text.strip()}'")           # Removes spaces from start and end
print(f"Replaced: '{text.replace('Regina', 'Saskatoon')}'")

# Check if string contains something
print(f"Contains 'Regina': { 'Regina' in text }")
print(f"Starts with 'Hello': { text.strip().startswith('Hello') }")
print(f"Ends with '!': { text.strip().endswith('!') }\n")

# Split and Join
sentence = "Python is awesome and powerful"
words = sentence.split()          # Split into list
print(f"Split into words: {words}")

new_sentence = " - ".join(words)
print(f"Joined with separator: {new_sentence}\n")

# 2. Basic File Handling
print("2. Writing and Reading Files:")

# Writing to a file
with open("my_notes.txt", "w") as file:
    file.write("Day 5 Python Learning Notes\n")
    file.write("===========================\n")
    file.write(f"Name: JAY\n")
    file.write(f"City: Regina, Saskatchewan\n")
    file.write(f"Date: April 13, 2026\n")
    file.write("Goal: Learning Python for backend development\n")

print("✅ File 'my_notes.txt' created and written successfully!\n")

# Reading from the file
print("3. Reading the file:")
with open("my_notes.txt", "r") as file:
    content = file.read()
    print(content)

# 3. Mini Project - Simple Todo List using File
print("\n4. Mini Project: Simple Todo List (Saved in file)")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Main Todo Program
tasks = load_tasks()

print("Current Tasks:")
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")

# Add a new task
new_task = input("\nEnter a new task (or press Enter to skip): ").strip()
if new_task:
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {new_task}")

print("\nUpdated Tasks:")
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")

print("\n=== Day 5 Completed Successfully! ===")
print("Check your folder - you should see 'my_notes.txt' and 'tasks.txt' files!")